"""
🔒Private Users Client
/users
(Для методов, требующих авторизации)
"""
from httpx import Response
from clients.api_client import APIClient
from clients.auth.auth_schema import AuthUserSchema
from clients.users.private_http_builder import get_private_http_client
from clients.users.users_schema import UpdateUserRequestSchema

#=======================================================================================================================
#------------------------------------------------------- Client --------------------------------------------------------
class PrivateUsersClient(APIClient):
    ENDPOINT = '/users'

    def get_user_me_api(self) -> Response:
        """
        Метод ПОЛУЧЕНИЯ данных ТЕКУЩЕГО пользователя.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=self.ENDPOINT)

    def get_user_api(self, user_id: str) -> Response:
        """
        Метод для ПОЛУЧЕНИЯ данных пользователя по User ID.

        :param user_id: ID пользователя
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f'{self.ENDPOINT}/{user_id}')

    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        """
        Метод для ЧАСТИЧНОГО ОБНОВЛЕНИЯ данных пользователя по User ID.

        :param user_id: ID пользователя
        :param request: Словарь с email, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f'{self.ENDPOINT}/{user_id}', json=request)

    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод для УДАЛЕНИЯ пользователя по User ID.

        :param user_id: ID пользователя
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f'{self.ENDPOINT}/{user_id}')

#-----------------------------------------------------------------------------------------------------------------------
# Builder
def get_private_users_client(user: AuthUserSchema) -> PrivateUsersClient:
    """
    Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user))
