"""
Base assertions
"""
import httpx
from typing import Any

#=======================================================================================================================
# Text Constants
error_title = """
╭────────╮
│ ERROR! │
╰────────╯"""
exp = '✅Expected:'
act = '❌Actual:  '


#------------------------------------------------------ Base API -------------------------------------------------------
# Status Code
def assert_status_code(response: httpx.Response, expected_code: int):
    """
    Проверка Status Code

    :param response: httpx.Response
    :param expected_code: Expected Status Code
    :raise AssertionError - если значения не совпадают
    """
    assert response.status_code == expected_code, f"""
{error_title}
⚠️Status code is incorrect!
{exp} {expected_code}
{act} {response.status_code}
"""


# Method
def assert_method(response: httpx.Response, expected_method: str):
    """
    Проверяет Request Method

    :param response: Response
    :param expected_method: Expected Request Method
    :raise AssertionError - если значения не совпадают
    """
    assert response.request.method == expected_method, f"""
{error_title}
⚠️Request Method is incorrect!
{exp} {expected_method}
{act} {response.request.method}
"""

#-------------------------------------------------------- Value --------------------------------------------------------
# "value" = "value"
def assert_value_equal(actual_obj: Any, field_name: str, expected_obj: Any):
    """
    Проверяет совпадение значений (value) двух объектов.

    Example:
    response_data.user.email == create_user_data.email  (actual_obj = expected_obj)
                                  или
    response_data.user.email == 'john_connor@email.com' (actual_obj = 'string')

    :param actual_obj: Actual поле/ключ
    :param expected_obj: Expected поле/ключ или 'string'
    :param field_name: Field/Key (для вывода в ошибке)
    :raise AssertionError
    """
    assert actual_obj == expected_obj, f"""
{error_title}
⚠️Values are not equal in field (key) —> "{field_name}"
{exp} "{field_name}": {expected_obj}
{act} "{field_name}": {actual_obj}
"""


# Value is NOT EMPTY
def assert_is_value(actual_obj: Any, field_name: str):
    """
    Проверяет, что значение не пустое

    :param actual_obj: Проверяемый ключ/поле (например: response_model.user.id)
    :param field_name: Название ключа/поля   (для вывода в ошибке)
    :raises AssertionError
    """
    assert actual_obj, f"""
{error_title}
⚠️"{field_name}" value is empty!
{exp} "..some value.."
{act} Empty/None
"""


# Value length
def assert_value_len(actual_obj: Any, field_name: str, expected_length: int):
    """
    Проверяет длину значения поля/ключа (key value)

    :param actual_obj: Объект проверки
    :param field_name: Название объекта проверки (для вывода в ошибке)
    :param expected_length: Ожидаемая длина
    :raise AssertionError
    """
    assert len(actual_obj) == expected_length, f"""
{error_title}
⚠️Incorrect "{field_name}" value length!
{exp} {expected_length}
{act} {len(actual_obj)}
"""

#=======================================================================================================================
