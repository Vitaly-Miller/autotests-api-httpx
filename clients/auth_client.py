"""
Authentication Client
"""
import httpx
from clients.api_client import APIClient
from schemas.auth_schema import RefreshRequestSchema, AuthDataSchema, AuthResponseSchema
from clients.httpx_public_client import get_httpx_public_client

#==================================================== Auth Client ======================================================
class AuthClient(APIClient):
    ENDPOINT = '/authentication'
    #--------------------------------------------------- Login ---------------------------------------------------------
    # API
    def login_api(self, auth_data: AuthDataSchema) -> httpx.Response:
        """
        API-метод аутентификации пользователя (Log in)

        :param auth_data: Pydantic-model c данными для аутентификации (Email и Password)
        :return httpx.Response
        """
        response = self.post(                           # ▶ Запрос
            url=f'{self.ENDPOINT}/login',
            json=auth_data.model_dump(by_alias=True)    # Pydantic-model —> Dict (serialize)
        )
        return response

    # Pydantic-model
    def login_pydantic(self, auth_data: AuthDataSchema) -> AuthResponseSchema:
        """
        Pydantic-метод аутентификации пользователя (Log in)

        :param auth_data: Данные с Email и Password в формате Pydantic-model
        :return: Ответ с данными об авторизации пользователя в формате Pydantic-model
        """
        response = self.login_api(auth_data)                               # ▶ Запрос через API-метод
        response_model = AuthResponseSchema.model_validate_json(response.text)  # Response —> Pydantic-model (deserialize)
        return response_model


    #-------------------------------------------------- Refresh --------------------------------------------------------
    # API
    def refresh_api(self, refresh_token: RefreshRequestSchema) -> httpx.Response:
        """
        API-метод обновления токена авторизации

        :param refresh_token: Pydantic-model c refresh_token
        :return: httpx.Response
        """
        response = self.post(                                # ▶ Запрос
            url=f'{self.ENDPOINT}/refresh',
            json=refresh_token.model_dump(by_alias=True)     # Pydantic-model —> Dict (serialize)
        )
        return response


#================================================= Client (✨Helper) ===================================================
def get_auth_client() -> AuthClient:
    """
    Функция получения экземпляра AuthClient с уже настроенным http-клиентом

    :return: Экземпляр AuthClient с (Base URL)
    """
    auth_client = AuthClient(client=get_httpx_public_client())
    return auth_client

#-----------------------------------------------------------------------------------------------------------------------
