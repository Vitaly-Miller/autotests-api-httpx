"""
Exercises (Fixtures)
"""
import httpx
import pytest
import allure
from clients.exercises_client import ExercisesClient, get_exercises_client
from schemas.courses_schema import CreateCourseSchema
from schemas.users_schema import CreateUserSchema
from schemas.exercises_schema import (
    CreateExerciseRequestSchema, CreateExerciseSchema,
    GetExerciseResponseSchema, GetExercisesQuerySchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema
)

#================================================== Exercises Client ===================================================
# Exercises Client
@pytest.fixture
@allure.title('◎ Exercises Client (fixture)')
def exercises_client(create_user: CreateUserSchema) -> ExercisesClient:
    """
    Fixture that provides an ExercisesClient() instance (with Authorization)

    :param create_user: Nested Pydantic fixture that creates a user
    :return: ExercisesClient() instance (with Authorization)
    """
    exercises_client = get_exercises_client(create_user.auth_data)
    return exercises_client                                # ExercisesClient()


#-------------------------------------------------- Create exercise ----------------------------------------------------
# API
@pytest.fixture
@allure.title('▷ Create Exercise (API-fixture)')
def create_exercise_api(exercises_client: ExercisesClient, create_course: CreateCourseSchema) -> httpx.Response:
    """
    API fixture that creates an exercise

    :param exercises_client: Nested Pydantic fixture that provides an ExercisesClient() instance (with Authorization)
    :param create_course: Nested Pydantic fixture that creates a course (to get the Course-ID)
    :return: httpx.Response
    """
    create_exercise_data = CreateExerciseRequestSchema(   # Pydantic-model c default fake-data
        courseId=create_course.course_id                  # Default —> реальный Course-ID из фикстуры
    )
    response = exercises_client.create_exercise_api(create_exercise_data)  # ▶ Запрос через API-метод
    return response                                       # httpx.Response


# Pydantic-model (full)
@pytest.fixture
@allure.title('▷ Create Exercise (Pydantic-fixture)')
def create_exercise(exercises_client: ExercisesClient, create_course: CreateCourseSchema) -> CreateExerciseSchema:
    """
    Pydantic fixture that creates an exercise

    :param exercises_client: Nested Pydantic fixture that provides an ExercisesClient() instance (with Authorization)
    :param create_course: Nested Pydantic fixture that creates a course (to get the Course-ID)
    :return: CreateExerciseSchema ✨<Request + Response>
    """
    exercise_data = CreateExerciseRequestSchema(         # Pydantic-model c default fake-data
        courseId=create_course.course_id                 # Default —> реальный Course-ID из фикстуры
    )
    response_model = exercises_client.create_exercise(exercise_data)   # ▶ Запрос через Pydantic-метод
    response_model_full = CreateExerciseSchema(request=exercise_data, response=response_model)  # Инициализация Pydantic-model (CoursesFullSchema) ✨<Request + Response>
    return response_model_full                           # Pydantic-model (CreateExerciseSchema) ✨<Request + Response>


#---------------------------------------------------- Get exercise -----------------------------------------------------
# API
@pytest.fixture
@allure.title('▷ Get Exercise (API-fixture)')
def get_exercise_api(exercises_client: ExercisesClient, create_exercise: CreateExerciseSchema) -> httpx.Response:
    """
    API fixture that gets an Exercise by Exercise-ID

    :param exercises_client: Nested Pydantic fixture that provides an ExercisesClient() instance (with Authorization)
    :param create_exercise: Nested Pydantic fixture that creates an exercise (to get the Exercise-ID)
    :return: httpx.Response
    """
    response = exercises_client.get_exercise_api(create_exercise.exercise_id)     # ▶ Запрос через API-метод
    return response                                                               # httpx.Response


