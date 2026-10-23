"""
🔒Private Users (Fixtures)
"""
import httpx
import pytest
import allure
from clients.users_client_private import UsersClientPrivate, get_users_client_private
from schemas.users_schema import CreateUserSchema, GetUserMeResponseSchema

#=============================================== Users Client (Private) ================================================
# Users Client (Private)
@pytest.fixture
@allure.title('◎ Users Client (Private) (fixture)')
def users_client_private(create_user: CreateUserSchema) -> UsersClientPrivate:
    """
    Fixture that provides a UsersClientPrivate() instance (with Authorization)

    :param create_user: Nested Pydantic fixture that creates a user
    :return: UsersClientPrivate() instance (with Authorization)
    """
    client = get_users_client_private(create_user.auth_data)
    return client                                          # UsersClientPrivate()


#----------------------------------------------------- Get User Me -----------------------------------------------------
# API
@pytest.fixture
@allure.title('▷ Get User Me (API-fixture)')
def get_user_me_api(users_client_private: UsersClientPrivate) -> httpx.Response:
    """
    API fixture that gets the current user's data

    :param users_client_private: Fixture that provides a UsersClientPrivate instance (with Authorization)
    :return: httpx.Response
    """
    response = users_client_private.get_user_me_api()     # ▶ Request via API method
    return response                                       # httpx.Response


# Pydantic-model
@pytest.fixture
@allure.title('▷ Get User Me (Pydantic-fixture)')
def get_user_me(users_client_private: UsersClientPrivate) -> GetUserMeResponseSchema:
    """
    Pydantic fixture that gets the current user's data

    :param users_client_private: UsersClientPrivate instance (with Authorization)
    :return: Pydantic-model (GetUserMeResponseSchema)
    """
    response_model = users_client_private.get_user_me()    # ▶ Request via Pydantic method
    return response_model                                  # Pydantic-model (GetUserMeResponseSchema)


#=======================================================================================================================
