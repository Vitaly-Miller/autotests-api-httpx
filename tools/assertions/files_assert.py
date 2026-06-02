"""
Files Assertions
"""
from typing import Any

import httpx

from schemas.errors_schema import ResponseErrorSchema, ErrorSchema, NotFoundErrorSchema
from schemas.files_schema import CreateFileResponseSchema, CreateFileRequestSchema
from tools.assertions.base_assert import assert_length_is, assert_is_value, assert_equal
from tools.assertions.errors_assert import assert_validate_error_response, assert_not_found_response

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
def assert_create_file_empty_filename_error_response(actual: httpx.Response):
    """
    Проверка Error Response при создании файла с пустым 'filename'

    Сравнивает Error Response с ожидаемой Pydantic-model (ResponseErrorSchema) при создании файла с пустым 'filename'

    :param actual: Response
    :return: AssertionError
    """
    expected_model = ResponseErrorSchema(          # Ожидаемая Pydantic-model (ResponseErrorSchema)
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


# Create file - empty 'directory'
def assert_create_file_empty_directory_error_response(actual: httpx.Response):
    """
    Проверка Error Response при создании файла с пустым 'directory'

    Сравнивает Error Response с ожидаемой Pydantic-model (ResponseErrorSchema) при создании файла с пустым 'directory'

    :param actual: Response
    :return: AssertionError
    """
    expected_model = ResponseErrorSchema(             # Ожидаемая Pydantic-model (ResponseErrorSchema)
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


# File not found
def assert_file_not_found_error_response(actual: httpx.Response):
    """
    Проверка Error Response при попытке получить несуществующий файл

    Сравнивает Error Response с Pydantic-model (NotFoundErrorSchema) при попытке получить несуществующий файл

    :param actual: Response
    :return: AssertionError
    """
    expected_model = NotFoundErrorSchema(            # Ожидаемая Pydantic-model (NotFoundErrorSchema)
        detail='File not found'
    )
    assert_not_found_response(actual, expected_model)

# Get File by invalid File ID (non-UUID format)
def assert_get_file_by_invalid_file_id_error_response(actual: httpx.Response):
    """
    Проверка Error Response при получении файла с невалидным File ID (non-UUID format)

    Сравнивает Error Response с ожидаемой Pydantic-model (ResponseErrorSchema) при создании файла с невалидным File ID (non-UUID format)

    :param actual: Response
    :return: AssertionError
    """
    expected_model = ResponseErrorSchema(             # Ожидаемая Pydantic-model (ResponseErrorSchema)
        detail=[
            ErrorSchema(
                type='uuid_parsing',
                loc=['path', 'file_id'],
                msg='Input should be a valid UUID, invalid character: found `i` at 1',
                input=actual.json()['detail'][0]['input'],     # 👈 тут 'invalid File ID' при передаче (пока решил так)
                ctx={"error": 'invalid character: found `i` at 1'}
            )
        ]
    )
    assert_validate_error_response(actual, expected_model)
