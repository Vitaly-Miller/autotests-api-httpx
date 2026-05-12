"""
сonftest.py
Хранение фикстур
"""
import json

import pytest
from httpx import Response
from clients.auth.auth_client import get_auth_client, AuthClient
from clients.auth.auth_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, UserFullSchema, CreateUserResponseSchema

#=======================================================================================================================
"""
---------------------- ⚠️-----------------------
❗️Pydantic-фикстуры - для Pre- Post-conditions ❗️
❗️API-фикстуры      - для Assertions           ❗️
------------------------------------------------
"""

"""===================================================== Clients ===================================================="""
# Public Users Client
@pytest.fixture                                      # scope='function' by Default
def public_users_client() -> PublicUsersClient:
    """
    Фикстура вызова Public Users Client Builder

    :return: PublicUsersClient
    """
    return get_public_users_client()


# Auth client (Authentication)
@pytest.fixture
def auth_client() -> AuthClient:
    """
    Фикстура вызова Auth Client Builder

    :return: AuthClient
    """
    return get_auth_client()


"""=================================================== Create User =================================================="""
#--------------------------------------------------- Pydantic-model ----------------------------------------------------
#--- v.1 --- Возвращает ✨объединенную Pydantic-model: UserFullSchema с данными пользователя <Request + Response>
@pytest.fixture
def create_user(public_users_client: PublicUsersClient) -> UserFullSchema:
    """
    Фикстура СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ (Create User)

    :param public_users_client: Вложенная фикстура Public Users Client
    :return: ✨Pydantic-model: UserFullSchema с объединенными данными пользователя <Request + Response>
    """
    create_user_payload = CreateUserRequestSchema()                          # Инициализация модели с fake-данными нового пользователя по Pydantic-схеме
    response = public_users_client.create_user(payload=create_user_payload)  # ︎▶ Запрос на создание пользователя через метод. Передаем сгенерированные в Pydantic-схеме fake-данные нового пользователя
    return UserFullSchema(request=create_user_payload, response=response)    # Pydantic-model: UserFullSchema ✨с объединенными данными пользователя <Request + Response>


#--- v.2 --- Возвращает Pydantic-model: CreateUserResponseSchema
@pytest.fixture
def create_user_2(public_users_client: PublicUsersClient) -> CreateUserResponseSchema:
    """
    Фикстура СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ (Create User)

    :param public_users_client: Вложенная фикстура Public Users Client
    :return: Pydantic-model: CreateUserResponseSchema
    """
    create_user_payload = CreateUserRequestSchema()                          # Инициализация модели с fake-данными нового пользователя по Pydantic-схеме
    response = public_users_client.create_user(payload=create_user_payload)  # ︎▶ Запрос на создание пользователя через метод. Передаем сгенерированные в Pydantic-схеме fake-данные нового пользователя
    return response                                                          # Pydantic-model: CreateUserResponseSchema


#------------------------------------------------ API —> httpx.Response ------------------------------------------------
@pytest.fixture
def create_user_api(public_users_client: PublicUsersClient) -> Response:
    """
    API-фикстура СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ (Create User)

    :param public_users_client: Вложенная фикстура Public Users Client
    :return: httpx.Response
    """
    create_user_payload = CreateUserRequestSchema()                              # Инициализация модели с fake-данными нового пользователя по Pydantic-схеме
    response = public_users_client.create_user_api(payload=create_user_payload)  # ︎▶ Запрос на создание пользователя через метод. Передаем сгенерированные в Pydantic-схеме fake-данные нового пользователя
    return response                                                              # httpx.Response
                                                                                 # ❗️Если нужно добраться до Request c 'password' - через парсинг JSON —> {dict}:
                                                                                 # request_body = json.loads(response.request.content)
                                                                                 # password = request_body["password"]


