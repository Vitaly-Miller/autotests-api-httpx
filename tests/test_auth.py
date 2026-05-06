"""
Test login user (auth)
"""
from clients.auth.auth_client import get_auth_client
from clients.auth.auth_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from http import HTTPStatus, HTTPMethod
from tools.assertions.auth import assert_login_response
from tools.assertions.base import assert_status_code, assert_method
from tools.assertions.schema import validation_json_schema


#=======================================================================================================================
def test_login():
    """
    Тест на авторизацию (Log in) зарегистрированного пользователя
    """
    #------------------------------------------- Precondition (Create User) --------------------------------------------
    # Инициализация клиента (public)
    public_users_client = get_public_users_client()

    # Инициализация модели с fake данными нового пользователя по Pydantic-схеме
    create_user_model = CreateUserRequestSchema()

    # Запрос на создание пользователя через API-метод
    create_user_response = public_users_client.create_user_api(payload=create_user_model)

    #--------------------------------------------- Authentication (Log in)  --------------------------------------------
    # Инициализация клиента (public)
    auth_client = get_auth_client()

    # Инициализация модели с fake данными нового пользователя по Pydantic-схеме
    login_payload = LoginRequestSchema(
        email=create_user_model.email,                   # Email из payload на создание пользователя
        password=create_user_model.password              # Password из payload на создание пользователя
    )

    # Запрос на Authentication (Log in) через API-метод
    auth_response = auth_client.login_api(login_payload)  # Передаем Email и Password

    # JSON-ответ -> Pydantic-модель (десериализация)
    auth_response_data = LoginResponseSchema.model_validate_json(auth_response.text)


    #--------------------------------------------------- Assertions ----------------------------------------------------
    assert_status_code(auth_response.status_code, HTTPStatus.OK)        # проверка статус-кода
    assert_method(auth_response.request.method, HTTPMethod.POST)        # проверка метода запроса
    assert_login_response(auth_response_data)          # Проверка типа токена, длину access- и refresh-токенов (3 in 1)


    # Validation JSON Schema
    validation_json_schema(auth_response.json(), LoginResponseSchema)

#=======================================================================================================================
