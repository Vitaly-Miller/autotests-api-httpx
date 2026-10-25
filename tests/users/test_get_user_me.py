"""
TEST Get User Me
"""
import httpx
import pytest
import allure
import jsonschema
from clients.users_client_private import get_users_client_private, UsersClientPrivate
from clients.users_client_public import get_users_client_public
from schemas.auth_schema import AuthDataSchema
from schemas.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserMeResponseSchema
from http import HTTPStatus, HTTPMethod
from tools.allure.annotations import Tag, Epic, Feature, Story
from tools.assertions.base_assert import assert_status_code, assert_request_method
from tools.assertions.schema_assert import validate_json_schema
from tools.assertions.users_assert import assert_create_user_response_non_empty, assert_user_id
from tools.tool import Tool

#=======================================================================================================================
# Class annotations
@pytest.mark.users
@pytest.mark.smoke
@allure.tag(Tag.SMOKE, Tag.USERS, Tag.GET)
@allure.epic(Epic.API)
@allure.feature(Feature.USERS)
@allure.story(Story.GET)
@allure.severity(allure.severity_level.NORMAL)
#-----------------------------------------------------------------------------------------------------------------------
class TestGetUserMe:
    @allure.title('Get User Me (v.1 - Via full-cycle fixture)')
    def test_get_user_me_1(self, get_user_me_api: httpx.Response):
        response = get_user_me_api
        response_model = CreateUserResponseSchema.model_validate_json(response.text)

        # Assertions
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_request_method(response.request.method, HTTPMethod.GET)
        assert_create_user_response_non_empty(response_model)
        assert_user_id(response_model)
        validate_json_schema(response, GetUserMeResponseSchema)


    @allure.title('Get User Me (v.2 - Via UsersClientPrivate instance fixture)')
    def test_get_user_me_2(self, users_client_private: UsersClientPrivate):
        response = users_client_private.get_user_me_api()
        response_model = CreateUserResponseSchema.model_validate_json(response.text)

        # Assertions
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_request_method(response.request.method, HTTPMethod.GET)
        assert_create_user_response_non_empty(response_model)
        assert_user_id(response_model)
        validate_json_schema(response, GetUserMeResponseSchema)


#------------------------------------------------ All manual (example) -------------------------------------------------
    @allure.title('Get User Me (v.3 - All manual)')
    def test_get_user_me_3_manual(self):
        #----------------------- Pre-conditions --------------------
        # Create User
        users_client_public = get_users_client_public()
        create_user_data = CreateUserRequestSchema()
        users_client_public.create_user(create_user_data)
        auth_data = AuthDataSchema(
            email=create_user_data.email,
            password=create_user_data.password
        )
        #------------------------ Get User Me -----------------------
        get_user_me_client = get_users_client_private(auth_data)
        response = get_user_me_client.get_user_me_api()
        response_model = CreateUserResponseSchema.model_validate_json(response.text)

        #------------------------ Assertions ------------------------
        # v.1 - Base API assertions (⚠️Hard coding is not recommended)
        assert response.status_code == 200, '❌Status code is incorrect!'
        assert response.request.method == 'GET', '❌Request Method is incorrect!'

        # v.2 - Base API assertions (via HTTPStatus and HTTPMethod)
        assert response.status_code == HTTPStatus.OK, '❌Incorrect status code!'
        assert response.request.method == HTTPMethod.GET, '❌Incorrect Request Method!'

        # Fields values assertions:
        assert response_model.user.email == create_user_data.email, '❌Different Email!'
        assert response_model.user.last_name == create_user_data.last_name, '❌Different Last Name!'
        assert response_model.user.first_name == create_user_data.first_name, '❌Different First Name!'
        assert response_model.user.middle_name == create_user_data.middle_name, '❌Different Middle Name!'

        # JSON schema validation
        jsonschema.validate(
            instance=response.json(),
            schema=CreateUserResponseSchema.model_json_schema(),
            format_checker=jsonschema.FormatChecker()
        )

#=======================================================================================================================
        # Tool.api_report(response)          # for PyCharm RUN-console API reporting only
