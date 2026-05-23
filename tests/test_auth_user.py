"""
Test User Authentication (Log in)
"""
"""
- Фикстура полного цикла: auth_user (Create User + Auth Client) 2-in-1
"""
import pytest
from httpx import Response
from clients.auth.auth_schema import AuthUserResponseSchema
from http import HTTPStatus, HTTPMethod
from tools.assertions.auth_assert import assert_auth_response_fields
from tools.assertions.base_assert import assert_status_code, assert_method
from tools.assertions.schema_assert import validation_json_schema
from tools.tool import Tool

#=======================================================================================================================
"""
---------------------------------------------------------- ⚠️-----------------------------------------------------------
Думаю, нет смысла в API-фикстурах для тестируемого функционала. 
Потому, что логика загоняется "под капот", а тест нужен ЖИВОЙ.
- А в живом тесте применять API-МЕТОДЫ для дальнейшей обработки Ассертами.
- Для PRE- POST-conditions применять Pydantic-фикстуры
...
✨НУ ЕСЛИ ПРИПРЕТ - можно и загнать всю базовую логику и в фикстуры для минимизации кода в тестах
------------------------------------------------------- ⬇⬇︎⬇︎⬇︎ --------------------------------------------------------
"""
@pytest.mark.smoke
@pytest.mark.users
def test_auth_user(auth_user_api: Response):          # Передача фикстуры 2-in-1 (Create User + Auth Client)
    response = auth_user_api                          # Сохраняем ответ работы фикстуры в переменную...
                                                      # ...✨НО можно фикстуру сразу загонять в ассерты. (если scope='function')

    #---------------------------------------------------- Assertions ---------------------------------------------------
    # Base API assertions
    assert_status_code(response, HTTPStatus.OK)
    assert_method(response, HTTPMethod.POST)

    # NON-Empty values
    assert_auth_response_fields(response=response)

    # Validation JSON Schema
    validation_json_schema(response, AuthUserResponseSchema)


#=======================================================================================================================
    Tool.api_report(response)
