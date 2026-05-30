"""
Files fixtures
"""
import httpx
import pytest
from clients.files_client import FilesClient, get_files_client
from schemas.files import CreateFileRequestSchema, CreateFileSchema, GetFileResponseSchema
from schemas.users import CreateUserSchema

#==================================================== Files Client =====================================================
# Files Client
@pytest.fixture
def files_client(create_user: CreateUserSchema) -> FilesClient:
    """
    Фикстура получения экземпляра FilesClient (c Авторизацией)

    :param create_user: Вложенная Pydantic-фикстура создания пользователя
    :return: Экземпляр класса class FilesClient (c Base URL + АВТОРИЗАЦИЯ)
    """
    files_client = get_files_client(create_user.auth_data)
    return files_client


#----------------------------------------------------- Create File -----------------------------------------------------
# API
@pytest.fixture
def create_file_api(files_client: FilesClient) -> httpx.Response:
    """
    API-фикстура создания файла

    :param files_client: Вложенная фикстура получения экземпляра FilesClient (c Авторизация)
    :return: httpx.Response
    """
    create_file_data = CreateFileRequestSchema()               # Инициализация Pydantic-модели c default fake-data
    response = files_client.create_file_api(create_file_data)  # ▶ Запрос через API-метод
    return response                                            # httpx.Response


# Pydantic-model
@pytest.fixture
def create_file(files_client: FilesClient) -> CreateFileSchema:
    """
    Pydantic-фикстура создания файла

    :param files_client: Вложенная фикстура получения экземпляра FilesClient (c Авторизацией)
    :return: Pydantic-model (CreateFileSchema) ✨<Request + Response>
    """
    create_file_data = CreateFileRequestSchema()                   # Инициализация Pydantic-model c default fake-data
    response_model = files_client.create_file(create_file_data)    # ▶ Запрос через Pydantic-метод
    response_full_model = CreateFileSchema(request=create_file_data, response=response_model) # Инициализация Pydantic-model (CreateFileSchema) ✨<Request + Response>
    return response_full_model                                     # Pydantic-model (CreateFileSchema) ✨<Request + Response>

#------------------------------------------------------- Get File ------------------------------------------------------
# API
@pytest.fixture
def get_file_api(files_client: FilesClient, create_file: CreateFileSchema) -> httpx.Response:
    """
    API-фикстура получения файла

    :param files_client: Вложенная фикстура получения экземпляра FilesClient (c Авторизацией)
    :param create_file: Вложенная Pydantic-фикстура создания файла
    :return: httpx.Response
    """
    response = files_client.get_file_api(create_file.file_id)      # ▶ Запрос через API-метод
    return response                                                # httpx.Response

# Pydantic-model
def get_file(files_client: FilesClient, create_file: CreateFileSchema) -> GetFileResponseSchema:
    """
    Pydantic-фикстура получения файла

    :param files_client: Вложенная фикстура получения экземпляра FilesClient (c Авторизацией)
    :param create_file: Вложенная Pydantic-фикстура создания файла
    :return: httpx.Response
    """
    response_model = files_client.get_file(create_file.file_id)    # ▶ Запрос через Pydantic-метод
    return response_model                                          # Pydantic-model (CreateFileSchema)
#-----------------------------------------------------------------------------------------------------------------------
