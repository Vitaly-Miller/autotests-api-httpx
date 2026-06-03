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
from tools.assertions.users_assert import assert_create_user_data_equal
from tools.data_generator import fake
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.smoke
@pytest.mark.users
class TestCreateUser:
    """v.1 - Через фикстуру создания пользователя"""
    def test_create_user_1(self, create_user_api: httpx.Response):
        response = create_user_api            # Сохраняем ответ фикстуры, но не обязательно...,
                                              # Исполняемую API-фикстуру можно сразу передавать в Assertions в качестве параметра
        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)    # Status code: 200
        assert_method(response, http.HTTPMethod.POST)     # Method POST
        assert_create_user_data_equal(response)                                   # 4-in-1 | Request Data = Response Data
        validate_json_schema(response, CreateUserResponseSchema)  # Validation JSON schema


    """v.2 - Через фикстуру получения экземпляра PublicUsersClient"""
    def test_create_user_2(self, public_users_client: PublicUsersClient):
        create_user_data = CreateUserRequestSchema()                              # # Pydantic-model with fake-data
        response = public_users_client.create_user_api(create_user_data)          # ▶ Запрос через API-метод

        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)    # Status code: 200
        assert_method(response, http.HTTPMethod.POST)     # Method POST
        assert_create_user_data_equal(response)                                   # 4-in-1 | Request Data = Response Data
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
            email=email                                                           # ... c заменой сгенерированного email на значение из parametrize
        )
        response = public_users_client.create_user_api(create_user_data)          # ▶ Запрос через API-метод

        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)    # Status code: 200
        assert_method(response, http.HTTPMethod.POST)     # Method POST
        assert_create_user_data_equal(response)                                   # 4-in-1 | Request Data = Response Data
        validate_json_schema(response, CreateUserResponseSchema)  # Validation JSON schema


    """v.4 - All manual"""
    def test_create_user_4_manual(self):
        public_users_client = get_public_users_client()  # Получение экземпляра PublicUsersClient
        create_user_data = CreateUserRequestSchema()     # Инициализация Pydantic-model с default fake-data нового пользователя
        response = public_users_client.create_user_api(create_user_data)              # ▶ Запрос через API-метод
        response_model = CreateUserResponseSchema.model_validate_json(response.text)  # Response —> Pydantic-model (deserialize for Assertions)

        # Assertions:
        # Base API assertions
        assert response.status_code == 200, '❌Incorrect status code!'           # Status code: 200 (⚠️Hard coding не рекомендуется)
        assert response.request.method == 'POST', '❌Incorrect Request Method!'  # Method POST      (⚠️Hard coding не рекомендуется)

        assert response.status_code == http.HTTPStatus.OK, '❌Incorrect status code!'          # Status code: 200  (через HTTPStatus)
        assert response.request.method == http.HTTPMethod.POST, '❌Incorrect Request Method!'  # Method POST       (через HTTPMethod)

        # Create User Data = Created User Data
        assert response_model.user.email == create_user_data.email, '❌Разные Email!'                    # проверка отправленного и полученного Email
        assert response_model.user.last_name == create_user_data.last_name, '❌Разные Last Name!'        # проверка отправленного и полученного Last Name
        assert response_model.user.first_name == create_user_data.first_name, '❌Разные First Name!'     # проверка отправленного и полученного First Name
        assert response_model.user.middle_name == create_user_data.middle_name, '❌Разные Middle Name!'  # проверка отправленного и полученного Middle Name

        # Validation JSON Schema
        jsonschema.validate(
            instance=response.json(),                             # Данные для валидации
            schema=CreateUserResponseSchema.model_json_schema(),  # JSON-схема, сгенерированная из Pidantic-схемы
            format_checker=jsonschema.FormatChecker()             # Проверка форматов
        )



#=======================================================================================================================
        # API Report
        # Tool.api_report(response)
