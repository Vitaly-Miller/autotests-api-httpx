"""
Authentication Client
/authentication
"""
from httpx import Response
from clients.api_client import APIClient
from clients.auth.auth_schema import LoginRequestSchema, RefreshRequestSchema, LoginResponseSchema
from clients.public_http_builder import get_public_http_client

#======================================================= Client ========================================================
class AuthClient(APIClient):
    ENDPOINT = '/authentication'
    #--------------------------------------------------- Login ---------------------------------------------------------
    def login_api(self, payload: LoginRequestSchema) -> Response:
        """
        Метод выполняет АУТЕНТИФИКАЦИЮ (login) пользователя.

        :param payload: Словарь с Email и Password.
        :return Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            url=f'{self.ENDPOINT}/login',
            json=payload.model_dump(by_alias=True)    # + ⚠ сериализация Model -> Dict (т.к. payload - Pydantic-модель)
        )

    def login(self, payload: LoginRequestSchema) -> LoginResponseSchema:
        """
        Метод получения валидированной Pydantic-модели с данными об авторизации пользователя.

        :param payload: Словарь с Email и Password
        :return: Валидированная Pydantic-модель с данными об авторизации пользователя
        :return: JSON-объект с данными об авторизации пользователя
        """
        response = self.login_api(payload)
        return LoginResponseSchema.model_validate_json(response.text)  # ⚠ <- Валидируем ответ (любой) -> Model
        return response.json()                                         # ⚠ <- Может вызвать ошибку, если придет не JSON

    #-------------------------------------------------- Refresh --------------------------------------------------------
    def refresh_api(self, payload: RefreshRequestSchema) -> Response:
        """
        Метод ОБНОВЛЯЕТ ТОКЕН авторизации.

        :param payload: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            url=f'{self.ENDPOINT}/refresh',
            json=payload.model_dump(by_alias=True)    # + ⚠ сериализация Model -> Dict (т.к. payload - Pydantic-модель)
        )

#=================================================== Client Builder ====================================================
def get_auth_client() -> AuthClient:
    """
    Функция создает экземпляр AuthClient с уже настроенным http-клиентом.

    :return: Готовый к использованию объект AuthenticationClient базовыми параметрами.
    """
    return AuthClient(client=get_public_http_client())


#-----------------------------------------------------------------------------------------------------------------------
