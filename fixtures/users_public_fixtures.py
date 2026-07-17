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
    Фикстура получения экземпляра UsersClientPublic() (c Base URL)

    :return: Экземпляр UsersClientPublic() (c Base URL)
    """
    users_client_public = get_users_client_public()
    return users_client_public     # UsersClientPublic()


#----------------------------------------------------- Create User -----------------------------------------------------
# API
@pytest.fixture
@allure.title('▷ Create User (API-fixture)')
def create_user_api(users_client_public: UsersClientPublic) -> httpx.Response:
    """
    API-фикстура создания пользователя

    :param users_client_public: Вложенная фикстура получения экземпляра UsersClientPublic (с Base URL)
    :return: httpx.Response
    """
    create_user_data = CreateUserRequestSchema()                      # Инициализация Pydantic-model с default fake-data
    response = users_client_public.create_user_api(create_user_data)  # ▶ Запрос через API-метод.
    return response                                                   # httpx.Response
                                   # ❗️Если тут нужно добраться до Request c 'password' - через парсинг JSON —> {dict}:
                                   # request_body = json.loads(response.request.content)
                                   # password = request_body["password"]
# Pydantic-model (full)
@pytest.fixture
@allure.title('▷ Create User (Pydantic-fixture)')
def create_user(users_client_public: UsersClientPublic) -> CreateUserSchema:
    """
    Pydantic-фикстура создания пользователя

    :param users_client_public: Вложенная фикстура получения экземпляра UsersClientPublic (с Base URL)
    :return: Pydantic-model (CreateUserSchema) ✨<Request + Response>
    """
    create_user_data = CreateUserRequestSchema()                                               # Инициализация модели с Default fake-data нового пользователя по Pydantic-схеме
    response_model = users_client_public.create_user(create_user_data)                         # ︎▶ Запрос через Pydantic-метод
    response_model_full = CreateUserSchema(request=create_user_data, response=response_model)  # Инициализация Pydantic-model (CreateUserSchema) ✨<Request + Response>
    return response_model_full                                                                 # Pydantic-model (CreateUserSchema) ✨<Request + Response>


#=======================================================================================================================
