"""
Files fixtures
"""
import httpx
import pytest
from clients.files_client import FilesClient, get_files_client
from schemas.files import CreateFileRequestSchema, FileFullSchema
from schemas.users import UserFullSchema

#==================================================== Files Client =====================================================
# Files Client
@pytest.fixture
def files_client(create_user: UserFullSchema) -> FilesClient:
    """
    Фикстура получения экземпляра FilesClient (c Авторизация)

    :param create_user: Вложенная Pydantic-фикстура создания пользователя
    :return: Экземпляр класса class FilesClient (c Base URL + АВТОРИЗАЦИЯ)
    """
    files_client = get_files_client(auth_data=create_user.auth_data)
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
    create_file_data = CreateFileRequestSchema()                                # Инициализация Pydantic-модели c default fake-data
    response = files_client.create_file_api(create_file_data=create_file_data)  # ▶ Запрос через API-метод
    return response                                                             # httpx.Response

# Pydantic-model
@pytest.fixture
def create_file(files_client: FilesClient) -> FileFullSchema:
    """
    Pydantic-фикстура создания файла

    :param files_client: Вложенная фикстура получения экземпляра FilesClient (c Авторизация)
    :return: Pydantic-model (FileFullSchema) ✨<Request + Response>
    """
    create_file_data = CreateFileRequestSchema()                             # Инициализация Pydantic-model c default fake-data
    response = files_client.create_file(create_file_data=create_file_data)   # ▶ Запрос через Pydantic-метод
    model = FileFullSchema(request=create_file_data, response=response)      # Инициализация Pydantic-model (FileFullSchema) ✨<Request + Response>
    return model                                                             # Pydantic-model (FileFullSchema) ✨<Request + Response>

#-----------------------------------------------------------------------------------------------------------------------
