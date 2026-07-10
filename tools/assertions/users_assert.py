"""
Users assertions
"""
import allure
from tools.logger import get_logger
from schemas.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base_assert import assert_equal, assert_is_value, assert_length

#------------ Logger -------------
logger = get_logger('USER-ASSERT')

#=======================================================================================================================
# Response data is non-empty
@allure.step('Response data is non-empty')                                        # Allure step title
def assert_create_user_response_non_empty(response: CreateUserResponseSchema):
    """
    Create User Response data is non-empty

    :param response: Pydantic-model (CreateUserResponseSchema)
    :raise AssertionError
    """
    logger.info('Response data is non-empty')                                     # Logger
    assert_is_value(response.user.id, 'id')
    assert_is_value(response.user.email, 'email')
    assert_is_value(response.user.first_name, 'first_name')
    assert_is_value(response.user.middle_name, 'middle_name')
    assert_is_value(response.user.last_name, 'last_name')



# Response data = Request data
@allure.step('Response data = Request data')                                      # Allure step title
def assert_create_user_response(response: CreateUserResponseSchema, request: CreateUserRequestSchema):
    """
    Create User Response data = Request data

    :param response: Pydantic-model (CreateUserResponseSchema)
    :param request: Pydantic-model (CreateUserRequestSchema)
    :raise AssertionError
    """
    logger.info('Response data = Request data')                                   # Logger
    assert_equal(response.user.email,request.email,'email')
    assert_equal(response.user.last_name,request.last_name,'last_name')
    assert_equal(response.user.first_name, request.first_name,'first_name')
    assert_equal(response.user.middle_name,request.middle_name,'middle_ame')


# User-ID validation
@allure.step('User-ID validation')                                                # Allure step title
def assert_user_id(response: CreateUserResponseSchema):
    """
    User-ID validation

    - User-ID is NOT-empty
    - User-ID length = 36 chars

    :param response: Pydantic-model (CreateUserResponseSchema)
    :raise AssertionError
    """
    logger.info('User-ID validation')                                             # Logger
    assert_is_value(response.user.id, 'id')                           # User-ID is NOT-empty
    assert_length(response.user.id, 36, 'id')          # User-ID length = 36 chars

#-----------------------------------------------------------------------------------------------------------------------
