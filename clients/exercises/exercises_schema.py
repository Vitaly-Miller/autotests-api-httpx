"""
Exercises Pydantic Schema
"""
from pydantic import BaseModel, Field

from tools.data_generator import fake

#================================================== ⬆︎REQUEST Schema ===================================================
#---------------------------------------------------- Get Exercises ----------------------------------------------------
class GetExercisesRequestSchema(BaseModel):
    """
    Схема запроса на получение списка заданий для определенного курса по Course ID (?query)

    .
    """
    course_id: str = Field(alias='courseId')

#--------------------------------------------------- Create Exercise ---------------------------------------------------
class CreateExerciseRequestSchema(BaseModel):
    """
    Схема запроса на создание нового задания

    .
    """
    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias='courseId', default_factory=fake.uuid4)    # ⚠️Default value for NEGATIVE tests only
    max_score: int = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: int = Field(alias='minScore', default_factory=fake.min_score)
    order_index: int = Field(alias='orderIndex', default_factory=fake.random_int)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias='estimatedTime', default_factory=fake.estimated_time)

#--------------------------------------------------- Update Exercise ---------------------------------------------------
class UpdateExerciseRequestSchema(BaseModel):
    """
    Схема для запроса на частичное обновление задания

    .
    """
    title: str | None
    course_id: str | None = Field(alias='courseId')
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    order_index: int | None = Field(alias='orderIndex')
    description: str | None
    estimated_time: str | None = Field(alias='estimatedTime')


#================================================== ⬇︎RESPONSE Schema ==================================================
#---------------------------------------------------- Get Exercises ----------------------------------------------------


#--------------------------------------------------- Create Exercise ---------------------------------------------------
class ExerciseSchema(BaseModel):
    """
    Схема ключа "exercise": {}

    .
    """
    id: str
    title: str
    course_id: str = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')

class CreateExerciseResponseSchema(BaseModel):
    """
    Схема ответа на создание нового задания

    .
    """
    exercise: ExerciseSchema

#--------------------------------------------------- Update Exercise ---------------------------------------------------


#--------------------------------------------------- Delete Exercise ---------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------
