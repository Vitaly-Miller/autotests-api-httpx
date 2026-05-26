"""
Test Get User Me
"""
import httpx
import pytest
import jsonschema
from clients.private_users_client import get_private_users_client, PrivateUsersClient
from clients.public_users_client import get_public_users_client
from schemas.auth import AuthUserSchema
from schemas.users import CreateUserRequestSchema, CreateUserResponseSchema, GetUserMeResponseSchema, UserFullSchema
from http import HTTPStatus, HTTPMethod
from tools.assertions.base_assert import assert_status_code, assert_method
from tools.assertions.get_user_me_assert import assert_get_user_me_response_fields
from tools.assertions.schema_assert import validation_json_schema
from tools.assertions.users_assert import assert_user_data_fields
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.smoke
@pytest.mark.users
class TestGetUserMe:
    """Через фикстуру получения данных текущего пользователя"""
    def test_get_user_me_1(self, get_user_me_api: httpx.Response):
        response = get_user_me_api      # Сохраняем ответ фикстуры, но не обязательно
                                        # Исполняемую API-фикстуру можно сразу передавать в Assertions в качестве параметра

        #------------------------ Assertions ------------------------
        # Base API assertions
        assert_status_code(response, HTTPStatus.OK)
        assert_method(response, HTTPMethod.GET)

        # # (6-in-1) NON-Empty value, ID length
        # Нет доступа к Request внутренней фикстуры Create User

        # User ID присвоен
        assert_get_user_me_response_fields(response=response)

        # Validation JSON Schema
        validation_json_schema(response, GetUserMeResponseSchema)



    """Через фикстуру создания пользователя"""
    def test_get_user_me_2(self, create_user: UserFullSchema):
        auth_data = create_user.auth_data                        # Получаем авторизационные данные через свойство UserFullSchema .auth_data
        get_user_me_client = get_private_users_client(auth_data) # Получаем экземпляр PrivateUsersClient (с Авторизацией))
        response = get_user_me_client.get_user_me_api()          # ▶ Запрос через API-метод

        #------------------------ Assertions ------------------------
        # Base API assertions
        assert_status_code(response, HTTPStatus.OK)
        assert_method(response, HTTPMethod.GET)

        # Fields assertions
        assert_user_data_fields(response, create_user.request)

        # (6-in-1) NON-Empty value, ID length
        assert_get_user_me_response_fields(response=response)

        # Validation JSON Schema
        validation_json_schema(response, GetUserMeResponseSchema)



    """Через фикстуру получения экземпляра PrivateUsersClient"""
    def test_get_user_me_3(self, private_users_client: PrivateUsersClient):
        response = private_users_client.get_user_me_api()   # ▶ Запрос через API-метод

        #------------------------ Assertions ------------------------
        # Base API assertions
        assert_status_code(response, HTTPStatus.OK)
        assert_method(response, HTTPMethod.GET)

        # Fields assertions
        # PASS: Нет доступа к Request внутренней фикстуры <create_user>

        # (6-in-1) NON-Empty value, ID length
        assert_get_user_me_response_fields(response=response)

        # Validation JSON Schema
        validation_json_schema(response, GetUserMeResponseSchema)



    """All manual"""
    def test_get_user_me_manual(self):
        #----------------------- Pre-conditions --------------------
        # Create User
        public_users_client = get_public_users_client()   # Получаем экземпляр PublicUsersClient (с Base URL)
        create_user_data = CreateUserRequestSchema()      # Инициализация Pydantic-модели с default fake-data нового пользователя
        public_users_client.create_user(create_user_data=create_user_data)  # ▶ Запрос через Pydantic-метод
        auth_data = AuthUserSchema(                       # Инициализируем модель с данными для авторизации
            email=create_user_data.email,                 # Вытаскиваем Email из Pydantic-модели
            password=create_user_data.password            # Вытаскиваем Password из Pydantic-модели
        )
        #------------------------ Get User Me -----------------------
        get_user_me_client = get_private_users_client(auth_data)  # Получаем экземпляр PrivateUsersClient
        response = get_user_me_client.get_user_me_api()           # ▶ Запрос через API-метод

        response_model = CreateUserResponseSchema.model_validate_json(response.text)  # Response —> Pydantic-model (Deserialize for Assertions)

        #------------------------ Assertions ------------------------
        # Base API assertions (⚠️Hard coding не рекомендуется)
        assert response.status_code == 200, '❌Status code is incorrect!'           # проверка статус-кода    (Hard coding)
        assert response.request.method == 'GET', '❌Request Method is incorrect!'   # проверка метода запроса (Hard coding)

        # Base API assertions (через HTTPStatus и HTTPMethod)
        assert response.status_code == HTTPStatus.OK, '❌Incorrect status code!'         # проверка статус-кода    (через HTTPStatus)
        assert response.request.method == HTTPMethod.GET, '❌Incorrect Request Method!'  # проверка метода запроса (через HTTPMethod)

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
