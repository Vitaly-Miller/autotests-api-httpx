"""
Courses Client
"""
import allure
import httpx
from clients.api_client import APIClient
from clients.private_httpx_client_builder import get_private_httpx_client
from schemas.auth_schema import AuthDataSchema
from schemas.courses_schema import (
    CreateCourseRequestSchema, CreateCourseResponseSchema, GetCoursesQwerySchema,
    UpdateCourseRequestSchema, UpdateCourseResponseSchema
)

#=================================================== Courses Client ====================================================
class CoursesClient(APIClient):
    ENDPOINT = '/api/v1/courses'
    #------------------------------------------------- Get Courses -----------------------------------------------------
    # API
    @allure.step('▶ Get courses by User-ID (API)')
    def get_courses_api(self, query_user_id: GetCoursesQwerySchema) -> httpx.Response:
        """
        API-метод получения списка курсов по User-ID (?query)

        :param query_user_id: Pydantic-model c User-ID (?query)
        :return: httpx.Response
        """
        response = self.get(                                                  # ▶ Запрос c Query-параметром
            url=self.ENDPOINT,
            params=query_user_id.model_dump(by_alias=True))                   # Pydantic-model —> Dict (serialize)
        return response                                                       # httpx.Response


    #-------------------------------------------------- Get Course -----------------------------------------------------
    # API
    @allure.step('▶ Get course by ID (API)')
    def get_course_api(self, course_id: str) -> httpx.Response:
        """
        API-метод получения курса по Course-ID

        :param course_id: Course-ID
        :return: httpx.Response
        """
        response = self.get(url=f'{self.ENDPOINT}/{course_id}')               # ▶ Запрос
        return response                                                       # httpx.Response


    #------------------------------------------------- Create Course ---------------------------------------------------
    # API
    @allure.step('▶ Create course (API)')
    def create_course_api(self, create_course_data: CreateCourseRequestSchema) -> httpx.Response:
        """
        API-метод создания курса

        :param create_course_data: Pydantic-model c данными для создания курса
        :return: httpx.Response
        """
        response = self.post(                                                 # ▶ Запрос
            url=self.ENDPOINT,
            json=create_course_data.model_dump(by_alias=True)        # Pydantic-model —> Dict (serialize)
        )
        return response                                                       # httpx.Response


    # Pydantic-model
    @allure.step('▶ Create Course (Pydantic)')
    def create_course(self, create_course_data: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        """
        Pydantic-метод создания курса

        :param create_course_data: Pydantic-model с данными для создания курса
        :return: Pydantic-model (CreateCourseResponseSchema)
        """
        response = self.create_course_api(create_course_data)                 # ▶ Запрос через API-метод
        response_model = CreateCourseResponseSchema.model_validate_json(response.text) # httpx.Response —> Pydantic-model (parsing-deserialize) (deserialize)
        return response_model                                                          # Pydantic-model (CreateCourseResponseSchema)


    #------------------------------------------------- Update Course ---------------------------------------------------
    # API
    @allure.step('▶ Update Course by ID (API)')
    def update_course_api(self, course_id: str, new_course_data: UpdateCourseRequestSchema) -> httpx.Response:
        """
        API-метод частичного обновления курса по Course-ID

        :param course_id: Course-ID
        :param new_course_data: Pydantic-model c данными, которые необходимо обновить
        :return: httpx.Response
        """
        response = self.patch(                                                # ▶ Запрос
            url=f'{self.ENDPOINT}/{course_id}',
            json=new_course_data.model_dump(by_alias=True)                    # Pydantic-model —> Dict (serialize)
        )
        return response                                                       # httpx.Response


    # Pydantic-model
    @allure.step('▶ Update Course by ID (Pydantic)')
    def update_course_pydantic(self, course_id: str, new_course_data: UpdateCourseRequestSchema) -> UpdateCourseResponseSchema:
        """
        Pydantic-метод частичного обновления курса по Course-ID

        :param course_id: Course-ID
        :param new_course_data: Pydantic-model c данными, которые необходимо обновить
        :return: Pydantic-model (UpdateCourseResponseSchema)
        """
        response = self.update_course_api(course_id, new_course_data)  # ▶ Запрос через API-метод
        response_model = UpdateCourseResponseSchema.model_validate_json(response.text) # httpx.Response —> Pydantic-model (parsing-deserialize) (deserialize)
        return response_model                                                          # Pydantic-model (UpdateCourseResponseSchema)


    #------------------------------------------------- Delete Course ---------------------------------------------------
    # API
    @allure.step('▶ Delete Course by ID (API)')
    def delete_course_api(self, course_id: str) -> httpx.Response:
        """
        API-метод удаления курса по Course-ID

        :param course_id: Course-ID
        :return: httpx.Response
        """
        response = self.delete(url=f'{self.ENDPOINT}/{course_id}')            # ▶ Запрос
        return response                                                       # httpx.Response



#================================================= Client (✨Helper) ===================================================
@allure.step('◎ Get Courses Client')
def get_courses_client(auth_data: AuthDataSchema) -> CoursesClient:
    """
    Функция получения экземпляра CoursesClient (с Авторизацией)

    :param auth_data: Pydantic-model c данными для аутентификации пользователя (Email, Password)
    :return: Экземпляр CoursesClient
    """
    courses_client = CoursesClient(client=get_private_httpx_client(auth_data))
    return courses_client                                                     # CoursesClient()
