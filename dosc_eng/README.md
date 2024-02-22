# Project: Working with the database
[Russian](../README.md) | **English**

## Project Description
The project "Working with the database" is a console application that when launched makes an API request, automatically creates a database and tables in it that are automatically populated with data from the request.
The project allows you to get various information about vacancies stored in the database by interacting with the program via the console.
The project can be launched in English or Russian, after launching the program it will prompt you to choose a language for further interaction.

## Components of the project
The project consists of the next components:

1. **A class for working with a database:**
    - The `DBManager` class has been created, in which static methods are defined `get_companies_and_vacancies_count`, `get_all_vacancies`, `get_avg_salary`, `get_vacancies_with_higher_salary`, `get_vacancies_with_keyword`.
    - These methods allow you to conveniently interact with the database and get information about companies and vacancies that are stored in this database.

2. **Function for working with the API:**
    - Created function `get_companies_data`, hat connects to the API hh.ru and receives information about companies.
    - The function returns a list of dictionaries, dictionaries store data about companies and vacancies of these companies.

3. **Functions of interaction with the database:**
      - The function `create_database` is implemented to create a database and tables in this database.
      - The function `save_data_to_database` is implemented to save the received data to the database tables.
      - The functions `create_database` and `save_data_to_database` are implemented in the file `utils.py `.

4. **Functions for user interaction:**
    - The functions `user_interaction_en` and `user_interaction_ru` are implemented to interact with the user via the console.

## Technologies
- The project is developed in the Python programming language. A third-party library `requests` is used to work with the API.
- A third-party library `psycopg2-binary` is used to work with the database.
- The project uses the `poetry` tool to manage the virtual environment.
- All the necessary dependencies to the project are in the file `pyproject.toml `.

## Instructions for using the program
The entire interface and all user interaction takes place in English or Russian.

All interaction with the application takes place by entering numbers to select an action.

Before launching the application, familiarize yourself with how to use it.

1. Run the application by running the command `python main.py ` or by clicking `Run 'main'` for the file `main.py `.

2. In the suggested menu, select one of the options by entering the appropriate number:
   - 1 - Getting a list of all companies and the number of vacancies for each company
   - 2 - Getting a list of all vacancies with the company name, vacancies, salaries and links to the vacancy
   - 3 - Getting an average salary for vacancies
   - 4 - Getting a list of all vacancies whose salary is higher than the average for all vacancies
   - 5 - Getting a list of all vacancies whose names contain the transmitted words, for example 'Manager'
   - 0 - Completion of the program
   
3. Follow the instructions in the console.

## Notes
- The project can be further developed and expanded for wider use
- Companies whose information is obtained and recorded in the database can be changed to others.
- To connect to the database is used the `config` function from the file `config.py `.
- The configuration itself is located in the `database.ini` file, which is not stored in the repository for security reasons.