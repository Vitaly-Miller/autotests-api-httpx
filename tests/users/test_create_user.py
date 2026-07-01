"""
TEST Create User
"""
import http
import httpx
import pytest
import allure
import jsonschema
from tools.data_generator import fake
from clients.public_users_client import PublicUsersClient, get_public_users_client
from schemas.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.allure.annotations import Epic, Feature, Story, Tag
from tools.assertions.base_assert import assert_status_code, assert_request_method
from tools.assertions.schema_assert import validate_json_schema
from tools.assertions.users_assert import (
    assert_create_user_response_data,
    assert_create_user_response_non_empty,
    assert_user_id
)

from tools.tool import Tool

#=======================================================================================================================
# Class annotations
@pytest.mark.users                                         # ┐ Pytest Marks
@pytest.mark.regression                                    # ┘
@allure.tag(Tag.REGRESSION, Tag.USERS, Tag.CREATE)   # ] Allure Tags
@allure.epic(Epic.API)                                     # ┐
@allure.feature(Feature.USERS)                             # │ Allure Behaviors
@allure.story(Story.CREATE)                                # ┘
@allure.parent_suite(Epic.API)                             # ┐
@allure.suite(Feature.USERS)                               # │ Allure Suites (optional)
@allure.sub_suite(Story.CREATE)                            # ┘
@allure.severity(allure.severity_level.BLOCKER)            # ] Allure Severity
#-----------------------------------------------------------------------------------------------------------------------
class TestCreateUser:
    @allure.title('Create User (v.1 - Через фикстуру полного цикла)')                          # Allure step Title
    def test_create_user_1(self, create_user_api: httpx.Response):
        response = create_user_api                                                             # Сохраняем ответ API-фикстуры (httpx.Response)
        response_model = CreateUserResponseSchema.model_validate_json(response.text)           # httpx.Response —> Pydantic-model (parsing-deserialize)
        request_model = CreateUserRequestSchema.model_validate_json(response.request.content)  # Request body —> Pydantic-model (parsing-deserialize)

        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.OK)               # Status code: 200
        assert_request_method(response.request.method, http.HTTPMethod.POST)       # Method: POST
        assert_create_user_response_non_empty(response_model)                                      # Response data is NON-empty
        assert_create_user_response_data(response_model,request_model)  # Response data = Request data (request_model)
        assert_user_id(response_model)                                                             # User-ID validation
        validate_json_schema(response, CreateUserResponseSchema)                   # JSON schema validation



    @allure.title('Create User (v.2 - Через фикстуру PublicUsersClient)')                      # Allure step Title
    def test_create_user_2(self, public_users_client: PublicUsersClient):
        create_user_data = CreateUserRequestSchema()                                           # Pydantic-model with fake-data
        response = public_users_client.create_user_api(create_user_data)                       # ▶ Запрос через API-метод
        response_model = CreateUserResponseSchema.model_validate_json(response.text)           # httpx.Response —> Pydantic-model (parsing-deserialize)

        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.OK)                   # Status code: 200
        assert_request_method(response.request.method, http.HTTPMethod.POST)           # Method: POST
        assert_create_user_response_non_empty(response_model)                                          # Response data is NON-empty
        assert_create_user_response_data(response_model, create_user_data)  # Response data = Request data (create_user_data)
        assert_user_id(response_model)                                                                 # User-ID validation
        validate_json_schema(response, CreateUserResponseSchema)                       # JSON schema validation



    @allure.tag(Tag.PARAMETRIZE)                                   # Allure Tag
    @allure.title('Create User (v.3 - Email parametrize 3-in-1)')  # Allure step Title (Статический)- ⚠️игнорируется при наличии динамического
    @pytest.mark.parametrize(                                      # Parametrize Email domain (3-in-1)
        'domain', [
            'amazon.com',
            'gmail.com',
            'yahoo.com'
        ]
    )
    def test_create_user_3_params(self, domain: str, public_users_client: PublicUsersClient):
        allure.dynamic.title(f'Create User (v.3 - Email domain: ...@{domain})')    # Allure step Title (⚠️Динамический - без-@)
        create_user_data = CreateUserRequestSchema(                                # Pydantic-model with fake-data, ...
            email=fake.email(domain=domain)                                        # ... значения Email-домена из parametrize (3-in-1)
        )
        response = public_users_client.create_user_api(create_user_data)               # ▶ Запрос через API-метод
        response_model = CreateUserResponseSchema.model_validate_json(response.text)   # httpx.Response —> Pydantic-model (parsing-deserialize)

        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.OK)                   # Status code: 200
        assert_request_method(response.request.method, http.HTTPMethod.POST)           # Method: POST
        assert_create_user_response_non_empty(response_model)                                          # Response data is NON-empty
        assert_create_user_response_data(response_model, create_user_data)  # Response data = Request data (create_user_data)
        assert_user_id(response_model)                                                                 # User-ID validation
        validate_json_schema(response, CreateUserResponseSchema)                       # JSON schema validation



#------------------------------------------------ All manual (example) -------------------------------------------------
    @allure.title('Create User (v.4 - All manual)')                                   # Allure step Title
    def test_create_user_4_manual(self):
        public_users_client = get_public_users_client()                               # Получение экземпляра PublicUsersClient
        create_user_data = CreateUserRequestSchema()                                  # Инициализация Pydantic-model с default fake-data нового пользователя
        response = public_users_client.create_user_api(create_user_data)              # ▶ Запрос через API-метод
        response_model = CreateUserResponseSchema.model_validate_json(response.text)  # httpx.Response —> Pydantic-model (parsing-deserialize) (deserialize for Assertions)

        # Assertions:
        # Base API assertions
        assert response.status_code == 200, '❌Incorrect status code!'           # Status code: 200 (⚠️Hard coding не рекомендуется)
        assert response.request.method == 'POST', '❌Incorrect Request Method!'  # Method: POST     (⚠️Hard coding не рекомендуется)

        assert response.status_code == http.HTTPStatus.OK, '❌Incorrect status code!'          # Status code: 200  (через HTTPStatus)
        assert response.request.method == http.HTTPMethod.POST, '❌Incorrect Request Method!'  # Method: POST      (через HTTPMethod)

        # Response data = Request data
        assert response_model.user.email == create_user_data.email, '❌Разные Email!'                    # Request Email = Response Email
        assert response_model.user.last_name == create_user_data.last_name, '❌Разные Last Name!'        # Request Last Name = Response Last Name
        assert response_model.user.first_name == create_user_data.first_name, '❌Разные First Name!'     # Request First Name = Response First Name
        assert response_model.user.middle_name == create_user_data.middle_name, '❌Разные Middle Name!'  # Request Middle Name = Response Middle Name

        # User-ID
        assert response_model.user.id is not None, '❌User-ID is Empty!'      # User-ID is NON-Empty
        assert len(response_model.user.id) == 36, '❌Wrong User-ID length'    # User-ID length = 36 chars

        # JSON schema validation
        jsonschema.validate(
            instance=response.json(),                             # Данные для валидации
            schema=CreateUserResponseSchema.model_json_schema(),  # JSON-схема, сгенерированная из Pidantic-схемы
            format_checker=jsonschema.FormatChecker()             # Проверка форматов
        )



#=======================================================================================================================
        # Tool.api_report(response)
