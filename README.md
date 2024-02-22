# Проект: Работа с базой данных
**Russian** | [English](dosc_eng/README.md)

## Описание проекта
Проект "Работа с базой данных" представляет собой консольное приложение, которое при запуске делает запрос по API, автоматически создает базу данных и таблицы в ней, автоматически заполняемые данными из запроса. 
Проект позволяет получать различную информацию о вакансиях, сохраненных в базе данных путём взаимодействия с программой через консоль.
Проект можно запустить на английском или русском языке, после запуска программы она предложит выбрать язык для дальнейшего взаимодействия.

## Составляющие части проекта
Проект состоит из следующих компонентов:

1. **Класс для работы с базой данных:**
    - Создан класс `DBManager`, в котором определены статические методы `get_companies_and_vacancies_count`, `get_all_vacancies`, `get_avg_salary`, `get_vacancies_with_higher_salary`, `get_vacancies_with_keyword`.
    - Данные методы позволяют удобно взаимодействовать с базой данной и получать информацию о компаниях и вакансиях, которые хранятся в этой базе данных.

2. **Функция для работы с API:**
    - Создана функция `get_companies_data`, которая по API подключается к hh.ru и получает информацию об указанных компаниях.
    - Функция возвращает список словарей, словари хранят данные о компаниях и вакансиях этих компаний.

3. **Функции взаимодействия с базой данной:**
      - Реализована функция `create_database` для создания базы данных и таблиц в этой БД.
      - Реализована функция `save_data_to_database` для сохранения полученных данных в таблицы БД.
      - Функции `create_database` и `save_data_to_database` реализованы в файле `utils.py`.

4. **Функции для взаимодействия с пользователем:**
    - Реализованы функции `user_interaction_en` и `user_interaction_ru` для взаимодействия с пользователем через консоль.

## Технологии
- Проект разработан на языке программирования Python. Для работы с API используется сторонняя библиотека `requests`.
- Для работы с базой данных используется сторонняя библиотека `psycopg2-binary`.
- В проекте для управления виртуальным окружением используется инструмент `poetry`.
- Все необходимые зависимости к проекту находятся в файле `pyproject.toml`.

## Инструкции по использованию программы 
Весь интерфейс и все взаимодействие с пользователем происходит на английском языке или русском языке.

Все взаимодействие с приложением происходит путем ввода цифр для выбора того или иного действия.

Перед запуском приложения ознакомьтесь с тем, как его использовать.

1. Запустите приложение, выполнив команду `python main.py` или нажав `Run 'main'` для файла `main.py`.

2. В предложенном меню выберите один из вариантов, введя соответсвующую цифру:
   - 1 - Получить список всех компаний и количество вакансий у каждой компании
   - 2 - Получить список всех вакансий с указанием названия компании, вакансии, зарплаты и ссылки на вакансию
   - 3 - Получить среднюю зарплату по вакансиям
   - 4 - Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям
   - 5 - Получить список всех вакансий, в названии которых содержатся переданные слова, например 'Менеджер'
   - 0 - Завершение программы
   
3. Следуйте инструкциям в консоли.

## Примечания
- Проект может быть доработан и расширен для более широкого использования.
- Компании, информация о которых получается и записывается в базу данных могут быть изменены на другие.
- Для подключения к БД используется функция `config` из файла `config.py`. 
- Сама конфигурация находится в файле `database.ini`, который не хранится в репозитории в целях безопасности.