"""
Errors assertions
"""
import allure
from tools.logger import get_logger
from schemas.errors_schema import ErrorSchema, ErrorResponseSchema, NotFoundErrorResponseSchema
from tools.assertions.base_assert import assert_equal, assert_length_equal

#------------- Logger ------------
logger = get_logger('ERRORS-ASSERT')

#=======================================================================================================================
# Validation Error
@allure.step('Validation Error')                                                # Allure step title
def assert_validate_error(actual: ErrorSchema, expected: ErrorSchema):
    """
    Validation Error

    :param actual: Pydantic-model (ErrorSchema)
    :param expected: Pydantic-model (ErrorSchema)
    :return: ValidationError
    """
    logger.info('Validation Error')                                             # Logger
    assert_equal(actual.type, expected.type, 'type')
    assert_equal(actual.loc, expected.loc, 'loc')
    assert_equal(actual.msg, expected.msg, 'msg')
    assert_equal(actual.input, expected.input, 'input')
    assert_equal(actual.ctx, expected.ctx, 'ctx')


# Validation Error Response
@allure.step('Validation Error Response')                                              # Allure step title
def assert_error_response(actual: ErrorResponseSchema, expected: ErrorResponseSchema):
    """
    Validation Error Response

    - Сравнивает длину (количество полей) ключа "detail:"
    - Сравнивает values (значения) ключа "detail:"

    :param actual: Pydantic-model (ErrorResponseSchema)
    :param expected: Pydantic-model (ErrorResponseSchema)
    :return: ValidationError
    """
    logger.info('Validation Error Response')                                           # Logger
    assert_length_equal(actual.detail, expected.detail, 'detail') # Сравнивает длины ключа "detail:"
    assert_equal(actual.detail, expected.detail, 'detail')        # Сравнивает значения ключа "detail:"



# Validation Not Found Error Response
@allure.step('Validation Not Found Error Response')                             # Allure step title
def assert_not_found_error_response(actual: NotFoundErrorResponseSchema, expected: NotFoundErrorResponseSchema):
    """
    Validation Not Found Error Response (при попытке получить несуществующую сущность)

    Сравнивает values (значения) ключа "detail:"

    :param actual: Pydantic-model (NotFoundErrorResponseSchema)
    :param expected: Pydantic-model (NotFoundErrorResponseSchema)
    :return: ValidationError
    """
    logger.info('Validation Not Found Error Response')                           # Logger
    assert_equal(actual.detail, expected.detail, 'detail')  # Сравнивает значения ключа "detail:"

#-----------------------------------------------------------------------------------------------------------------------
