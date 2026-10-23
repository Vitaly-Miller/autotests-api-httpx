"""
Courses (Fixtures)
"""
import httpx
import pytest
import allure
from clients.courses_client import get_courses_client, CoursesClient
from schemas.courses_schema import CreateCourseRequestSchema, CreateCourseSchema, GetCoursesQuerySchema
from schemas.files_schema import CreateFileSchema
from schemas.users_schema import CreateUserSchema

#=================================================== Courses Client ====================================================
# Courses Client
@pytest.fixture
@allure.title('◎ Courses Client (fixture)')
def courses_client(create_user: CreateUserSchema) -> CoursesClient:
    """
    Fixture that provides a CoursesClient() instance (with Authorization)


    :param create_user: Nested Pydantic fixture that creates a user
    :return: CoursesClient() instance (with Authorization)
    """
    courses_client = get_courses_client(create_user.auth_data)
    return courses_client            # CoursesClient()


#---------------------------------------------------- Create course ----------------------------------------------------
# API
@pytest.fixture
@allure.title('▷ Create Course (API-fixture)')
def create_course_api(
    courses_client: CoursesClient,    # ┐  ✨DEDUPLICATION within a single test is a fundamental Pytest feature
    create_user: CreateUserSchema,    # ┘  ✨Same User! Even though both fixtures create a user
    create_file: CreateFileSchema
) -> httpx.Response:
    """
    API fixture that creates a course

    ✨DEDUPLICATION within a single test is a fundamental Pytest feature.
    ✨The same User! Even though both fixtures create a user.

    :param courses_client: Nested Pydantic fixture that provides a CoursesClient instance (with Authorization)
    :param create_user:    Nested Pydantic fixture that creates a user (✨the same User ⬆︎)
    :param create_file:    Nested Pydantic fixture that creates a file
    :return: httpx.Response
    """
    create_course_data = CreateCourseRequestSchema(  # Initialize Pydantic model with default fake data
        previewFileId=create_file.file_id,           # Replace default with real File-ID
        createdByUserId=create_user.user_id          # Replace default with real User-ID
    )
    response = courses_client.create_course_api(create_course_data)   # ▶ Request via API method
    return response                                                   # httpx.Response


# Pydantic-model (full)
@pytest.fixture
@allure.title('▷ Create Course (Pydantic-fixture)')
def create_course(
    courses_client: CoursesClient,    # ┐  ✨DEDUPLICATION within a single test is a fundamental Pytest feature
    create_user: CreateUserSchema,    # ┘  ✨Same User! Even though both fixtures create a user
    create_file: CreateFileSchema
) -> CreateCourseSchema:
    """
    Pydantic fixture that creates a course

    ✨DEDUPLICATION within a single test is a fundamental Pytest feature.
    ✨The same User! Even though both fixtures create a user.

    :param courses_client: Nested Pydantic fixture that provides a CoursesClient instance (with Authorization)
    :param create_user:    Nested Pydantic fixture that creates a user (✨the same User ⬆︎)
    :param create_file:    Nested Pydantic fixture that creates a file
    :return: Pydantic-model (CoursesFullSchema) ✨<Request + Response>
    """
    create_course_data = CreateCourseRequestSchema(  # Initialize Pydantic model with default fake data, except:...
        previewFileId=create_file.file_id,           # ... Replace default with real File-ID
        createdByUserId=create_user.user_id          # ... Replace default with real User-ID
    )
    response_model = courses_client.create_course(create_course_data)   # ▶ Request via Pydantic method
    response_model_full = CreateCourseSchema(request=create_course_data, response=response_model)   # Initialize Pydantic model (CoursesFullSchema) ✨<Request + Response>
    return response_model_full                       # Pydantic-model (CoursesFullSchema) ✨<Request + Response>


#----------------------------------------------------- Get courses -----------------------------------------------------
# API
@pytest.fixture
@allure.title('▷ Get Courses (API-fixture)')
def get_courses_api(courses_client: CoursesClient, create_user: CreateUserSchema) -> httpx.Response:
    """
    API fixture that gets a list of courses by User-ID

    :param courses_client: Built-in Pydantic fixture that provides a CoursesClient() instance
    :param create_user: Built-in Pydantic fixture that creates a user
    :return: httpx.Response
    """
    user_id_query_model = GetCoursesQuerySchema(userId=create_user.user_id)       # Pydantic-model
    response = courses_client.get_courses_api(user_id_query_model)                # ▶ Request via API method
    return response                                                               # httpx.Response


#=======================================================================================================================
