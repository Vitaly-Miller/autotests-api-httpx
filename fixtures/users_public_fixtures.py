"""
Public Users (Fixtures)
"""
import httpx
import pytest
import allure
from clients.users_client_public import get_users_client_public, UsersClientPublic
from schemas.users_schema import CreateUserSchema, CreateUserRequestSchema

#================================================ Users Client (Public) ================================================
# Users Client (Public)
@pytest.fixture
@allure.title('◎ Users Client (Public) (fixture)')
def users_client_public() -> UsersClientPublic:
    """
    Fixture that provides a UsersClientPublic() instance (with Base URL)

    :return: UsersClientPublic() instance (with Base URL)
    """
    users_client_public = get_users_client_public()
    return users_client_public


#----------------------------------------------------- Create User -----------------------------------------------------
# API
@pytest.fixture
@allure.title('▷ Create User (API-fixture)')
def create_user_api(users_client_public: UsersClientPublic) -> httpx.Response:
    """
    API fixture that creates a user

    :param users_client_public: Nested fixture that provides a UsersClientPublic instance (with Base URL)
    :return: httpx.Response
    """
    create_user_data = CreateUserRequestSchema()
    response = users_client_public.create_user_api(create_user_data)
    return response


# Pydantic-model (full)
@pytest.fixture
@allure.title('▷ Create User (Pydantic-fixture)')
def create_user(users_client_public: UsersClientPublic) -> CreateUserSchema:
    """
    Pydantic fixture that creates a user

    :param users_client_public: Nested fixture that provides a UsersClientPublic instance (with Base URL)
    :return: Pydantic-model (CreateUserSchema) ✨<Request + Response>
    """
    create_user_data = CreateUserRequestSchema()
    response_model = users_client_public.create_user(create_user_data)
    response_model_full = CreateUserSchema(request=create_user_data, response=response_model)
    return response_model_full


#=======================================================================================================================
