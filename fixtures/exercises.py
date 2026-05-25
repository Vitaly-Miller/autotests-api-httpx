"""
Exercises fixtures
"""
import httpx
import pytest
from clients.exercises.exercises_client import ExercisesClient, get_exercises_client
from clients.users.users_schema import UserFullSchema

#================================================== Exercises Client ===================================================
# Exercises Client
@pytest.fixture
def exercises_client(create_user: UserFullSchema) -> ExercisesClient:
    """
    Фикстура вызова экземпляра ExercisesClient (c Авторизацией)

    :param create_user: Вложенная Pydantic-фикстура создания пользователя
    :return: Экземпляр ExercisesClient (c Авторизацией)
    """
    return get_exercises_client(auth_data=create_user.auth_data)



#-----------------------------------------------------------------------------------------------------------------------
# API


# Pydantic-model


#-----------------------------------------------------------------------------------------------------------------------
