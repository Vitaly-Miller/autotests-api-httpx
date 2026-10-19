"""
Courses Client
"""
import allure
import httpx
from tools.api_coverage import tracker
from tools.endpoints import Endpoint
from clients.api_client import APIClient
from clients.httpx_client_private import get_httpx_client_private
from schemas.auth_schema import AuthDataSchema
from schemas.courses_schema import (
    CreateCourseRequestSchema, CreateCourseResponseSchema, GetCoursesQuerySchema,
    UpdateCourseRequestSchema, UpdateCourseResponseSchema
)

#=================================================== Courses Client ====================================================
class CoursesClient(APIClient):
    """
    Client for working with /api/v1/courses

    .
    """
    #--------------------------------------------------- Get Courses ---------------------------------------------------
    # API
    @allure.step('▶ Get courses by User-ID (API)')
    @tracker.track_coverage_httpx(Endpoint.COURSES)
    def get_courses_api(self, query_user_id: GetCoursesQuerySchema) -> httpx.Response:
        """
        API method for getting a list of courses by User-ID (?query)

        :param query_user_id: Pydantic model with User-ID (?query)
        :return: httpx.Response
        """
        response = self.get(
            url=Endpoint.COURSES,
            params=query_user_id.model_dump(by_alias=True))
        return response

    #---------------------------------------------------- Get Course ---------------------------------------------------
    # API
    @allure.step('▶ Get course by ID (API)')
    @tracker.track_coverage_httpx(f'{Endpoint.COURSES}/{{course_id}}')
    def get_course_api(self, course_id: str) -> httpx.Response:
        """
        API method for getting a course by Course-ID

        :param course_id: Course-ID
        :return: httpx.Response
        """
        response = self.get(url=f'{Endpoint.COURSES}/{course_id}')
        return response


    #--------------------------------------------------- Create Course -------------------------------------------------
    # API
    @allure.step('▶ Create course (API)')
    @tracker.track_coverage_httpx(Endpoint.COURSES)
    def create_course_api(self, create_course_data: CreateCourseRequestSchema) -> httpx.Response:
        """
        API method for creating a course

        :param create_course_data: Pydantic model with course creation data
        :return: httpx.Response
        """
        response = self.post(
            url=Endpoint.COURSES,
            json=create_course_data.model_dump(by_alias=True)
        )
        return response


    # Pydantic-model
    @allure.step('▶ Create Course (Pydantic)')
    def create_course(self, create_course_data: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        """
        Pydantic method for creating a course

        :param create_course_data: Pydantic model with course creation data
        :return: Pydantic-model (CreateCourseResponseSchema)
        """
        response = self.create_course_api(create_course_data)
        response_model = CreateCourseResponseSchema.model_validate_json(response.text)
        return response_model


    #--------------------------------------------------- Update Course -------------------------------------------------
    # API
    @allure.step('▶ Update Course by ID (API)')
    @tracker.track_coverage_httpx(f'{Endpoint.COURSES}/{{course_id}}')
    def update_course_api(self, course_id: str, new_course_data: UpdateCourseRequestSchema) -> httpx.Response:
        """
        API method for partially updating a course by Course-ID

        :param course_id: Course-ID
        :param new_course_data: Pydantic model with the data to update
        :return: httpx.Response
        """
        response = self.patch(
            url=f'{Endpoint.COURSES}/{course_id}',
            json=new_course_data.model_dump(by_alias=True)
        )
        return response


    # Pydantic-model
    @allure.step('▶ Update Course by ID (Pydantic)')
    def update_course_pydantic(self, course_id: str, new_course_data: UpdateCourseRequestSchema) -> UpdateCourseResponseSchema:
        """
        Pydantic method for partially updating a course by Course-ID

        :param course_id: Course-ID
        :param new_course_data: Pydantic model with the data to update
        :return: Pydantic-model (UpdateCourseResponseSchema)
        """
        response = self.update_course_api(course_id, new_course_data)
        response_model = UpdateCourseResponseSchema.model_validate_json(response.text)
        return response_model


    #--------------------------------------------------- Delete Course -------------------------------------------------
    # API
    @allure.step('▶ Delete Course by ID (API)')
    @tracker.track_coverage_httpx(f'{Endpoint.COURSES}/{{course_id}}')
    def delete_course_api(self, course_id: str) -> httpx.Response:
        """
        API method for deleting a course by Course-ID

        :param course_id: Course-ID
        :return: httpx.Response
        """
        response = self.delete(url=f'{Endpoint.COURSES}/{course_id}')
        return response



#================================================== Client (builder) ===================================================
@allure.step('◎ Get Courses Client')
def get_courses_client(auth_data: AuthDataSchema) -> CoursesClient:
    """
    Returns a CoursesClient instance (with authorization)

    :param auth_data: Pydantic model with user authentication data (email, password)
    :return: CoursesClient instance
    """
    courses_client = CoursesClient(client=get_httpx_client_private(auth_data))
    return courses_client


#=======================================================================================================================
