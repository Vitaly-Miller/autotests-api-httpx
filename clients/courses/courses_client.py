"""
Courses Client
/courses
"""
from httpx import Response
from clients.private_http_builder import get_private_http_client
from clients.api_client import APIClient
from clients.auth.auth_schema import AuthUserSchema
from clients.courses.courses_schema import (
    GetCoursesRequestSchema,
    CreateCourseRequestSchema,
    UpdateCourseRequestSchema,
    CreateCourseResponseSchema
)
#======================================================= Client ========================================================
class CoursesClient(APIClient):
    ENDPOINT = '/courses'
    #------------------------------------------------- Get Courses -----------------------------------------------------
    def get_courses_api(self, query_user_id: GetCoursesRequestSchema) -> Response:
        """
        Метод для ПОЛУЧЕНИЯ СПИСКА курсов по User ID (?query).

        :param query_user_id: Словарь с User ID
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=self.ENDPOINT, params=query_user_id)  # NOQA

    #-------------------------------------------------- Get Course -----------------------------------------------------
    def get_course_api(self, course_id: str) -> Response:
        """
        Метод для ПОЛУЧЕНИЯ курса по его ID.

        :param course_id: Course ID
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f'{self.ENDPOINT}/{course_id}')

    #------------------------------------------------- Create Course ---------------------------------------------------
    def create_course_api(self, payload: CreateCourseRequestSchema) -> Response:
        """
        Метод для СОЗДАНИЯ курса.

        :param payload: Словарь с title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            url=self.ENDPOINT,
            json=payload.model_dump(by_alias=True)    # + ⚠ сериализация Model -> Dict (т.к. payload - Pydantic-модель)
        )

    def create_course(self, payload: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        """
        Метод получения валидированной Pydantic-model с данными о созданном файле.

        :param payload: Словарь с title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId.
        :return: Валидированная Pydantic-модель с данными об авторизации пользователя
        :return: JSON-объект с данными созданного курса
        """
        response = self.create_course_api(payload)
        return CreateCourseResponseSchema.model_validate_json(response.text)  # ⚠ <- Валидируем ответ (любой) -> Model
        return response.json()                                                # ⚠ <- Может вызвать ошибку, если придет не JSON

    #------------------------------------------------- Update Course ---------------------------------------------------
    def update_course_api(self, course_id: str, payload: UpdateCourseRequestSchema) -> Response:
        """
        Метод для ЧАСТИЧНОГО ОБНОВЛЕНИЯ курса по его ID.

        :param course_id: Course ID
        :param payload: Словарь с данными, которые необходимо обновить
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(
            url=f'{self.ENDPOINT}/{course_id}',
            json=payload.model_dump(by_alias=True)     # + ⚠ сериализация Model -> Dict (т.к. payload - Pydantic-модель)
        )

    #------------------------------------------------- Delete Course ---------------------------------------------------
    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод для УДАЛЕНИЯ курса по его ID.

        :param course_id: Course ID
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f'{self.ENDPOINT}/{course_id}')


##==================================================== Client Builder ==================================================
def get_courses_client(auth_data: AuthUserSchema) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :param auth_data: Данные для аутентификации пользователя (Email, Password)
    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(auth_data))
