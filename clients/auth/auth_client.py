"""
Authentication Client
/authentication
"""
import httpx
from clients.api_client import APIClient
from clients.auth.auth_schema import LoginRequestSchema, RefreshRequestSchema, LoginResponseSchema
from clients.public_http_builder import get_public_http_client

#==================================================== Auth Client ======================================================
class AuthClient(APIClient):
    ENDPOINT = '/authentication'
    #--------------------------------------------------- Login ---------------------------------------------------------
    # API 🟨
    def login_api(self, payload: LoginRequestSchema) -> httpx.Response:
        """
        Метод выполняет АУТЕНТИФИКАЦИЮ (log in) пользователя

        :param payload: Данные с Email и Password в формате Pydantic-model
        :return httpx.Response
        """
        return self.post(
            url=f'{self.ENDPOINT}/login',
            json=payload.model_dump(by_alias=True)    # сериализация Model —> Dict (т.к. payload - Pydantic-модель)
        )

    # Pydantic-model
    def login(self, payload: LoginRequestSchema) -> LoginResponseSchema:
        """
        Метод выполняет АУТЕНТИФИКАЦИЮ (log in) пользователя с получением данных об авторизации в формате Pydantic-model

        :param payload: Данные с Email и Password в формате Pydantic-model
        :return: Ответ с данными об авторизации пользователя в формате Pydantic-model
        """
        response = self.login_api(payload)
        return LoginResponseSchema.model_validate_json(response.text)  # Валидируем ответ (любой) —> Model


    #-------------------------------------------------- Refresh --------------------------------------------------------
    # API 🟨
    def refresh_api(self, payload: RefreshRequestSchema) -> httpx.Response:
        """
        Метод ОБНОВЛЯЕТ ТОКЕН авторизации

        :param payload: Данные с refreshToken в формате Pydantic-model
        :return: httpx.Response
        """
        return self.post(
            url=f'{self.ENDPOINT}/refresh',
            json=payload.model_dump(by_alias=True)    # сериализация Model —> Dict (т.к. payload - Pydantic-модель)
        )


#================================================= Client (✨Helper) ===================================================
def get_auth_client() -> AuthClient:
    """
    Функция создает экземпляр AuthClient с уже настроенным http-клиентом

    :return: Готовый к использованию объект AuthenticationClient базовыми параметрами.
    """
    return AuthClient(client=get_public_http_client())

#-----------------------------------------------------------------------------------------------------------------------
