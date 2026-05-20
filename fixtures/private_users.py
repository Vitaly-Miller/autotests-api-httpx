"""
🔒Private Users fixtures
"""
import httpx
import pytest
from clients.users.private_users_client import PrivateUsersClient, get_private_users_client
from clients.users.users_schema import UserFullSchema, GetUserMeResponseSchema

#=============================================== 🔒Private Users Client ================================================
# 🔒Private Users Client
@pytest.fixture
def private_users_client(create_user: UserFullSchema) -> PrivateUsersClient:
    """
    Фикстура вызова Private Users Client (c Base URL + АВТОРИЗАЦИЯ)

    :param create_user: Фикстура создания пользователя
    :return: Экземпляр класса PrivateUsersClient (c Base URL + АВТОРИЗАЦИЯ)
    """
    return get_private_users_client(auth_data=create_user.auth_data)


#----------------------------------------------------- Get User Me -----------------------------------------------------
# API
@pytest.fixture
def get_user_me_api(private_users_client: PrivateUsersClient) -> httpx.Response:
    """
    Фикстура получения данных ТЕКУЩЕГО пользователя

    :param private_users_client: Экземпляр класса PrivateUsersClient (c Base URL + Auth)
    :return: httpx.Response
    """
    response = private_users_client.get_user_me_api()   # ▶ Запрос на получение данных ТЕКУЩЕГО пользователя
    return response                                     # httpx.Response

# Pydantic-model
@pytest.fixture
def get_user_me(private_users_client: PrivateUsersClient) -> GetUserMeResponseSchema:
    """
    Фикстура получения данных ТЕКУЩЕГО пользователя в формате Pydantic-model

    :param private_users_client: Экземпляр класса PrivateUsersClient (c Base URL + Auth)
    :return: Pydantic-model: GetUserMeResponseSchema
    """
    response = private_users_client.get_user_me()       # ▶ Запрос на получение данных ТЕКУЩЕГО пользователя
    return response                                     # Pydantic-model: GetUserMeResponseSchema

#-----------------------------------------------------------------------------------------------------------------------