# Pydantic-model
@pytest.fixture
@allure.title('▷ Get Exercise (Pydantic-fixture)')
def get_exercise(exercises_client: ExercisesClient, create_exercise: CreateExerciseSchema) -> GetExerciseResponseSchema:
    """
    Pydantic fixture that gets an Exercise by Exercise-ID

    :param exercises_client: Nested Pydantic fixture that provides an ExercisesClient() instance (with Authorization)
    :param create_exercise: Nested Pydantic fixture that creates an exercise (to get the Exercise-ID)
    :return: Pydantic-model (GetExerciseResponseSchema)
    """
    response_model = exercises_client.get_exercise(create_exercise.exercise_id)   # ▶ Запрос через Pydantic-метод
    return response_model                                                         # Pydantic-model (GetExercisesResponseSchema)


#---------------------------------------------------- Get exercises ----------------------------------------------------
# API
@pytest.fixture
@allure.title('▷ Get Exercises (API-fixture)')
def get_exercises_api(exercises_client: ExercisesClient, create_course: CreateCourseSchema) -> httpx.Response:
    """
    API fixture that gets a list of Exercises by Course-ID

    :param exercises_client: Nested Pydantic fixture that provides an ExercisesClient() instance (with Authorization)
    :param create_course: Nested Pydantic fixture that creates a course (to get the Course-ID)
    :return: httpx.Response
    """
    course_id_query_model = GetExercisesQuerySchema(courseId=create_course.course_id) # Pydantic-model

    response = exercises_client.get_exercises_api(course_id_query_model)              # ▶ Запрос через API-метод
    return response                                                                   # httpx.Response


#--------------------------------------------------- Update exercise ---------------------------------------------------
# API
@pytest.fixture
@allure.title('▷ Update Exercise (API-fixture)')
def update_exercise_api(exercises_client: ExercisesClient, create_exercise: CreateExerciseSchema) -> httpx.Response:
    """
    API fixture that updates an Exercise by ID

    :param exercises_client: Nested Pydantic fixture that provides an ExercisesClient() instance (with Authorization)
    :param create_exercise: Nested Pydantic fixture that creates an exercise (to get the Exercise-ID)
    :return: httpx.Response
    """
    new_exercise_data = UpdateExerciseRequestSchema()         # Pydantic-model c fake-data (Update ALL)
    response = exercises_client.update_exercise_api(          # ▶ Запрос через API-метод
        create_exercise.exercise_id,                # Передаем Exercise-ID
        new_exercise_data                     # Передаем данные, которые необходимо обновить
    )
    return response                                           # httpx.Response


# Pydantic-model
@pytest.fixture
@allure.title('▷ Update Exercise (Pydantic-fixture)')
def update_exercise(exercises_client: ExercisesClient, create_exercise: CreateExerciseSchema) -> UpdateExerciseResponseSchema:
    """
    Pydantic fixture that updates an Exercise by ID

    :param exercises_client: Nested Pydantic fixture that provides an ExercisesClient() instance (with Authorization)
    :param create_exercise: Nested Pydantic fixture that creates an exercise (to get the Exercise-ID)
    :return: httpx.Response
    """
    new_exercise_data = UpdateExerciseRequestSchema()        # Pydantic-model c fake-data (Update ALL)
    response_model = exercises_client.update_exercise(       # ▶ Запрос через Pydantic-метод
        create_exercise.exercise_id,               # Передаем Exercise-ID
        new_exercise_data                    # Передаем данные, которые необходимо обновить
    )
    return response_model                                    # Pydantic-model (UpdateExerciseResponseSchema)


#--------------------------------------------------- Delete exercise ---------------------------------------------------
# API
@pytest.fixture
@allure.title('▷ Delete Exercise (API-fixture)')
def delete_exercise_api(exercises_client: ExercisesClient, create_exercise: CreateExerciseSchema) -> httpx.Response:
    """
    API fixture that deletes an Exercise by ID

    :param exercises_client: Nested Pydantic fixture that provides an ExercisesClient() instance (with Authorization)
    :param create_exercise: Nested Pydantic fixture that creates an exercise (to get the Exercise-ID)
    :return: httpx.Response
    """
    response = exercises_client.delete_exercise_api(create_exercise.exercise_id)   # ▶ Запрос через API-метод
    return response                                                                # httpx.Response


#=======================================================================================================================
