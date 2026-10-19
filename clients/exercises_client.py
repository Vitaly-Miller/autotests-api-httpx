"""
Exercises Client
"""
import httpx
import allure

from tools.api_coverage import tracker
from tools.endpoints import Endpoint
from clients.api_client import APIClient
from clients.httpx_client_private import get_httpx_client_private
from schemas.auth_schema import AuthDataSchema
from schemas.exercises_schema import (
    CreateExerciseRequestSchema,
    GetExerciseResponseSchema, GetExercisesQuerySchema, UpdateExerciseRequestSchema,
    CreateExerciseResponseSchema, UpdateExerciseResponseSchema
)

#================================================= Exercises Client ====================================================
class ExercisesClient(APIClient):
    """
    Client for working with /api/v1/exercises

    .
    """
    #------------------------------------------------- Create Exercise -------------------------------------------------
    # API
    @allure.step('▶ Create Exercise (API)')
    @tracker.track_coverage_httpx(f'{Endpoint.EXERCISES}')
    def create_exercise_api(self, create_exercise_data: CreateExerciseRequestSchema) -> httpx.Response:
        """
        API method for creating an exercise

        :param create_exercise_data: Pydantic model with exercise data
        :return: httpx.Response
        """
        response = self.post(
            url=Endpoint.EXERCISES,
            json=create_exercise_data.model_dump(by_alias=True)
        )
        return response


    # Pydantic-model
    @allure.step('▶ Create Exercise (Pydantic)')
    def create_exercise(self, exercise_data: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Pydantic method for creating an exercise

        :param exercise_data: Pydantic model with exercise data
        :return: Pydantic-model (CreateExerciseResponseSchema)
        """
        response = self.create_exercise_api(exercise_data)
        response_model = CreateExerciseResponseSchema.model_validate_json(response.text)
        return response_model


    #-------------------------------------------------- Get Exercise ---------------------------------------------------
    # API
    @allure.step('▶ Get Exercise by ID (API)')
    @tracker.track_coverage_httpx(f'{Endpoint.EXERCISES}/{{exercise_id}}')
    def get_exercise_api(self, exercise_id: str) -> httpx.Response:
        """
        API method for getting an exercise by Exercise-ID

        :param exercise_id: Exercise-ID
        :return: httpx.Response
        """
        response = self.get(url=f'{Endpoint.EXERCISES}/{exercise_id}')
        return response


    # Pydantic-model
    @allure.step('▶ Get Exercise by ID (Pydantic)')
    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Pydantic method for getting an exercise by Exercise-ID

        :param exercise_id: Exercise-ID
        :return: Pydantic-model (GetExerciseResponseSchema)
        """
        response = self.get_exercise_api(exercise_id)
        response_model = GetExerciseResponseSchema.model_validate_json(response.text)
        return response_model


    #-------------------------------------------------- Get Exercises --------------------------------------------------
    # API
    @allure.step('▶ Get Exercises by Course-ID (API)')
    @tracker.track_coverage_httpx(f'{Endpoint.EXERCISES}')
    def get_exercises_api(self, query_course_id: GetExercisesQuerySchema) -> httpx.Response:
        """
        API method for getting a list of exercises by Course-ID (?query)

        :param query_course_id: Pydantic model with Course-ID (?query)
        :return: httpx.Response
        """
        response = self.get(
            url=Endpoint.EXERCISES,
            params=query_course_id.model_dump(by_alias=True))
        return response


    #------------------------------------------------- Update Exercise -------------------------------------------------
    # API
    @allure.step('▶ Update Exercise by ID (API)')
    @tracker.track_coverage_httpx(f'{Endpoint.EXERCISES}/{{exercise_id}}')
    def update_exercise_api(self, exercise_id: str, new_exercise_data: UpdateExerciseRequestSchema) -> httpx.Response:
        """
        API method for partially updating an exercise

        :param exercise_id: Exercise-ID
        :param new_exercise_data: Pydantic model with the data to update
        :return: httpx.Response
        """
        response = self.patch(
            url=f'{Endpoint.EXERCISES}/{exercise_id}',
            json=new_exercise_data.model_dump(by_alias=True)
        )
        return response


    # Pydantic-model
    @allure.step('▶ Update Exercise by ID (Pydantic)')
    def update_exercise(self, exercise_id: str, new_exercise_data: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        """
        Pydantic method for partially updating an exercise

        :param exercise_id: Exercise-ID
        :param new_exercise_data: Pydantic model with the data to update
        :return: Pydantic-model (UpdateExerciseResponseSchema)
        """
        response = self.update_exercise_api(
            exercise_id,
            new_exercise_data
        )
        response_model = UpdateExerciseResponseSchema.model_validate_json(response.text)
        return response_model


    #------------------------------------------------- Delete Exercise -------------------------------------------------
    # API
    @allure.step('▶ Delete Exercise by ID (API)')
    @tracker.track_coverage_httpx(f'{Endpoint.EXERCISES}/{{exercise_id}}')
    def delete_exercise_api(self, exercise_id: str) -> httpx.Response:
        """
        API method for deleting an exercise by Exercise-ID

        :param exercise_id: Exercise-ID
        :return: httpx.Response
        """
        response = self.delete(url=f'{Endpoint.EXERCISES}/{exercise_id}')
        return response


#=================================================== Client (builder) ==================================================
@allure.step('◎ Get Exercises Client')
def get_exercises_client(auth_data: AuthDataSchema) -> ExercisesClient:
    """
    Returns an ExercisesClient instance with a preconfigured HTTP client (with authorization)

    :param auth_data: Pydantic model with user authentication data (email, password)
    :return: ExercisesClient instance (with authorization)
    """
    exercises_client = ExercisesClient(client=get_httpx_client_private(auth_data))
    return exercises_client


#=======================================================================================================================
