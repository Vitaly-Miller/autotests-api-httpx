"""
Authentication Client
"""
import allure
import httpx
from tools.api_coverage import tracker
from tools.endpoints import Endpoint
from clients.api_client import APIClient
from clients.httpx_client_public import get_httpx_client_public
from schemas.auth_schema import RefreshRequestSchema, AuthDataSchema, AuthResponseSchema

#===================================================== Auth Client =====================================================
class AuthClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication

    .
    """
    #--------------------------------------------------- Login ---------------------------------------------------------
    # API
    @allure.step('▶ Login User (API)')                                 # Allure step Title
    @tracker.track_coverage_httpx(f'{Endpoint.AUTH}/login')            # API Coverage tracker
    def login_api(self, auth_data: AuthDataSchema) -> httpx.Response:
        """
        API-метод аутентификации пользователя (Log in)

        :param auth_data: Pydantic-model c данными для аутентификации (Email и Password)
        :return httpx.Response
        """
        response = self.post(                                          # ▶ Запрос
            url=f'{Endpoint.AUTH}/login',                              # Endpoint (by Enum)
            json=auth_data.model_dump(by_alias=True)                   # Pydantic-model —> Dict (serialize)
        )
        return response                                                # httpx.Response


    # Pydantic-model
    @allure.step('▶ Login User (Pydantic)')                                     # Allure step Title
    def login_pydantic(self, auth_data: AuthDataSchema) -> AuthResponseSchema:
        """
        Pydantic-метод аутентификации пользователя (Log in)

        :param auth_data: Данные с Email и Password в формате Pydantic-model
        :return: Ответ с данными об авторизации пользователя в формате Pydantic-model
        """
        response = self.login_api(auth_data)                                    # ▶ Запрос через API-метод
        response_model = AuthResponseSchema.model_validate_json(response.text)  # httpx.Response —> Pydantic-model (deserialize)
        return response_model                                                   # Pydantic-model (AuthResponseSchema)


    #-------------------------------------------------- Refresh --------------------------------------------------------
    # API
    @allure.step('▶ Refresh Token (API)')                              # Allure step Title
    @tracker.track_coverage_httpx(f'{Endpoint.AUTH}/refresh')          # API Coverage tracker
    def refresh_api(self, refresh_token: RefreshRequestSchema) -> httpx.Response:
        """
        API-метод обновления токена авторизации

        :param refresh_token: Pydantic-model c refresh_token
        :return: httpx.Response
        """
        response = self.post(                                          # ▶ Запрос
            url=f'{Endpoint.AUTH}/refresh',                            # Endpoint (by Enum)
            json=refresh_token.model_dump(by_alias=True)               # Pydantic-model —> Dict (serialize)
        )
        return response                                                # httpx.Response


#================================================== Client (builder) ===================================================
@allure.step('◎ Get Auth Client')                                      # Allure step Title
def get_auth_client() -> AuthClient:
    """
    Функция получения экземпляра AuthClient с уже настроенным http-клиентом

    :return: Экземпляр AuthClient с (Base URL)
    """
    auth_client = AuthClient(client=get_httpx_client_public())
    return auth_client                                                 # AuthClient()

#=======================================================================================================================
