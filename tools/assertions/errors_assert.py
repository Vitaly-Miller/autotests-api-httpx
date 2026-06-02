"""
Errors assertions
"""
import httpx
from schemas.errors_schema import ErrorSchema, ResponseErrorSchema, NotFoundErrorSchema
from tools.assertions.base_assert import assert_equal, assert_length_equal

#=======================================================================================================================
def assert_validate_error(actual: httpx.Response, expected: httpx.Response):
    """
    5-in-1 | Check API-Response Validation fields errors

    :param actual: Response (for deserialize —> Pydantic-model)
    :param expected: Response (for deserialize —> Pydantic-model)
    :return: ValidationError
    """
    actual_model = ErrorSchema.model_validate_json(actual.text)       # actual_Response  —> Pydantic-model (Deserialize for Assertions)
    expected_model = ErrorSchema.model_validate_json(expected.text)   # expected_Response —> Pydantic-model (Deserialize for Assertions)

    assert_equal(actual_model.type, expected_model.type, 'type')
    assert_equal(actual_model.loc, expected_model.loc, 'loc')
    assert_equal(actual_model.msg, expected_model.msg, 'msg')
    assert_equal(actual_model.input, expected_model.input, 'input')
    assert_equal(actual_model.ctx, expected_model.ctx, 'ctx')



def assert_validate_error_response(actual: httpx.Response, expected_model: ResponseErrorSchema):
    """
    2-in-1 | Проверка Error Response (длина, значения)

    - Сравнивает количество элементов в объекте "detail"
    - Сравнивает значения элементов в объекте "detail"

    :param actual: Response (for deserialize —> Pydantic-model)
    :param expected_model: Pydantic-model (ResponseErrorSchema)
    :return: ValidationError
    """
    actual_model = ResponseErrorSchema.model_validate_json(actual.text)   # Response  —> Pydantic-model (Deserialize for Assertions)

    assert_length_equal(actual_model.detail, expected_model.detail, 'detail') # Сравниваем количество элементов в объекте "detail"
    assert_equal(actual_model.detail, expected_model.detail, 'detail')    # Сравниваем значения элементов в объекте "detail"



def assert_not_found_response(actual: httpx.Response, expected_model: NotFoundErrorSchema):
    """
    Сравнивает Error Response с Pydantic-model (NotFoundErrorSchema) при попытке получить несуществующую сущность

    :param actual: Response (for deserialize —> Pydantic-model)
    :param expected_model: Pydantic-model (NotFoundErrorSchema)
    :return:
    """
    actual_model = NotFoundErrorSchema.model_validate_json(actual.text)    # actual_Response  —> Pydantic-model (Deserialize for Assertions)

    assert_equal(actual_model.detail, expected_model.detail, 'detail')

#-----------------------------------------------------------------------------------------------------------------------
