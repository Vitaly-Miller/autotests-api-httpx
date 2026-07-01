"""
Files Assertions
"""
import httpx
import allure
from schemas.errors_schema import ErrorResponseSchema, ErrorSchema, NotFoundErrorResponseSchema
from schemas.files_schema import CreateFileResponseSchema, CreateFileRequestSchema, FileSchema, GetFileResponseSchema
from tools.assertions.base_assert import assert_length, assert_is_value, assert_equal
from tools.assertions.errors_assert import assert_error_response, assert_not_found_error_response

#=======================================================================================================================
# Response data is NON-empty
@allure.step('Check Response data is NON-empty')
def assert_create_file_response_non_empty(response_model: CreateFileResponseSchema):
    """
    Check Response data is NON-empty

    :param response_model: Pydantic-model (CreateFileResponseSchema)
    :raise AssertionError
    """
    assert_is_value(response_model.file.id, 'id')
    assert_is_value(response_model.file.filename, 'filename')
    assert_is_value(response_model.file.directory, 'directory')
    assert_is_value(response_model.file.url, 'url')


# Response data = Request data
@allure.step('Check Response data = Request data')
def assert_create_file_response_data(response_model: CreateFileResponseSchema, request_model: CreateFileRequestSchema):
    """
    Response data = Request data

    :param response_model: Pydantic-model (CreateFileResponseSchema)
    :param request_model: Pydantic-model (CreateFileRequestSchema)
    :raise AssertionError
    """
    expected_url = f'http://localhost:8000/static/{request_model.directory}/{request_model.filename}'  # URL for comparison

    assert_equal(response_model.file.filename,request_model.filename,'filename')
    assert_equal(response_model.file.directory,request_model.directory,'directory')
    assert_equal(response_model.file.url,expected_url,'url')



# File-ID validation
@allure.step('File-ID validation')
def assert_file_id(response_model: CreateFileResponseSchema | GetFileResponseSchema, file_id: str | None = None):
    """
    File-ID validation

    - NON-empty File-ID
    - File-ID length = 36 chars
    - File-ID = expected File-ID (optional)


    :param response_model: Pydantic-model (CreateFileResponseSchema)
    :param file_id: File-ID / None (optional)
    :raise AssertionError
    """
    assert_is_value(response_model.file.id, 'id')                       # NON-empty File-ID
    assert_length(response_model.file.id,36,'id')         # File-ID length = 36 chars

    if file_id:
        assert_equal(response_model.file.id, file_id, 'id')   # File-ID = expected File-ID


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
        actual_response_model = ErrorResponseSchema.model_validate_json(response.text)  # httpx.Response  —> Pydantic-model
        expected_response_model = ErrorResponseSchema(                                  # Инициализация ожидаемой Pydantic-model
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
        assert_error_response(actual_response_model, expected_response_model)



# Create file by Empty Directory
def assert_create_file_empty_directory_error_response(response: httpx.Response):
    """
    Validation Error Response by Empty Directory

    Сравнивает Error Response с ожидаемой Pydantic-model (ErrorResponseSchema) при создании файла с пустым 'directory'

    :param response: httpx.Response
    :return: AssertionError
    """
    with allure.step('Validation create file Error Response by Empty Directory'):       # Allure step Title
        actual_response_model = ErrorResponseSchema.model_validate_json(response.text)  # httpx.Response  —> Pydantic-model
        expected_response_model = ErrorResponseSchema(                                  # Инициализация ожидаемой Pydantic-model
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
        assert_error_response(actual_response_model, expected_response_model)



#------------------------------------------------------- Get File ------------------------------------------------------
@allure.step('Validation get file Error Response by invalid File-ID (non-UUID)')
def assert_get_file_invalid_id_error_response(response: httpx.Response):
    """
    Проверка Error Response при получении файла с невалидным File-ID (non-UUID format)

    Сравнивает Error Response с ожидаемой Pydantic-model (ErrorResponseSchema) при создании файла с невалидным File-ID (non-UUID format)

    :param response: httpx.Response
    :return: AssertionError
    """
    actual_response_model = ErrorResponseSchema.model_validate_json(response.text)  # httpx.Response  —> Pydantic-model
    expected_response_model = ErrorResponseSchema(
        detail=[
            ErrorSchema(
                type='uuid_parsing',
                loc=['path', 'file_id'],
                msg='Input should be a valid UUID, invalid character: found `i` at 1',
                input=response.json()['detail'][0]['input'],     # 👈 тут 'invalid File-ID' при передаче (пока решил так)
                ctx={"error": 'invalid character: found `i` at 1'}
            )
        ]
    )
    assert_error_response(actual_response_model, expected_response_model)


@allure.step('Validation get NON-Existent file Error Response')
def assert_file_not_found_error_response(response: httpx.Response):
    """
    Get NON-existent File / Error Response message

    Сравнивает Error Response с Pydantic-model (NotFoundErrorResponseSchema)

    :param response: httpx.Response
    :return: AssertionError
    """
    actual_response_model = NotFoundErrorResponseSchema.model_validate_json(response.text)  # httpx.Response  —> Pydantic-model
    expected_response_model = NotFoundErrorResponseSchema(
        detail='File not found'                                                             # Expected error message
    )    
    assert_not_found_error_response(actual_response_model, expected_response_model)  # "detail": "File not found"






#-----------------------------------------------------------------------------------------------------------------------
