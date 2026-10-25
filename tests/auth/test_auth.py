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
@pytest.mark.auth
@pytest.mark.smoke
@pytest.mark.regression
@allure.tag(Tag.REGRESSION, Tag.SMOKE, Tag.AUTH)
@allure.epic(Epic.API)
@allure.feature(Feature.AUTH)
@allure.story(Story.LOGIN)
@allure.severity(allure.severity_level.BLOCKER)
#-----------------------------------------------------------------------------------------------------------------------
class TestAuth:
    @allure.title('Authentication (v.1 - Via full-cycle API fixture)')
    def test_auth_1(self, auth_api: httpx.Response):
        response = auth_api
        response_model = AuthResponseSchema.model_validate_json(response.text)

        # Assertions
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_request_method(response.request.method, HTTPMethod.POST)
        assert_auth_response_non_empty(response_model)
        assert_token(response_model)
        validate_json_schema(response, AuthResponseSchema)


    @allure.title('Authentication (v.2 - Via fixtures: create_user + auth_client)')
    def test_auth_2(self, create_user: CreateUserSchema, auth_client: AuthClient):
        auth_data = AuthDataSchema(
            email=create_user.email,
            password=create_user.password
        )
        response = auth_client.login_api(auth_data)
        response_model = AuthResponseSchema.model_validate_json(response.text)

        # Assertions
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_request_method(response.request.method, HTTPMethod.POST)
        assert_auth_response_non_empty(response_model)
        assert_token(response_model)
        validate_json_schema(response, AuthResponseSchema)


#=======================================================================================================================
        # Tool.api_report(response)          # for PyCharm RUN-console API reporting only
