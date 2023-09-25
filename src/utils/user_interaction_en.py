from src.config import config
from src.classes.db_manager import DBManager


def user_interaction_en():
    """Function for interacting with the user via the console in English"""

    # variable configuration that stores data for connecting to the database
    parameters = config()

    while True:
        print("The next actions are available. Make a choice:")
        print("1 - Get a list of all companies and the number of vacancies for each company")
        print("2 - Get a list of all vacancies with the company name,vacancies,salaries and links to the vacancy")
        print("3 - Get an average salary for vacancies")
        print("4 - Get a list of all vacancies whose salary is higher than the average for all vacancies")
        print("5 - Get a list of all vacancies whose names contain the passed words, for example 'Developer'")
        print("0 - Completion of the program")

        # Creating an instance of the DBManager class
        db_manager_en = DBManager()

        choice_en = input("Enter the action number: ")

        if choice_en == "1":

            result = db_manager_en.get_companies_and_vacancies_count('coursework_5', parameters)
            for el in result:
                print(el)

        elif choice_en == "2":
            print("The value None means that the salary is not specified")

            result = db_manager_en.get_all_vacancies('coursework_5', parameters)
            for el in result:
                print(el)

        elif choice_en == "3":
            print("In many vacancies, the upper fork of the salary is not indicated, "
                  "so the average is calculated according to the lower fork")

            salary = db_manager_en.get_avg_salary('coursework_5', parameters)
            round_salary = round(salary)
            print(f'The average salary for vacancies is - {round_salary} RUB')

        elif choice_en == "4":

            result = db_manager_en.get_vacancies_with_higher_salary('coursework_5', parameters)
            for el in result:
                print(el)

        elif choice_en == "5":

            user_keyword = input('Enter a keyword to search: ')

            result = db_manager_en.get_vacancies_with_keyword('coursework_5', parameters, user_keyword)
            if result:
                for el in result:
                    print(el)
            else:
                print(f'no vacancies found for the keyword {user_keyword}')

        elif choice_en == "0":
            print("Completion of the program...")
            print("Thanks for using the program, come back again :)")
            exit()
        else:
            print("Wrong choice. Please select an existing option.")
