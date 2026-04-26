"""
Exercises Client
"""
from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client
from clients.auth.auth_schema import AuthUserSchema
from clients.exercises.exercises_schema import (
    CreateExerciseRequestSchema,
    UpdateExerciseRequestSchema,
    GetExercisesRequestSchema
)
#=======================================================================================================================
#------------------------------------------------------- Client --------------------------------------------------------
class ExercisesClient(APIClient):
    ENDPOINT = '/exercises'

    def get_exercises_api(self, query_course_id: GetExercisesRequestSchema) -> Response:
        """
        Метод получения списка заданий для определенного курса Course ID (?query).

        :param query_course_id: Словарь с Course ID
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=self.ENDPOINT, params=query_course_id)  # NOQA

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получение информации о задании по Exercise ID.

        :param exercise_id: Exercise ID
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f'{self.ENDPOINT}/{exercise_id}')

    def create_exercise_api(self, json: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания задания.

        :param json: Данные в формате JSON
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url=self.ENDPOINT, json=json.model_dump(by_alias=True))

    def update_exercise_api(self, exercise_id: str, json: UpdateExerciseRequestSchema) -> Response:
        """
        Метод частичного обновления данных задания.

        :param exercise_id: Exercise ID
        :param json: Обновляемые данные в формате JSON
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f'{self.ENDPOINT}/{exercise_id}', json=json.model_dump(by_alias=True))

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаление задания.

        :param exercise_id: Exercise ID
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f'{self.ENDPOINT}/{exercise_id}')


#--------------------------------------------------- Client Builder ----------------------------------------------------
def get_exercise_client(user: AuthUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
