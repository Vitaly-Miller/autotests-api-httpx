"""
Courses Pydantic Schema
"""
from pydantic import BaseModel, Field
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema

#================================================== ⬆︎REQUEST Schema ===================================================
#----------------------------------------------------- Get Courses -----------------------------------------------------
class GetCoursesRequestSchema(BaseModel):
    """
    Схема запроса получение списка курсов по User ID (?qwery)

    .
    """
    user_id: str = Field(alias='userId')

#---------------------------------------------------- Create Course ----------------------------------------------------
class CreateCourseRequestSchema(BaseModel):
    """
    Схема запроса на создание нового курса

    .
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
    Схема запроса на частичное обновление курса

    .
    """
    title: str | None
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    description: str | None
    estimated_time: str | None = Field(alias='estimatedTime')


#================================================= ⬆︎RESPONSE Schema ===================================================
#---------------------------------------------------- Get Courses ------------------------------------------------------


#--------------------------------------------------- Create Course -----------------------------------------------------
class PreviewFileSchema(FileSchema):
    """
    Схема ключа "previewFile": {}

    Наследуется: FileSchema
    """
    pass

class CreatedByUserSchema(UserSchema):
    """
    Схема ключа "createdByUser": {}

    Наследуется: UserSchema
    """
    pass

class CourseSchema(BaseModel):
    """
    Схема ключа "course": {}

    .
    """
    id: str
    title: str
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    description: str
    preview_file: PreviewFileSchema = Field(alias='previewFile')
    estimated_time: str = Field(alias='estimatedTime')
    created_by_user: CreatedByUserSchema = Field(alias='createdByUser')

class CreateCourseResponseSchema(BaseModel):
    """
    Схема ответа на создание нового курса

    .
    """
    course: CourseSchema

#--------------------------------------------------- Update Course -----------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------
