"""
Base assertions
"""
from typing import Any

#=======================================================================================================================
# Status Code
def assert_status_code(actual: int, expected: int):
    """
    Проверка Status Code

    :param actual: Actual Status Code
    :param expected: Expected Status Code
    :raise AssertionError - если значения не совпадают
    """
    assert actual == expected, f"""
❌Status code is incorrect!
🔸Expected code: {expected}
🔹Actual code:   {actual}
"""

# Method
def assert_method(actual: str, expected: str):
    """
    Проверяет Request Method.

    :param actual: Actual Request Method
    :param expected: Expected Request Method
    :raise AssertionError - если значения не совпадают
    """
    assert actual == expected, (f"""
❌Request Method is incorrect!
🔸Expected method: {expected}
🔹Actual method:   {actual}
""")

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
    Проверяет, что фактическое значение является истинным

    :param actual: Фактическое значение
    :param field_name: Название проверяемого значения
    :raises AssertionError: Если фактическое значение ложно
    """
    assert actual, f"""
❌"{field_name}" value is empty!
🔸Expected value: NOT empty
🔹Actual value:   Empty (None)
"""


# Value length
def assert_value_len(actual: Any, expected: int, field_name: str):
    assert len(actual) == expected, f"""
❌Incorrect "{field_name}" value length!
🔸Expected length: {expected}
🔹Actual length:   {len(actual)}
"""


#=======================================================================================================================
