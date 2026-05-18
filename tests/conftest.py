"""
сonftest.py
Хранение фикстур
"""
import httpx
import json
import pytest
from clients.auth.auth_client import get_auth_client, AuthClient
from clients.auth.auth_schema import AuthUserResponseSchema, AuthUserSchema
from clients.courses.courses_client import CoursesClient, get_courses_client
from clients.exercises.exercises_client import ExercisesClient, get_exercises_client
from clients.files.files_client import get_files_client, FilesClient
from clients.users.private_users_client import PrivateUsersClient, get_private_users_client
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, UserFullSchema, CreateUserResponseSchema

#=======================================================================================================================
"""
---------------------- ⚠️-----------------------
❗️Pydantic-фикстуры - для Pre- Post-conditions ❗️
❗️API-фикстуры      - для Assertions           ❗️
------------------------------------------------
"""

"""=================================================== CLASS Clients ================================================"""
# Public Users Client
@pytest.fixture                                      # scope='function' by Default
def public_users_client() -> PublicUsersClient:
    """
    Фикстура вызова класса PublicUsersClient

    :return: class PublicUsersClient
    """
    return get_public_users_client()

# Auth Client (Authentication)
@pytest.fixture
def auth_client() -> AuthClient:
    """
    Фикстура вызова Auth Client (c Base URL)

    :return: class AuthClient
    """
    return get_auth_client()

# Private Users Client
@pytest.fixture
def private_users_client(create_user: UserFullSchema) -> PrivateUsersClient: # Передаем фикстуру для Pre-condition (create_user)
    """
    Фикстура вызова Private Users Client (c Base URL + АВТОРИЗАЦИЯ)

    :param create_user: Фикстура создания пользователя
    :return: class PrivateUsersClient
    """
    return get_private_users_client(auth_data=create_user.auth_data)

# Files Client
@pytest.fixture
def files_client(create_user: UserFullSchema) -> FilesClient: # Передаем фикстуру для Pre-condition (create_user)
    """
    Фикстура вызова FilesClient (c Base URL + АВТОРИЗАЦИЯ)

    :param create_user: Фикстура создания пользователя
    :return: class FilesClient
    """
    return get_files_client(auth_data=create_user.auth_data)

# Courses Client
@pytest.fixture
def courses_client(create_user: UserFullSchema) -> CoursesClient:  # Передаем фикстуру для Pre-condition (create_user)
    """
    Фикстура вызова Courses Client (c Base URL + АВТОРИЗАЦИЯ)

    :param create_user: Фикстура создания пользователя
    :return: class CoursesClient
    """
    return get_courses_client(auth_data=create_user.auth_data)

# Exercises Client
@pytest.fixture
def exercises_client(create_user: UserFullSchema) -> ExercisesClient:  # Передаем фикстуру для Pre-condition (create_user)
    """
    Фикстура вызова Exercises Client (c Base URL + АВТОРИЗАЦИЯ)

    :param create_user: Фикстура создания пользователя
    :return: class ExercisesClient
    """
    return get_exercises_client(auth_data=create_user.auth_data)


"""=================================================== Create User =================================================="""
# Pydantic-model
@pytest.fixture
def create_user(public_users_client: PublicUsersClient) -> UserFullSchema:
    """
    Фикстура СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ (Create User)

    :param public_users_client: Вложенная фикстура Public Users Client
    :return: ✨Pydantic-model: UserFullSchema с объединенными данными пользователя <Request + Response>
    """
    create_user_data = CreateUserRequestSchema()                          # Инициализация модели с fake-данными нового пользователя по Pydantic-схеме
    response = public_users_client.create_user(create_user_data=create_user_data) # ︎▶ Запрос на создание пользователя через метод. Передаем сгенерированные в Pydantic-схеме fake-данные нового пользователя
    return UserFullSchema(request=create_user_data, response=response)    # Pydantic-model: UserFullSchema ✨с объединенными данными пользователя <Request + Response>


# API
@pytest.fixture
def create_user_api(public_users_client: PublicUsersClient) -> httpx.Response:
    """
    API-фикстура СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ (Create User)

    :param public_users_client: Вложенная фикстура Public Users Client
    :return: httpx.Response
    """
    create_user_data = CreateUserRequestSchema()                            # Инициализация модели с fake-данными нового пользователя по Pydantic-схеме
    response = public_users_client.create_user_api(create_user_data=create_user_data)  # ︎▶ Запрос на создание пользователя через метод. Передаем сгенерированные в Pydantic-схеме fake-данные нового пользователя
    return response                                                         # httpx.Response
                                                                            # ❗️Если нужно добраться до Request c 'password' - через парсинг JSON —> {dict}:
                                                                            # request_body = json.loads(response.request.content)
                                                                            # password = request_body["password"]


"""============================================== Auth (Authentication) ============================================="""
# Pydantic-model
@pytest.fixture
def auth_user(create_user: UserFullSchema, auth_client: AuthClient) -> AuthUserResponseSchema:
    """
    Фикстура АВТОРИЗАЦИИ (Log in) пользователя

    :param create_user: Вложенная Pydantic-model-фикстура СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ (Create User)
    :param auth_client: Вложенная фикстура АВТОРИЗАЦИИ пользователя (Log in)
    :return: Response (Pydantic-model)
    """
    response = auth_client.login(auth_data=create_user.auth_data)  # ▶ Запрос на Authentication (Log in) через метод. Передаем payload c Email и Password и сохраняем ответ в переменную
    return response                                                # Pydantic-model: AuthUserResponseSchema


# API
@pytest.fixture
def auth_user_api(create_user: UserFullSchema, auth_client: AuthClient) -> httpx.Response:
    """
    API-фикстура АВТОРИЗАЦИИ (Log in) пользователя

    :param create_user: Вложенная фикстура СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ (Create User)
    :param auth_client: Вложенная фикстура АВТОРИЗАЦИИ пользователя (Log in)
    :return: httpx.Response
    """
    response = auth_client.login_api(auth_data=create_user.auth_data)  # ▶ Запрос на Login (Authentication) через API-метод. Передаем payload c Email и Password и сохраняем ответ в переменную
    return response                         # httpx.Response


#-----------------------------------------------------------------------------------------------------------------------
"""=================================================== Get User Me =================================================="""
# API
@pytest.fixture
def get_user_me(private_users_client: PrivateUsersClient) -> httpx.Response:  # Передаем фикстуру для Pre-condition
    response = private_users_client.get_user_me_api()   # 🟩Get-запрос на получение данных ТЕКУЩЕГО пользователя
    return response                                     # httpx.Response

#-----------------------------------------------------------------------------------------------------------------------
