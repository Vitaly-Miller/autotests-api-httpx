"""
API Client
"""
from httpx import Client, Response, URL, QueryParams         # для аннотации типов
from httpx._types import RequestData, RequestFiles   # NOQA  # для аннотации типов (работа с файлами)
from typing import Any                                       # для аннотации типов

#=======================================================================================================================
class APIClient:
    def __init__(self, client: Client):
        """
        Базовый API-клиент, принимающий httpx.Client-сессию.

        :param client: Экземпляр httpx.Client для выполнения запросов
        """
        self.client = client

    # 🟩GET ------------------------------------------------------------------------------------------------------------
    def get(self,
            url: URL | str,
            params: QueryParams | None = None) -> Response:
        """
        GET-запрос.

        :param url: URL-адрес эндпоинта.
        :param params: Параметры запроса (например, ?key=value).
        :return Объект httpx.Response с данными ответа.
        """
        return self.client.get(url=url, params=params)

    # 🟨POST -----------------------------------------------------------------------------------------------------------
    def post(self,
             url: URL | str,
             json: Any | None = None,
             data: RequestData | None = None,
             files: RequestFiles | None = None) -> Response:
        """
        POST-запрос.

        :param url: URL-адрес эндпоинта.
        :param json: Данные в формате JSON.
        :param data: Форматированные данные формы (например, application/x-www-form-urlencoded).
        :param files: Файлы для загрузки на сервер.
        :return Объект httpx.Response с данными ответа.
        """
        return self.client.post(url=url, json=json, data=data, files=files)

    # 🟪PATCH ---------------------------------------------------------------------------------------------------------
    def patch(self,
              url: URL | str,
              json: Any | None = None) -> Response:
        """
        PATCH-запрос (Частичное обновление ресурса, передавая только измененные данные).

        :param url: URL-адрес эндпоинта.
        :param json: Данные для обновления в формате JSON.
        :return Объект httpx.Response с данными ответа.
        """
        return self.client.patch(url=url, json=json)

    # 🟦PUT ------------------------------------------------------------------------------------------------------------
    def put(self,
            url: URL | str,
            json: Any | None = None) -> Response:
        """
        PUT-запрос (Полное обновление данных).

        :param url: URL-адрес эндпоинта.
        :param json: Данные для обновления в формате JSON.
        :return Объект httpx.Response с данными ответа.
        """
        return self.client.put(url=url, json=json)

    # 🟥DELETE ---------------------------------------------------------------------------------------------------------
    def delete(self,
               url: URL | str) -> Response:
        """
        DELETE-запрос (удаление данных).

        :param url: URL-адрес эндпоинта.
        :return Объект httpx.Response с данными ответа.
        """
        return self.client.delete(url=url)

#-----------------------------------------------------------------------------------------------------------------------
