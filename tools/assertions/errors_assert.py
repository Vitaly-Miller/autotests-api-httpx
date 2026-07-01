"""
Errors assertions
"""
import allure
from schemas.errors_schema import ErrorSchema, ErrorResponseSchema, NotFoundErrorResponseSchema
from tools.assertions.base_assert import assert_equal, assert_length_equal

#=======================================================================================================================
# Error
@allure.step('Validation Error')
def assert_validate_error(actual: ErrorSchema, expected: ErrorSchema):
    """
    Validation Error

    :param actual: Pydantic-model (ErrorSchema)
    :param expected: Pydantic-model (ErrorSchema)
    :return: ValidationError
    """
    assert_equal(actual.type, expected.type, 'type')
    assert_equal(actual.loc, expected.loc, 'loc')
    assert_equal(actual.msg, expected.msg, 'msg')
    assert_equal(actual.input, expected.input, 'input')
    assert_equal(actual.ctx, expected.ctx, 'ctx')


# Error Response
@allure.step('Validation Response Error')
def assert_error_response(actual: ErrorResponseSchema, expected: ErrorResponseSchema):
    """
    Validation Error Response

    - Сравнивает длину (количество полей) в объекте "detail"
    - Сравнивает values (значения полей) в объекте "detail"

    :param actual: Pydantic-model (ErrorResponseSchema)
    :param expected: Pydantic-model (ErrorResponseSchema)
    :return: ValidationError
    """
    assert_length_equal(actual.detail, expected.detail, 'detail') # Сравниваем количество элементов в объекте "detail"
    assert_equal(actual.detail, expected.detail, 'detail')    # Сравниваем значения элементов в объекте "detail"


# Not Found Error Response
@allure.step('Validation Not Found Response Error')
def assert_not_found_error_response(actual: NotFoundErrorResponseSchema, expected: NotFoundErrorResponseSchema):
    """
    Validation Not Found Error Response (при попытке получить несуществующую сущность)

    :param actual: Pydantic-model (NotFoundErrorResponseSchema)
    :param expected: Pydantic-model (NotFoundErrorResponseSchema)
    :return: ValidationError
    """
    assert_equal(actual.detail, expected.detail, 'detail')  # Сравниваем значения элементов в объектах "detail"

#-----------------------------------------------------------------------------------------------------------------------
