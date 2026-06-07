"""
Files Assertions
"""
import httpx
from schemas.errors_schema import ErrorResponseSchema, ErrorSchema, NotFoundErrorResponseSchema
from schemas.files_schema import CreateFileResponseSchema, CreateFileRequestSchema, FileSchema, GetFileResponseSchema
from tools.assertions.base_assert import assert_length, assert_is_value, assert_equal
from tools.assertions.errors_assert import assert_validate_error_response, assert_not_found_response

#=======================================================================================================================
# Response data is NON-empty
def assert_create_file_response_non_empty(response: httpx.Response):
    """
    Response data is NON-empty

    :param response: httpx.Response (for deserialize —> Pydantic-model)
    :raise AssertionError
    """
    response_model = CreateFileResponseSchema.model_validate_json(response.text)    # Response —> Pydantic-model

    assert_is_value(response_model.file.id, 'id')
    assert_is_value(response_model.file.filename, 'filename')
    assert_is_value(response_model.file.directory, 'directory')
    assert_is_value(response_model.file.url, 'url')


# Response data = Request data
def assert_create_file_response(response: httpx.Response, request_model: CreateFileRequestSchema):
    """
    Response data = Request data

    :param response: httpx.Response with File data (for deserialize —> Pydantic-model)
    :param request_model: Pydantic-model with File data
    :raise AssertionError
    """
    response_model = CreateFileResponseSchema.model_validate_json(response.text)   # Response —> Pydantic-model                                                    # Условие, если не передать request_model, то ...

    expected_url = f'http://localhost:8000/static/{request_model.directory}/{request_model.filename}'  # URL for comparison

    assert_equal(response_model.file.filename,request_model.filename,'filename')
    assert_equal(response_model.file.directory,request_model.directory,'directory')
    assert_equal(response_model.file.url,expected_url,'url')



# File ID validation
def assert_file_id(response: httpx.Response, file_id: str | None = None):
    """
    File ID validation

    - NON-empty File ID
    - File ID length = 36 chars
    - File ID = expected File ID (optional)


    :param response: httpx.Response with File data (for deserialize —> Pydantic-model)
    :param file_id: File ID / None
    :raise AssertionError
    """
    response_model = CreateFileResponseSchema.model_validate_json(response.text)  # Response —> Pydantic-model

    assert_is_value(response_model.file.id, 'id')                       # NON-empty File ID
    assert_length(response_model.file.id,36,'id')         # File ID length = 36 chars

    if file_id:
        assert_equal(response_model.file.id, file_id, 'id')  # File ID = expected File ID


#-----------------------------------------------------------------------------------------------------------------------


#====================================================== Negative =======================================================
#----------------------------------------------------- Create File -----------------------------------------------------
# Create file by filename="" (empty)
def assert_create_file_empty_filename_error_response(actual: httpx.Response):
    """
    Проверка Error Response при создании файла с пустым filename=""

    Сравнивает Error Response с ожидаемой Pydantic-model (ErrorResponseSchema) при создании файла с пустым 'filename'

    :param actual: Response
    :return: AssertionError
    """
    expected_model = ErrorResponseSchema(
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


# Create file by filename="" (empty)
def assert_create_file_empty_directory_error_response(actual: httpx.Response):
    """
    Проверка Error Response при создании файла с пустым directory=""

    Сравнивает Error Response с ожидаемой Pydantic-model (ErrorResponseSchema) при создании файла с пустым 'directory'

    :param actual: Response
    :return: AssertionError
    """
    expected_model = ErrorResponseSchema(
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


#------------------------------------------------------- Get File ------------------------------------------------------
# Get File by invalid File ID (non-UUID format)
def assert_invalid_file_id_error_response(actual: httpx.Response):
    """
    Проверка Error Response при получении файла с невалидным File ID (non-UUID format)

    Сравнивает Error Response с ожидаемой Pydantic-model (ErrorResponseSchema) при создании файла с невалидным File ID (non-UUID format)

    :param actual: Response
    :return: AssertionError
    """
    expected_model = ErrorResponseSchema(
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


# Get Non-existent File
def assert_file_not_found_error_response(actual: httpx.Response):
    """
    Проверка Error Response при попытке получить несуществующий файл

    Сравнивает Error Response с Pydantic-model (NotFoundErrorResponseSchema) при попытке получить несуществующий файл

    :param actual: Response
    :return: AssertionError
    """
    expected_model = NotFoundErrorResponseSchema(
        detail='File not found'
    )
    assert_not_found_response(actual, expected_model)

#-----------------------------------------------------------------------------------------------------------------------
