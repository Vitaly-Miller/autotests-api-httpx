"""
Courses Client
/courses
"""
import httpx
from clients.api_client import APIClient
from clients.httpx_private_client import get_httpx_private_client
from schemas.auth_schema import AuthDataSchema
from schemas.courses_schema import (
    GetCoursesRequestSchema,
    CreateCourseRequestSchema,
    UpdateCourseRequestSchema,
    CreateCourseResponseSchema, UpdateCourseResponseSchema
)

#=================================================== Courses Client ====================================================
class CoursesClient(APIClient):
    ENDPOINT = '/courses'
    #------------------------------------------------- Get Courses -----------------------------------------------------
    # API
    def get_courses_api(self, query_user_id: GetCoursesRequestSchema) -> httpx.Response:
        """
        API-метод получения списка курсов по User ID (?query)

        :param query_user_id: Pydantic-model c User ID (?query)
        :return: httpx.Response
        """
        response = self.get(url=self.ENDPOINT, params=query_user_id)  # NOQA  # ▶ Запрос
        return response                                                       # httpx.Response

    #-------------------------------------------------- Get Course -----------------------------------------------------
    # API
    def get_course_api(self, course_id: str) -> httpx.Response:
        """
        API-метод получения курса по Course ID

        :param course_id: Course ID
        :return: httpx.Response
        """
        response = self.get(url=f'{self.ENDPOINT}/{course_id}')               # ▶ Запрос
        return response                                                       # httpx.Response

    #------------------------------------------------- Create Course ---------------------------------------------------
    # API
    def create_course_api(self, create_course_data: CreateCourseRequestSchema) -> httpx.Response:
        """
        API-метод создания курса

        :param create_course_data: Pydantic-model c данными для создания курса
        :return: httpx.Response
        """
        response = self.post(                                                 # ▶ Запрос
            url=self.ENDPOINT,
            json=create_course_data.model_dump(by_alias=True)                 # Pydantic-model —> Dict (serialize)
        )
        return response                                                       # httpx.Response

    # Pydantic-model
    def create_course(self, create_course_data: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        """
        Pydantic-метод создания курса

        :param create_course_data: Pydantic-model с данными для создания курса
        :return: Pydantic-model (CreateCourseResponseSchema)
        """
        response = self.create_course_api(create_course_data)                 # ▶ Запрос через API-метод
        response_model = CreateCourseResponseSchema.model_validate_json(response.text) # Response —> Pydantic-model (deserialize)
        return response_model                                                          # Pydantic-model (CreateCourseResponseSchema)

    #------------------------------------------------- Update Course ---------------------------------------------------
    # API
    def update_course_api(self, course_id: str, update_course_data: UpdateCourseRequestSchema) -> httpx.Response:
        """
        API-метод частичного обновления курса по Course ID

        :param course_id: Course ID
        :param update_course_data: Pydantic-model c данными, которые необходимо обновить
        :return: httpx.Response
        """
        response = self.patch(                                                # ▶ Запрос
            url=f'{self.ENDPOINT}/{course_id}',
            json=update_course_data.model_dump(by_alias=True)                 # Pydantic-model —> Dict (serialize)
        )
        return response                                                       # httpx.Response


    # Pydantic-model
    def update_course(self, course_id: str, update_course_data: UpdateCourseRequestSchema) -> UpdateCourseResponseSchema:
        """
        Pydantic-метод частичного обновления курса по Course ID

        :param course_id: Course ID
        :param update_course_data: Pydantic-model c данными, которые необходимо обновить
        :return: Pydantic-model (UpdateCourseResponseSchema)
        """
        response = self.update_course_api(course_id, update_course_data)  # ▶ Запрос через API-метод
        response_model = UpdateCourseResponseSchema.model_validate_json(response.text) # Response —> Pydantic-model (deserialize)
        return response_model                                                          # Pydantic-model (UpdateCourseResponseSchema)

    #------------------------------------------------- Delete Course ---------------------------------------------------
    # API
    def delete_course_api(self, course_id: str) -> httpx.Response:
        """
        API-метод удаления курса по Course ID

        :param course_id: Course ID
        :return: httpx.Response
        """
        response = self.delete(url=f'{self.ENDPOINT}/{course_id}')            # ▶ Запрос
        return response                                                       # httpx.Response



#================================================= Client (✨Helper) ===================================================
def get_courses_client(auth_data: AuthDataSchema) -> CoursesClient:
    """
    Функция получения экземпляра CoursesClient (с Авторизацией)

    :param auth_data: Pydantic-model c данными для аутентификации пользователя (Email, Password)
    :return: Экземпляр CoursesClient
    """
    courses_client = CoursesClient(client=get_httpx_private_client(auth_data))
    return courses_client
