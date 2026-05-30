"""
Files Assertions
"""
import httpx
from schemas.files import CreateFileResponseSchema, CreateFileRequestSchema, FileSchema
from tools.assertions.base_assert import assert_value_len, assert_is_value, assert_value_equal

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
    assert_value_equal(
        response_model.file.filename,
        'filename',
        request_model.filename)

    assert_value_equal(
        response_model.file.directory,
        'directory',
        request_model.directory)

    assert_value_equal(
        response_model.file.url,
        'url',
        f'http://localhost:8000/static/{request_model.directory}/{request_model.filename}')



def assert_create_file_id_length(response: httpx.Response):
    """
    File ID length = 36 chars

    Actions:

    - Response —> Pydantic-model (Deserialize for Assertions)

    :param response: httpx.Response
    :return: AssertionError
    """
    response_model = CreateFileResponseSchema.model_validate_json(response.text)        # Response —> Pydantic-model (Deserialize for Assertions)
    assert_value_len(response_model.file.id,'id', 36)  # Длина File ID = 36 знаков



#-----------------------------------------------------------------------------------------------------------------------
