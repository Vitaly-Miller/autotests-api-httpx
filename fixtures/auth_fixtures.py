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
    Фикстура получения экземпляра AuthClient() (c Base URL)

    :return: Экземпляр AuthClient() (c Base URL)
    """
    auth_client = get_auth_client()
    return auth_client                                          # AuthClient()

#-------------------------------------------------------- Auth ---------------------------------------------------------
# API
@pytest.fixture
@allure.title('▷ Authenticate User (API-fixture)')
def auth_api(create_user: CreateUserSchema, auth_client: AuthClient) -> httpx.Response:
    """
    API-фикстура авторизации пользователя (Log in)

    :param create_user: Вложенная Pydantic-фикстура создания пользователя
    :param auth_client: Вложенная фикстура получения экземпляра AuthClient (c Base URL)
    :return: httpx.Response
    """
    response = auth_client.login_api(create_user.auth_data)     # ▶ Запрос через API-метод
    return response                                             # httpx.Response


# Pydantic-model
@pytest.fixture
@allure.title('▷ Authenticate User (Pydantic-fixture)')
def auth(create_user: CreateUserSchema, auth_client: AuthClient) -> AuthResponseSchema:
    """
    Pydantic-фикстура авторизации пользователя (Log in)

    :param create_user: Вложенная Pydantic-фикстура создания пользователя
    :param auth_client: Вложенная фикстура получения экземпляра AuthClient (c Base URL)
    :return: Pydantic-model (AuthResponseSchema)
    """
    response_model = auth_client.login_pydantic(create_user.auth_data)   # ▶ Запрос через Pydantic-метод
    return response_model                                                # Pydantic-model (AuthResponseSchema)

#-----------------------------------------------------------------------------------------------------------------------
