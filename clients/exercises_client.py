"""
Exercises Client
"""
import httpx
import allure
from clients.api_client import APIClient
from clients.httpx_private_client import get_httpx_private_client
from schemas.auth_schema import AuthDataSchema
from schemas.exercises_schema import (
    CreateExerciseRequestSchema,
    GetExerciseResponseSchema, GetExercisesQwerySchema, UpdateExerciseRequestSchema,
    CreateExerciseResponseSchema, UpdateExerciseResponseSchema
)

#================================================== Exercises Client ===================================================
class ExercisesClient(APIClient):
    ENDPOINT = '/api/v1/exercises'
    #---------------------------------------------- Create Exercise ----------------------------------------------------
    # API
    @allure.step('▶ Create Exercise (API)')
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
    @allure.step('▶ Create Exercise (Pydantic)')
    def create_exercise(self, exercise_data: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Pydantic-метод создания задания

        :param exercise_data: Pydantic-model с данными о задании
        :return: Pydantic-model (CreateExerciseResponseSchema)
        """
        response = self.create_exercise_api(exercise_data)                                # ▶ Запрос через API-метод
        response_model = CreateExerciseResponseSchema.model_validate_json(response.text)  # httpx.Response —> Pydantic-model (parsing-deserialize) (deserialize)
        return response_model                                                             # Pydantic-model(CreateExerciseResponseSchema)


    #------------------------------------------------ Get Exercise -----------------------------------------------------
    # API
    @allure.step('▶ Get Exercise by ID (API)')
    def get_exercise_api(self, exercise_id: str) -> httpx.Response:
        """
        API-метод получения информации о задании по Exercise-ID

        :param exercise_id: Exercise-ID
        :return: httpx.Response
        """
        response = self.get(url=f'{self.ENDPOINT}/{exercise_id}')          # ▶ Запрос
        return response                                                    # httpx.Response


    # Pydantic-model
    @allure.step('▶ Get Exercise by ID (Pydantic)')
    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Pydantic-метод получения информации о задании по Exercise-ID

        :param exercise_id: Exercise-ID
        :return: Pydantic-model (GetExerciseResponseSchema)
        """
        response = self.get_exercise_api(exercise_id)                                 # ▶ Запрос через API-метод
        response_model = GetExerciseResponseSchema.model_validate_json(response.text) # httpx.Response —> Pydantic-model (parsing-deserialize) (deserialize)
        return response_model                                                         # Pydantic-model (GetExerciseResponseSchema)


    #------------------------------------------------ Get Exercises ----------------------------------------------------
    # API
    @allure.step('▶ Get Exercises by Course-ID (API)')
    def get_exercises_api(self, query_course_id: GetExercisesQwerySchema) -> httpx.Response:
        """
        API-метод получения списка заданий по Course-ID (?query)

        :param query_course_id: Pydantic-model с Course-ID (?query)
        :return: httpx.Response
        """
        response = self.get(                                      # ▶ Запрос c Query-параметром
            url=self.ENDPOINT,
            params=query_course_id.model_dump(by_alias=True))     # Pydantic-model —> Dict (serialize)
        return response                                           # httpx.Response


    #---------------------------------------------- Update Exercise ----------------------------------------------------
    # API
    @allure.step('▶ Update Exercise by ID (API)')
    def update_exercise_api(self, exercise_id: str, new_exercise_data: UpdateExerciseRequestSchema) -> httpx.Response:
        """
        API-метод частичного обновления данных задания

        :param exercise_id: Exercise-ID
        :param new_exercise_data: Pydantic-model c данными, которые необходимо обновить
        :return: httpx.Response
        """
        response = self.patch(                                    # ▶ Запрос
            url=f'{self.ENDPOINT}/{exercise_id}',
            json=new_exercise_data.model_dump(by_alias=True)      # Pydantic-model —> Dict (serialize)
        )
        return response                                           # httpx.Response


    # Pydantic-model
    @allure.step('▶ Update Exercise by ID (Pydantic)')
    def update_exercise(self, exercise_id: str, new_exercise_data: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        """
        Pydantic-метод частичного обновления данных задания

        :param exercise_id: Exercise-ID
        :param new_exercise_data: Pydantic-model c данными, которые необходимо обновить
        :return: Pydantic-model (UpdateExerciseResponseSchema)
        """
        response = self.update_exercise_api(             # ▶ Запрос через API-метод
            exercise_id,                       # Передаем  Exercise-ID
            new_exercise_data            # Передаем Pydantic-model данными, которые необходимо обновить
        )
        response_model = UpdateExerciseResponseSchema.model_validate_json(response.text) # httpx.Response —> Pydantic-model (parsing-deserialize) (deserialize)
        return response_model                            # Pydantic-model (UpdateExerciseResponseSchema)


    #---------------------------------------------- Delete Exercise ----------------------------------------------------
    # API
    @allure.step('▶ Delete Exercise by ID (API)')
    def delete_exercise_api(self, exercise_id: str) -> httpx.Response:
        """
        Метод удаление задания по Exercise-ID

        :param exercise_id: Exercise-ID
        :return: httpx.Response
        """
        response = self.delete(url=f'{self.ENDPOINT}/{exercise_id}')    # ▶ Запрос
        return response                                                 # httpx.Response


#================================================= Client (✨Helper) ===================================================
@allure.step('◎ Get Exercises Client')
def get_exercises_client(auth_data: AuthDataSchema) -> ExercisesClient:
    """
    Функция получения экземпляра ExercisesClient с уже настроенным HTTP-клиентом (с Авторизацией)

    :param auth_data: Pydantic-model c данными для аутентификации пользователя (Email, Password)
    :return: Экземпляр ExercisesClient (с Авторизацией)
    """
    exercises_client = ExercisesClient(client=get_httpx_private_client(auth_data))
    return exercises_client                                             # ExercisesClient(
