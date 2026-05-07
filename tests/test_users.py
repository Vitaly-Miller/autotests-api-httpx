"""
Test Create User
"""
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from http import HTTPStatus, HTTPMethod
from tools.assertions.base import assert_status_code, assert_method
from tools.assertions.schema import validation_json_schema
from tools.assertions.users import assert_create_user_response

#=======================================================================================================================
def test_create_user():
    """
    Тест создания нового пользователя
    """
    # Инициализация клиента (public)
    public_users_client = get_public_users_client()

    # Инициализация модели с fake данными нового пользователя по Pydantic-схеме
    create_user_payload = CreateUserRequestSchema()

    # ▷ Запрос на создание пользователя через API-метод
    response = public_users_client.create_user_api(payload=create_user_payload)

    # JSON-ответ —> Pydantic модель (десериализация)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)


    #-------------------------------------------- Assertions (классический) --------------------------------------------
    assert response.status_code == 200           # проверка статус-кода    (⚠️Hard coding не рекомендуется)
    assert response.request.method == 'POST'     # проверка метода запроса (⚠️Hard coding не рекомендуется)

    assert response.status_code == HTTPStatus.OK, '❌Incorrect status code!'             # проверка статус-кода (через HTTPStatus)
    assert response.request.method == HTTPMethod.POST, '❌Incorrect Request Method!'     # проверка метода запроса (через HTTPMethod)

    assert response_data.user.email == create_user_payload.email, '❌Разные Email!'                    # проверка отправленного и полученного email
    assert response_data.user.last_name == create_user_payload.last_name, '❌Разные Last Name!'        # проверка отправленного и полученного Last Name
    assert response_data.user.first_name == create_user_payload.first_name, '❌Разные First Name!'     # проверка отправленного и полученного First Name
    assert response_data.user.middle_name == create_user_payload.middle_name, '❌Разные Middle Name!'  # проверка отправленного и полученного Middle Name


    #------------------------------------ Assertions (✅через СВОИ assertion-функции) ----------------------------------
    # Base
    assert_status_code(response, HTTPStatus.OK)                                    # проверка статус-кода
    assert_method(response, HTTPMethod.POST)                                       # проверка метода запроса
    assert_create_user_response(response_data, create_user_payload)    # Проверка совпадения полей запроса и ответа (4 in 1)

    # Validation JSON Schema (✅через СВОЮ функию)
    validation_json_schema(response, CreateUserResponseSchema)

#=======================================================================================================================
