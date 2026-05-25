"""
Test Get User Me 2
"""
"""
- Фикстура get_user_me (полный цикл: Create User + Get User Me)
"""
import http
import httpx
import pytest
from schemas.users import GetUserMeResponseSchema
from tools.assertions.base_assert import assert_status_code, assert_method
from tools.assertions.get_user_me_assert import assert_get_user_me_response_fields
from tools.assertions.schema_assert import validation_json_schema

#=======================================================================================================================
@pytest.mark.smoke
@pytest.mark.users
def test_get_user_me(get_user_me_api: httpx.Response):   # Передача фикстуры get_user_me

    response = get_user_me_api                           # Сохраняем ответ в переменную

    #---------------------------------------------------- Assertions ---------------------------------------------------
    # Base API assertions
    assert_status_code(response, http.HTTPStatus.OK)
    assert_method(response, http.HTTPMethod.GET)

    # Fields assertions
    # Нет доступа к Request внутренней фикстуры Create User

    # User ID присвоен
    assert_get_user_me_response_fields(response)

    # Validation JSON Schema
    validation_json_schema(response, GetUserMeResponseSchema)
#=======================================================================================================================
