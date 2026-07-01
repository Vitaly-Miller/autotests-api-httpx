"""
Files Assertions
"""
import httpx
import allure
from schemas.errors_schema import ErrorResponseSchema, ErrorSchema, NotFoundErrorResponseSchema
from schemas.files_schema import CreateFileResponseSchema, CreateFileRequestSchema, GetFileResponseSchema
from tools.assertions.base_assert import assert_length, assert_is_value, assert_equal
from tools.assertions.errors_assert import assert_error_response, assert_not_found_error_response

#=======================================================================================================================
# Response data is NON-empty
@allure.step('Check Response data is NON-empty')
def assert_create_file_response_non_empty(response: CreateFileResponseSchema):
    """
    Check Response data is NON-empty

    :param response: Pydantic-model (CreateFileResponseSchema)
    :raise AssertionError
    """
    assert_is_value(response.file.id, 'id')
    assert_is_value(response.file.filename, 'filename')
    assert_is_value(response.file.directory, 'directory')
    assert_is_value(response.file.url, 'url')


# Response data = Request data
@allure.step('Check Response created file data = Request create file data')
def assert_create_file_response_data(response: CreateFileResponseSchema, request: CreateFileRequestSchema):
    """
    Check Response data = Request data

    :param response: Pydantic-model (CreateFileResponseSchema)
    :param request: Pydantic-model (CreateFileRequestSchema)
    :raise AssertionError
    """
    expected_url = f'http://localhost:8000/static/{request.directory}/{request.filename}'  # URL for comparison

    assert_equal(response.file.filename,request.filename,'filename')
    assert_equal(response.file.directory,request.directory,'directory')
    assert_equal(response.file.url,expected_url,'url')



# File-ID validation
@allure.step('File-ID validation')
def assert_file_id(response: CreateFileResponseSchema | GetFileResponseSchema, file_id: str | None = None):
    """
    File-ID validation

    - NON-empty File-ID
    - File-ID length = 36 chars
    - File-ID = expected File-ID (optional)


    :param response: Pydantic-model (CreateFileResponseSchema)
    :param file_id: File-ID / None (optional)
    :raise AssertionError
    """
    assert_is_value(response.file.id, 'id')                       # NON-empty File-ID
    assert_length(response.file.id,36,'id')         # File-ID length = 36 chars

    if file_id:
        assert_equal(response.file.id, file_id, 'id')   # File-ID = expected File-ID


#-----------------------------------------------------------------------------------------------------------------------


#====================================================== NEGATIVE =======================================================
#----------------------------------------------------- Create File -----------------------------------------------------
# Create file by Empty File Name
def assert_create_file_empty_filename_error_response(response: httpx.Response):
    """
    Validation Error Response by Empty File Name

    Сравнивает Error Response с ожидаемой Pydantic-model (ErrorResponseSchema) при создании файла с пустым 'filename'

    :param response: httpx.Response
    :return: AssertionError
    """
    with allure.step('Validation create file Error Response by Empty File Name'):       # Allure step Title
        actual_response = ErrorResponseSchema.model_validate_json(response.text)  # httpx.Response  —> Pydantic-model
        expected_response = ErrorResponseSchema(                                  # Инициализация ожидаемой Pydantic-model
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
        assert_error_response(actual_response, expected_response)



# Create file by Empty Directory
def assert_create_file_empty_directory_error_response(response: httpx.Response):
    """
    Validation Error Response by Empty Directory

    Сравнивает Error Response с ожидаемой Pydantic-model (ErrorResponseSchema) при создании файла с пустым 'directory'

    :param response: httpx.Response
    :return: AssertionError
    """
    with allure.step('Validation create file Error Response by Empty Directory'):       # Allure step Title
        actual_response = ErrorResponseSchema.model_validate_json(response.text)  # httpx.Response  —> Pydantic-model
        expected_response = ErrorResponseSchema(                                  # Инициализация ожидаемой Pydantic-model
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
        assert_error_response(actual_response, expected_response)



#------------------------------------------------------- Get File ------------------------------------------------------
@allure.step('Validation get file Error Response by invalid File-ID (non-UUID)')
def assert_get_file_invalid_id_error_response(response: httpx.Response):
    """
    Проверка Error Response при получении файла с невалидным File-ID (non-UUID format)

    Сравнивает Error Response с ожидаемой Pydantic-model (ErrorResponseSchema) при создании файла с невалидным File-ID (non-UUID format)

    :param response: httpx.Response
    :return: AssertionError
    """
    actual_response = ErrorResponseSchema.model_validate_json(response.text)  # httpx.Response  —> Pydantic-model
    expected_response = ErrorResponseSchema(
        detail=[
            ErrorSchema(
                type='uuid_parsing',
                loc=['path', 'file_id'],
                msg='Input should be a valid UUID, invalid character: found `i` at 1',
                input=response.json()['detail'][0]['input'],        # 👈 тут 'invalid File-ID' при передаче (пока решил так)
                ctx={"error": 'invalid character: found `i` at 1'}  # ⚠️ Требуется улучшение - не учитывать символы после <...`i` at> ...
            )
        ]
    )
    assert_error_response(actual_response, expected_response)


@allure.step('Validation get NON-Existent file Error Response')
def assert_file_not_found_error_response(response: httpx.Response):
    """
    Get NON-existent File / Error Response message

    Сравнивает Error Response с Pydantic-model (NotFoundErrorResponseSchema)

    :param response: httpx.Response
    :return: AssertionError
    """
    actual_response = NotFoundErrorResponseSchema.model_validate_json(response.text)  # httpx.Response  —> Pydantic-model
    expected_response = NotFoundErrorResponseSchema(
        detail='File not found'                                                             # Expected error message
    )
    assert_not_found_error_response(actual_response, expected_response)  # "detail": "File not found"






#-----------------------------------------------------------------------------------------------------------------------
