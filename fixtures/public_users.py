"""
Public Users fixtures
"""
import httpx
import pytest
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import UserFullSchema, CreateUserRequestSchema

#================================================= Public Users Client =================================================
# Public Users Client
@pytest.fixture
def public_users_client() -> PublicUsersClient:
    """
    Фикстура получения экземпляра PublicUsersClient (c Base URL)

    :return: Экземпляр PublicUsersClient (c Base URL)
    """
    client = get_public_users_client()
    return client

#----------------------------------------------------- Create User -----------------------------------------------------
# API
@pytest.fixture
def create_user_api(public_users_client: PublicUsersClient) -> httpx.Response:
    """
    API-фикстура создания пользователя

    :param public_users_client: Вложенная фикстура получения экземпляра PublicUsersClient (с Base URL)
    :return: httpx.Response
    """
    create_user_data = CreateUserRequestSchema()          # Инициализация модели с Default fake-data нового пользователя нового пользователя по Pydantic-схеме
    response = public_users_client.create_user_api(create_user_data=create_user_data)  # ▶ Запрос на создание пользователя через API-метод. Передаем fake-данные нового пользователя.
    return response                                       # httpx.Response
                                                          # ❗️Если тут нужно добраться до Request c 'password' - через парсинг JSON —> {dict}:
                                                          # request_body = json.loads(response.request.content)
                                                          # password = request_body["password"]
# Pydantic-model
@pytest.fixture
def create_user(public_users_client: PublicUsersClient) -> UserFullSchema:
    """
    Pydantic-фикстура создания пользователя

    :param public_users_client: Вложенная фикстура получения экземпляра PublicUsersClient (с Base URL)
    :return: Pydantic-model (UserFullSchema) ✨<Request + Response>
    """
    create_user_data = CreateUserRequestSchema()                                   # Инициализация модели с Default fake-data нового пользователя по Pydantic-схеме
    response = public_users_client.create_user(create_user_data=create_user_data)  # ︎▶ Запрос
    model = UserFullSchema(request=create_user_data, response=response)             # Pydantic-model (UserFullSchema) ✨с объединенными данными <Request + Response>
    return model


#-----------------------------------------------------------------------------------------------------------------------
