"""
Base assertions
"""

from typing import Any
from httpx import Response

#=======================================================================================================================
#--------------------------------------------------------- API ---------------------------------------------------------
# Status Code
def assert_status_code(response: Response, expected: int):
    """
    Проверка Status Code

    :param response: Response
    :param expected: Expected Status Code
    :raise AssertionError - если значения не совпадают
    """
    assert response.status_code == expected, f"""
❌Status code is incorrect!
🔸Expected code: {expected}
🔹Actual code:   {response.status_code}
"""

# Method
def assert_method(response: Response, expected: str):
    """
    Проверяет Request Method.

    :param response: Response
    :param expected: Expected Request Method
    :raise AssertionError - если значения не совпадают
    """
    assert response.request.method == expected, f"""
❌Request Method is incorrect!
🔸Expected method: {expected}
🔹Actual method:   {response.request.method}
"""

#-------------------------------------------------------- Value --------------------------------------------------------
# {"key": "value"} = {"key": "value"}
def assert_equal(actual: Any, expected: Any, field_name: str):
    """
    Проверяет совпадение значений в поле двух объектов.

    (exemple: response_data.user.email == create_user_payload.email)
    :param actual: Actual value
    :param expected: Expected value
    :param field_name: Field name ("key")
    :raise AssertionError - если значения не совпадают
    """
    assert actual == expected, f"""
❌Values are not equal in field (key) —> "{field_name}"
🔸Expected value: {expected}
🔹Actual value:   {actual}
"""

# Value is NOT EMPTY
def assert_is_true(actual: Any, field_name: str):
    """
    Проверяет, что значение не пустое

    :param actual: Фактическое значение
    :param field_name: Название проверяемого объекта
    :raises AssertionError - Если фактическое значение ложно
    """
    assert actual, f"""
❌"{field_name}" value is empty!
🔸Expected value: NOT empty
🔹Actual value:   Empty (None)
"""

# Value length
def assert_value_len(actual: Any, expected_len: int, field_name: str):
    """
    Проверяет длину значения

    :param actual: Объект измерения
    :param expected_len: Ожидаемая длина
    :param field_name: Название проверяемого объекта
    :raise AssertionError - Если значения разные
    """
    assert len(actual) == expected_len, f"""
❌Incorrect "{field_name}" value length!
🔸Expected length: {expected_len}
🔹Actual length:   {len(actual)}
"""

#=======================================================================================================================
