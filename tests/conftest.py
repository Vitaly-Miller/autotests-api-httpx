"""
сonftest.py
Хранение фикстур
"""
import httpx
import json
import pytest
from clients.auth.auth_client import get_auth_client, AuthClient
from clients.auth.auth_schema import AuthUserResponseSchema, AuthUserSchema
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
# class PublicUsersClient
@pytest.fixture                                      # scope='function' by Default
def public_users_client() -> PublicUsersClient:
    """
    Фикстура вызова класса PublicUsersClient

    :return: class PublicUsersClient
    """
    return get_public_users_client()


# class AuthClient (Authentication)
@pytest.fixture
def auth_client() -> AuthClient:
    """
    Фикстура вызова класса AuthClient

    :return: class AuthClient
    """
    return get_auth_client()

# class PrivateUsersClient
@pytest.fixture
def private_users_client(create_user: UserFullSchema) -> PrivateUsersClient: # Передаем фикстуру для Pre-condition (create_user)
    """
    Фикстура вызова класса PrivateUsersClient c авторизацией

    :param create_user: Фикстура создания пользователя
    :return: class PrivateUsersClient
    """
    auth_data = AuthUserSchema(                          # Инициализируем данные для авторизации через схему. Сохраняем в переменную Email и Pass
        email=create_user.email,                         # Вытаскиваем .Email из модели <create_user>
        password=create_user.password)                   # Вытаскиваем .Password из модели <create_user>
    return get_private_users_client(auth_data=auth_data) #




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
    create_user_data = CreateUserRequestSchema()                          # Инициализация модели с fake-данными нового пользователя по Pydantic-схеме
    response = public_users_client.create_user(create_user_data=create_user_data) # ︎▶ Запрос на создание пользователя через метод. Передаем сгенерированные в Pydantic-схеме fake-данные нового пользователя
    return UserFullSchema(request=create_user_data, response=response)    # Pydantic-model: UserFullSchema ✨с объединенными данными пользователя <Request + Response>


#--- v.2 --- Возвращает Pydantic-model: CreateUserResponseSchema
@pytest.fixture
def create_user_2(public_users_client: PublicUsersClient) -> CreateUserResponseSchema:
    """
    Фикстура СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ (Create User)

    :param public_users_client: Вложенная фикстура Public Users Client
    :return: Pydantic-model: CreateUserResponseSchema
    """
    create_user_data = CreateUserRequestSchema()                           # Инициализация модели с fake-данными нового пользователя по Pydantic-схеме
    response = public_users_client.create_user(create_user_data=create_user_data)  # ︎▶ Запрос на создание пользователя через метод. Передаем сгенерированные в Pydantic-схеме fake-данные нового пользователя
    return response                                                        # Pydantic-model: CreateUserResponseSchema


#------------------------------------------------ API —> httpx.Response ------------------------------------------------
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
#---------------------------------------------------- Pydantic-model ---------------------------------------------------
#--- v.1 --- Базируется на объединенной Pydantic-model: UserFullSchema
@pytest.fixture
def auth_user(create_user: UserFullSchema, auth_client: AuthClient) -> AuthUserResponseSchema:
    """
    Фикстура АВТОРИЗАЦИИ (Log in) пользователя

    :param create_user: Вложенная Pydantic-model-фикстура СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ (Create User)
    :param auth_client: Вложенная фикстура АВТОРИЗАЦИИ пользователя (Log in)
    :return: Response (Pydantic-model)
    """
    auth_data = AuthUserSchema(              # Инициализация модели с fake-данными нового пользователя по Pydantic-схеме
        email=create_user.email,             # Email из Pydantic-модели UserFullSchema
        password=create_user.password        # Password из Pydantic-модели UserFullSchema
    )
    response = auth_client.login(auth_data=auth_data)  # ▶ Запрос на Authentication (Log in) через метод. Передаем payload c Email и Password и сохраняем ответ в переменную
    return response                          # Pydantic-model: LoginResponseSchema


