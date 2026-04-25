"""
Exercises Client
"""
from httpx import Response
from clients.api_client import APIClient
from clients.exercises.exercises_schema import (
    CreateExerciseSchema,
    UpdateExerciseSchema,
    GetExercisesQuerySchema
)

#=======================================================================================================================
#------------------------------------------------------- Client --------------------------------------------------------
class ExercisesClient(APIClient):
    ENDPOINT = '/exercises'

    def get_exercises_api(self, query_course_id: GetExercisesQuerySchema) -> Response:
        """
        Метод получение списка заданий для определенного курса Course ID (?query).

        :param query_course_id: Словарь с Course ID
        :return Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=self.ENDPOINT, params=query_course_id)  # NOQA

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получение информации о задании по Exercise ID.

        :param exercise_id: Exercise ID (str)
        :return Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f'{self.ENDPOINT}/{exercise_id}')

    def create_exercise_api(self, json: CreateExerciseSchema) -> Response:
        """
        Метод создание задания.

        :param json: Данные в формате JSON
        :return Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url=self.ENDPOINT, json=json)

    def update_exercise_api(self, exercise_id: str, json: UpdateExerciseSchema) -> Response:
        """
        Обновления данных задания.

        :param exercise_id: Exercise ID (str)
        :param json: Обновляемые данные в формате JSON
        :return Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f'{self.ENDPOINT}/{exercise_id}', json=json)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удаление задания.

        :param exercise_id: Exercise ID (str)
        :return Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f'{self.ENDPOINT}/{exercise_id}')
