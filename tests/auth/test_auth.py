"""
TEST User Auth (Log in)
"""
import httpx
import pytest
import allure
from clients.auth_client import AuthClient
from schemas.users_schema import CreateUserSchema
from schemas.auth_schema import AuthResponseSchema, AuthDataSchema
from http import HTTPStatus, HTTPMethod
from tools.allure.annotations import Epic, Feature, Story, Tag
from tools.assertions.auth_assert import assert_token, assert_auth_response_non_empty
from tools.assertions.base_assert import assert_status_code, assert_request_method
from tools.assertions.schema_assert import validate_json_schema
from tools.tool import Tool

#=======================================================================================================================
# Class annotations
@pytest.mark.auth                                         # ┐
@pytest.mark.smoke                                        # │ Pytest Marks
@pytest.mark.regression                                   # ┘
@allure.tag(Tag.REGRESSION, Tag.SMOKE, Tag.AUTH)    # ] Allure Tags
@allure.epic(Epic.API)                                    # ┐
@allure.feature(Feature.AUTH)                             # │ Allure Behaviors
@allure.story(Story.LOGIN)                                # ┘
@allure.severity(allure.severity_level.BLOCKER)           # ] Allure Severity
#-----------------------------------------------------------------------------------------------------------------------
class TestAuth:
    @allure.title('Authentication (v.1 - Через API-фикстуру полного цикла)')               # Allure step Title
    def test_auth_1(self, auth_api: httpx.Response):
        response = auth_api                                                      # Сохраняем ответ API-фикстуры (httpx.Response)
        response_model = AuthResponseSchema.model_validate_json(response.text)   # httpx.Response —> Pydantic-model (deserialize)

        # Assertions
        assert_status_code(response.status_code, HTTPStatus.OK)           # Status code: 200
        assert_request_method(response.request.method, HTTPMethod.POST)   # Method: POST
        assert_auth_response_non_empty(response_model)                                   # Response data is non-empty
        assert_token(response_model)                                                     # Token validation
        validate_json_schema(response, AuthResponseSchema)               # JSON schema validation



    @allure.title('Authentication (v.2 - Через фикстуры: create_user + auth_client)')              # Allure step Title
    def test_auth_2(self, create_user: CreateUserSchema, auth_client: AuthClient):
        auth_data = AuthDataSchema(                            # Pydantic-model with fake-data (Email и Password),...
            email=create_user.email,                           # ... замена default на —> реальное значение из фикстуры
            password=create_user.password                      # ... замена default на —> реальное значение из фикстуры
        )
        response = auth_client.login_api(auth_data)                              # ▶ Запрос через API-метод
        response_model = AuthResponseSchema.model_validate_json(response.text)   # httpx.Response —> Pydantic-model (deserialize)

        # Assertions
        assert_status_code(response.status_code, HTTPStatus.OK)           # Status code: 200
        assert_request_method(response.request.method, HTTPMethod.POST)   # Method: POST
        assert_auth_response_non_empty(response_model)                                   # Response data is non-empty
        assert_token(response_model)                                                     # Token validation
        validate_json_schema(response, AuthResponseSchema)               # JSON schema validation


#=======================================================================================================================
        # Tool.api_report(response)
