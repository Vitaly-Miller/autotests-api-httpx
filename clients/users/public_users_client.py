"""
PUBLIC Users Client
/users
(Для методов, НЕ требующих авторизации)
"""
from httpx import Response
from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema

#=======================================================================================================================
#------------------------------------------------------- Client --------------------------------------------------------
class PublicUsersClient(APIClient):
    ENDPOINT = '/users'

    def create_user_api(self, payload: CreateUserRequestSchema) -> Response:
        """
        Метод для СОЗДАНИЯ нового пользователя.

        :param payload: Словарь с данными для создания пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url=self.ENDPOINT, json=payload.model_dump(by_alias=True))  # 👈Сериализация

    def create_user(self, payload: CreateUserRequestSchema) -> CreateUserResponseSchema:
        """
        Метод получения JSON-ответа о созданном пользователе.

        :param payload: Словарь с данными для создания пользователя.
        :return: Ответ от сервера о созданном пользователе в виде JSON объекта
        """
        response = self.create_user_api(payload)
        return response.json()


#----------------------------------------------- Client Builder (Public) -----------------------------------------------
def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PrivateUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())
