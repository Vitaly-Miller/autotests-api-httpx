"""
conftest.py
Хранение фикстур
"""
"""
⚠️НЕ ИСПОЛЬЗУЕТСЯ! 
- ФИКСТУРЫ РАСПРЕДЕЛЕНЫ ПО МОДУЛЯМ-ФАЙЛАМ
- conftest.py вынесен в корень проекта и использует pytest_plugins = ()
"""
import httpx
import pytest
from clients.auth_client import get_auth_client, AuthClient
from schemas.auth import AuthUserResponseSchema
from clients.courses_client import CoursesClient, get_courses_client
from clients.exercises_client import ExercisesClient, get_exercises_client
from clients.files_client import get_files_client, FilesClient
from clients.private_users_client import PrivateUsersClient, get_private_users_client
from clients.public_users_client import get_public_users_client, PublicUsersClient
from schemas.users import CreateUserRequestSchema, GetUserMeResponseSchema, UserFullSchema

#=======================================================================================================================
"""
---------------------- ⚠️-----------------------
❗️Pydantic-фикстуры - для Pre- Post-conditions ❗️
❗️API-фикстуры      - для Assertions           ❗️
------------------------------------------------
"""

"""==================================================== Clients ====================================================="""
# Public Users Client
@pytest.fixture   # scope='function' by Default
def public_users_client() -> PublicUsersClient:
    """
    Фикстура вызова класса Public Users Client (c Base URL)

    :return: Экземпляр класса PublicUsersClient (c Base URL)
    """
    return get_public_users_client()


# Auth Client (Authentication)
@pytest.fixture
def auth_client() -> AuthClient:
    """
    Фикстура вызова Auth Client (c Base URL)

    :return: Экземпляр класса AuthClient (c Base URL)
    """
    return get_auth_client()


# Private Users Client
@pytest.fixture
def private_users_client(create_user: UserFullSchema) -> PrivateUsersClient:
    """
    Фикстура вызова Private Users Client (c Base URL + АВТОРИЗАЦИЯ)

    :param create_user: Фикстура создания пользователя
    :return: Экземпляр класса PrivateUsersClient (c Base URL + АВТОРИЗАЦИЯ)
    """
    return get_private_users_client(auth_data=create_user.auth_data)


# Files Client
@pytest.fixture
def files_client(create_user: UserFullSchema) -> FilesClient:
    """
    Фикстура вызова FilesClient (c Base URL + АВТОРИЗАЦИЯ)

    :param create_user: Фикстура создания пользователя
    :return: Экземпляр класса class FilesClient (c Base URL + АВТОРИЗАЦИЯ)
    """
    return get_files_client(auth_data=create_user.auth_data)


# Courses Client
@pytest.fixture
def courses_client(create_user: UserFullSchema) -> CoursesClient:
    """
    Фикстура вызова Courses Client (c Base URL + АВТОРИЗАЦИЯ)

    :param create_user: Фикстура создания пользователя
    :return: Экземпляр класса CoursesClient (c Base URL + АВТОРИЗАЦИЯ)
    """
    return get_courses_client(auth_data=create_user.auth_data)


# Exercises Client
@pytest.fixture
def exercises_client(create_user: UserFullSchema) -> ExercisesClient:
    """
    Фикстура вызова Exercises Client (c Base URL + АВТОРИЗАЦИЯ)

    :param create_user: Фикстура создания пользователя
    :return: Экземпляр класса ExercisesClient (c Base URL + АВТОРИЗАЦИЯ)
    """
    return get_exercises_client(auth_data=create_user.auth_data)


