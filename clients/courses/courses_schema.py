"""
Courses Schema
"""
from pydantic import BaseModel, Field

#=======================================================================================================================
#-------------------------------------------------- Pydantic Schemas ---------------------------------------------------
class GetCoursesQuerySchema(BaseModel):
    userId: str = Field(alias='user_id')

class CreateCourseRequestSchema(BaseModel):
    title: str
    maxScore: int = Field(alias='max_score')
    minScore: int = Field(alias='min_score')
    description: str
    estimatedTime: str = Field(alias='estimated_time')
    previewFileId: str = Field(alias='preview_file_id')
    createdByUserId: str = Field(alias='created_by_user_id')

class UpdateCourseRequestSchema(BaseModel):
    title: str | None
    maxScore: int | None = Field(alias='max_score')
    minScore: int | None = Field(alias='min_score')
    description: str | None
    estimatedTime: str | None = Field(alias='estimated_time')

#-----------------------------------------------------------------------------------------------------------------------
