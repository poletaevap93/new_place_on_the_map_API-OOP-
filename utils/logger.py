import datetime    # для фиксации времени и даты запуска тестов
import os

from requests import Response


class Logger():
    file_name = f"logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"     #f"logs/log_" - файг будет храниться в папке logs, название файла log_, берем настоящее время, указывая формат, и плюс расширение нашего файла .log (как называется файл и из чего он будет состоять)

    @classmethod   # это означает, что метод write_log_to_file сможет обращаться к переменным класса
    def write_log_to_file(cls, data: str):   # cls - так надо написать; data - это данные, а не дата. Будут иметь строчный тип данных
        with open(Logger.file_name, 'a', encoding='utf=8') as logger_file:   # указываем кодировку utf=8. (Открываем файл file_name)
            logger_file.write(data)    # записываем в logger_file данные


    @classmethod
    def add_request(cls, url: str, method: str):# получение данных по запросу
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f"\n-----\n"  # перенос строки и пробелы для разделения логов
        data_to_add += f"test: {test_name}\n"   # += - будет прибавляться к каждой новой строчке. Здесь помещается название теста
        data_to_add += f"time: {str(datetime.datetime.now())}\n"   # здесь помещается время
        data_to_add += f"Request method: {method}\n"
        data_to_add += f"Request URL: {url}\n"
        data_to_add += "\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, result: Response):  # получение данных по ответу
        cookies_as_dict = dict(result.cookies)   # чтобы помещать в файл куки
        headers_as_dict = dict(result.headers)    # чтобы помещать в файл заголовки

        data_to_add = f"Response code: {result.status_code}\n"  # добавляем статус код
        data_to_add += f"Response text: {result.text}\n"   # содержимое ответа
        data_to_add += f"Response headers: {headers_as_dict}\n"
        data_to_add += f"Response cookies: {cookies_as_dict}\n"
        data_to_add += f"\n-----\n"

        cls.write_log_to_file(data_to_add)

