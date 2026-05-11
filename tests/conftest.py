"""
сonftest.py
Хранение фикстур
"""
import pytest
from httpx import Response
from clients.auth.auth_client import get_auth_client, AuthClient
from clients.auth.auth_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, UserFullSchema

#=======================================================================================================================
"""
---------------------- ⚠️-----------------------
❗️Pydantic-фикстуры - для Pre- Post-conditions ❗️
❗️API-фикстуры      - для Assertions           ❗️
------------------------------------------------
"""
#--------------------------------------------------- Client (public) ---------------------------------------------------
@pytest.fixture                                      # scope='function' by Default
def public_users_client() -> PublicUsersClient:
    """
    Фикстура вызова Client Builder (Public) - get_public_users_client()

    :return: Client Builder (Public) - get_public_users_client()
    """
    return get_public_users_client()

#--------------------------------------------- Auth client (Authentication) --------------------------------------------
@pytest.fixture
def auth_client() -> AuthClient:
    """
    Фикстура вызова Client Builder (Public) - get_auth_client()

    :return: Client Builder (Public) - get_auth_client()
    """
    return get_auth_client()


#----------------------------------------------------- Create User -----------------------------------------------------
@pytest.fixture
def create_user(public_users_client: PublicUsersClient) -> UserFullSchema:
    """
    Фикстура СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ (Create User)

    :param public_users_client: Вложенная фикстура Public Users Client
    :return: ✨Объединенные данные о пользователе (Request + Response) в формате Pydantic-model
    """
    create_user_payload = CreateUserRequestSchema()                          # Инициализация модели с fake-данными нового пользователя по Pydantic-схеме
    response = public_users_client.create_user(payload=create_user_payload)  # ︎▶ Запрос на создание пользователя через метод. Передаем сгенерированные в Pydantic-схеме fake-данные нового пользователя
    return UserFullSchema(request=create_user_payload, response=response)    # Возвращает Pydantic-model ✨с объединенными данные о пользователе (Request + Response)

# API
@pytest.fixture
def create_user_api(public_users_client: PublicUsersClient) -> Response:
    """
    API фикстура СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ (Create User)

    :param public_users_client: Вложенная фикстура Public Users Client
    :return: httpx.Response
    """
    create_user_payload = CreateUserRequestSchema()                              # Инициализация модели с fake-данными нового пользователя по Pydantic-схеме
    response = public_users_client.create_user_api(payload=create_user_payload)  # ︎▶ Запрос на создание пользователя через метод. Передаем сгенерированные в Pydantic-схеме fake-данные нового пользователя
    return response                                                              # Возвращает httpx.Response
                                                                                 # ❗️Если нужно добраться до Request c 'password' - через JSON —> {dict} (парсинг):
                                                                                                                       # request_body = json.loads(response.request.content)
                                                                                                                       # print(request_body["password"])


#------------------------------------------------ Auth (Authentication) ------------------------------------------------
@pytest.fixture
def auth(create_user: UserFullSchema, auth_client: AuthClient) -> LoginResponseSchema:
    """
    Фикстура АВТОРИЗАЦИИ (Log in) созданного пользователя

    :param create_user: Вложенная фикстура СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ (Create User)
    :param auth_client: Вложенная фикстура АВТОРИЗАЦИИ пользователя (Log in)
    :return: Response (Pydantic-model)
    """
    login_payload = LoginRequestSchema(     # Инициализация модели с fake-данными нового пользователя по Pydantic-схеме
        email=create_user.email,            # Email из модели UserFullSchema
        password=create_user.password       # Password из модели UserFullSchema
    )
    response = auth_client.login(login_payload)  # ▶ Запрос на Authentication (Log in) через метод. Передаем payload c Email и Password и сохраняем ответ в переменную
    return response                              # Возвращает Response в формате Pydantic-model



# API
@pytest.fixture
def auth_api(create_user: UserFullSchema, auth_client: AuthClient) -> Response:
    """
    API-фикстура АВТОРИЗАЦИИ (Log in) созданного пользователя

    :param create_user: Вложенная фикстура СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ (Create User)
    :param auth_client: Вложенная фикстура АВТОРИЗАЦИИ пользователя (Log in)
    :return: httpx.Response
    """
    login_payload = LoginRequestSchema(     # Инициализация модели с fake-данными нового пользователя по Pydantic-схеме
        email=create_user.email,            # Email из модели UserFullSchema
        password=create_user.password       # Password из модели UserFullSchema
    )
    response = auth_client.login_api(login_payload)  # ▶ Запрос на Login (Authentication) через API-метод. Передаем payload c Email и Password и сохраняем ответ в переменную
    return response                                  # Возвращает httpx.Response
#-----------------------------------------------------------------------------------------------------------------------
