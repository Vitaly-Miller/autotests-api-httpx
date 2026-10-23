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
@pytest.mark.users                                   # ┐ Pytest Marks
@pytest.mark.smoke                                   # ┘
@allure.tag(Tag.SMOKE, Tag.USERS, Tag.GET)     # ] Allure Tags
@allure.epic(Epic.API)                               # ┐
@allure.feature(Feature.USERS)                       # │ Allure Behaviors
@allure.story(Story.GET)                             # ┘
@allure.severity(allure.severity_level.NORMAL)       # ] Allure Severity
#-----------------------------------------------------------------------------------------------------------------------
class TestGetUserMe:
    @allure.title('Get User Me (v.1 - Via full-cycle fixture)')
    def test_get_user_me_1(self, get_user_me_api: httpx.Response):
        response = get_user_me_api                                                    # Save API fixture response (httpx.Response)
        response_model = CreateUserResponseSchema.model_validate_json(response.text)  # httpx.Response —> Pydantic-model (parsing-deserialize)

        # Assertions
        assert_status_code(response.status_code, HTTPStatus.OK)        # Status code: 200
        assert_request_method(response.request.method, HTTPMethod.GET) # Method: GET
        assert_create_user_response_non_empty(response_model)                         # Response data is non-empty
        assert_user_id(response_model)                                                # User-ID validation
        validate_json_schema(response, GetUserMeResponseSchema)       # JSON schema validation


    @allure.title('Get User Me (v.2 - Via UsersClientPrivate instance fixture)')
    def test_get_user_me_2(self, users_client_private: UsersClientPrivate):
        response = users_client_private.get_user_me_api()                             # ▶ Request via API method
        response_model = CreateUserResponseSchema.model_validate_json(response.text)  # httpx.Response —> Pydantic-model (parsing-deserialize)

        # Assertions
        assert_status_code(response.status_code, HTTPStatus.OK)        # Status code: 200
        assert_request_method(response.request.method, HTTPMethod.GET) # Method: GET
        assert_create_user_response_non_empty(response_model)                         # Response data is non-empty
        assert_user_id(response_model)                                                # User-ID validation
        validate_json_schema(response, GetUserMeResponseSchema)       # JSON schema validation


#------------------------------------------------ All manual (example) -------------------------------------------------
    @allure.title('Get User Me (v.3 - All manual)')
    def test_get_user_me_3_manual(self):
        #----------------------- Pre-conditions --------------------
        # Create User
        users_client_public = get_users_client_public()   # Get UsersClientPublic instance (with Base URL)
        create_user_data = CreateUserRequestSchema()      # Initialize Pydantic model with default fake data for a new user
        users_client_public.create_user(create_user_data) # ▶ Request via Pydantic method
        auth_data = AuthDataSchema(                       # Initialize model with default auth data
            email=create_user_data.email,                 # Replace default with —> real value
            password=create_user_data.password            # Replace default with —> real value
        )
        #------------------------ Get User Me -----------------------
        get_user_me_client = get_users_client_private(auth_data)     # Get UsersClientPrivate instance
        response = get_user_me_client.get_user_me_api()              # ▶ Request via API method
        response_model = CreateUserResponseSchema.model_validate_json(response.text)  # httpx.Response —> Pydantic-model (parsing-deserialize) (Deserialize for Assertions)

        #------------------------ Assertions ------------------------
        # v.1 - Base API assertions (⚠️Hard coding is not recommended)
        assert response.status_code == 200, '❌Status code is incorrect!'           # status code check    (Hard coding)
        assert response.request.method == 'GET', '❌Request Method is incorrect!'   # request method check (Hard coding)

        # v.2 - Base API assertions (via HTTPStatus and HTTPMethod)
        assert response.status_code == HTTPStatus.OK, '❌Incorrect status code!'         # status code check    (via HTTPStatus)
        assert response.request.method == HTTPMethod.GET, '❌Incorrect Request Method!'  # request method check (via HTTPMethod)

        # Fields values assertions:
        assert response_model.user.email == create_user_data.email, '❌Different Email!'                    # check sent vs received Email
        assert response_model.user.last_name == create_user_data.last_name, '❌Different Last Name!'        # check sent vs received Last Name
        assert response_model.user.first_name == create_user_data.first_name, '❌Different First Name!'     # check sent vs received First Name
        assert response_model.user.middle_name == create_user_data.middle_name, '❌Different Middle Name!'  # check sent vs received Middle Name

        # JSON schema validation
        jsonschema.validate(
            instance=response.json(),                             # Data to validate
            schema=CreateUserResponseSchema.model_json_schema(),  # JSON schema generated from Pydantic schema
            format_checker=jsonschema.FormatChecker()             # Format checking
        )

#=======================================================================================================================
        # Tool.api_report(response)          # for PyCharm RUN-console API reporting only