#--- v.2 --- Базируется на Парсинге сырого Request Body (bytes)
@pytest.fixture
def auth_user_2(create_user_api: httpx.Response, auth_client: AuthClient) -> AuthUserResponseSchema:
    """
    Фикстура АВТОРИЗАЦИИ (Log in) пользователя

    :param create_user_api: Вложенная API-фикстура СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ (Create User)
    :param auth_client: Вложенная фикстура АВТОРИЗАЦИИ пользователя (Log in)
    :return: Response (Pydantic-model)
    """
    request_body = json.loads(create_user_api.request.content)  # ✨Парсинг сырого Request Bytes —> {dict}
    auth_data = AuthUserSchema(             # Инициализация модели с fake-данными нового пользователя по Pydantic-схеме
        email=request_body['email'],        # Email из распарсенного Request Body
        password=request_body['password']   # Password распарсенного Request Body
    )
    response = auth_client.login(auth_data=auth_data)  # ▶ Запрос на Authentication (Log in) через метод. Передаем payload c Email и Password и сохраняем ответ в переменную
    return response                          # Pydantic-model: LoginResponseSchema


#------------------------------------------------ API —> httpx.Response ------------------------------------------------
#--- v.1 --- Базируется на объединенной Pydantic-model: UserFullSchema
@pytest.fixture
def auth_user_api(create_user: UserFullSchema, auth_client: AuthClient) -> httpx.Response:
    """
    API-фикстура АВТОРИЗАЦИИ (Log in) пользователя

    :param create_user: Вложенная фикстура СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ (Create User)
    :param auth_client: Вложенная фикстура АВТОРИЗАЦИИ пользователя (Log in)
    :return: httpx.Response
    """
    auth_data = AuthUserSchema(             # Инициализация модели с fake-данными нового пользователя по Pydantic-схеме
        email=create_user.email,            # Email из Pydantic-модели UserFullSchema
        password=create_user.password       # Password из Pydantic-модели UserFullSchema
    )
    response = auth_client.login_api(auth_data=auth_data)  # ▶ Запрос на Login (Authentication) через API-метод. Передаем payload c Email и Password и сохраняем ответ в переменную
    return response                         # httpx.Response

#--- v.2 --- Базируется на Парсинге сырого Request Body (bytes)
@pytest.fixture
def auth_user_api_2(create_user_api: httpx.Response, auth_client: AuthClient) -> httpx.Response:
    """
    API-фикстура АВТОРИЗАЦИИ (Log in) пользователя

    + Парсинг Request JSON —> {dict}
    :param create_user_api: Вложенная API-фикстура СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ (Create User)
    :param auth_client: Вложенная фикстура АВТОРИЗАЦИИ пользователя (Log in)
    :return: httpx.Response
    """
    request_body = json.loads(create_user_api.request.content)  # ✨Парсинг сырого Request Bytes —> {dict}
    auth_data = AuthUserSchema(             # Инициализация модели с fake-данными нового пользователя по Pydantic-схеме
        email=request_body['email'],        # Email из распарсенного Request Body
        password=request_body['password']   # Password распарсенного Request Body
    )
    response = auth_client.login_api(auth_data=auth_data)  # ▶ Запрос на Login (Authentication) через API-метод. Передаем payload c Email и Password и сохраняем ответ в переменную
    return response                         # httpx.Response

#-----------------------------------------------------------------------------------------------------------------------
"""=================================================== Get User Me =================================================="""
@pytest.fixture
def get_user_me(create_user: UserFullSchema) -> httpx.Response:           # Передаем фикстуру для Pre-condition
    # 1. Авторизационные данные созданного пользователя:
    auth_data = AuthUserSchema(                      # Инициализируем данные для авторизации через схему. Сохраняем в переменную Email и Pass
        email=create_user.email,                     # Вытаскиваем .Email из модели
        password=create_user.password)               # Вытаскиваем .Password из модели
    # 2. Get User Me
    get_user_me_client = get_private_users_client(auth_data)  # Получаем экземпляр PrivateUsersClient c уже настроенным HTTP-клиентом с Base URL
    response = get_user_me_client.get_user_me_api()           # 🟩Get-запрос на получение данных ТЕКУЩЕГО пользователя
    return response                                           # httpx.Response

#-----------------------------------------------------------------------------------------------------------------------
