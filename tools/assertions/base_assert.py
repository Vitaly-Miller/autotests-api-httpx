"""
Base assertions
"""
import http
import allure
from typing import Any, Sized             # Sized - объект, у которого есть длина (len)
from tools.logger import get_logger

#------------- Logger ------------
logger = get_logger('- BASE-ASSERT')

#=======================================================================================================================
# Text constants
exp = '✅ Expected:'
act = '❌ Actual:  '

#----------------------------------------------------- Base API --------------------------------------------------------
# Status Code
def assert_status_code(actual: int, expected: int):
    """
    Status Code

    :param actual: Actual Response Status Code
    :param expected: Expected Response Status Code
    :raise AssertionError
    """
    pretty_expected = expected
    if isinstance(expected, http.HTTPStatus):                        # <http.HTTPStatus.OK> —>
        pretty_expected = f'{expected.value}-{expected.phrase}'      # —> 200-OK
    with allure.step(f'Status code = {pretty_expected}'):            # Allure step title
        error_message = \
            (f'⚠️ Status code is incorrect!\n'                       # 
             f'{exp} {expected}\n'                                   # Формируем Error Message
             f'{act} {actual}\n')                                    #
        logger.info(f'Status code = "{pretty_expected}"')            # Logger
        assert actual == expected, error_message


# Request Method
def assert_request_method(actual: str, expected: str):
    """
    API Request Method

    :param actual: Actual API Request Method
    :param expected: Expected API Request Method
    :raise AssertionError
    """
    with allure.step(f'Request method = {expected}'):                # Allure step title
        error_message = \
            (f'⚠️ Request Method is incorrect!\n'                    #
             f'{exp} {expected}\n'                                   # Формируем Error Message
             f'{act} {actual}\n')                                    #
        logger.info(f'Request method = "{expected}"')                # Logger
        assert actual == expected, error_message


#-------------------------------------------------------- Equal --------------------------------------------------------
# Actual Object = Expected Object
@allure.step('Value of {name}')                                      # Allure step title
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
    error_message = \
        (f'⚠️ Values are NOT equal in "{name}"!\n'                   #
         f'{exp} "{name}": {expected}\n'                             # Формируем Error Message
         f'{act} "{name}": {actual}\n')                              #
    logger.info(f'Value of "{name}" = "{expected}"')                 # Logger
    assert actual == expected, error_message


# Object-1 ≠ Object-2
@allure.step('Value of {obj_1_name} ≠ value of {obj_2_name}')        # Allure step title
def assert_not_equal(obj_1: Any, obj_1_name: str, obj_2: Any, obj_2_name: str):
    """
    Проверяет НЕсовпадение значений двух объектов (Object-1 ≠ Object-2)

    Example:
    response_model.token.access_token != response_model.token.refresh_token

    :param obj_1: Object-1
    :param obj_1_name: Object-1 name
    :param obj_2: Expected object
    :param obj_2_name: Object-2 name
    :raise AssertionError
    """
    error_message = \
        (f'⚠️ Values are equal!\n'                                   # 
         f'"{obj_1_name}": "{obj_1}"\n'                              # 
         f'"{obj_2_name}": "{obj_2}"\n'                              # Формируем Error Message
         f'{exp} "{obj_1_name}" value ≠ "{obj_2_name}" value\n'      #
         f'{act} "{obj_1_name}" value = "{obj_2_name}" value\n')     #
    logger.info(f'Value of "{obj_1_name}" ≠ value of "{obj_2_name}"')# Logger
    assert obj_1 != obj_2, error_message

#-------------------------------------------------------- Empty --------------------------------------------------------
# Value is NON-empty
@allure.step('Value of {name} is non-empty')                         # Allure step title
def assert_is_value(actual: Any, name: str):
    """
    Проверяет, что значение не пустое

    :param actual: Actual object (ex.: response_model.user.id)
    :param name: Object name (for Assertion Error output)
    :raises AssertionError
    """
    error_message = \
        (f'⚠️ "{name}" value is empty!\n'                            #
         f'{exp} "{name}": "...some value..."\n'                     #  Формируем Error Message
         f'{act} "{name}": "" <— Empty/None\n')                      #
    logger.info(f'Value of "{name}" is non-empty')                   # Logger
    assert actual, error_message


#------------------------------------------------------- Length --------------------------------------------------------
# Length = ...
@allure.step('Length of {obj_name} = {expected_length}')             # Allure step title
def assert_length(obj: Sized, expected_length: int, obj_name: str):
    """
    Проверяет длину объекта (manual length)

    :param obj: Actual object (ex.: response_model.user.id)
    :param expected_length: Expected length (manual)
    :param obj_name: Object name
    :raise AssertionError
    """
    error_message = \
        (f'⚠️ Incorrect "{obj_name}" value length!\n'                #
         f'{exp} {expected_length}\n'                                # Формируем Error Message
         f'{act} {len(obj)}\n')                                      #
    logger.info(f'Length of "{obj_name}" = {expected_length}')       # Logger
    assert len(obj) == expected_length, error_message


# Actual Length = Expected Length
def assert_length_equal(actual: Sized, expected: Sized, name: str):
    """
    Сравнивает равенства длин двух объектов

    :param actual: Actual object (actual.field)
    :param expected: Expected object (expected.field)
    :param name: Название объекта/поля

    :raise AssertionError
    """
    with allure.step(f'Lengths of "actual.{name}" = "expected.{name}" = {len(expected)}'):  # Allure step title
        error_message = \
            (f'⚠️ Values "{name}" have different lengths!\n'         #
             f'{exp} {len(expected)}\n'                              # Формируем Error Message
             f'{act} {len(actual)}\n')                               #
        logger.info(f'Lengths of "actual.{name}" = "expected.{name}" = {len(expected)}')    # Logger
        assert len(actual) == len(expected), error_message

#=======================================================================================================================
