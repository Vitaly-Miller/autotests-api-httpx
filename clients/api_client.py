"""
API Client
"""
import httpx
import allure
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

    # GET ------------------------------------------------------------------------------------------------------------
    @allure.step('🟢 GET-request')
    def get(self,
            url: httpx.URL | str,
            params: httpx.QueryParams | None = None) -> httpx.Response:
        """
        GET-запрос

        :param url: URL-адрес эндпоинта
        :param params: Параметры запроса в формате qwery (например, ?key=value) / None
        :return: httpx.Response
        """
        return self.client.get(url=url, params=params)


    # POST -----------------------------------------------------------------------------------------------------------
    @allure.step('🟡 POST-request')
    def post(self,
             url: httpx.URL | str,
             json: Any | None = None,
             data: RequestData | None = None,
             files: RequestFiles | None = None) -> httpx.Response:
        """
        POST-запрос

        :param url: URL-адрес эндпоинта
        :param json: Данные
        :param data: Данные
        :param files: Файлы для загрузки на сервер
        :return: httpx.Response
        """
        return self.client.post(url=url, json=json, data=data, files=files)


    # PATCH ----------------------------------------------------------------------------------------------------------
    @allure.step('🟣 PATCH-request')
    def patch(self,
              url: httpx.URL | str,
              json: Any | None = None) -> httpx.Response:
        """
        PATCH-запрос (Частичное обновление)

        :param url: URL-адрес эндпоинта
        :param json: Данные для частичного обновления
        :return: httpx.Response
        """
        return self.client.patch(url=url, json=json)


    # PUT ------------------------------------------------------------------------------------------------------------
    @allure.step('🔵 PUT-request')
    def put(self,
            url: httpx.URL | str,
            json: Any | None = None) -> httpx.Response:
        """
        PUT-запрос (Полное обновление)

        :param url: URL-адрес эндпоинта
        :param json: Данные для обновления в формате JSON
        :return: httpx.Response
        """
        return self.client.put(url=url, json=json)


    # DELETE ---------------------------------------------------------------------------------------------------------
    @allure.step('🔴 DELETE-request')
    def delete(self,
               url: httpx.URL | str) -> httpx.Response:
        """
        DELETE-запрос (удаление данных)

        :param url: URL-адрес эндпоинта
        :return: httpx.Response
        """
        return self.client.delete(url=url)

#=======================================================================================================================
