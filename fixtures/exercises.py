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
    Фикстура вызова Exercises Client (c Base URL + АВТОРИЗАЦИЯ)

    :param create_user: Фикстура создания пользователя
    :return: Экземпляр класса ExercisesClient (c Base URL + АВТОРИЗАЦИЯ)
    """
    return get_exercises_client(auth_data=create_user.auth_data)



#-----------------------------------------------------------------------------------------------------------------------
# API


# Pydantic-model


#-----------------------------------------------------------------------------------------------------------------------
