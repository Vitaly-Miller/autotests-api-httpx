"""
PUBLIC Users Client
/users
(Для методов, НЕ требующих авторизации)
"""
from httpx import Response
from clients.api_client import APIClient
from clients.users.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserRequestSchema

#=======================================================================================================================
#------------------------------------------------------- Client --------------------------------------------------------
class PublicUsersClient(APIClient):
    ENDPOINT = '/users'

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Метод для СОЗДАНИЯ нового пользователя.

        :param request: Словарь с данными для создания пользователя (create_user_payload)
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url=self.ENDPOINT, json=request)

#-----------------------------------------------------------------------------------------------------------------------
# Builder (Public client)
def get_public_users_client() -> PublicUsersClient:
    return PublicUsersClient(client=get_public_http_client())
