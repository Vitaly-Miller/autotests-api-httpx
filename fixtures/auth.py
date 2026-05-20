"""
Auth (Authentication) fixtures
"""
import httpx
import pytest
from clients.auth.auth_client import AuthClient, get_auth_client
from clients.auth.auth_schema import AuthUserResponseSchema
from clients.users.users_schema import UserFullSchema

#===================================================== Auth Client =====================================================
# Auth Client
@pytest.fixture
def auth_client() -> AuthClient:
    """
    Фикстура вызова Auth Client (c Base URL)

    :return: Экземпляр класса AuthClient (c Base URL)
    """
    return get_auth_client()

#------------------------------------------------ Auth (Authentication) ------------------------------------------------
# API
@pytest.fixture
def auth_user_api(create_user: UserFullSchema, auth_client: AuthClient) -> httpx.Response:
    """
    API-фикстура АВТОРИЗАЦИИ (Log in) пользователя

    :param create_user: Вложенная фикстура СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ (Create User)
    :param auth_client: Вложенная фикстура АВТОРИЗАЦИИ пользователя (Log in)
    :return: httpx.Response
    """
    response = auth_client.login_api(auth_data=create_user.auth_data)    # ▶ Запрос на Authentication (Log in) через API-метод. Передаем auth_data c Email и Password и сохраняем ответ в переменную.
    return response                                                      # httpx.Response


# Pydantic-model
@pytest.fixture
def auth_user(create_user: UserFullSchema, auth_client: AuthClient) -> AuthUserResponseSchema:
    """
    Фикстура АВТОРИЗАЦИИ (Log in) пользователя (Pydantic-model)

    :param create_user: Вложенная Pydantic-model-фикстура СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ (Create User)
    :param auth_client: Вложенная фикстура АВТОРИЗАЦИИ пользователя (Log in)
    :return: Pydantic-model: AuthUserResponseSchema
    """
    response = auth_client.login(auth_data=create_user.auth_data)        # ▶ Запрос на Authentication (Log in). Передаем auth_data c Email и Password и сохраняем ответ в переменную.
    return response                                                      # Pydantic-model: AuthUserResponseSchema

#-----------------------------------------------------------------------------------------------------------------------
