"""
Files (Fixtures)
"""
import httpx
import pytest
import allure
from typing import Generator
from clients.files_client import FilesClient, get_files_client
from schemas.users_schema import CreateUserSchema
from schemas.files_schema import CreateFileRequestSchema, CreateFileSchema, GetFileResponseSchema

#==================================================== Files Client =====================================================
# Files Client
@pytest.fixture
@allure.title('◎ Files Client (fixture)')
def files_client(create_user: CreateUserSchema) -> FilesClient:
    """
    Fixture that provides a FilesClient() instance (with Authorization)

    :param create_user: Nested Pydantic fixture that creates a user
    :return: Instance of class FilesClient() (with Base URL + AUTHORIZATION)
    """
    files_client = get_files_client(create_user.auth_data)
    return files_client                                           # FilesClient()


#----------------------------------------------------- Create File -----------------------------------------------------
# API
@pytest.fixture
@allure.title('▷ Create File (API-fixture)')
def create_file_api(files_client: FilesClient) -> httpx.Response:
    """
    API fixture that creates a file

    :param files_client: Nested fixture that provides a FilesClient instance (with Authorization)
    :return: httpx.Response
    """
    create_file_data = CreateFileRequestSchema()                  # Initialize Pydantic model with default fake data
    response = files_client.create_file_api(create_file_data)     # ▶ Request via API method
    return response                                               # httpx.Response


# Pydantic-model
@pytest.fixture
@allure.title('▷ Create File (Pydantic-fixture)')
def create_file(files_client: FilesClient) -> CreateFileSchema:
    """
    Pydantic fixture that creates a file

    :param files_client: Nested fixture that provides a FilesClient instance (with Authorization)
    :return: Pydantic-model (CreateFileSchema) ✨<Request + Response>
    """
    create_file_data = CreateFileRequestSchema()                  # Initialize Pydantic model with default fake data
    response_model = files_client.create_file(create_file_data)   # ▶ Request via Pydantic method
    response_model_full = CreateFileSchema(                       # Initialize Pydantic model (CreateFileSchema) ✨<Request + Response>
        request=create_file_data,
        response=response_model)
    return response_model_full                                    # Pydantic-model (CreateFileSchema) ✨<Request + Response>


# Pydantic-model (full) + delete file
@pytest.fixture
@allure.title('▷ Create temporary File (Pydantic-fixture)')
def create_file_temp(files_client: FilesClient) -> Generator[CreateFileSchema]:
    """
    Pydantic fixture that creates a temporary file + deletes it after the test

    :param files_client: Nested fixture that provides a FilesClient instance (with Authorization)
    :return: httpx.Response
    """
    create_file_data = CreateFileRequestSchema()                  # Initialize Pydantic model with default fake data
    response_model = files_client.create_file(create_file_data)   # ▶ Request via Pydantic method
    response_model_full = CreateFileSchema(                       # Initialize Pydantic model (CreateFileSchema) ✨<Request + Response>
        request=create_file_data,
        response=response_model)
    yield response_model_full                                     # Pydantic-model (CreateFileSchema) ✨<Request + Response>
    files_client.delete_file_api(response_model_full.file_id)     # Delete file after test


#------------------------------------------------------ Get File -------------------------------------------------------
# API
@pytest.fixture
@allure.title('▷ Get File (API-fixture)')
def get_file_api(files_client: FilesClient, create_file: CreateFileSchema) -> httpx.Response:
    """
    API fixture that gets a file by ID

    :param files_client: Nested fixture that provides a FilesClient instance (with Authorization)
    :param create_file: Nested Pydantic fixture that creates a file
    :return: httpx.Response
    """
    response = files_client.get_file_api(create_file.file_id)     # ▶ Request via API method
    return response                                               # httpx.Response


# Pydantic-model
@pytest.fixture
@allure.title('▷ Get File (Pydantic-fixture)')
def get_file(files_client: FilesClient, create_file: CreateFileSchema) -> GetFileResponseSchema:
    """
    Pydantic fixture that gets a file by ID

    :param files_client: Nested fixture that provides a FilesClient instance (with Authorization)
    :param create_file: Nested Pydantic fixture that creates a file
    :return: Pydantic-model (GetFileResponseSchema)
    """
    response_model = files_client.get_file(create_file.file_id)   # ▶ Request via Pydantic method
    return response_model                                         # Pydantic-model (GetFileResponseSchema)


#----------------------------------------------------- Delete File -----------------------------------------------------
# API
@pytest.fixture
@allure.title('▷ Delete File (Pydantic-fixture)')
def delete_file_api(files_client: FilesClient, create_file: CreateFileSchema) -> httpx.Response:
    """
    API fixture that deletes a file

    :param files_client: Nested fixture that provides a FilesClient instance (with Authorization)
    :param create_file: Nested Pydantic fixture that creates a file
    :return: httpx.Response
    """
    response = files_client.delete_file_api(create_file.file_id)   # ▶ Request via API method
    return response                                                # httpx.Response


#=======================================================================================================================
