"""
Courses Client
/courses
"""
import httpx
from clients.api_client import APIClient
from clients.private_http_client_builder import get_private_http_client
from clients.auth.auth_schema import AuthUserSchema
from clients.courses.courses_schema import (
    GetCoursesRequestSchema,
    CreateCourseRequestSchema,
    UpdateCourseRequestSchema,
    CreateCourseResponseSchema
)


#=================================================== Courses Client ====================================================
class CoursesClient(APIClient):
    ENDPOINT = '/courses'
    #------------------------------------------------- Get Courses -----------------------------------------------------
    # API 🟩
    def get_courses_api(self, query_user_id: GetCoursesRequestSchema) -> httpx.Response:
        """
        Метод для получения СПИСКА курсов по User ID (?query)

        :param query_user_id: User ID в формате Pydantic-модели
        :return: httpx.Response
        """
        return self.get(url=self.ENDPOINT, params=query_user_id)  # NOQA

    #-------------------------------------------------- Get Course -----------------------------------------------------
    # API 🟩
    def get_course_api(self, course_id: str) -> httpx.Response:
        """
        Метод для получения курса по его Course ID

        :param course_id: Course ID
        :return: httpx.Response
        """
        return self.get(url=f'{self.ENDPOINT}/{course_id}')

    #------------------------------------------------- Create Course ---------------------------------------------------
    # API 🟨
    def create_course_api(self, create_course_data: CreateCourseRequestSchema) -> httpx.Response:
        """
        Метод для СОЗДАНИЯ курса

        :param create_course_data: Данные для создания курса в формате Pydantic-model
        :return: httpx.Response
        """
        return self.post(
            url=self.ENDPOINT,
            json=create_course_data.model_dump(by_alias=True)    # ⚠ сериализация Model —> Dict (т.к. payload - Pydantic-модель)
        )

    # Pydantic-model
    def create_course(self, create_course_data: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        """
        Метод для СОЗДАНИЯ курса с получением данных о созданном курсе в формате Pydantic-model

        :param create_course_data: Данные для создания курса в формате Pydantic-model
        :return: Pydantic-model: CreateCourseResponseSchema
        """
        response = self.create_course_api(create_course_data)
        return CreateCourseResponseSchema.model_validate_json(response.text)  # Валидируем ответ (любой) —> Model

    #------------------------------------------------- Update Course ---------------------------------------------------
    # API 🟪
    def update_course_api(self, course_id: str, update_course_data: UpdateCourseRequestSchema) -> httpx.Response:
        """
        Метод для частичного ОБНОВЛЕНИЯ курса по Course ID

        :param course_id: Course ID
        :param update_course_data: Данными, которые необходимо обновить в формате Pydantic-model
        :return: httpx.Response
        """
        return self.patch(
            url=f'{self.ENDPOINT}/{course_id}',
            json=update_course_data.model_dump(by_alias=True)     # сериализация Model —> Dict (т.к. payload - Pydantic-модель)
        )

    #------------------------------------------------- Delete Course ---------------------------------------------------
    # API 🟥
    def delete_course_api(self, course_id: str) -> httpx.Response:
        """
        Метод для УДАЛЕНИЯ курса по его Course ID

        :param course_id: Course ID
        :return: httpx.Response
        """
        return self.delete(url=f'{self.ENDPOINT}/{course_id}')


#================================================= Client (✨Helper) ===================================================
def get_courses_client(auth_data: AuthUserSchema) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом

    :param auth_data: Данные для аутентификации (log in) пользователя (Email, Password) в формате Pydantic-model
    :return: Готовый к использованию CoursesClient
    """
    return CoursesClient(client=get_private_http_client(auth_data))
