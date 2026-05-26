"""
Test Create User
"""
import httpx
import pytest
import jsonschema
from clients.public_users_client import PublicUsersClient, get_public_users_client
from schemas.users import CreateUserRequestSchema, CreateUserResponseSchema
from http import HTTPStatus, HTTPMethod
from tools.assertions.base_assert import assert_status_code, assert_method
from tools.assertions.schema_assert import validation_json_schema
from tools.assertions.users_assert import assert_user_data_fields
from tools.data_generator import fake
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.smoke
@pytest.mark.users
class TestCreateUser:
    """Через фикстуру создания пользователя"""
    def test_create_user_1(self, create_user_api: httpx.Response):
        response = create_user_api                           # Сохраняем ответ фикстуры, но не обязательно
                                                             # Исполняемую API-фикстуру можно сразу передавать в Assertions в качестве параметра
        #------------------------ Assertions ------------------------
        # Base API assertions
        assert_status_code(response, HTTPStatus.OK)
        assert_method(response, HTTPMethod.POST)

        # Value equal
        assert_user_data_fields(response=response)  # Проверка совпадения полей Запроса и Ответа

        # Validation JSON Schema
        validation_json_schema(response, CreateUserResponseSchema)



    """Через фикстуру получения экземпляра PublicUsersClient"""
    def test_create_user_2(self, public_users_client: PublicUsersClient):
        create_user_data = CreateUserRequestSchema()       # Инициализация Pydantic-модели с генерацией fake User data нового пользователя
        response = public_users_client.create_user_api(create_user_data=create_user_data)   # ▶ Запрос через API-метод

        #------------------------ Assertions ------------------------
        # Base API assertions
        assert_status_code(response, HTTPStatus.OK)
        assert_method(response, HTTPMethod.POST)

        # Value equal (Проверка совпадения полей запроса и ответа 4-in-1)
        assert_user_data_fields(response=response)

        # Validation JSON Schema
        validation_json_schema(response, CreateUserResponseSchema)



    """Через фикстуру получения экземпляра PublicUsersClient + Параметризация"""
    @pytest.mark.parametrize(                                      # email parametrize (3-in-1)
        'email', [
            fake.email('amazon.com'),
            fake.email('gmail.com'),
            fake.email('yahoo.com')
        ]
    )
    def test_create_user_param(self, email: str, public_users_client: PublicUsersClient):
        create_user_data = CreateUserRequestSchema(email=email)    # Инициализация Pydantic-модели с default-генерацией fake User data нового пользователя, ...
                                                                   # ... c заменой сгенерированного email на значение из parametrize
        response = public_users_client.create_user_api(create_user_data=create_user_data)   # ▶ Запрос через API-метод

        #------------------------ Assertions ------------------------
        # Base API assertions
        assert_status_code(response, HTTPStatus.OK)
        assert_method(response, HTTPMethod.POST)

        # Value equal (Проверка совпадения полей запроса и ответа 4-in-1)
        assert_user_data_fields(response=response)

        # Validation JSON Schema
        validation_json_schema(response, CreateUserResponseSchema)



    """All manual"""
    def test_create_user_manual(self):
        public_users_client = get_public_users_client()  # Получение экземпляра PublicUsersClient
        create_user_data = CreateUserRequestSchema()     # Инициализация Pydantic-model с default fake-data нового пользователя
        response = public_users_client.create_user_api(create_user_data=create_user_data)  # ▶ Запрос через API-метод
        response_model = CreateUserResponseSchema.model_validate_json(response.text)       # Response —> Pydantic-model (deserialize for Assertions)

        #------------------------ Assertions ------------------------
        # Base API assertions (⚠️Hard coding не рекомендуется)
        assert response.status_code == 200, '❌Status code is incorrect!'           # проверка статус-кода    (Hard coding)
        assert response.request.method == 'POST', '❌Request Method is incorrect!'  # проверка метода запроса (Hard coding)

        # Base API assertions (через HTTPStatus и HTTPMethod)
        assert response.status_code == HTTPStatus.OK, '❌Incorrect status code!'          # проверка статус-кода    (через HTTPStatus)
        assert response.request.method == HTTPMethod.POST, '❌Incorrect Request Method!'  # проверка метода запроса (через HTTPMethod)

        # Fields values assertions
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
        Tool.api_report(response)
