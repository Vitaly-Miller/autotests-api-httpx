"""
Files Assertions
"""
import httpx

from schemas.errors_schema import ResponseErrorSchema, ErrorSchema
from schemas.files_schema import CreateFileResponseSchema, CreateFileRequestSchema
from tools.assertions.base_assert import assert_length_is, assert_is_value, assert_equal
from tools.assertions.errors_assert import assert_validate_error_response

#=======================================================================================================================
def assert_create_file_values_non_empty(response: httpx.Response):
    """
    4-in-1 | NON-empty response values

    Actions:

    - Response —> Pydantic-model (Deserialize for Assertions)

    :param response: httpx.Response
    :raise AssertionError
    """
    response_model = CreateFileResponseSchema.model_validate_json(response.text)   # Response —> Pydantic-model (Deserialize for Assertions)

    assert_is_value(response_model.file.id, 'id')                # Поле не пустое
    assert_is_value(response_model.file.filename, 'filename')    # Поле не пустое
    assert_is_value(response_model.file.directory, 'directory')  # Поле не пустое
    assert_is_value(response_model.file.url, 'url')              # Поле не пустое


def assert_create_file_data_equal(response: httpx.Response, request_model: CreateFileRequestSchema):
    """
    3-in-1 | Request Data = Response Data

    - filename
    - directory
    - url

    Actions:

    - Response —> Pydantic-model (Deserialize for Assertions)

    :param response: httpx.Response with File data
    :param request_model: Pydantic-model with File data
    :raise AssertionError
    """
    response_model = CreateFileResponseSchema.model_validate_json(response.text)   # Response —> Pydantic-model (Deserialize for Assertions)

    # Create File Data = Created File Data:
    assert_equal(
        response_model.file.filename,
        request_model.filename,
        'filename')

    assert_equal(
        response_model.file.directory,
        request_model.directory,
        'directory')

    assert_equal(
        response_model.file.url,
        f'http://localhost:8000/static/{request_model.directory}/{request_model.filename}',
        'url')


def assert_create_file_id_length(response: httpx.Response):
    """
    File ID length = 36 chars

    Actions:

    - Response —> Pydantic-model (Deserialize for Assertions)

    :param response: httpx.Response
    :return: AssertionError
    """
    response_model = CreateFileResponseSchema.model_validate_json(response.text)    # Response —> Pydantic-model (Deserialize for Assertions)

    assert_length_is(
        response_model.file.id,
        36,
        'id')


#-----------------------------------------------------------------------------------------------------------------------


#====================================================== Negative =======================================================
# Create file - empty 'filename'
def assert_create_file_empty_filename(actual: httpx.Response):
    """
    Сравнивает Error Response при пустом 'filename' при создании файла с ожидаемой Pydantic-model (ResponseErrorSchema)

    :param actual: Response
    :return: AssertionError
    """
    expected_model = ResponseErrorSchema(
        detail=[
            ErrorSchema(
                type='missing',
                loc=['body', 'filename'],
                msg='Field required',
                input=None,
                ctx=None
            )
        ]
    )
    assert_validate_error_response(actual, expected_model) #

#-----------------------------------------------------------------------------------------------------------------------
# Create file - empty 'directory'
def assert_create_file_empty_directory(actual: httpx.Response):
    """
    Сравнивает Error Response при пустом 'directory' при создании файла с ожидаемой Pydantic-model (ResponseErrorSchema)

    :param actual: Response
    :return: AssertionError
    """
    expected_model = ResponseErrorSchema(
        detail=[
            ErrorSchema(
                type='missing',
                loc=['body', 'directory'],
                msg='Field required',
                input=None,
                ctx=None
            )
        ]
    )
    assert_validate_error_response(actual, expected_model)

#-----------------------------------------------------------------------------------------------------------------------
