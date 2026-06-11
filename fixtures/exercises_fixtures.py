"""
Exercises (Fixtures)
"""
from urllib import response

import httpx
import pytest
from clients.exercises_client import ExercisesClient, get_exercises_client
from schemas.courses_schema import CreateCourseSchema
from schemas.exercises_schema import (
    CreateExerciseRequestSchema, CreateExerciseSchema,
    GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema
)
from schemas.users_schema import CreateUserSchema

#================================================== Exercises Client ===================================================
# Exercises Client
@pytest.fixture
def exercises_client(create_user: CreateUserSchema) -> ExercisesClient:
    """
    Фикстура получения экземпляра ExercisesClient() (c Авторизацией)

    :param create_user: Вложенная Pydantic-фикстура создания пользователя
    :return: Экземпляр ExercisesClient() (c Авторизацией)
    """
    exercises_client = get_exercises_client(create_user.auth_data)
    return exercises_client                                # ExercisesClient()


#-------------------------------------------------- Create exercise ----------------------------------------------------
# API
@pytest.fixture
def create_exercise_api(exercises_client: ExercisesClient, create_course: CreateCourseSchema) -> httpx.Response:
    """
    API-фикстура создания задания

    :param exercises_client: Вложенная Pydantic-фикстура получения экземпляра ExercisesClient() (с Авторизацией)
    :param create_course: Вложенная Pydantic-фикстура создания курса (для получения Course ID)
    :return: httpx.Response
    """
    create_exercise_data = CreateExerciseRequestSchema(    # Pydantic-model c default fake-data
        courseId=create_course.course_id                   # Default —> реальный Course ID из фикстуры
    )
    response = exercises_client.create_exercise_api(create_exercise_data)  # ▶ Запрос через API-метод
    return response                                                        # httpx.Response


# Pydantic-model (full)
@pytest.fixture
def create_exercise(exercises_client: ExercisesClient, create_course: CreateCourseSchema) -> CreateExerciseSchema:
    """
    Pydantic-фикстура создания задания

    :param exercises_client: Вложенная Pydantic-фикстура получения экземпляра ExercisesClient() (с Авторизацией)
    :param create_course: Вложенная Pydantic-фикстура создания курса (для получения Course ID)
    :return: CreateExerciseSchema ✨<Request + Response>
    """
    exercise_data = CreateExerciseRequestSchema(           # Pydantic-model c default fake-data
        courseId=create_course.course_id                   # Default —> реальный Course ID из фикстуры
    )
    response_model = exercises_client.create_exercise(exercise_data)   # ▶ Запрос через Pydantic-метод
    response_model_full = CreateExerciseSchema(request=exercise_data, response=response_model)   # Инициализация Pydantic-model (CoursesFullSchema) ✨<Request + Response>
    return response_model_full                                         # Pydantic-model (CreateExerciseSchema) ✨<Request + Response>


#---------------------------------------------------- Get exercise -----------------------------------------------------
# API
@pytest.fixture
def get_exercise_api(exercises_client: ExercisesClient, create_exercise: CreateExerciseSchema) -> httpx.Response:
    """
    API-фикстура получения задания

    :param exercises_client: Вложенная Pydantic-фикстура получения экземпляра ExercisesClient() (с Авторизацией)
    :param create_exercise: Вложенная Pydantic-фикстура создания задания (для с Exercise ID)
    :return: httpx.Response
    """
    response = exercises_client.get_exercise_api(create_exercise.exercise_id)     # ▶ Запрос через API-метод
    return response                                                               # httpx.Response


# Pydantic-model
@pytest.fixture
def get_exercise(exercises_client: ExercisesClient, create_exercise: CreateExerciseSchema) -> GetExerciseResponseSchema:
    """
    Pydantic-фикстура получения задания

    :param exercises_client: Вложенная Pydantic-фикстура получения экземпляра ExercisesClient() (с Авторизацией)
    :param create_exercise: Вложенная Pydantic-фикстура создания задания (для получения Exercise ID)
    :return: Pydantic-model (GetExerciseResponseSchema)
    """
    response_model = exercises_client.get_exercise(create_exercise.exercise_id)   # ▶ Запрос через Pydantic-метод
    return response_model                                                         # Pydantic-model (GetExercisesResponseSchema)


#--------------------------------------------------- Update exercise ---------------------------------------------------
# API
@pytest.fixture
def update_exercise_api(exercises_client: ExercisesClient, create_exercise: CreateExerciseSchema) -> httpx.Response:
    """
    API-фикстура обновления задания

    :param exercises_client: Вложенная Pydantic-фикстура получения экземпляра ExercisesClient() (с Авторизацией)
    :param create_exercise: Вложенная Pydantic-фикстура создания задания (для получения Exercise ID)
    :return: httpx.Response
    """
    new_exercise_data = UpdateExerciseRequestSchema()                 # Pydantic-model c fake-data (Update ALL)
    response = exercises_client.update_exercise_api(                  # ▶ Запрос через API-метод
        create_exercise.exercise_id,                        # Передаем Exercise ID
        new_exercise_data                             # Передаем данные, которые необходимо обновить
    )
    return response                                                   # httpx.Response


# Pydantic-model
@pytest.fixture
def update_exercise(exercises_client: ExercisesClient, create_exercise: CreateExerciseSchema) -> UpdateExerciseResponseSchema:
    """
    Pydantic-фикстура обновления задания

    :param exercises_client: Вложенная Pydantic-фикстура получения экземпляра ExercisesClient() (с Авторизацией)
    :param create_exercise: Вложенная Pydantic-фикстура создания задания (для получения Exercise ID)
    :return: httpx.Response
    """
    new_exercise_data = UpdateExerciseRequestSchema()                 # Pydantic-model c fake-data (Update ALL)
    response_model = exercises_client.update_exercise(                # ▶ Запрос через Pydantic-метод
        create_exercise.exercise_id,                        # Передаем Exercise ID
        new_exercise_data                             # Передаем данные, которые необходимо обновить
    )
    return response_model                                             # Pydantic-model (UpdateExerciseResponseSchema)

#--------------------------------------------------- Delete exercise ---------------------------------------------------
# API
@pytest.fixture
def delete_exercise_api(exercises_client: ExercisesClient, create_exercise: CreateExerciseSchema) -> httpx.Response:
    """
    API-фикстура удаления задания

    :param exercises_client: Вложенная Pydantic-фикстура получения экземпляра ExercisesClient() (с Авторизацией)
    :param create_exercise: Вложенная Pydantic-фикстура создания задания (для получения Exercise ID)
    :return: httpx.Response
    """
    response = exercises_client.delete_exercise_api(create_exercise.exercise_id) # ▶ Запрос через API-метод
    return response                                                              # httpx.Response
#-----------------------------------------------------------------------------------------------------------------------
