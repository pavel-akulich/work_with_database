from src.utils.utils import create_database, save_data_to_database
from src.utils.hh_api import get_companies_data
from config import config
from src.utils.user_interaction_ru import user_interaction_ru
from src.utils.user_interaction_en import user_interaction_en


def main():
    """The main function to run the program"""

    # variable configuration that stores data for connecting to the database
    parameters = config()

    # the list of companies about which data will be received can be replaced with the companies you need
    name_companies = [
        'Яндекс Крауд',
        'Сбер. IT',
        'Lamoda',
        'Альфа-Банк',
        'VK, ВКонтакте'
    ]

    data = get_companies_data(name_companies)
    create_database('database_vacancies', parameters)
    save_data_to_database(data, 'database_vacancies', parameters)

    input_language = input('Select Language: 1 - RU, 2 -EN: ')
    if input_language == '1':
        print(f'Эта программа позволяет получать информацию из БД о вакансиях компаний - {name_companies}')
        user_interaction_ru()
    elif input_language == '2':
        print(f'This program allows you to get information from DB about vacancies of companies - {name_companies}')
        user_interaction_en()
    else:
        print('Wrong choice. Please select an existing option.')


if __name__ == '__main__':
    main()
