"""
Exercises Schema
"""
from pydantic import BaseModel, Field

#=======================================================================================================================
#-------------------------------------------------- Pydantic Schemas ---------------------------------------------------
class CreateExerciseSchema(BaseModel):
    title: str
    course_id: str = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')


class UpdateExerciseSchema(BaseModel):
    title: str | None
    course_id: str | None = Field(alias='courseId')
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    order_index: int | None = Field(alias='orderIndex')
    description: str | None
    estimated_time: str | None = Field(alias='estimatedTime')


#-----------------------------------------------------------------------------------------------------------------------
