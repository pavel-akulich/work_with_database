-- Creating a database
CREATE DATABASE database_name;

-- Creating a table of employers
CREATE TABLE employers (
employer_id int PRIMARY KEY,
company_name VARCHAR(255) NOT NULL,
company_url VARCHAR UNIQUE NOT NULL
);

-- Creating a table with vacancies of these employers
CREATE TABLE vacancies (
    employer_id int REFERENCES employers(employer_id),
    vacancy_id SERIAL PRIMARY KEY,
    title VARCHAR NOT NULL,
    city VARCHAR(255),
    vacancy_url VARCHAR UNIQUE,
    salary_from int NULL,
    salary_to int NULL,
    description text
);

--Getting a list of all companies and the number of vacancies for each company
SELECT employers.company_name, COUNT(vacancies.employer_id) AS vacancy_count
FROM employers
LEFT JOIN vacancies ON employers.employer_id = vacancies.employer_id
GROUP BY employers.company_name;



--Getting a list of all vacancies with the company name, job title and salary and links to the vacancy
SELECT employers.company_name, title AS vacancy_title, vacancy_url, salary_from, salary_to FROM vacancies
LEFT JOIN employers USING(employer_id);

--Getting the average salary for vacancies
SELECT AVG(salary_from) AS average_salary_from FROM vacancies
WHERE salary_from IS NOT NULL;



--Getting a list of all vacancies whose salary is higher than the average for all vacancies
SELECT employers.company_name, title AS vacancy_title, vacancy_url, salary_from
FROM vacancies
INNER JOIN employers USING(employer_id)
WHERE salary_from > (
    SELECT AVG(salary_from)
    FROM vacancies
    WHERE salary_from IS NOT NULL
);


--Getting a list of all vacancies whose names contain the words passed to the method, for example "Manager"
SELECT employers.company_name, title AS vacancy_title, vacancy_url, salary_from, salary_to
FROM vacancies
LEFT JOIN employers USING(employer_id)
WHERE title LIKE '%keyword%';
