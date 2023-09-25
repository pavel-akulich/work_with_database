from src.config import config
from src.classes.db_manager import DBManager


def user_interaction_ru():
    """Функция для взаимодействия с пользователем через консоль на русском языке"""

    # переменная конфигурация, хранящая данные для подключения к БД
    parameters = config()

    while True:
        print("Доступны следующие действия. Сделайте выбор:")
        print("1 - Получить список всех компаний и количество вакансий у каждой компании")
        print("2 - Получить список всех вакансий с указанием названия компании,вакансии,зарплаты и ссылки на вакансию")
        print("3 - Получить среднюю зарплату по вакансиям")
        print("4 - Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям")
        print("5 - Получить список всех вакансий, в названии которых содержатся переданные слова, например 'Менеджер'")
        print("0 - Завершение программы")

        # Создаем экземпляр класса DBManager
        db_manager_ru = DBManager()

        choice_ru = input("Введите номер действия: ")

        if choice_ru == "1":

            result = db_manager_ru.get_companies_and_vacancies_count('coursework_5', parameters)
            for el in result:
                print(el)

        elif choice_ru == "2":
            print("Значение None означает,что зарплата не указана")

            result = db_manager_ru.get_all_vacancies('coursework_5', parameters)
            for el in result:
                print(el)

        elif choice_ru == "3":
            print("Во многих вакансиях не указана верхняя вилка зарплаты, поэтому средняя считается по нижней вилке")

            salary = db_manager_ru.get_avg_salary('coursework_5', parameters)
            round_salary = round(salary)
            print(f'Средняя зарплата по вакансиям составляет - {round_salary} RUB')

        elif choice_ru == "4":

            result = db_manager_ru.get_vacancies_with_higher_salary('coursework_5', parameters)
            for el in result:
                print(el)

        elif choice_ru == "5":

            user_keyword = input('Введите ключевое слово для поиска: ')

            result = db_manager_ru.get_vacancies_with_keyword('coursework_5', parameters, user_keyword)
            if result:
                for el in result:
                    print(el)
            else:
                print(f'По слову {user_keyword} не найдено вакансий')

        elif choice_ru == "0":
            print("Завершение программы...")
            print("Спасибо за использование программы, возвращайтесь снова :)")
            exit()
        else:
            print("Неправильный выбор. Пожалуйста, выберите существующий вариант.")
