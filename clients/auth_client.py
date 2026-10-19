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
    Client for working with /api/v1/authentication
    """
    #--------------------------------------------------- Login ---------------------------------------------------------
    # API
    @allure.step('▶ Login User (API)')
    @tracker.track_coverage_httpx(f'{Endpoint.AUTH}/login')
    def login_api(self, auth_data: AuthDataSchema) -> httpx.Response:
        """
        API method for user authentication (log in)

        :param auth_data: Pydantic model with authentication data (email and password)
        :return: httpx.Response
        """
        response = self.post(
            url=f'{Endpoint.AUTH}/login',
            json=auth_data.model_dump(by_alias=True)
        )
        return response


    # Pydantic-model
    @allure.step('▶ Login User (Pydantic)')
    def login_pydantic(self, auth_data: AuthDataSchema) -> AuthResponseSchema:
        """
        Pydantic method for user authentication (log in)

        :param auth_data: Email and password as a Pydantic model
        :return: User authentication response as a Pydantic model
        """
        response = self.login_api(auth_data)
        response_model = AuthResponseSchema.model_validate_json(response.text)
        return response_model


    #-------------------------------------------------- Refresh --------------------------------------------------------
    # API
    @allure.step('▶ Refresh Token (API)')
    @tracker.track_coverage_httpx(f'{Endpoint.AUTH}/refresh')
    def refresh_api(self, refresh_token: RefreshRequestSchema) -> httpx.Response:
        """
        API method for refreshing the access token

        :param refresh_token: Pydantic model with refresh_token
        :return: httpx.Response
        """
        response = self.post(
            url=f'{Endpoint.AUTH}/refresh',
            json=refresh_token.model_dump(by_alias=True)
        )
        return response


#================================================== Client (builder) ===================================================
@allure.step('◎ Get Auth Client')
def get_auth_client() -> AuthClient:
    """
    Returns an AuthClient instance with a preconfigured HTTP client

    :return: AuthClient instance (with Base URL)
    """
    auth_client = AuthClient(client=get_httpx_client_public())
    return auth_client


#=======================================================================================================================
