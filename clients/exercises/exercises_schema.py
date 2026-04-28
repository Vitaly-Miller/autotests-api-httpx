"""
Exercises Pydantic Schemas
"""
from pydantic import BaseModel, Field

#=================================================== REQUEST schema ====================================================
#---------------------------------------------------- Get Exercises ----------------------------------------------------
class GetExercisesRequestSchema(BaseModel):
    """
    Схема запроса на получение списка заданий для определенного курса по Course ID (?query).
    """
    course_id: str = Field(alias='courseId')

#--------------------------------------------------- Create Exercise ---------------------------------------------------
class CreateExerciseRequestSchema(BaseModel):
    """
    Схема запроса на создание нового задания.
    """
    title: str
    course_id: str = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')

#--------------------------------------------------- Update Exercise ---------------------------------------------------
class UpdateExerciseRequestSchema(BaseModel):
    """
    Схема для запроса на частичное обновление задания.
    """
    title: str | None
    course_id: str | None = Field(alias='courseId')
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    order_index: int | None = Field(alias='orderIndex')
    description: str | None
    estimated_time: str | None = Field(alias='estimatedTime')


#=================================================== RESPONSE schema ===================================================
#---------------------------------------------------- Get Exercises ----------------------------------------------------


#--------------------------------------------------- Create Exercise ---------------------------------------------------


#--------------------------------------------------- Update Exercise ---------------------------------------------------


#--------------------------------------------------- Delete Exercise ---------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------
