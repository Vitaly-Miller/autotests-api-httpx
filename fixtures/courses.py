"""
Courses fixtures
"""
import httpx
import pytest
from clients.courses.courses_client import get_courses_client, CoursesClient
from clients.courses.courses_schema import CreateCourseRequestSchema, CoursesFullSchema
from clients.users.users_schema import UserFullSchema

#=================================================== Courses Client ====================================================
# Courses Client
@pytest.fixture
def courses_client(create_user: UserFullSchema) -> CoursesClient:
    """
    Фикстура вызова экземпляра CoursesClient (с Авторизацией)

    :param create_user: Вложенная Pydantic-фикстура создания пользователя
    :return: Экземпляр CoursesClient (с Авторизацией)
    """
    return get_courses_client(auth_data=create_user.auth_data)



#-----------------------------------------------------------------------------------------------------------------------
# API
@pytest.fixture
def create_course_api(courses_client: CoursesClient) -> httpx.Response:
    """
    API-фикстура создания курса

    :param courses_client: Вложенная фикстура вызова экземпляра CoursesClient (с Авторизацией)
    :return: httpx.Response
    """
    create_course_data = CreateCourseRequestSchema()
    response = courses_client.create_course_api(create_course_data=create_course_data)
    return response

# Pydantic-model
@pytest.fixture
def create_course(courses_client: CoursesClient) -> CoursesFullSchema:
    """
    Pydantic-фикстура создания курса

    :param courses_client: Вложенная фикстура вызова CoursesClient (с Авторизацией)
    :return: Pydantic-model: CoursesFullSchema
    """
    create_course_data = CreateCourseRequestSchema()
    response = courses_client.create_course(create_course_data=create_course_data)
    return CoursesFullSchema(request=create_course_data, response=response)

#-----------------------------------------------------------------------------------------------------------------------
