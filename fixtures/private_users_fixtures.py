"""
🔒Private Users (Fixtures)
"""
import httpx
import pytest
import allure
from clients.private_users_client import PrivateUsersClient, get_private_users_client
from schemas.users_schema import CreateUserSchema, GetUserMeResponseSchema

#================================================ Private Users Client =================================================
# Private Users Client
@pytest.fixture
@allure.title('Private Users Client (fixture)')
def private_users_client(create_user: CreateUserSchema) -> PrivateUsersClient:
    """
    Фикстура получения экземпляра PrivateUsersClient() (c Авторизацией)

    :param create_user: Вложенная Pydantic-фикстура создания пользователя
    :return: Экземпляр PrivateUsersClient() (c Авторизацией)
    """
    client = get_private_users_client(create_user.auth_data)
    return client                                          # PrivateUsersClient()


#----------------------------------------------------- Get User Me -----------------------------------------------------
# API
@pytest.fixture
@allure.title('Get User Me (API-fixture)')
def get_user_me_api(private_users_client: PrivateUsersClient) -> httpx.Response:
    """
    API-фикстура получения данных текущего пользователя

    :param private_users_client: Фикстура вызова экземпляра PrivateUsersClient (с Авторизацией)
    :return: httpx.Response
    """
    response = private_users_client.get_user_me_api()     # ▶ Запрос через API-метод
    return response                                       # httpx.Response


# Pydantic-model
@pytest.fixture
@allure.title('Get User Me (Pydantic-fixture)')
def get_user_me(private_users_client: PrivateUsersClient) -> GetUserMeResponseSchema:
    """
    Pydantic-фикстура получения данных текущего пользователя

    :param private_users_client: Экземпляр PrivateUsersClient (c Авторизацией)
    :return: Pydantic-model (GetUserMeResponseSchema)
    """
    response_model = private_users_client.get_user_me()    # ▶ Запрос через Pydantic-метод
    return response_model                                           # Pydantic-model (GetUserMeResponseSchema)


#-----------------------------------------------------------------------------------------------------------------------
