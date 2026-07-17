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
    Фикстура получения экземпляра FilesClient() (c Авторизацией)

    :param create_user: Вложенная Pydantic-фикстура создания пользователя
    :return: Экземпляр класса class FilesClient() (c Base URL + АВТОРИЗАЦИЯ)
    """
    files_client = get_files_client(create_user.auth_data)
    return files_client                                           # FilesClient()


#----------------------------------------------------- Create File -----------------------------------------------------
# API
@pytest.fixture
@allure.title('▷ Create File (API-fixture)')
def create_file_api(files_client: FilesClient) -> httpx.Response:
    """
    API-фикстура создания файла

    :param files_client: Вложенная фикстура получения экземпляра FilesClient (c Авторизация)
    :return: httpx.Response
    """
    create_file_data = CreateFileRequestSchema()                  # Инициализация Pydantic-модели c default fake-data
    response = files_client.create_file_api(create_file_data)     # ▶ Запрос через API-метод
    return response                                               # httpx.Response


# Pydantic-model
@pytest.fixture
@allure.title('▷ Create File (Pydantic-fixture)')
def create_file(files_client: FilesClient) -> CreateFileSchema:
    """
    Pydantic-фикстура создания файла

    :param files_client: Вложенная фикстура получения экземпляра FilesClient (c Авторизацией)
    :return: Pydantic-model (CreateFileSchema) ✨<Request + Response>
    """
    create_file_data = CreateFileRequestSchema()                  # Инициализация Pydantic-model c default fake-data
    response_model = files_client.create_file(create_file_data)   # ▶ Запрос через Pydantic-метод
    response_model_full = CreateFileSchema(                       # Инициализация Pydantic-model (CreateFileSchema) ✨<Request + Response>
        request=create_file_data,
        response=response_model)
    return response_model_full                                    # Pydantic-model (CreateFileSchema) ✨<Request + Response>


# Pydantic-model (full) + delete file
@pytest.fixture
@allure.title('▷ Create temporary File (Pydantic-fixture)')
def create_file_temp(files_client: FilesClient) -> Generator[CreateFileSchema]:
    """
    Pydantic-фикстура создания временного файла + удаления после теста

    :param files_client: Вложенная фикстура получения экземпляра FilesClient (c Авторизация)
    :return: httpx.Response
    """
    create_file_data = CreateFileRequestSchema()                  # Инициализация Pydantic-модели c default fake-data
    response_model = files_client.create_file(create_file_data)   # ▶ Запрос через Pydantic-метод
    response_model_full = CreateFileSchema(                       # Инициализация Pydantic-model (CreateFileSchema) ✨<Request + Response>
        request=create_file_data,
        response=response_model)
    yield response_model_full                                     # Pydantic-model (CreateFileSchema) ✨<Request + Response>
    files_client.delete_file_api(response_model_full.file_id)     # Удаление файла после теста


#------------------------------------------------------ Get File -------------------------------------------------------
# API
@pytest.fixture
@allure.title('▷ Get File (API-fixture)')
def get_file_api(files_client: FilesClient, create_file: CreateFileSchema) -> httpx.Response:
    """
    API-фикстура получения файла по ID

    :param files_client: Вложенная фикстура получения экземпляра FilesClient (c Авторизацией)
    :param create_file: Вложенная Pydantic-фикстура создания файла
    :return: httpx.Response
    """
    response = files_client.get_file_api(create_file.file_id)     # ▶ Запрос через API-метод
    return response                                               # httpx.Response


# Pydantic-model
@pytest.fixture
@allure.title('▷ Get File (Pydantic-fixture)')
def get_file(files_client: FilesClient, create_file: CreateFileSchema) -> GetFileResponseSchema:
    """
    Pydantic-фикстура получения файла by ID

    :param files_client: Вложенная фикстура получения экземпляра FilesClient (c Авторизацией)
    :param create_file: Вложенная Pydantic-фикстура создания файла
    :return: Pydantic-model (GetFileResponseSchema)
    """
    response_model = files_client.get_file(create_file.file_id)   # ▶ Запрос через Pydantic-метод
    return response_model                                         # Pydantic-model (GetFileResponseSchema)


#----------------------------------------------------- Delete File -----------------------------------------------------
# API
@pytest.fixture
@allure.title('▷ Delete File (Pydantic-fixture)')
def delete_file_api(files_client: FilesClient, create_file: CreateFileSchema) -> httpx.Response:
    """
    API-фикстура удаления файла

    :param files_client: Вложенная фикстура получения экземпляра FilesClient (c Авторизацией)
    :param create_file: Вложенная Pydantic-фикстура создания файла
    :return: httpx.Response
    """
    response = files_client.delete_file_api(create_file.file_id)   # ▶ Запрос через API-метод
    return response                                                # httpx.Response


#=======================================================================================================================
