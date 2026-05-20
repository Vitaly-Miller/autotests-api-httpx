"""
Public Users fixtures
"""
import httpx
import pytest
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import UserFullSchema, CreateUserRequestSchema

#================================================= Public Users Client =================================================
# Public Users Client
@pytest.fixture   # scope='function' by Default
def public_users_client() -> PublicUsersClient:
    """
    Фикстура вызова класса Public Users Client (c Base URL)

    :return: Экземпляр класса PublicUsersClient (c Base URL)
    """
    return get_public_users_client()

#----------------------------------------------------- Create User -----------------------------------------------------
# API
@pytest.fixture
def create_user_api(public_users_client: PublicUsersClient) -> httpx.Response:
    """
    API-фикстура СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ (Create User)

    :param public_users_client: Вложенная фикстура Public Users Client
    :return: httpx.Response
    """
    create_user_data = CreateUserRequestSchema()          # Инициализация модели с fake-данными нового пользователя по Pydantic-схеме
    response = public_users_client.create_user_api(create_user_data=create_user_data)  # ▶ Запрос на создание пользователя через метод. Передаем fake-данные нового пользователя.
    return response                                       # httpx.Response
                                                          # ❗️Если нужно добраться до Request c 'password' - через парсинг JSON —> {dict}:
                                                          # request_body = json.loads(response.request.content)
                                                          # password = request_body["password"]
# Pydantic-model
@pytest.fixture
def create_user(public_users_client: PublicUsersClient) -> UserFullSchema:
    """
    Фикстура СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ (Create User)

    :param public_users_client: Вложенная фикстура Public Users Client
    :return: ✨Pydantic-model: UserFullSchema с объединенными данными пользователя <Request + Response>
    """
    create_user_data = CreateUserRequestSchema()                         # Инициализация модели с fake-данными нового пользователя по Pydantic-схеме
    response = public_users_client.create_user(create_user_data=create_user_data) # ︎▶ Запрос на создание пользователя. Передаем fake-данные нового пользователя.
    return UserFullSchema(request=create_user_data, response=response)   # Pydantic-model: UserFullSchema ✨с объединенными данными пользователя <Request + Response>


#-----------------------------------------------------------------------------------------------------------------------
