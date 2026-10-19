"""
Users Client (Public)
(For methods that do NOT require authorization)
"""
import httpx
import allure
from tools.api_coverage import tracker
from tools.endpoints import Endpoint
from clients.api_client import APIClient
from clients.httpx_client_public import get_httpx_client_public
from schemas.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


#================================================ Users Client (Public) ================================================
class UsersClientPublic(APIClient):
    """
    Client for working with /api/v1/users (Public)

    .
    """
    #------------------------------------------------- Create User -----------------------------------------------------
    # API
    @allure.step('▶ Create User (API)')
    @tracker.track_coverage_httpx(f'{Endpoint.USERS}')
    def create_user_api(self, create_user_data: CreateUserRequestSchema) -> httpx.Response:
        """
        API method for creating a new user

        :param create_user_data: Pydantic model with user creation data
        :return: httpx.Response
        """
        response = self.post(
            url=Endpoint.USERS,
            json=create_user_data.model_dump(by_alias=True))
        return response


    # Pydantic-model
    @allure.step('▶ Create User (Pydantic)')
    def create_user(self, create_user_data: CreateUserRequestSchema) -> CreateUserResponseSchema:
        """
        Pydantic method for creating a new user

        :param create_user_data: Pydantic model with user creation data
        :return: Pydantic-model (CreateUserResponseSchema)
        """
        response = self.create_user_api(create_user_data)
        response_model = CreateUserResponseSchema.model_validate_json(response.text)
        return response_model



#================================================== Client (builder) ===================================================
@allure.step('◎ Get Users Client (Public)')
def get_users_client_public() -> UsersClientPublic:
    """
    Returns a UsersClientPublic() instance with a configured httpx.Client (Public)

    :return: Configured UsersClientPublic() instance
    """
    users_client_public = UsersClientPublic(client=get_httpx_client_public())
    return users_client_public


#=======================================================================================================================
