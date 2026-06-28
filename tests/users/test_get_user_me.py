"""
TEST Get User Me
"""
import httpx
import pytest
import allure
import jsonschema
from clients.private_users_client import get_private_users_client, PrivateUsersClient
from clients.public_users_client import get_public_users_client
from schemas.auth_schema import AuthDataSchema
from schemas.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserMeResponseSchema
from http import HTTPStatus, HTTPMethod
from tools.allure.annotations import Tag, Epic, Feature, Story
from tools.assertions.base_assert import assert_status_code, assert_method
from tools.assertions.schema_assert import validate_json_schema
from tools.assertions.users_assert import assert_create_user_response_non_empty, assert_user_id
from tools.tool import Tool

#=======================================================================================================================
# Class annotations
@pytest.mark.users                                   # ┐ Pytest Marks
@pytest.mark.smoke                                   # ┘
@allure.tag(Tag.SMOKE, Tag.USERS, Tag.GET)     # ] Allure Tags
@allure.epic(Epic.API)                               # ┐
@allure.feature(Feature.USERS)                       # │ Allure Behaviors
@allure.sub_suite(Story.GET)                         # ┘
@allure.parent_suite(Epic.API)                       # ┐
@allure.suite(Feature.USERS)                         # │ Allure Suites (optional)
@allure.sub_suite(Story.GET)                         # ┘
@allure.severity(allure.severity_level.NORMAL)       # ] Allure Severity
#-----------------------------------------------------------------------------------------------------------------------
class TestGetUserMe:
    @allure.title('Get User Me (v.1 - Через фикстуру полного цикла)')           # — Allure Title
    def test_get_user_me_1(self, get_user_me_api: httpx.Response):
        response = get_user_me_api      # Сохраняем ответ фикстуры, но не обязательно...,
                                        # Исполняемую API-фикстуру можно сразу передавать в Assertions в качестве параметра
        # Assertions
        assert_status_code(response, HTTPStatus.OK)       # Status code: 200
        assert_method(response, HTTPMethod.GET)         # Method: GET
        assert_create_user_response_non_empty(response)                         # Response data is NON-empty
        assert_user_id(response)                                                # User ID validation
        validate_json_schema(response, GetUserMeResponseSchema) # Validation JSON schema



    @allure.title('Get User Me (v.2 - Через фикстуру получения экземпляра PrivateUsersClient)')  # — Allure Title
    def test_get_user_me_2(self, private_users_client: PrivateUsersClient):
        response = private_users_client.get_user_me_api()                       # ▶ Запрос через API-метод

        # Assertions
        assert_status_code(response, HTTPStatus.OK)       # Status code: 200
        assert_method(response, HTTPMethod.GET)         # Method: GET
        assert_create_user_response_non_empty(response)                         # Response data is NON-empty
        assert_user_id(response)                                                # User ID validation
        validate_json_schema(response, GetUserMeResponseSchema) # Validation JSON schema



    @allure.title('Get User Me (v.3 - All manual)')       # — Allure Title
    def test_get_user_me_3_manual(self):
        #----------------------- Pre-conditions --------------------
        # Create User
        public_users_client = get_public_users_client()   # Получаем экземпляр PublicUsersClient (с Base URL)
        create_user_data = CreateUserRequestSchema()      # Инициализация Pydantic-модели с default fake-data нового пользователя
        public_users_client.create_user_pydantic(create_user_data) # ▶ Запрос через Pydantic-метод
        auth_data = AuthDataSchema(                       # Инициализируем модель с default-данными для авторизации
            email=create_user_data.email,                 # Замена default на —> реальное значение
            password=create_user_data.password            # Замена default на —> реальное значение
        )
        #------------------------ Get User Me -----------------------
        get_user_me_client = get_private_users_client(auth_data)     # Получаем экземпляр PrivateUsersClient
        response = get_user_me_client.get_user_me_api()              # ▶ Запрос через API-метод

        response_model = CreateUserResponseSchema.model_validate_json(response.text)  # Response —> Pydantic-model (Deserialize for Assertions)

        #------------------------ Assertions ------------------------
        # v.1 - Base API assertions (⚠️Hard coding не рекомендуется)
        assert response.status_code == 200, '❌Status code is incorrect!'           # проверка статус-кода    (Hard coding)
        assert response.request.method == 'GET', '❌Request Method is incorrect!'   # проверка метода запроса (Hard coding)

        # v.2 - Base API assertions (через HTTPStatus и HTTPMethod)
        assert response.status_code == HTTPStatus.OK, '❌Incorrect status code!'         # проверка статус-кода    (через HTTPStatus)
        assert response.request.method == HTTPMethod.GET, '❌Incorrect Request Method!'  # проверка метода запроса (через HTTPMethod)

        # Fields values assertions:
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
        # Tool.api_report(response)
