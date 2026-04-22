"""
Authentication Client
/authentication
"""
from httpx import Response
from clients.api_client import APIClient
from clients.authentication.authentication_schema import LoginRequestSchema, RefreshRequestSchema, LoginResponseSchema
from clients.users.public_http_builder import get_public_http_client

#=======================================================================================================================
#------------------------------------------------------- Client --------------------------------------------------------
class AuthenticationClient(APIClient):
    ENDPOINT = '/authentication'

    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Метод выполняет АУТЕНТИФИКАЦИЮ пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url=f'{self.ENDPOINT}/login', json=request)

    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """
        Метод ОБНОВЛЯЕТ ТОКЕН авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url=f'{self.ENDPOINT}/refresh', json=request)


    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        """
        Отправляет запрос на аутентификацию

        :param request:
        :return: Ответ авторизации в формате JSON
        """
        response = self.login_api(request)
        return response.json()

#-----------------------------------------------------------------------------------------------------------------------
# Builder (Public client)
def get_authentication_client() -> AuthenticationClient:
    """
    Функция создает экземпляр AuthenticationClient с уже настроенным http-клиентом.

    :return: Готовый к использованию объект AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())


#-----------------------------------------------------------------------------------------------------------------------
