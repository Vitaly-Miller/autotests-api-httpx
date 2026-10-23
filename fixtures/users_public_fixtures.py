"""
Public Users (Fixtures)
"""
import httpx
import pytest
import allure
from clients.users_client_public import get_users_client_public, UsersClientPublic
from schemas.users_schema import CreateUserSchema, CreateUserRequestSchema

#================================================ Users Client (Public) ================================================
# Users Client (Public)
@pytest.fixture
@allure.title('◎ Users Client (Public) (fixture)')
def users_client_public() -> UsersClientPublic:
    """
    Fixture that provides a UsersClientPublic() instance (with Base URL)

    :return: UsersClientPublic() instance (with Base URL)
    """
    users_client_public = get_users_client_public()
    return users_client_public     # UsersClientPublic()


#----------------------------------------------------- Create User -----------------------------------------------------
# API
@pytest.fixture
@allure.title('▷ Create User (API-fixture)')
def create_user_api(users_client_public: UsersClientPublic) -> httpx.Response:
    """
    API fixture that creates a user

    :param users_client_public: Nested fixture that provides a UsersClientPublic instance (with Base URL)
    :return: httpx.Response
    """
    create_user_data = CreateUserRequestSchema()                      # Initialize Pydantic model with default fake data
    response = users_client_public.create_user_api(create_user_data)  # ▶ Request via API method.
    return response                                                   # httpx.Response
                                   # ❗️To get the Request with 'password' here - parse JSON —> {dict}:
                                   # request_body = json.loads(response.request.content)
                                   # password = request_body["password"]
# Pydantic-model (full)
@pytest.fixture
@allure.title('▷ Create User (Pydantic-fixture)')
def create_user(users_client_public: UsersClientPublic) -> CreateUserSchema:
    """
    Pydantic fixture that creates a user

    :param users_client_public: Nested fixture that provides a UsersClientPublic instance (with Base URL)
    :return: Pydantic-model (CreateUserSchema) ✨<Request + Response>
    """
    create_user_data = CreateUserRequestSchema()                                               # Initialize model with default fake data for a new user via Pydantic schema
    response_model = users_client_public.create_user(create_user_data)                         # ︎▶ Request via Pydantic method
    response_model_full = CreateUserSchema(request=create_user_data, response=response_model)  # Initialize Pydantic model (CreateUserSchema) ✨<Request + Response>
    return response_model_full                                                                 # Pydantic-model (CreateUserSchema) ✨<Request + Response>


#=======================================================================================================================
