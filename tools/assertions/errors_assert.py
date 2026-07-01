"""
Errors assertions
"""
import httpx
import allure
from schemas.errors_schema import ErrorSchema, ErrorResponseSchema, NotFoundErrorResponseSchema
from tools.assertions.base_assert import assert_equal, assert_length_equal

#=======================================================================================================================
# Error
def assert_validate_error(actual: httpx.Response, expected: httpx.Response):
    """
    Validation Error

    :param actual: Response (for deserialize —> Pydantic-model)
    :param expected: Response (for deserialize —> Pydantic-model)
    :return: ValidationError
    """
    actual_model = ErrorSchema.model_validate_json(actual.text)       # actual_Response  —> Pydantic-model
    expected_model = ErrorSchema.model_validate_json(expected.text)   # expected_Response —> Pydantic-model

    # Response data = Request data:
    assert_equal(actual_model.type, expected_model.type, 'type')
    assert_equal(actual_model.loc, expected_model.loc, 'loc')
    assert_equal(actual_model.msg, expected_model.msg, 'msg')
    assert_equal(actual_model.input, expected_model.input, 'input')
    assert_equal(actual_model.ctx, expected_model.ctx, 'ctx')


# Error Response
@allure.step('Validation Response Error')
def assert_error_response(actual_model: ErrorResponseSchema, expected_model: ErrorResponseSchema):
    """
    Validation Error Response

    - Сравнивает длину (количество полей) в объекте "detail"
    - Сравнивает values (значения полей) в объекте "detail"

    :param actual_model: Pydantic-model (ErrorResponseSchema)
    :param expected_model: Pydantic-model (ErrorResponseSchema)
    :return: ValidationError
    """
    assert_length_equal(actual_model.detail, expected_model.detail, 'detail') # Сравниваем количество элементов в объекте "detail"
    assert_equal(actual_model.detail, expected_model.detail, 'detail')    # Сравниваем значения элементов в объекте "detail"


# Not Found Error Response
@allure.step('Validation Not Found Response Error')
def assert_not_found_error_response(actual_model: NotFoundErrorResponseSchema, expected_model: NotFoundErrorResponseSchema):
    """
    Validation Not Found Error Response (при попытке получить несуществующую сущность)

    :param actual_model: Pydantic-model (NotFoundErrorResponseSchema)
    :param expected_model: Pydantic-model (NotFoundErrorResponseSchema)
    :return: ValidationError
    """
    assert_equal(actual_model.detail, expected_model.detail, 'detail')  # Сравниваем значения элементов в объектах "detail"

#-----------------------------------------------------------------------------------------------------------------------
