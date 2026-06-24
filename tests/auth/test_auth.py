"""
TEST User Auth (Log in)
"""
import allure
import httpx
import pytest
from allure_commons.types import Severity
from clients.auth_client import AuthClient
from schemas.users_schema import CreateUserSchema
from schemas.auth_schema import AuthResponseSchema, AuthDataSchema
from http import HTTPStatus, HTTPMethod
from tools.allure.annotations import Epic, Feature, Story, Tag
from tools.assertions.auth_assert import assert_token, assert_auth_response_non_empty
from tools.assertions.base_assert import assert_status_code, assert_method
from tools.assertions.schema_assert import validate_json_schema
from tools.tool import Tool

#=======================================================================================================================
# Class annotations
@pytest.mark.auth                                         # ┐
@pytest.mark.smoke                                        # │ Pytest Marks
@pytest.mark.regression                                   # ┘
@allure.tag(Tag.AUTH, Tag.REGRESSION, Tag.SMOKE)    # ] Allure Tags
@allure.epic(Epic.API)                                    # ┐
@allure.feature(Feature.AUTH)                            # │ Allure Behaviors
@allure.story(Story.LOGIN)                                # ┘
@allure.parent_suite(Epic.API)                            # ┐
@allure.suite(Feature.AUTH)                               # │ Allure Suites
@allure.sub_suite(Story.LOGIN)                            # ┘
@allure.severity(Severity.BLOCKER)                        # ] Allure Severity
#-----------------------------------------------------------------------------------------------------------------------
class TestAuth:
    @allure.title('Auth (v.1 - Через API-фикстуру полного цикла)')    # — Allure Title
    def test_auth_1(self, auth_api: httpx.Response):
        response = auth_api        # Сохраняем ответ фикстуры, но не обязательно,...
                                   # Исполняемую API-фикстуру можно сразу передавать в Assertions в качестве параметра
        # Assertions
        assert_status_code(response, HTTPStatus.OK)          # Status code: 200
        assert_method(response, HTTPMethod.POST)           # Method: POST
        assert_auth_response_non_empty(response)                                   # Response data is NON-empty
        assert_token(response)                                                     # Token validation
        validate_json_schema(response, AuthResponseSchema)         # Validation JSON schema



    @allure.title('Auth (v.2 - Через фикстуры: Создания пользователя + Авторизации пользователя)')  # — Allure Title
    def test_auth_2(self, create_user: CreateUserSchema, auth_client: AuthClient):
        auth_data = AuthDataSchema(                      # Pydantic-model with fake-data (Email и Password),...
            email=create_user.email,                     # Замена default на —> реальное значение из фикстуры
            password=create_user.password                # Замена default на —> реальное значение из фикстуры
        )
        response = auth_client.login_api(auth_data)                                # ▶ Запрос через API-метод

        # Assertions
        assert_status_code(response, HTTPStatus.OK)          # Status code: 200
        assert_method(response, HTTPMethod.POST)           # Method: POST
        assert_auth_response_non_empty(response)                                   # Response data is NON-empty
        assert_token(response)                                                     # Token validation
        validate_json_schema(response, AuthResponseSchema)         # Validation JSON schema


#=======================================================================================================================
        # API Report
        # Tool.api_report(response)
