"""
Test Create User
"""
import http
import httpx
import pytest
import jsonschema
from clients.public_users_client import PublicUsersClient, get_public_users_client
from schemas.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base_assert import assert_status_code, assert_method
from tools.assertions.schema_assert import validate_json_schema
from tools.assertions.users_assert import assert_create_user_response_equal, assert_user_id
from tools.data_generator import fake
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.smoke
@pytest.mark.users
class TestCreateUser:
    """v.1 - Через фикстуру создания пользователя"""
    def test_create_user_1(self, create_user_api: httpx.Response):
        response = create_user_api  # Сохраняем ответ фикстуры, но не обязательно...,
                                    # Исполняемую API-фикстуру можно сразу передавать в Assertions в качестве параметра
        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)    # Status code: 200
        assert_method(response, http.HTTPMethod.POST)     # Method: POST
        assert_create_user_response_equal(response)                                   # Request data = Response data
        assert_user_id(response)                                                  # 2-in-1 | User ID validation
        validate_json_schema(response, CreateUserResponseSchema)  # Validation JSON schema


    """v.2 - Через фикстуру получения экземпляра PublicUsersClient"""
    def test_create_user_2(self, public_users_client: PublicUsersClient):
        create_user_data = CreateUserRequestSchema()                              # # Pydantic-model with fake-data
        response = public_users_client.create_user_api(create_user_data)          # ▶ Запрос через API-метод

        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)    # Status code: 200
        assert_method(response, http.HTTPMethod.POST)     # Method: POST
        assert_create_user_response_equal(response)                                   # Request data = Response data
        assert_user_id(response)                                                  # User ID validation
        validate_json_schema(response, CreateUserResponseSchema)  # Validation JSON schema


    """v.3 - Через фикстуру получения экземпляра PublicUsersClient + Параметризация"""
    @pytest.mark.parametrize(                                                     # parametrize 'email' (3-in-1)
        'email', [
            fake.email('amazon.com'),
            fake.email('gmail.com'),
            fake.email('yahoo.com')
        ]
    )
    def test_create_user_3_param(self, email: str, public_users_client: PublicUsersClient):
        create_user_data = CreateUserRequestSchema(                               # Pydantic-model with fake-data, ...
            email=email                                                           # ... значения из parametrize (3-in-1)
        )
        response = public_users_client.create_user_api(create_user_data)          # ▶ Запрос через API-метод

        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)    # Status code: 200
        assert_method(response, http.HTTPMethod.POST)     # Method: POST
        assert_create_user_response_equal(response)                                   # Request data = Response data
        assert_user_id(response)                                                  # User ID validation
        validate_json_schema(response, CreateUserResponseSchema)  # Validation JSON schema


    """v.4 - All manual"""
    def test_create_user_4_manual(self):
        public_users_client = get_public_users_client()                               # Получение экземпляра PublicUsersClient
        create_user_data = CreateUserRequestSchema()                                  # Инициализация Pydantic-model с default fake-data нового пользователя
        response = public_users_client.create_user_api(create_user_data)              # ▶ Запрос через API-метод
        response_model = CreateUserResponseSchema.model_validate_json(response.text)  # Response —> Pydantic-model (deserialize for Assertions)

        # Assertions:
        # Base API assertions
        assert response.status_code == 200, '❌Incorrect status code!'           # Status code: 200 (⚠️Hard coding не рекомендуется)
        assert response.request.method == 'POST', '❌Incorrect Request Method!'  # Method: POST     (⚠️Hard coding не рекомендуется)

        assert response.status_code == http.HTTPStatus.OK, '❌Incorrect status code!'          # Status code: 200  (через HTTPStatus)
        assert response.request.method == http.HTTPMethod.POST, '❌Incorrect Request Method!'  # Method: POST      (через HTTPMethod)

        # Request Data = Response Data
        assert response_model.user.email == create_user_data.email, '❌Разные Email!'                    # Request Email = Response Email
        assert response_model.user.last_name == create_user_data.last_name, '❌Разные Last Name!'        # Request Last Name = Response Last Name
        assert response_model.user.first_name == create_user_data.first_name, '❌Разные First Name!'     # Request First Name = Response First Name
        assert response_model.user.middle_name == create_user_data.middle_name, '❌Разные Middle Name!'  # Request Middle Name = Response Middle Name

        # User ID
        assert response_model.user.id is not None, '❌User ID is Empty!'      # User ID is NON-Empty
        assert len(response_model.user.id) == 36, '❌Wrong User ID length'    # User ID length = 36 chars

        # Validation JSON Schema
        jsonschema.validate(
            instance=response.json(),                             # Данные для валидации
            schema=CreateUserResponseSchema.model_json_schema(),  # JSON-схема, сгенерированная из Pidantic-схемы
            format_checker=jsonschema.FormatChecker()             # Проверка форматов
        )



#=======================================================================================================================
        # Tool.api_report(response)
