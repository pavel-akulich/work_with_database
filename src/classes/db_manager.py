import psycopg2


class DBManager:
    """
    A utility class for managing and querying data related to companies and job vacancies.

    This class provides static methods for retrieving information about companies and job vacancies
    from a PostgreSQL database. It includes methods to retrieve company statistics, list all vacancies,
    calculate average salaries, find vacancies with above-average salaries, and search for vacancies by keyword.

    Args:
    database_name (str): The name of the PostgreSQL database to connect to.
    params (dict): A dictionary containing database connection parameters.
    """

    @staticmethod
    def get_companies_and_vacancies_count(database_name: str, params: dict):
        """Returns a list of all companies and the number of vacancies for each company."""
        conn = psycopg2.connect(dbname=database_name, **params)

        with conn.cursor() as cur:
            cur.execute("""
                    SELECT employers.company_name, COUNT(vacancies.employer_id) AS vacancy_count
                    FROM employers
                    LEFT JOIN vacancies ON employers.employer_id = vacancies.employer_id
                    GROUP BY employers.company_name;
            """)

            result = cur.fetchall()

        conn.commit()
        conn.close()

        return result

    @staticmethod
    def get_all_vacancies(database_name: str, params: dict):
        """
        Returns a list of all vacancies with the company name, job title, salary and links to the vacancy.
        """
        conn = psycopg2.connect(dbname=database_name, **params)

        with conn.cursor() as cur:
            cur.execute("""
            SELECT employers.company_name, title AS vacancy_title, vacancy_url, salary_from, salary_to FROM vacancies
            LEFT JOIN employers USING(employer_id);
            """)

            result = cur.fetchall()

        conn.commit()
        conn.close()

        return result

    @staticmethod
    def get_avg_salary(database_name: str, params: dict):
        """Returns the average salary for vacancies (for the lower fork of the salary)."""
        conn = psycopg2.connect(dbname=database_name, **params)

        with conn.cursor() as cur:
            cur.execute("""
                    SELECT AVG(salary_from)::numeric AS average_salary_from FROM vacancies
                    WHERE salary_from IS NOT NULL;

            """)

            result = cur.fetchone()

        conn.commit()
        conn.close()

        return result[0] if result else None

    @staticmethod
    def get_vacancies_with_higher_salary(database_name: str, params: dict):
        """Returns a list of all vacancies whose salary is higher than the average for all vacancies."""
        conn = psycopg2.connect(dbname=database_name, **params)

        with conn.cursor() as cur:
            cur.execute("""
                    SELECT employers.company_name, title AS vacancy_title, vacancy_url, salary_from
                    FROM vacancies 
                    INNER JOIN employers USING(employer_id)
                    WHERE salary_from > ( SELECT AVG (salary_from) FROM vacancies WHERE salary_from IS NOT NULL)
            """)

            result = cur.fetchall()

        conn.commit()
        conn.close()

        return result

    @staticmethod
    def get_vacancies_with_keyword(database_name: str, params: dict, keyword: str):
        """Returns a list of all vacancies whose names contain the words passed to the method, for example Manager"""
        conn = psycopg2.connect(dbname=database_name, **params)

        with conn.cursor() as cur:
            cur.execute("""
                    SELECT employers.company_name, title AS vacancy_title, vacancy_url, salary_from, salary_to
                    FROM vacancies
                    LEFT JOIN employers USING(employer_id)
                    WHERE title LIKE %s
            """, ('%' + keyword + '%',))

            result = cur.fetchall()

        conn.commit()
        conn.close()

        return result
