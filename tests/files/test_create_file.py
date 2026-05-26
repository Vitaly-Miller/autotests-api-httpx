"""
Create File (⚠️ДОДЕЛАТЬ)
"""
import http
import httpx
import pytest
from tools.assertions.base_assert import assert_status_code, assert_method
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.smoke
@pytest.mark.files
class TestFiles:
    #===================================== Фикстура полного цикла create_file_api ======================================
    def test_create_file(self, create_file_api: httpx.Response):
        response = create_file_api   # Сохраняем ответ в переменную

        #------------------------------------------------ Assertions ---------------------------------------------------
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
    #===================================================================================================================
        Tool.api_report(response)
