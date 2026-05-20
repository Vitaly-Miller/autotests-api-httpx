"""
Files fixtures
"""
import httpx
import pytest

from clients.courses.courses_client import get_courses_client, CoursesClient
from clients.users.users_schema import UserFullSchema

#=================================================== Courses Client ====================================================
# Courses Client
@pytest.fixture
def courses_client(create_user: UserFullSchema) -> CoursesClient:
    """
    Фикстура вызова Courses Client (c Base URL + АВТОРИЗАЦИЯ)

    :param create_user: Фикстура создания пользователя
    :return: Экземпляр класса CoursesClient (c Base URL + АВТОРИЗАЦИЯ)
    """
    return get_courses_client(auth_data=create_user.auth_data)



#-----------------------------------------------------------------------------------------------------------------------
# API


# Pydantic-model


#-----------------------------------------------------------------------------------------------------------------------
