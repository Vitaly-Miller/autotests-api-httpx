"""
Create File (ДОДЕЛАТЬ)
"""
from tools.tool import Tool

"""
- Фикстура 
"""
import http
import httpx
import pytest
from tools.assertions.base_assert import assert_status_code, assert_method

#=======================================================================================================================
@pytest.mark.smoke
@pytest.mark.files
def test_create_file(create_file_api: httpx.Response):   # Передача фикстуры create_file_api

    response = create_file_api                           # Сохраняем ответ в переменную

    #---------------------------------------------------- Assertions ---------------------------------------------------
    # Base API assertions
    assert_status_code(response, http.HTTPStatus.OK)
    assert_method(response, http.HTTPMethod.POST)
    #
    # # Fields assertions
    # # Нет доступа к Request внутренней фикстуры Create User
    #
    # # User ID присвоен
    # assert_get_user_me_response_fields(response)
    #
    # # Validation JSON Schema
    # validation_json_schema(response, GetUserMeResponseSchema)
#=======================================================================================================================
    Tool.api_report(response)
