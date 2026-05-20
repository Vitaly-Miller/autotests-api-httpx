"""
Files fixtures
"""
import httpx
import pytest
from clients.files.files_client import FilesClient, get_files_client
from clients.users.users_schema import UserFullSchema

#==================================================== Files Client =====================================================
# Files Client
@pytest.fixture
def files_client(create_user: UserFullSchema) -> FilesClient:
    """
    Фикстура вызова FilesClient (c Base URL + АВТОРИЗАЦИЯ)

    :param create_user: Фикстура создания пользователя
    :return: Экземпляр класса class FilesClient (c Base URL + АВТОРИЗАЦИЯ)
    """
    return get_files_client(auth_data=create_user.auth_data)


#-----------------------------------------------------------------------------------------------------------------------
# API


# Pydantic-model


#-----------------------------------------------------------------------------------------------------------------------
