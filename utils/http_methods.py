# здесь хранятся кастомные методы для отправки запросов (GET, POST, PUT, DELETE)

import requests

from utils.logger import Logger

class Http_methods:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        Logger.add_request(url, method="GET")   # каждый раз, когда будет вызываться кастомный метод гет, в логах будет появляться название. Результат запроса
        result = requests.get(url,headers=Http_methods.headers, cookies=Http_methods.cookie)
        Logger.add_response(result)   # чтобы фиксировать в логах ответ от сервера. Результат ответа
        return result

    @staticmethod  # должен обязательно содержать какое то тело, которое будет передаватьcя в json формате
    def post(url, body):
        Logger.add_request(url, method="POST")
        result = requests.post(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def put(url, body):
        Logger.add_request(url, method="PUT")
        result = requests.put(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def delete(url, body):
        Logger.add_request(url, method="DELETE")
        result = requests.delete(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
        Logger.add_response(result)
        return result

























