from typing import Any

import requests


def get_companies_data(company_names: list[str]) -> list[dict[str, Any]]:
    """A function that uses the API to get data about the company and vacancies"""
    # A list that stores dictionaries containing data about the company and the vacancies of these companies
    data = []

    for name_company in company_names:
        url = 'https://api.hh.ru/employers'

        headers = {
            'User-Agent': 'MyApp/company_parser pavelakulich1999@gmail.com'
        }
        params = {
            'text': {name_company}
        }

        # API request to hh.ru to get companies and their vacancies
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            json_data = response.json()

            # Creating a list that will store the vacancies of the relevant companies
            vacancies = []

            # Creating a variable that stores a link to vacancies
            vacancies_url = json_data['items'][0]['vacancies_url']

            # request for a list of vacancies
            vacancies_response = requests.get(vacancies_url)

            if vacancies_response.status_code == 200:
                # Parsing the JSON response
                data_vacancies = vacancies_response.json()

                for vacancy in data_vacancies['items']:
                    vacancies.append(vacancy)

            data.append({
                'employer': json_data['items'][0],
                'vacancies': vacancies
            })
        else:
            raise Exception(f'Error in the request for {name_company}')

    return data