"""===================================================== Методы ====================================================="""
#----------------------------------------------------- Create User -----------------------------------------------------
# API
@pytest.fixture
def create_user_api(public_users_client: PublicUsersClient) -> httpx.Response:
    """
    API-фикстура СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ (Create User)

    :param public_users_client: Вложенная фикстура Public Users Client
    :return: httpx.Response
    """
    create_user_data = CreateUserRequestSchema()          # Инициализация модели с fake-данными нового пользователя по Pydantic-схеме
    response = public_users_client.create_user_api(create_user_data=create_user_data)  # ▶ Запрос на создание пользователя через метод. Передаем fake-данные нового пользователя.
    return response                                       # httpx.Response
                                                          # ❗️Если нужно добраться до Request c 'password' - через парсинг JSON —> {dict}:
                                                          # request_body = json.loads(response.request.content)
                                                          # password = request_body["password"]
# Pydantic-model
@pytest.fixture
def create_user(public_users_client: PublicUsersClient) -> UserFullSchema:
    """
    Фикстура СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ (Create User)

    :param public_users_client: Вложенная фикстура Public Users Client
    :return: ✨Pydantic-model: UserFullSchema с объединенными данными пользователя <Request + Response>
    """
    create_user_data = CreateUserRequestSchema()                         # Инициализация модели с fake-данными нового пользователя по Pydantic-схеме
    response = public_users_client.create_user(create_user_data=create_user_data) # ︎▶ Запрос на создание пользователя. Передаем fake-данные нового пользователя.
    return UserFullSchema(request=create_user_data, response=response)   # Pydantic-model: UserFullSchema ✨с объединенными данными пользователя <Request + Response>


#------------------------------------------------ Auth (Authentication) ------------------------------------------------
# API
@pytest.fixture
def auth_user_api(create_user: UserFullSchema, auth_client: AuthClient) -> httpx.Response:
    """
    API-фикстура АВТОРИЗАЦИИ (Log in) пользователя

    :param create_user: Вложенная фикстура СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ (Create User)
    :param auth_client: Вложенная фикстура АВТОРИЗАЦИИ пользователя (Log in)
    :return: httpx.Response
    """
    response = auth_client.login_api(auth_data=create_user.auth_data)    # ▶ Запрос на Authentication (Log in) через API-метод. Передаем auth_data c Email и Password и сохраняем ответ в переменную.
    return response                                                      # httpx.Response


# Pydantic-model
@pytest.fixture
def auth_user(create_user: UserFullSchema, auth_client: AuthClient) -> AuthUserResponseSchema:
    """
    Фикстура АВТОРИЗАЦИИ (Log in) пользователя (Pydantic-model)

    :param create_user: Вложенная Pydantic-model-фикстура СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ (Create User)
    :param auth_client: Вложенная фикстура АВТОРИЗАЦИИ пользователя (Log in)
    :return: Pydantic-model: AuthUserResponseSchema
    """
    response = auth_client.login(auth_data=create_user.auth_data)        # ▶ Запрос на Authentication (Log in). Передаем auth_data c Email и Password и сохраняем ответ в переменную.
    return response                                                      # Pydantic-model: AuthUserResponseSchema


#----------------------------------------------------- Get User Me -----------------------------------------------------
# API
@pytest.fixture
def get_user_me_api(private_users_client: PrivateUsersClient) -> httpx.Response:
    """
    Фикстура получения данных ТЕКУЩЕГО пользователя

    :param private_users_client: Экземпляр класса PrivateUsersClient (c Base URL + Auth)
    :return: httpx.Response
    """
    response = private_users_client.get_user_me_api()   # ▶ Запрос на получение данных ТЕКУЩЕГО пользователя
    return response                                     # httpx.Response

# Pydantic-model
@pytest.fixture
def get_user_me(private_users_client: PrivateUsersClient) -> GetUserMeResponseSchema:
    """
    Фикстура получения данных ТЕКУЩЕГО пользователя в формате Pydantic-model

    :param private_users_client: Экземпляр класса PrivateUsersClient (c Base URL + Auth)
    :return: Pydantic-model: GetUserMeResponseSchema
    """
    response = private_users_client.get_user_me()       # ▶ Запрос на получение данных ТЕКУЩЕГО пользователя
    return response                                     # Pydantic-model: GetUserMeResponseSchema


#-----------------------------------------------------------------------------------------------------------------------
