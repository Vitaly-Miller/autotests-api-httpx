"""
TEST Create Exercise
"""
import httpx
import http
import pytest
import allure
from clients.exercises_client import ExercisesClient
from schemas.courses_schema import CreateCourseSchema
from schemas.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from tools.allure.annotations import Epic, Feature, Story, Tag
from tools.assertions.base_assert import assert_request_method, assert_status_code
from tools.assertions.schema_assert import validate_json_schema
from tools.assertions.exercises_assert import (
    assert_create_exercise_response,
    assert_create_exercise_response_non_empty,
    assert_exercise_id
)
from tools.tool import Tool

#=======================================================================================================================
# Class annotations
@pytest.mark.exercises                                        # ┐ Pytest Marks
@pytest.mark.regression                                       # ┘
@allure.tag(Tag.REGRESSION, Tag.EXERCISES, Tag.CREATE)  # ] Allure Tags
@allure.epic(Epic.API)                                        # ┐
@allure.feature(Feature.EXERCISES)                            # │ Allure Behaviors
@allure.story(Story.CREATE)                                   # ┘
@allure.parent_suite(Epic.API)                                # ┐
@allure.suite(Feature.EXERCISES)                              # │ Allure Suites (optional)
@allure.sub_suite(Story.CREATE)                               # ┘
@allure.severity(allure.severity_level.NORMAL)                # ] Allure Severity
#-----------------------------------------------------------------------------------------------------------------------
class TestCreateExercise:
    @allure.title('Create Exercise (v.1 - Через API-фикстуру полного цикла)')  # Allure step Title
    def test_create_exercise_1(self, create_exercise_api: httpx.Response):     # Через API-фикстуру полного цикла        ┐
        response = create_exercise_api                                         # Сохраняем ответ API-фикстуры            ┘
        response_model = CreateExerciseResponseSchema.model_validate_json(response.text)           # httpx.Response —> Pydantic-model (deserialize)
        request_model = CreateExerciseRequestSchema.model_validate_json(response.request.content)  # httpx.Response —> Pydantic-model (deserialize)

        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.OK)          # Status Code: 200
        assert_request_method(response.request.method, http.HTTPMethod.POST)  # Method: POST
        assert_create_exercise_response_non_empty(response_model)                            # Response data is NON-empty
        assert_create_exercise_response(response_model, request_model) # Response data = Request data
        assert_exercise_id(response_model)                                                   # Exercise-ID validation
        validate_json_schema(response, CreateExerciseResponseSchema)         # JSON Schema validation



    @allure.title('Create Exercise (v.2 - Через фикстуры: exercises_client, create_course)')  # Allure step Title
    def test_create_exercise_2(                                       #                                                  ─┐
            self,                                                     #                                                   │
            exercises_client: ExercisesClient,                        # Фикстура получения экземпляра ExercisesClient()   │
            create_course: CreateCourseSchema                         # Pydantic-фикстура создания курса                  │
    ):                                                                #                                                   │
        create_exercise_data = CreateExerciseRequestSchema(           # Pydantic-model c fake-data                        │
            courseId=create_course.course_id                          # Fake data —> Реальное значение из фикстуры        │
        )                                                             #                                                  ─┘
        response = exercises_client.create_exercise_api(create_exercise_data)             # ▶ Запрос через API-метод
        response_model = CreateExerciseResponseSchema.model_validate_json(response.text)  # httpx.Response —> Pydantic-model (deserialize)

        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.OK)         # Status Code: 200
        assert_request_method(response.request.method, http.HTTPMethod.POST) # Method: POST
        assert_create_exercise_response_non_empty(response_model)                           # Response data is NON-empty
        assert_create_exercise_response(response_model, create_exercise_data) # Response data = Request data
        assert_exercise_id(response_model)                                                  # Exercise-ID validation
        validate_json_schema(response, CreateExerciseResponseSchema)        # JSON Schema validation


#=======================================================================================================================
        # Tool.api_report(response)
