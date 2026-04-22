"""
API Client
"""
from httpx import Client, Response, URL, QueryParams         # для аннотации типов
from typing import Any                                       # для аннотации типов
from pydantic import BaseModel

#=======================================================================================================================
class APIClient:
    def __init__(self, client: Client):
        self.client = client

    # 🟩GET ------------------------------------------------------------------------------------------------------------
    def get(self,
            url: URL | str,
            params: QueryParams | None = None,
            headers: dict | None = None) -> Response:
        """
        GET-запрос.

        :param     url: URL-адрес эндпоинта.
        :param  params: Параметры запроса (например, ?key=value).
        :param headers: Headers.
        :return       : Объект httpx.Response с данными ответа.
        """
        return self.client.get(url=url, params=params, headers=headers)

    # 🟨POST -----------------------------------------------------------------------------------------------------------
    def post(self,
             url: URL | str,
             params: QueryParams | None = None,
             json: Any | None = None,
             data: Any | None = None,
             files: Any | None = None,
             timeout: float | None = None) -> Response:
        """
        POST-запрос.

        :param     url: URL-адрес эндпоинта.
        :param  params: Параметры запроса.
        :param    json: Данные в формате JSON.
        :param    data: Форматированные данные формы (например, application/x-www-form-urlencoded).
        :param   files: Файлы для загрузки на сервер.
        :param timeout: Timeout
        :return       : Объект httpx.Response с данными ответа.
        """
        if isinstance(json, BaseModel):
            json = json.model_dump(by_alias=True)
        return self.client.post(url=url, params=params, json=json, data=data, files=files, timeout=timeout)

    # 🟪PATCH ---------------------------------------------------------------------------------------------------------
    def patch(self,
              url: URL | str,
              json: Any | None = None,
              data: Any | None = None,
              files: Any | None = None) -> Response:
        """
        PATCH-запрос (Частичное обновление ресурса, передавая измененные данные).

        :param   url: URL-адрес эндпоинта.
        :param  json: Данные для обновления в формате JSON.
        :param  data: Передает параметры в x-www-form-urlencoded формате.
        :param files: Позволяет загружать файлы на сервер.
        :return     : Объект httpx.Response с данными ответа.
        """
        return self.client.patch(url=url, json=json, data=data, files=files)

    # 🟦PUT ------------------------------------------------------------------------------------------------------------
    def put(self,
            url: URL | str,
            json: Any | None = None) -> Response:
        """
        PUT-запрос (Полное обновление данных).

        :param  url: URL-адрес эндпоинта.
        :param json: Данные для обновления в формате JSON.
        :return    : Объект httpx.Response с данными ответа.
        """
        return self.client.put(url=url, json=json)

    # 🟥DELETE ---------------------------------------------------------------------------------------------------------
    def delete(self,
               url: URL | str,
               params: QueryParams | None = None) -> Response:
        """
        DELETE-запрос (удаление данных).

        :param    url: URL-адрес эндпоинта.
        :param params: Параметры запроса.
        :return      : Объект httpx.Response с данными ответа.
        """
        return self.client.delete(url=url, params=params)

#-----------------------------------------------------------------------------------------------------------------------
