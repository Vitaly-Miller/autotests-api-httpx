"""
Courses Client
/courses
"""
from httpx import Response
from clients.api_client import APIClient
from clients.authentication.authentication_schema import AuthenticationUserSchema
from clients.courses.courses_schema import GetCoursesQuerySchema, CreateCourseRequestSchema, UpdateCourseRequestSchema
from clients.users.private_http_builder import get_private_http_client

#=======================================================================================================================
#----------------------------------------------------- Client ----------------------------------------------------------
class CoursesClient(APIClient):
    ENDPOINT = '/courses'

    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Метод для ПОЛУЧЕНИЯ СПИСКА курсов по User ID.

        :param query: User ID
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=self.ENDPOINT, params=query)  # NOQA

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод для ПОЛУЧЕНИЯ курса по его ID.

        :param course_id: Course ID
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f'{self.ENDPOINT}/{course_id}')

    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Метод для СОЗДАНИЯ курса.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url=self.ENDPOINT, json=request)

    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:
        """
        Метод для ЧАСТИЧНОГО ОБНОВЛЕНИЯ курса по его ID.

        :param course_id: Course ID
        :param request: Словарь с ...
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f'{self.ENDPOINT}/{course_id}', json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод для УДАЛЕНИЯ курса по его ID.

        :param course_id: Course ID
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f'{self.ENDPOINT}/{course_id}')


#-----------------------------------------------------------------------------------------------------------------------
# Builder
def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))
