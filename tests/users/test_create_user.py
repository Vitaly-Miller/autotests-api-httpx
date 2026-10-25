"""
TEST Create User
"""
import http
import httpx
import pytest
import allure
import jsonschema
from tools.data_generator import fake
from clients.users_client_public import UsersClientPublic, get_users_client_public
from schemas.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.allure.annotations import Epic, Feature, Story, Tag
from tools.assertions.base_assert import assert_status_code, assert_request_method
from tools.assertions.schema_assert import validate_json_schema
from tools.assertions.users_assert import (
    assert_create_user_response_non_empty,
    assert_create_user_response,
    assert_user_id
)
from tools.tool import Tool

#=======================================================================================================================
# Class annotations
@pytest.mark.users
@pytest.mark.regression
@allure.tag(Tag.REGRESSION, Tag.USERS, Tag.CREATE)
@allure.epic(Epic.API)
@allure.feature(Feature.USERS)
@allure.story(Story.CREATE)
@allure.severity(allure.severity_level.BLOCKER)
#-----------------------------------------------------------------------------------------------------------------------
class TestCreateUser:
    @allure.title('Create User (v.1 - Via full-cycle fixture)')
    def test_create_user_1(self, create_user_api: httpx.Response):
        response = create_user_api
        response_model = CreateUserResponseSchema.model_validate_json(response.text)
        request_model = CreateUserRequestSchema.model_validate_json(response.request.content)

        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.OK)
        assert_request_method(response.request.method, http.HTTPMethod.POST)
        assert_create_user_response_non_empty(response_model)
        assert_create_user_response(response_model,request_model)
        assert_user_id(response_model)
        validate_json_schema(response, CreateUserResponseSchema)


    @allure.title('Create User (v.2 - Via UsersClientPublic fixture)')
    def test_create_user_2(self, users_client_public: UsersClientPublic):
        create_user_data = CreateUserRequestSchema()
        response = users_client_public.create_user_api(create_user_data)
        response_model = CreateUserResponseSchema.model_validate_json(response.text)

        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.OK)
        assert_request_method(response.request.method, http.HTTPMethod.POST)
        assert_create_user_response_non_empty(response_model)
        assert_create_user_response(response_model, create_user_data)
        assert_user_id(response_model)
        validate_json_schema(response, CreateUserResponseSchema)



    @allure.title('Create User (v.3 - Email parametrize 3-in-1)')
    @allure.tag(Tag.PARAMETRIZE)
    @pytest.mark.parametrize(
        'domain', [
            'amazon.com',
            'gmail.com',
            'yahoo.com'
        ]
    )
    def test_create_user_3_params(self, domain: str, users_client_public: UsersClientPublic):
        create_user_data = CreateUserRequestSchema(
            email=fake.email(domain=domain)
        )
        response = users_client_public.create_user_api(create_user_data)
        response_model = CreateUserResponseSchema.model_validate_json(response.text)

        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.OK)
        assert_request_method(response.request.method, http.HTTPMethod.POST)
        assert_create_user_response_non_empty(response_model)
        assert_create_user_response(response_model, create_user_data)
        assert_user_id(response_model)
        validate_json_schema(response, CreateUserResponseSchema)


#------------------------------------------------ All manual (example) -------------------------------------------------
    @allure.title('Create User (v.4 - All manual)')
    def test_create_user_4_manual(self):
        users_client_public = get_users_client_public()
        create_user_data = CreateUserRequestSchema()
        response = users_client_public.create_user_api(create_user_data)
        response_model = CreateUserResponseSchema.model_validate_json(response.text)

        # Assertions:
        # Base API assertions
        assert response.status_code == 200, '❌Incorrect status code!'
        assert response.request.method == 'POST', '❌Incorrect Request Method!'

        assert response.status_code == http.HTTPStatus.OK, '❌Incorrect status code!'
        assert response.request.method == http.HTTPMethod.POST, '❌Incorrect Request Method!'

        # Response data = Request data
        assert response_model.user.email == create_user_data.email, '❌Different Email!'
        assert response_model.user.last_name == create_user_data.last_name, '❌Different Last Name!'
        assert response_model.user.first_name == create_user_data.first_name, '❌Different First Name!'
        assert response_model.user.middle_name == create_user_data.middle_name, '❌Different Middle Name!'

        # User-ID
        assert response_model.user.id is not None, '❌User-ID is Empty!'
        assert len(response_model.user.id) == 36, '❌Wrong User-ID length'

        # JSON schema validation
        jsonschema.validate(
            instance=response.json(),
            schema=CreateUserResponseSchema.model_json_schema(),
            format_checker=jsonschema.FormatChecker()
        )


#=======================================================================================================================
        # Tool.api_report(response)          # for PyCharm RUN-console API reporting only
