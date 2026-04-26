"""
Authentication Client
/authentication
"""
from httpx import Response
from clients.api_client import APIClient
from clients.auth.auth_schema import LoginRequestSchema, RefreshRequestSchema, LoginResponseSchema
from clients.public_http_builder import get_public_http_client

#=======================================================================================================================
#------------------------------------------------------- Client --------------------------------------------------------
class AuthClient(APIClient):
    ENDPOINT = '/authentication'

    def login_api(self, payload: LoginRequestSchema) -> Response:
        """
        Метод выполняет АУТЕНТИФИКАЦИЮ (login) пользователя.

        :param payload: Словарь с Email и Password.
        :return Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url=f'{self.ENDPOINT}/login', json=payload.model_dump(by_alias=True))

    def refresh_api(self, payload: RefreshRequestSchema) -> Response:
        """
        Метод ОБНОВЛЯЕТ ТОКЕН авторизации.

        :param payload: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url=f'{self.ENDPOINT}/refresh', json=payload.model_dump(by_alias=True))


    def login(self, payload: LoginRequestSchema) -> LoginResponseSchema:
        """
        Авторизует (логинит) зарегистрированного пользователя через готовый метод login_api()

        :param payload: Словарь с Email и Password
        :return: Ответ авторизации в формате JSON для получения необходимых данных пользователя
        """
        response = self.login_api(payload) # обращение в методу login_api()
        return response.json()             # тело ответа из которого будем вытаскивать необходимые данные (token, User ID ...)


#--------------------------------------------------- Client Builder ----------------------------------------------------
def get_auth_client() -> AuthClient:
    """
    Функция создает экземпляр AuthClient с уже настроенным http-клиентом.

    :return: Готовый к использованию объект AuthenticationClient базовыми параметрами.
    """
    return AuthClient(client=get_public_http_client())


#-----------------------------------------------------------------------------------------------------------------------
