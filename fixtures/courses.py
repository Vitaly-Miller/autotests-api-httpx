"""
Courses fixtures
"""
import httpx
import pytest
from clients.courses.courses_client import get_courses_client, CoursesClient
from schemas.courses import CreateCourseRequestSchema, CoursesFullSchema
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
# API (⚠️В разработке - необходимы реальные данные previewFileId и createdByUserId для позитивного сценария)
@pytest.fixture
def create_course_api(courses_client: CoursesClient) -> httpx.Response:
    """
    API-фикстура создания курса

    :param courses_client: Вложенная фикстура получения экземпляра CoursesClient (с Авторизацией)
    :return: httpx.Response
    """
    create_course_data = CreateCourseRequestSchema(   # Инициализация Pydantic-модели c default fake-data, кроме: ...
        previewFileId='...',                          # ⚠️
        createdByUserId='...'                         # ⚠️
    )
    response = courses_client.create_course_api(create_course_data=create_course_data)   # ▶ Запрос через API-метод
    return response                                   # httpx.Response

# Pydantic-model (⚠️В разработке - необходимы реальные данные previewFileId и createdByUserId для позитивного сценария)
@pytest.fixture
def create_course(courses_client: CoursesClient) -> CoursesFullSchema:
    """
    Pydantic-фикстура создания курса

    :param courses_client: Вложенная фикстура получения CoursesClient (с Авторизацией)
    :return: Pydantic-model (CoursesFullSchema) ✨<Request + Response>
    """
    create_course_data = CreateCourseRequestSchema(   # Инициализация Pydantic-модели c default fake-data, кроме: ...
        previewFileId='...',                          # ⚠️
        createdByUserId='...'                         # ⚠️
    )
    response = courses_client.create_course(create_course_data=create_course_data)  # ▶ Запрос через Pydantic-метод
    model = CoursesFullSchema(request=create_course_data, response=response)        # Инициализация Pydantic-model (CoursesFullSchema) ✨<Request + Response>
    return model                                                                    # Pydantic-model (CoursesFullSchema) ✨<Request + Response>

#-----------------------------------------------------------------------------------------------------------------------
