"""
Test Create User
(Фикстура create_user_api)

"""
import pytest
from httpx import Response
from clients.users.users_schema import CreateUserResponseSchema
from http import HTTPStatus, HTTPMethod
from tools.assertions.base_assert import assert_status_code, assert_method
from tools.assertions.schema_assert import validation_json_schema
from tools.assertions.users_assert import assert_user_data_fields

#=======================================================================================================================
@pytest.mark.smoke
@pytest.mark.users
def test_create_user(create_user_api: Response):         # Передаем фикстуру создания пользователя

    response = create_user_api                           # Сохраняем ответ в переменную
                                                         # Но не обязательно.
                                                         # Исполняемую фикстуру можно сразу передавать в Assertions в качестве параметра response=create_user_api)

    #---------------------------------------------------- Assertions ---------------------------------------------------
    # Base API assertions
    assert_status_code(response, HTTPStatus.OK)
    assert_method(response, HTTPMethod.POST)

    # Value equal
    assert_user_data_fields(response=response)  # Проверка совпадения полей Запроса и Ответа

    # Validation JSON Schema
    validation_json_schema(response, CreateUserResponseSchema)

#=======================================================================================================================
