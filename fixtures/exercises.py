"""
Exercises fixtures
"""
import httpx
import pytest
from clients.exercises_client import ExercisesClient, get_exercises_client
from schemas.courses import CreateCoursesSchema
from schemas.exercises import CreateExerciseRequestSchema, CreateExerciseSchema
from schemas.users import CreateUserSchema

#================================================== Exercises Client ===================================================
# Exercises Client
@pytest.fixture
def exercises_client(create_user: CreateUserSchema) -> ExercisesClient:
    """
    Фикстура получения экземпляра ExercisesClient (c Авторизацией)

    :param create_user: Вложенная Pydantic-фикстура создания пользователя
    :return: Экземпляр ExercisesClient (c Авторизацией)
    """
    exercises_client = get_exercises_client(create_user.auth_data)
    return exercises_client


#-------------------------------------------------- Create exercise ----------------------------------------------------
# API
def create_exercise_api(exercises_client: ExercisesClient, create_course: CreateCoursesSchema) -> httpx.Response:
    """
    API-фикстура создания задания

    :param exercises_client: Вложенная Pydantic-фикстура получения экземпляра ExercisesClient (с Авторизацией)
    :param create_course: Вложенная Pydantic-фикстура создания курса (для получения Course ID)
    :return: httpx.Response
    """
    create_exercise_data = CreateExerciseRequestSchema(    # Инициализация Pydantic-модели c default fake-data
        courseId=create_course.course_id                   # Заменяем default на реальный Course ID
    )
    response = exercises_client.create_exercise_api(create_exercise_data)  # ▶ Запрос через API-метод
    return response                                                        # httpx.Response


# Pydantic-model
def create_exercise(exercises_client: ExercisesClient, create_course: CreateCoursesSchema) -> CreateExerciseSchema:
    """
    Pydantic-фикстура создания задания

    :param exercises_client: Вложенная Pydantic-фикстура получения экземпляра ExercisesClient (с Авторизацией)
    :param create_course: Вложенная Pydantic-фикстура создания курса (для получения Course ID)
    :return: httpx.Response
    """
    create_exercise_data = CreateExerciseRequestSchema(    # Инициализация Pydantic-модели c default fake-data
        courseId=create_course.course_id                   # Заменяем default на реальный Course ID
    )
    response = exercises_client.create_exercise(create_exercise_data)             # ▶ Запрос через Pydantic-метод
    model = CreateExerciseSchema(request=create_exercise_data, response=response)   # Инициализация Pydantic-model (CoursesFullSchema) ✨<Request + Response>
    return model                                                                  # Pydantic-model (CoursesFullSchema) ✨<Request + Response>


#-----------------------------------------------------------------------------------------------------------------------
