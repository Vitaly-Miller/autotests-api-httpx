"""
Base assertions
"""
import allure
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
@allure.step('Check that Status Code is {expected}')
def assert_status_code(actual: int, expected: int):
    """
    Check Status Code

    :param actual: Actual Response Status Code
    :param expected: Expected Response Status Code
    :raise AssertionError
    """
    assert actual == expected, f"""{error_title}
⚠️ Status code is incorrect!
{exp} {expected}
{act} {actual}
"""


# Request Method
@allure.step('Check that Request Method is {expected}')
def assert_request_method(actual: str, expected: str):
    """
    Check API Request Method

    :param actual: Actual API Request Method
    :param expected: Expected API Request Method
    :raise AssertionError
    """
    assert actual == expected, f"""{error_title}
⚠️ Request Method is incorrect!
{exp} {expected}
{act} {actual}
"""


#-------------------------------------------------------- Equal --------------------------------------------------------
# Object_1 = Object_2
@allure.step('Check value of <{name}>')
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
@allure.step('Check values of <{obj_1_name}> ≠ <{obj_2_name}>')
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
{exp} <{obj_1_name}> value ≠ <{obj_2_name}> value
{act} <{obj_1_name}> value = <{obj_2_name}> value
"""


#-------------------------------------------------------- Empty --------------------------------------------------------
# NON-empty values
@allure.step('Check <{name}> value is NON-empty')
def assert_is_value(actual_obj: Any, name: str):
    """
    Проверяет, что значение не пустое

    :param actual_obj: Actual object (ex.: response_model.user.id)
    :param name: Object name (for Assertion Error output)
    :raises AssertionError
    """
    assert actual_obj, f"""{error_title}
⚠️ "{name}" value is empty!
{exp} "{name}": "...some value..."
{act} "{name}": "" <— Empty/None
"""

#------------------------------------------------------- Length --------------------------------------------------------
# Length = ...
@allure.step('Check <{name}> length = {expected_length}')
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
@allure.step('Check that lengths of <Request-{name}> = <Response-{name}>')
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
