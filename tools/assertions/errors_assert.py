"""
Errors assertions
"""
import httpx
from schemas.error import ErrorSchema, ResponseErrorSchema
from tools.assertions.base_assert import assert_equal, assert_length_equal

#=======================================================================================================================
def assert_validate_error(actual: httpx.Response, expected: httpx.Response):
    """
    Check API-Response Validation fields errors

    Actions:

    - Response —> Pydantic-model (Deserialize for Assertions)

    :param actual: Actual response
    :param expected: Expected response
    :return:
    """
    actual_model = ErrorSchema.model_validate_json(actual.text)       # actual_Response  —> Pydantic-model (Deserialize for Assertions)
    expected_model = ErrorSchema.model_validate_json(expected.text)   # expecte_Response —> Pydantic-model (Deserialize for Assertions)

    assert_equal(actual_model.type, expected_model.type, 'type')
    assert_equal(actual_model.loc, expected_model.loc, 'loc')
    assert_equal(actual_model.msg, expected_model.msg, 'msg')
    assert_equal(actual_model.input, expected_model.input, 'input')
    assert_equal(actual_model.ctx, expected_model.ctx, 'ctx')



def assert_validate_error_response(actual: httpx.Response, expected: httpx.Response | ResponseErrorSchema):
    """
    Проверка длин ключа "detail" from Response and Request

    :param actual:
    :param expected:
    :return:
    """
    actual_model = ResponseErrorSchema.model_validate_json(actual.text)       # actual_Response  —> Pydantic-model (Deserialize for Assertions)

    # Если expected — Pydantic-model (ResponseErrorSchema), то ...
    if isinstance(expected, ResponseErrorSchema):
        expected_model = expected
    else:
        expected_model = ResponseErrorSchema.model_validate_json(expected.text)   # expecte_Response —> Pydantic-model (Deserialize for Assertions)


    assert_length_equal(actual_model.detail, expected_model.detail, 'detail')
    #assert_equal(actual_model.detail, expected_model.detail, 'detail')       # <— выводит большой tracelog при падении
    #      ⬇︎
    # Альтернатива assert_equal, для меньшего tracelog при падении (удобнее для allure-отчетов):
    for index, detail in enumerate(expected_model.detail):
        assert actual_model.detail[index] == detail
#-----------------------------------------------------------------------------------------------------------------------
