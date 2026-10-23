"""
Authentication (Fixtures)
"""
import httpx
import pytest
import allure
from clients.auth_client import AuthClient, get_auth_client
from schemas.auth_schema import AuthResponseSchema
from schemas.users_schema import CreateUserSchema

#===================================================== Auth Client =====================================================
# Auth Client
@pytest.fixture
@allure.title('◎ Auth Client (fixture)')
def auth_client() -> AuthClient:
    """
    Fixture that provides an AuthClient() instance (with Base URL)

    :return: AuthClient() instance (with Base URL)
    """
    auth_client = get_auth_client()
    return auth_client                                          # AuthClient()


#-------------------------------------------------------- Auth ---------------------------------------------------------
# API
@pytest.fixture
@allure.title('▷ Authenticate User (API-fixture)')
def auth_api(create_user: CreateUserSchema, auth_client: AuthClient) -> httpx.Response:
    """
    API fixture for user authorization (Log in)

    :param create_user: Nested Pydantic fixture that creates a user
    :param auth_client: Nested fixture that provides an AuthClient instance (with Base URL)
    :return: httpx.Response
    """
    response = auth_client.login_api(create_user.auth_data)     # ▶ Request via API method
    return response                                             # httpx.Response


# Pydantic-model
@pytest.fixture
@allure.title('▷ Authenticate User (Pydantic-fixture)')
def auth(create_user: CreateUserSchema, auth_client: AuthClient) -> AuthResponseSchema:
    """
    Pydantic fixture for user authorization (Log in)

    :param create_user: Nested Pydantic fixture that creates a user
    :param auth_client: Nested fixture that provides an AuthClient instance (with Base URL)
    :return: Pydantic-model (AuthResponseSchema)
    """
    response_model = auth_client.login_pydantic(create_user.auth_data)   # ▶ Request via Pydantic method
    return response_model                                                # Pydantic-model (AuthResponseSchema)


#=======================================================================================================================
