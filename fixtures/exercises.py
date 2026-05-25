"""
Exercises fixtures
"""
import httpx
import pytest
from clients.exercises_client import ExercisesClient, get_exercises_client
from schemas.users import UserFullSchema

#================================================== Exercises Client ===================================================
# Exercises Client
@pytest.fixture
def exercises_client(create_user: UserFullSchema) -> ExercisesClient:
    """
    Фикстура получения экземпляра ExercisesClient (c Авторизацией)

    :param create_user: Вложенная Pydantic-фикстура создания пользователя
    :return: Экземпляр ExercisesClient (c Авторизацией)
    """
    exercises_client = get_exercises_client(auth_data=create_user.auth_data)
    return exercises_client



#-------------------------------------------------- Create exercise ----------------------------------------------------
# API
def create_exercise() -> httpx.Response:
    ...

# Pydantic-model


#-----------------------------------------------------------------------------------------------------------------------
