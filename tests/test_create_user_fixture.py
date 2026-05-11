"""
Test Create User
Тест создания пользователя

"""
import pytest
from httpx import Response
from clients.users.users_schema import CreateUserResponseSchema
from http import HTTPStatus, HTTPMethod
from tools.assertions.base import assert_status_code, assert_method
from tools.assertions.schema import validation_json_schema
from tools.assertions.users import assert_create_user_fields

#=======================================================================================================================
@pytest.mark.smoke
@pytest.mark.users
def test_create_user(create_user_api: Response):         # Передаем фикстуру создания пользователя в тест

    response = create_user_api                           # Сохраняем ОТВЕТ в переменную
                                                         # Но не обязательно. Исполняемую фикстуру можно сразу передавать в Assertions в качестве параметра response=)

    #---------------------------------------------------- Assertions ---------------------------------------------------
    # Base assertions
    assert_status_code(response, HTTPStatus.OK)    # проверка статус-кода
    assert_method(response, HTTPMethod.POST)       # проверка метода запроса
    # # Create User assertions
    assert_create_user_fields(response=response)                     # Проверка совпадения полей Запроса и Ответа (4 in 1)
    # # Validation JSON Schema
    validation_json_schema(response, CreateUserResponseSchema)

#=======================================================================================================================
