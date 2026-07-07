"""
Files Assertions
"""
import httpx
import allure
from config import settings
from schemas.errors_schema import ErrorResponseSchema, ErrorSchema, NotFoundErrorResponseSchema
from schemas.files_schema import CreateFileResponseSchema, CreateFileRequestSchema, GetFileResponseSchema
from tools.assertions.base_assert import assert_length, assert_is_value, assert_equal
from tools.assertions.errors_assert import assert_error_response, assert_not_found_error_response

#=======================================================================================================================
# Create File Response data is non-empty
@allure.step('Create File Response data is non-empty')
def assert_create_file_response_non_empty(response: CreateFileResponseSchema):
    """
    Create File Response data is non-empty

    :param response: Pydantic-model (CreateFileResponseSchema)
    :raise AssertionError
    """
    assert_is_value(response.file.id, 'id')
    assert_is_value(response.file.filename, 'filename')
    assert_is_value(response.file.directory, 'directory')
    assert_is_value(response.file.url, 'url')


# Create File Response data = Request data
@allure.step('Create File Response data = Request data')
def assert_create_file_response(response: CreateFileResponseSchema, request: CreateFileRequestSchema):
    """
    Create File Response data = Request data

    :param response: Pydantic-model (CreateFileResponseSchema)
    :param request: Pydantic-model (CreateFileRequestSchema)
    :raise AssertionError
    """
    expected_url = f'{settings.httpx_client.base_url}/static/{request.directory}/{request.filename}'  # URL for comparison

    assert_equal(response.file.filename,request.filename,'filename')
    assert_equal(response.file.directory,request.directory,'directory')
    assert_equal(response.file.url,expected_url,'url')



# File-ID validation
@allure.step('File-ID validation')
def assert_file_id(response: CreateFileResponseSchema | GetFileResponseSchema, file_id: str | None = None):
    """
    File-ID validation

    - File-ID is non-empty
    - File-ID length = 36 chars
    - Actual File-ID = Expected File-ID (optional)

    :param response: Pydantic-model (CreateFileResponseSchema)
    :param file_id: File-ID / None (optional)
    :raise AssertionError
    """
    assert_is_value(response.file.id, 'id')                       # File-ID is non-empty
    assert_length(response.file.id,36,'id')         # File-ID length = 36 chars

    if file_id:
        assert_equal(response.file.id, file_id, 'id')    # Actual File-ID = Expected File-ID


#-----------------------------------------------------------------------------------------------------------------------


#====================================================== NEGATIVE =======================================================
#----------------------------------------------------- Create File -----------------------------------------------------
# Create File Error Response by empty "filename"
def assert_create_file_empty_filename_error_response(response: httpx.Response):
    """
    Create File Error Response by empty "filename"

    :param response: httpx.Response
    :return: AssertionError
    """
    with allure.step('Create File Error Response by empty "filename"'):           # Allure step Title
        actual_response = ErrorResponseSchema.model_validate_json(response.text)   # httpx.Response  —> Pydantic-model (deserialize)
        expected_response = ErrorResponseSchema(                                   # Инициализация ожидаемой Pydantic-model
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



# Create File Error Response by empty "directory"
def assert_create_file_empty_directory_error_response(response: httpx.Response):
    """
    Create File Error Response by empty "directory"

    :param response: httpx.Response
    :return: AssertionError
    """
    with allure.step('Create File Error Response by empty "directory"'):           # Allure step Title
        actual_response = ErrorResponseSchema.model_validate_json(response.text)   # httpx.Response —> Pydantic-model (deserialize)
        expected_response = ErrorResponseSchema(                                   # Инициализация ожидаемой Pydantic-model
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
# Get File Error Response by invalid File-ID (non-UUID)
@allure.step('Get File Error Response by invalid File-ID (non-UUID)')
def assert_get_file_invalid_id_error_response(response: httpx.Response):
    """
    Get File Error Response by invalid File-ID (non-UUID)

    - actual   - Deserialize httpx.Response —> Pydantic-model (ErrorResponseSchema)
    - expected - Initialize (ErrorResponseSchema)

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


# Get File Not Found Error Response by non-existent file
@allure.step('Get File Not Found Error Response by non-existent file')
def assert_get_file_not_found_error_response(response: httpx.Response):
    """
    Get File Not Found Error Response by non-existent file

    - actual   - Deserialize httpx.Response —> Pydantic-model (NotFoundErrorResponseSchema)
    - expected - Initialize (NotFoundErrorResponseSchema)

    :param response: httpx.Response
    :return: AssertionError
    """
    actual_response = NotFoundErrorResponseSchema.model_validate_json(response.text)  # httpx.Response —> Pydantic-model (deserialize)
    expected_response = NotFoundErrorResponseSchema(
        detail='File not found'                                                       # Expected error message
    )
    assert_not_found_error_response(actual_response, expected_response)






#-----------------------------------------------------------------------------------------------------------------------
