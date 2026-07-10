"""
🔒Private Users (Fixtures)
"""
import httpx
import pytest
import allure
from clients.users_client_private import UsersClientPrivate, get_users_client_private
from schemas.users_schema import CreateUserSchema, GetUserMeResponseSchema

#================================================ Users Client (Private) =================================================
# Users Client (Private)
@pytest.fixture
@allure.title('◎ Users Client (Private) (fixture)')
def users_client_private(create_user: CreateUserSchema) -> UsersClientPrivate:
    """
    Фикстура получения экземпляра UsersClientPrivate() (c Авторизацией)

    :param create_user: Вложенная Pydantic-фикстура создания пользователя
    :return: Экземпляр UsersClientPrivate() (c Авторизацией)
    """
    client = get_users_client_private(create_user.auth_data)
    return client                                          # UsersClientPrivate()


#----------------------------------------------------- Get User Me -----------------------------------------------------
# API
@pytest.fixture
@allure.title('▷ Get User Me (API-fixture)')
def get_user_me_api(users_client_private: UsersClientPrivate) -> httpx.Response:
    """
    API-фикстура получения данных текущего пользователя

    :param users_client_private: Фикстура вызова экземпляра UsersClientPrivate (с Авторизацией)
    :return: httpx.Response
    """
    response = users_client_private.get_user_me_api()     # ▶ Запрос через API-метод
    return response                                       # httpx.Response


# Pydantic-model
@pytest.fixture
@allure.title('▷ Get User Me (Pydantic-fixture)')
def get_user_me(users_client_private: UsersClientPrivate) -> GetUserMeResponseSchema:
    """
    Pydantic-фикстура получения данных текущего пользователя

    :param users_client_private: Экземпляр UsersClientPrivate (c Авторизацией)
    :return: Pydantic-model (GetUserMeResponseSchema)
    """
    response_model = users_client_private.get_user_me()    # ▶ Запрос через Pydantic-метод
    return response_model                                  # Pydantic-model (GetUserMeResponseSchema)


#=======================================================================================================================
