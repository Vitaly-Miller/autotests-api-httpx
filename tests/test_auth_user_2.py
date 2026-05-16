"""
Test Log in (Authentication) 2
(Фикстура auth_user)
"""
import pytest
from httpx import Response
from clients.auth.auth_schema import AuthUserResponseSchema
from http import HTTPStatus, HTTPMethod
from tools.assertions.auth_assert import assert_login_response_fields
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
def test_login(auth_user_api: Response):          # Передача фикстуры 2-in-1 (СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ c ✨АВТОРИЗАЦИЕЙ)
    response = auth_user_api                      # Сохраняем ответ в переменную...
                                                  # ...✨НО можно фикстуру сразу загонять в ассерты.

    #---------------------------------------------------- Assertions ---------------------------------------------------
    # Base assertions
    assert_status_code(response, HTTPStatus.OK)   # проверка статус-кода
    assert_method(response, HTTPMethod.POST)      # проверка метода запроса
    # Authentication assertions
    assert_login_response_fields(response=response)                 # Проверка на НЕпустоту полей (6-in-1)
    # Validation JSON Schema
    validation_json_schema(response, AuthUserResponseSchema)


#=======================================================================================================================
    Tool.api_report(response)
