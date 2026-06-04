"""
Base assertions
"""
import httpx
from typing import Any, Sized             # Sized - объект, у которого есть длина (len)

#=======================================================================================================================
# Text Constants
error_title = """
╭──────────────────╮
│ Assertion ERROR! │
╰──────────────────╯"""
exp = '✅ Expected:'
act = '❌ Actual:  '


#----------------------------------------------------- Base API --------------------------------------------------------
# Status Code
def assert_status_code(response: httpx.Response, expected_code: int):
    """
    Проверка Status Code

    :param response: Response
    :param expected_code: Expected Status Code
    :raise AssertionError - если значения не совпадают
    """
    assert response.status_code == expected_code, f"""{error_title}
⚠️ Status code is incorrect!
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
    assert response.request.method == expected_method, f"""{error_title}
⚠️ Request Method is incorrect!
{exp} {expected_method}
{act} {response.request.method}
"""


#-------------------------------------------------------- Equal --------------------------------------------------------
# Object_1 = Object_2
def assert_equal(actual: Any, expected: Any | str, name: str):
    """
    Проверяет совпадение values двух объектов (actual_obj = expected_obj)

    Example:
    response_model.user.email == create_user_data.email
                             или
    response_model.user.email == 'john_connor@email.com'

    :param actual:   Actual object
    :param expected: Expected object / 'string'
    :param name:     Object Name (для вывода в ошибке)
    :raise AssertionError
    """
    assert actual == expected, f"""{error_title}
⚠️ Values are NOT equal in "{name}"
{exp} "{name}": {expected}
{act} "{name}": {actual}
"""

# Object_1 ≠ Object_2
def assert_not_equal(obj_1: Any, obj_1_name: str, obj_2: Any, obj_2_name: str):
    """
    Проверяет НЕсовпадение двух объектов (obj_1 ≠ obj_2)

    Example:
    response_model.token.access_token != response_model.token.refresh_token

    :param obj_1: Object_1
    :param obj_1_name: Имя Object_1 (для вывода при ошибке)
    :param obj_2: Object_2
    :param obj_2_name: Имя Object_2 (для вывода при ошибке)
    :raise AssertionError
    """
    assert obj_1 != obj_2, f"""{error_title}
⚠️ Values are equal! 
"{obj_1_name}": "{obj_1}"
"{obj_2_name}": "{obj_2}"
{exp} "{obj_1_name}" value ≠ "{obj_2_name}" value
{act} "{obj_1_name}" value = "{obj_2_name}" value
"""


#-------------------------------------------------------- Empty --------------------------------------------------------
# NON-empty values
def assert_is_value(obj: Any, name: str):
    """
    Проверяет, что значение не пустое

    :param obj:  Object       (например: response_model.user.id)
    :param name: Object name  (для вывода в ошибке)
    :raises AssertionError
    """
    assert obj, f"""{error_title}
⚠️ "{name}" value is empty!
{exp} "{name}": "...some value..."
{act} "{name}": "" <— Empty/None
"""


#------------------------------------------------------- Length --------------------------------------------------------
# Length = ...
def assert_length(obj: Sized, expected_length: int, name: str):
    """
    Проверяет длину объекта (Manual length)

    :param obj: Object (например: response_model.user.id)
    :param expected_length: Ожидаемая длина (manual)
    :param name: Object name (для вывода в ошибке)
    :raise AssertionError
    """
    assert len(obj) == expected_length, f"""{error_title}
⚠️ Incorrect "{name}" value length!
{exp} {expected_length}
{act} {len(obj)}
"""

# Length_1 = Length_2
def assert_length_equal(obj_1: Sized, obj_2: Sized, name: str):
    """
    Сравнивает равенства длин двух объектов

    :param obj_1: Object_1  (actual_obj.field)
    :param obj_2: Object_2  (expected_obj.field)
    :param name: Название объекта/поля (для вывода в ошибке)

    :raise AssertionError
    """
    assert len(obj_1) == len(obj_2), f"""{error_title}
⚠️ Values "{name}" have different lengths!
{exp} {len(obj_2)}
{act} {len(obj_1)}
"""


#-----------------------------------------------------------------------------------------------------------------------
