"""
Exercises Client
"""
import httpx
from clients.api_client import APIClient
from clients.httpx_private_client import get_httpx_private_client
from schemas.auth_schema import AuthDataSchema
from schemas.exercises_schema import (
    CreateExerciseRequestSchema,
    GetExercisesResponseSchema, UpdateExerciseRequestSchema,
    GetExercisesRequestSchema, CreateExerciseResponseSchema
)

#================================================== Exercises Client ===================================================
class ExercisesClient(APIClient):
    ENDPOINT = '/exercises'
    #---------------------------------------------- Create Exercise ----------------------------------------------------
    # API
    def create_exercise_api(self, create_exercise_data: CreateExerciseRequestSchema) -> httpx.Response:
        """
        API-метод создания задания

        :param create_exercise_data: Pydantic-model с данными о задании
        :return: httpx.Response
        """
        response = self.post(                                     # ▶ Запрос
            url=self.ENDPOINT,
            json=create_exercise_data.model_dump(by_alias=True)   # Pydantic-model —> Dict (serialize)
        )
        return response                                           # httpx.Response

    # Pydantic-model
    def create_exercise(self, exercise_data: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Pydantic-метод создания задания

        :param exercise_data: Pydantic-model с данными о задании
        :return: Pydantic-model (CreateExerciseResponseSchema)
        """
        response = self.create_exercise_api(exercise_data)                                # ▶ Запрос через API-метод
        response_model = CreateExerciseResponseSchema.model_validate_json(response.text)  # Response —> Pydantic-model (deserialize)
        return response_model                                                             # Pydantic-model(CreateExerciseResponseSchema)


    #------------------------------------------------ Get Exercise -----------------------------------------------------
    # API
    def get_exercise_api(self, exercise_id: str) -> httpx.Response:
        """
        API-метод получения информации о задании по Exercise ID

        :param exercise_id: Exercise ID
        :return: httpx.Response
        """
        response = self.get(url=f'{self.ENDPOINT}/{exercise_id}')          # ▶ Запрос
        return response                                                    # httpx.Response

    # Pydantic-model
    def get_exercise(self, exercise_id: str) -> GetExercisesResponseSchema:
        """
        Pydantic-метод получения информации о задании по Exercise ID

        :param exercise_id: Exercise ID
        :return: Pydantic-model (GetExercisesResponseSchema)
        """
        response = self.get_exercise_api(exercise_id)                                  # ▶ Запрос через API-метод
        response_model = GetExercisesResponseSchema.model_validate_json(response.text) # Response —> Pydantic-model (deserialize)
        return response_model                                                          # Pydantic-model (GetExercisesResponseSchema)


    #------------------------------------------------ Get Exercises ----------------------------------------------------
    # API
    def get_exercises_api(self, query_course_id: GetExercisesRequestSchema) -> httpx.Response:
        """
        API-метод получения списка заданий для определенного курса Course ID (?query)

        :param query_course_id: Pydantic-model с Course ID (?query)
        :return: httpx.Response
        """
        response = self.get(url=self.ENDPOINT, params=query_course_id)  # NOQA   # ▶ Запрос
        return response                                                          # httpx.Response


    #---------------------------------------------- Update Exercise ----------------------------------------------------
    # API
    def update_exercise_api(self, exercise_id: str, json: UpdateExerciseRequestSchema) -> httpx.Response:
        """
        API-метод частичного обновления данных задания

        :param exercise_id: Exercise ID
        :param json: Pydantic-model данными, которые необходимо обновить
        :return: httpx.Response
        """
        response = self.patch(                                    # ▶ Запрос
            url=f'{self.ENDPOINT}/{exercise_id}',
            json=json.model_dump(by_alias=True)                   # Pydantic-model —> Dict (serialize)
        )
        return response                                           # httpx.Response

    #---------------------------------------------- Delete Exercise ----------------------------------------------------
    # API
    def delete_exercise_api(self, exercise_id: str) -> httpx.Response:
        """
        Метод удаление задания по Exercise ID

        :param exercise_id: Exercise ID
        :return: httpx.Response
        """
        response = self.delete(url=f'{self.ENDPOINT}/{exercise_id}')             # ▶ Запрос
        return response                                                          # httpx.Response


#================================================= Client (✨Helper) ===================================================
def get_exercises_client(auth_data: AuthDataSchema) -> ExercisesClient:
    """
    Функция получения экземпляра ExercisesClient с уже настроенным HTTP-клиентом (с Авторизацией)

    :param auth_data: Pydantic-model c данными для аутентификации пользователя (Email, Password)
    :return: Экземпляр ExercisesClient (с Авторизацией)
    """
    exercises_client = ExercisesClient(client=get_httpx_private_client(auth_data))
    return exercises_client
