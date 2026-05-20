"""
API Client
"""
import httpx
from httpx._types import RequestData, RequestFiles   # NOQA  # для аннотации типов (работа с файлами)
from typing import Any                                       # для аннотации типов

#===================================================== API Client ======================================================
class APIClient:
    def __init__(self, client: httpx.Client):
        """
        Базовый API-клиент, принимающий httpx.Client-сессию.

        :param client: Экземпляр httpx.Client для выполнения запросов
        """
        self.client = client

    # 🟩GET ------------------------------------------------------------------------------------------------------------
    def get(self,
            url: httpx.URL | str,
            params: httpx.QueryParams | None = None) -> httpx.Response:
        """
        GET-запрос

        :param url: URL-адрес эндпоинта
        :param params: Параметры запроса (например, ?key=value)
        :return: httpx.Response
        """
        return self.client.get(url=url, params=params)

    # 🟨POST -----------------------------------------------------------------------------------------------------------
    def post(self,
             url: httpx.URL | str,
             json: Any | None = None,
             data: RequestData | None = None,
             files: RequestFiles | None = None) -> httpx.Response:
        """
        POST-запрос

        :param url: URL-адрес эндпоинта
        :param json: Данные в формате JSON
        :param data: Форматированные данные формы (например, application/x-www-form-urlencoded)
        :param files: Файлы для загрузки на сервер
        :return: httpx.Response
        """
        return self.client.post(url=url, json=json, data=data, files=files)

    # 🟪PATCH ----------------------------------------------------------------------------------------------------------
    def patch(self,
              url: httpx.URL | str,
              json: Any | None = None) -> httpx.Response:
        """
        PATCH-запрос (Частичное обновление ресурса, передавая только измененные данные)

        :param url: URL-адрес эндпоинта
        :param json: Данные для обновления в формате JSON
        :return: httpx.Response
        """
        return self.client.patch(url=url, json=json)

    # 🟦PUT ------------------------------------------------------------------------------------------------------------
    def put(self,
            url: httpx.URL | str,
            json: Any | None = None) -> httpx.Response:
        """
        PUT-запрос (Полное обновление данных)

        :param url: URL-адрес эндпоинта
        :param json: Данные для обновления в формате JSON
        :return: httpx.Response
        """
        return self.client.put(url=url, json=json)

    # 🟥DELETE ---------------------------------------------------------------------------------------------------------
    def delete(self,
               url: httpx.URL | str) -> httpx.Response:
        """
        DELETE-запрос (удаление данных)

        :param url: URL-адрес эндпоинта
        :return: httpx.Response
        """
        return self.client.delete(url=url)

#=======================================================================================================================
