"""
Courses (Fixtures)
"""
import httpx
import pytest
from clients.courses_client import get_courses_client, CoursesClient
from schemas.courses_schema import CreateCourseRequestSchema, CreateCourseSchema
from schemas.files_schema import CreateFileSchema
from schemas.users_schema import CreateUserSchema

#=================================================== Courses Client ====================================================
# Courses Client
@pytest.fixture
def courses_client(create_user: CreateUserSchema) -> CoursesClient:
    """
    Фикстура получения экземпляра CoursesClient() (с Авторизацией)

    :param create_user: Вложенная Pydantic-фикстура создания пользователя
    :return: Экземпляр CoursesClient() (с Авторизацией)
    """
    courses_client = get_courses_client(create_user.auth_data)
    return courses_client                            # CoursesClient()


#---------------------------------------------------- Create course ----------------------------------------------------
# API
@pytest.fixture
def create_course_api(
    courses_client: CoursesClient, # ┐  ✨ДЕДУПЛИКАЦИЯ внутри одного теста — это фундаментальное свойство Pytest.
    create_user: CreateUserSchema, # ┘  ✨Один и тоже User! Несмотря на то, что обе фикстуры создают пользователя.
    create_file: CreateFileSchema
) -> httpx.Response:
    """
    API-фикстура создания курса

    ✨ДЕДУПЛИКАЦИЯ внутри одного теста — это фундаментальное свойство Pytest.
    ✨Один и тоже User! Несмотря на то, что обе фикстуры создают пользователя.

    :param courses_client: Вложенная Pydantic-фикстура получения экземпляра CoursesClient (с Авторизацией)
    :param create_user:    Вложенная Pydantic-фикстура создания пользователя (✨тот же User ⬆︎)
    :param create_file:    Вложенная Pydantic-фикстура создания файла
    :return: httpx.Response
    """
    create_course_data = CreateCourseRequestSchema(  # Инициализация Pydantic-модели c default fake-data
        previewFileId=create_file.file_id,           # Заменяем default на реальный File ID
        createdByUserId=create_user.user_id          # Заменяем default на реальный User ID
    )
    response = courses_client.create_course_api(create_course_data)   # ▶ Запрос через API-метод
    return response                                                   # httpx.Response


# Pydantic-model (full)
@pytest.fixture
def create_course(
    courses_client: CoursesClient, # ┐  ✨ДЕДУПЛИКАЦИЯ внутри одного теста — это фундаментальное свойство Pytest.
    create_user: CreateUserSchema, # ┘  ✨Один и тоже User! Несмотря на то, что обе фикстуры создают пользователя.
    create_file: CreateFileSchema
) -> CreateCourseSchema:
    """
    Pydantic-фикстура создания курса

    ✨ДЕДУПЛИКАЦИЯ внутри одного теста — это фундаментальное свойство Pytest.
    ✨Один и тоже User! Несмотря на то, что обе фикстуры создают пользователя.

    :param courses_client: Вложенная Pydantic-фикстура получения экземпляра CoursesClient (с Авторизацией)
    :param create_user:    Вложенная Pydantic-фикстура создания пользователя (✨тот же User ⬆︎)
    :param create_file:    Вложенная Pydantic-фикстура создания файла
    :return: Pydantic-model (CoursesFullSchema) ✨<Request + Response>
    """
    create_course_data = CreateCourseRequestSchema(  # Инициализация Pydantic-модели c default fake-data, кроме: ...
        previewFileId=create_file.file_id,           # Заменяем default на реальный File ID
        createdByUserId=create_user.user_id          # Заменяем default на реальный User ID
    )
    response_model = courses_client.create_course(create_course_data)    # ▶ Запрос через Pydantic-метод
    response_model_full = CreateCourseSchema(request=create_course_data, response=response_model)   # Инициализация Pydantic-model (CoursesFullSchema) ✨<Request + Response>
    return response_model_full                                           # Pydantic-model (CoursesFullSchema) ✨<Request + Response>

#-----------------------------------------------------------------------------------------------------------------------
