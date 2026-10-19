"""
Users Client (🔒Private)
(For methods that require authorization)
"""
import httpx
import allure
from tools.api_coverage import tracker
from tools.endpoints import Endpoint
from clients.api_client import APIClient
from schemas.auth_schema import AuthDataSchema
from clients.httpx_client_private import get_httpx_client_private
from schemas.users_schema import (
    UpdateUserRequestSchema,
    GetUserResponseSchema,
    GetUserMeResponseSchema,
    UserUpdateResponseSchema
)

#============================================== Users Client (Private) ===============================================
class UsersClientPrivate(APIClient):
    """
    Client for working with /api/v1/users (🔒Private)

    .
    """
    #--------------------------------------------------- Get User Me ---------------------------------------------------
    # API
    @allure.step('▶ Get User Me (API)')
    @tracker.track_coverage_httpx(f'{Endpoint.USERS}/me')
    def get_user_me_api(self) -> httpx.Response:
        """
        API method for getting the current user's data

        :return: httpx.Response
        """
        response = self.get(url=f'{Endpoint.USERS}/me')
        return response


    # Pydantic-model
    @allure.step('▶ Get User Me (Pydantic)')
    def get_user_me(self) -> GetUserMeResponseSchema:
        """
        Pydantic method for getting the current user's data

        :return: Pydantic-model (GetUserMeResponseSchema)
        """
        response = self.get_user_me_api()
        response_model = GetUserMeResponseSchema.model_validate_json(response.text)
        return response_model


    #---------------------------------------------------- Get User -----------------------------------------------------
    # API
    @allure.step('▶ Get User by ID (API)')
    @tracker.track_coverage_httpx(f'{Endpoint.USERS}/{{user_id}}')
    def get_user_api(self, user_id: str) -> httpx.Response:
        """
        API method for getting user data by User-ID

        :param user_id: User-ID
        :return: httpx.Response
        """
        response = self.get(url=f'{Endpoint.USERS}/{user_id}')
        return response


    # Pydantic-model
    @allure.step('▶ Get User by ID (Pydantic)')
    def get_user_pydantic(self, user_id: str) -> GetUserResponseSchema:
        """
        Pydantic method for getting user data by User-ID

        :param user_id: User-ID
        :return: Pydantic-model (GetUserResponseSchema)
        """
        response = self.get_user_api(user_id)
        response_model = GetUserResponseSchema.model_validate_json(response.text)
        return response_model


    #--------------------------------------------------- Update User ---------------------------------------------------
    # API
    @allure.step('▶ Update User by ID (API)')
    @tracker.track_coverage_httpx(f'{Endpoint.USERS}/{{user_id}}')
    def update_user_api(self, user_id: str, update_data: UpdateUserRequestSchema) -> httpx.Response:
        """
        API method for partially updating a user by User-ID

        :param user_id: User-ID
        :param update_data: Pydantic model with the data to update
        :return: httpx.Response
        """
        response = self.patch(
            url=f'{Endpoint.USERS}/{user_id}',
            json=update_data.model_dump(by_alias=True)
        )
        return response


    # Pydantic-model
    @allure.step('▶ Update User by ID (Pydantic)')
    def update_user_pydantic(self, user_id: str, update_data: UpdateUserRequestSchema) -> UserUpdateResponseSchema:
        """
        Pydantic method for partially updating a user by User-ID

        :param user_id: User-ID
        :param update_data: Pydantic model with the data to update
        :return: Pydantic-model (UserUpdateResponseSchema)
        """
        response = self.update_user_api(user_id, update_data)
        response_model = UserUpdateResponseSchema.model_validate_json(response.text)
        return response_model


    #--------------------------------------------------- Delete User ---------------------------------------------------
    # API
    @allure.step('▶ Delete User by ID (API)')
    @tracker.track_coverage_httpx(f'{Endpoint.USERS}/{{user_id}}')
    def delete_user_api(self, user_id: str) -> httpx.Response:
        """
        API method for deleting a user by User-ID

        :param user_id: User-ID
        :return: httpx.Response
        """
        response = self.delete(url=f'{Endpoint.USERS}/{user_id}')
        return response



#================================================== Client (builder) ===================================================
@allure.step('◎ Get Users Client (Private)')
def get_users_client_private(auth_data: AuthDataSchema) -> UsersClientPrivate:
    """
    Returns a UsersClientPrivate() instance with a configured httpx.Client (Private)

    :param auth_data: Pydantic model with user authentication data (email, password)
    :return: Configured UsersClientPrivate() instance
    """
    users_client_private = UsersClientPrivate(client=get_httpx_client_private(auth_data))
    return users_client_private


#=======================================================================================================================
