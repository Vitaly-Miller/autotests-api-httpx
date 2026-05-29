"""
Base assertions
"""
import httpx
from typing import Any

#=======================================================================================================================
# Text Constants
error_title = """
╭──────────────────╮
│ Assertion ERROR! │
╰──────────────────╯"""
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
    Проверяет API Request Method

    :param response: Response
    :param expected_method: Expected API Request Method
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
def assert_value_equal(actual_obj: Any, obj_name: str, expected_obj: Any | str):
    """
    Проверяет совпадение values двух объектов (actual_obj = expected_obj)

    Example:
    response_model.user.email == create_user_data.email
                             или
    response_model.user.email == 'john_connor@email.com'

    :param actual_obj:      Actual Object
    :param expected_obj:    Expected Object / 'string'
    :param obj_name: Object Name (для вывода в ошибке)
    :raise AssertionError
    """
    assert actual_obj == expected_obj, f"""
{error_title}
⚠️Values are NOT equal in "{obj_name}"
{exp} "{obj_name}": {expected_obj}
{act} "{obj_name}": {actual_obj}
"""


# "value" ≠ "value"
def assert_value_not_equal(obj_1: Any, obj_1_name: str, obj_2: Any, obj_2_name: str):
    """
    Проверяет НЕсовпадение values двух объектов (obj_1 ≠ obj_2)

    Example:
    response_model.token.access_token != response_model.token.refresh_token

    :param obj_1: Значение Object_1
    :param obj_1_name: Имя Object_1 (для вывода при ошибке)
    :param obj_2: Значение Object_2
    :param obj_2_name: Имя Object_2 (для вывода при ошибке)
    :raise AssertionError
    """
    assert obj_1 != obj_2, f"""
{error_title}
⚠️Values are equal! 
{obj_1_name}: {obj_1}
{obj_2_name}: {obj_2}
{exp} {obj_1_name} value ≠ {obj_2_name} value
{act} {obj_1_name} value = {obj_2_name} value
"""


# Value is NOT EMPTY
def assert_is_value(actual_obj: Any, obj_name: str):
    """
    Проверяет, что значение не пустое

    :param actual_obj: Проверяемый ключ/поле (например: response_model.user.id)
    :param obj_name: Object name  (для вывода в ошибке)
    :raises AssertionError
    """
    assert actual_obj, f"""
{error_title}
⚠️"{obj_name}" value is empty!
{exp} "{obj_name}": "...some value..."
{act} "{obj_name}": "" <— Empty/None
"""


# Value length
def assert_value_len(actual_obj: Any, obj_name: str, expected_length: int):
    """
    Проверяет длину value

    :param actual_obj: Объект проверки
    :param obj_name: Название объекта проверки (для вывода в ошибке)
    :param expected_length: Ожидаемая длина
    :raise AssertionError
    """
    assert len(actual_obj) == expected_length, f"""
{error_title}
⚠️Incorrect "{obj_name}" value length!
{exp} {expected_length}
{act} {len(actual_obj)}
"""

#=======================================================================================================================
