"""
API Client
"""
import httpx
import allure
from httpx._types import RequestData, RequestFiles
from typing import Any

#===================================================== API Client ======================================================
class APIClient:
    def __init__(self, client: httpx.Client):
        """
        Base API client that accepts a httpx.Client session.

        :param client: httpx.Client instance used to send requests
        """
        self.client = client


    @allure.step('🟢 GET-request')
    def get(self,
            url: httpx.URL | str,
            params: httpx.QueryParams | None = None) -> httpx.Response:
        """
        GET request

        :param url: Endpoint URL
        :param params: Query string parameters (e.g. ?key=value) / None
        :return: httpx.Response
        """
        return self.client.get(url=url, params=params)


    @allure.step('🟡 POST-request')
    def post(self,
             url: httpx.URL | str,
             json: Any | None = None,
             data: RequestData | None = None,
             files: RequestFiles | None = None) -> httpx.Response:
        """
        POST request

        :param url: Endpoint URL
        :param json: Request body as JSON
        :param data: Form data
        :param files: Files to upload to the server
        :return: httpx.Response
        """
        return self.client.post(url=url, json=json, data=data, files=files)


    @allure.step('🟣 PATCH-request')
    def patch(self,
              url: httpx.URL | str,
              json: Any | None = None) -> httpx.Response:
        """
        PATCH request (partial update)

        :param url: Endpoint URL
        :param json: Data for the partial update
        :return: httpx.Response
        """
        return self.client.patch(url=url, json=json)


    @allure.step('🔵 PUT-request')
    def put(self,
            url: httpx.URL | str,
            json: Any | None = None) -> httpx.Response:
        """
        PUT request (full update)

        :param url: Endpoint URL
        :param json: Update data in JSON format
        :return: httpx.Response
        """
        return self.client.put(url=url, json=json)


    @allure.step('🔴 DELETE-request')
    def delete(self,
               url: httpx.URL | str) -> httpx.Response:
        """
        DELETE request (data deletion)

        :param url: Endpoint URL
        :return: httpx.Response
        """
        return self.client.delete(url=url)


#=======================================================================================================================
