"""
Courses Pydantic Schemas
"""
from pydantic import BaseModel, Field

#=================================================== REQUEST schema ====================================================
#----------------------------------------------------- Get Courses -----------------------------------------------------
class GetCoursesRequestSchema(BaseModel):
    """
    Схема для запроса списка курсов по User ID (?qwery).
    """
    user_id: str = Field(alias='userId')


#---------------------------------------------------- Create Course ----------------------------------------------------
class CreateCourseRequestSchema(BaseModel):
    """
    Схема для создания нового курса.
    """
    title: str
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    description: str
    estimated_time: str = Field(alias='estimatedTime')
    preview_file_id: str = Field(alias='previewFileId')
    created_by_user_id: str = Field(alias='createdByUserId')


#---------------------------------------------------- Update Course ----------------------------------------------------
class UpdateCourseRequestSchema(BaseModel):
    """
    Схема для частичного обновления курса.
    """
    title: str | None
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    description: str | None
    estimated_time: str | None = Field(alias='estimatedTime')


#================================================== RESPONSE schema ====================================================
#---------------------------------------------------- Get Courses ------------------------------------------------------


#--------------------------------------------------- Create Course -----------------------------------------------------


#--------------------------------------------------- Update Course -----------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------
