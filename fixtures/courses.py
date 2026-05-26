"""
Courses fixtures
"""
import httpx
import pytest
from clients.courses_client import get_courses_client, CoursesClient
from schemas.courses import CreateCourseRequestSchema, CoursesFullSchema
from schemas.files import FileFullSchema
from schemas.users import UserFullSchema

#=================================================== Courses Client ====================================================
# Courses Client
@pytest.fixture
def courses_client(create_user: UserFullSchema) -> CoursesClient:
    """
    Фикстура получения экземпляра CoursesClient (с Авторизацией)

    :param create_user: Вложенная Pydantic-фикстура создания пользователя
    :return: Экземпляр CoursesClient (с Авторизацией)
    """
    courses_client = get_courses_client(auth_data=create_user.auth_data)
    return courses_client


#---------------------------------------------------- Create course ----------------------------------------------------
# API
@pytest.fixture
def create_course_api(
    courses_client: CoursesClient, # ┐ ✨ДЕДУПЛИКАЦИЯ внутри одного теста — это фундаментальное свойство Pytest.
    create_user: UserFullSchema,   # ┘ ✨Один и тоже User! Несмотря на то, что обе фикстуры создают пользователя.
    create_file: FileFullSchema
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
    create_course_data = CreateCourseRequestSchema(  # Инициализация Pydantic-модели c default fake-data, кроме: ...
        previewFileId=create_file.file_id,           # Берем File ID из FileFullSchema
        createdByUserId=create_user.user_id          # Берем User ID из UserFullSchema
    )
    response = courses_client.create_course_api(create_course_data=create_course_data)   # ▶ Запрос через API-метод
    return response                                  # httpx.Response



# Pydantic-model
@pytest.fixture
def create_course(
    courses_client: CoursesClient, # ┐ ✨ДЕДУПЛИКАЦИЯ внутри одного теста — это фундаментальное свойство Pytest.
    create_user: UserFullSchema,   # ┘ ✨Один и тоже User! Несмотря на то, что обе фикстуры создают пользователя.
    create_file: FileFullSchema
) -> CoursesFullSchema:
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
        previewFileId=create_file.file_id,           # Берем File ID из FileFullSchema
        createdByUserId=create_user.user_id          # Берем User ID из UserFullSchema
    )
    response = courses_client.create_course(create_course_data=create_course_data)  # ▶ Запрос через Pydantic-метод
    model = CoursesFullSchema(request=create_course_data, response=response)        # Инициализация Pydantic-model (CoursesFullSchema) ✨<Request + Response>
    return model                                                                    # Pydantic-model (CoursesFullSchema) ✨<Request + Response>

#-----------------------------------------------------------------------------------------------------------------------