"""============================================== Auth (Authentication) ============================================="""
#---------------------------------------------------- Pydantic-model ---------------------------------------------------
#--- v.1 --- Базируется на объединенной Pydantic-model: UserFullSchema
@pytest.fixture
def auth(create_user: UserFullSchema, auth_client: AuthClient) -> LoginResponseSchema:
    """
    Фикстура АВТОРИЗАЦИИ (Log in) пользователя

    :param create_user: Вложенная Pydantic-model-фикстура СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ (Create User)
    :param auth_client: Вложенная фикстура АВТОРИЗАЦИИ пользователя (Log in)
    :return: Response (Pydantic-model)
    """
    login_payload = LoginRequestSchema(          # Инициализация модели с fake-данными нового пользователя по Pydantic-схеме
        email=create_user.email,                 # Email из Pydantic-модели UserFullSchema
        password=create_user.password            # Password из Pydantic-модели UserFullSchema
    )
    response = auth_client.login(login_payload)  # ▶ Запрос на Authentication (Log in) через метод. Передаем payload c Email и Password и сохраняем ответ в переменную
    return response                              # Pydantic-model: LoginResponseSchema


#--- v.2 --- Базируется на Парсинге сырого Request Body bytes
@pytest.fixture
def auth_2(create_user_api: Response, auth_client: AuthClient) -> LoginResponseSchema:
    """
    Фикстура АВТОРИЗАЦИИ (Log in) пользователя

    :param create_user_api: Вложенная API-фикстура СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ (Create User)
    :param auth_client: Вложенная фикстура АВТОРИЗАЦИИ пользователя (Log in)
    :return: Response (Pydantic-model)
    """
    request_body = json.loads(create_user_api.request.content)  # ✨Парсинг сырого Request bytes —> {dict}
    login_payload = LoginRequestSchema(              # Инициализация модели с fake-данными нового пользователя по Pydantic-схеме
        email=request_body['email'],                 # Email из распарсенного Request Body
        password=request_body['password']            # Password распарсенного Request Body
    )
    response = auth_client.login(login_payload)      # ▶ Запрос на Authentication (Log in) через метод. Передаем payload c Email и Password и сохраняем ответ в переменную
    return response                                  # Pydantic-model: LoginResponseSchema


#------------------------------------------------ API —> httpx.Response ------------------------------------------------
#--- v.1 --- Базируется на объединенной Pydantic-model: UserFullSchema
@pytest.fixture
def auth_api(create_user: UserFullSchema, auth_client: AuthClient) -> Response:
    """
    API-фикстура АВТОРИЗАЦИИ (Log in) пользователя

    :param create_user: Вложенная фикстура СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ (Create User)
    :param auth_client: Вложенная фикстура АВТОРИЗАЦИИ пользователя (Log in)
    :return: httpx.Response
    """
    login_payload = LoginRequestSchema(              # Инициализация модели с fake-данными нового пользователя по Pydantic-схеме
        email=create_user.email,                     # Email из Pydantic-модели UserFullSchema
        password=create_user.password                # Password из Pydantic-модели UserFullSchema
    )
    response = auth_client.login_api(login_payload)  # ▶ Запрос на Login (Authentication) через API-метод. Передаем payload c Email и Password и сохраняем ответ в переменную
    return response                                  # httpx.Response

#--- v.2 --- Базируется на Парсинге сырого Request Body bytes
@pytest.fixture
def auth_api_2(create_user_api: Response, auth_client: AuthClient) -> Response:
    """
    API-фикстура АВТОРИЗАЦИИ (Log in) пользователя

    + Парсинг Request JSON —> {dict}
    :param create_user_api: Вложенная API-фикстура СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ (Create User)
    :param auth_client: Вложенная фикстура АВТОРИЗАЦИИ пользователя (Log in)
    :return: httpx.Response
    """
    request_body = json.loads(create_user_api.request.content)  # ✨Парсинг сырого Request bytes —> {dict}
    login_payload = LoginRequestSchema(              # Инициализация модели с fake-данными нового пользователя по Pydantic-схеме
        email=request_body['email'],                 # Email из распарсенного Request Body
        password=request_body['password']            # Password распарсенного Request Body
    )
    response = auth_client.login_api(login_payload)  # ▶ Запрос на Login (Authentication) через API-метод. Передаем payload c Email и Password и сохраняем ответ в переменную
    return response                                  # httpx.Response

#-----------------------------------------------------------------------------------------------------------------------
