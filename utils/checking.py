"""Методы для проверки ответов запросов"""
import json

from requests import Response


class Checking():

    """Метод для проверки статус кода"""
    @staticmethod
    def check_status_code(response: Response, status_code):     #status_code - это тот статус, который ожидается получить,который будет задаваться
        assert status_code == response.status_code              # response.status_code  - тот, который будет браться из ответа
        if response.status_code == status_code:
            print("Проверка на статус код: Успешно! Статус код = " + str(response.status_code))
        else:
            print("Проверка на статус код: Провал. Статус код = " + str(response.status_code))


    """Метод для проверки наличия обязательных полей в ответах запросов"""

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)           # функция loads преобразует строку, которую получаем, в формат Json, чтоб можно было с ней работать, получать значения и тд
        assert list (token) == expected_value             # с помщью функции List получаем все значения из ответов, все обязательные поя, все ключи. Проверяем, что все поля совпадют с тем, что мы ожидаем получить (а именно, надо прописать названия полей ответов, которые указаны в документации)
        print("Все поля присутствуют.")


    """Метод для проверки значений обязательных полей в ответах запросов"""

    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " верен!")


    """Метод для проверки на наличие слова в ответе запроса"""
    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_world):
        check = response.json()
        check_info = check.get(field_name)
        if search_world in check_info:
            print("Слово " + search_world + " содержится в ответе")
        else:
            print("Слово " + search_world + " отсутствует в ответе")




