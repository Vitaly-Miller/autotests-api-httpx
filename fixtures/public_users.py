"""
Public Users fixtures
"""
import httpx
import pytest
from clients.public_users_client import get_public_users_client, PublicUsersClient
from schemas.users import CreateUserSchema, CreateUserRequestSchema

#================================================= Public Users Client =================================================
# Public Users Client
@pytest.fixture
def public_users_client() -> PublicUsersClient:
    """
    Фикстура получения экземпляра PublicUsersClient (c Base URL)

    :return: Экземпляр PublicUsersClient (c Base URL)
    """
    public_users_client = get_public_users_client()
    return public_users_client


#----------------------------------------------------- Create User -----------------------------------------------------
# API
@pytest.fixture
def create_user_api(public_users_client: PublicUsersClient) -> httpx.Response:
    """
    API-фикстура создания пользователя

    :param public_users_client: Вложенная фикстура получения экземпляра PublicUsersClient (с Base URL)
    :return: httpx.Response
    """
    create_user_data = CreateUserRequestSchema()                      # Инициализация Pydantic-model с default fake-data
    response = public_users_client.create_user_api(create_user_data)  # ▶ Запрос через API-метод.
    return response                                                   # httpx.Response
                                   # ❗️Если тут нужно добраться до Request c 'password' - через парсинг JSON —> {dict}:
                                   # request_body = json.loads(response.request.content)
                                   # password = request_body["password"]
# Pydantic-model
@pytest.fixture
def create_user(public_users_client: PublicUsersClient) -> CreateUserSchema:
    """
    Pydantic-фикстура создания пользователя

    :param public_users_client: Вложенная фикстура получения экземпляра PublicUsersClient (с Base URL)
    :return: Pydantic-model (CreateUserSchema) ✨<Request + Response>
    """
    create_user_data = CreateUserRequestSchema()                         # Инициализация модели с Default fake-data нового пользователя по Pydantic-схеме
    response_model = public_users_client.create_user(create_user_data)   # ︎▶ Запрос через Pydantic-метод
    response_full_model = CreateUserSchema(request=create_user_data, response=response_model)  # Инициализация Pydantic-model (CreateUserSchema) ✨<Request + Response>
    return response_full_model                                           # Pydantic-model (CreateUserSchema) ✨<Request + Response>


#-----------------------------------------------------------------------------------------------------------------------
