"""
Files fixtures
"""
import httpx
import pytest
from clients.files.files_client import FilesClient, get_files_client
from clients.files.files_schema import CreateFileRequestSchema, FileFullSchema
from clients.users.users_schema import UserFullSchema

#==================================================== Files Client =====================================================
# Files Client
@pytest.fixture
def files_client(create_user: UserFullSchema) -> FilesClient:
    """
    Фикстура вызова FilesClient (c Base URL + АВТОРИЗАЦИЯ)

    :param create_user: Вложенная фикстура создания пользователя
    :return: Экземпляр класса class FilesClient (c Base URL + АВТОРИЗАЦИЯ)
    """
    return get_files_client(auth_data=create_user.auth_data)


#----------------------------------------------------- Create File -----------------------------------------------------
# API
@pytest.fixture
def create_file_api(files_client: FilesClient) -> httpx.Response:
    """
    API-фикстура создания файла

    :param files_client: Вложенная фикстура Files Client (с Авторизацией)
    :return: httpx.Response
    """
    create_file_data = CreateFileRequestSchema()                                # Инициализация модели c Default data по Pydantic-схеме
    response = files_client.create_file_api(create_file_data=create_file_data)  # ▶ Запрос на создание на создание файла через API-метод. Передаем данные файла.
    return response                                                             # httpx.Response

# Pydantic-model
@pytest.fixture
def create_file(files_client: FilesClient) -> FileFullSchema:
    """
    Фикстура создания файла

    :param files_client: Вложенная фикстура Files Client (с Авторизацией)
    :return: Pydantic-model: FileFullSchema
    """
    create_file_data = CreateFileRequestSchema()                            # Инициализация модели c Default data по Pydantic-схеме
    response = files_client.create_file(create_file_data=create_file_data)  # ▶ Запрос на создание на создание файла. Передаем данные файла
    return FileFullSchema(request=create_file_data, response=response)      # Pydantic-model: FileFullSchema ✨с объединенными данными <Request + Response>

#-----------------------------------------------------------------------------------------------------------------------
