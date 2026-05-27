"""
Courses Pydantic Schema
"""
from pydantic import BaseModel, Field
from schemas.files import FileSchema
from schemas.users import UserSchema
from tools.data_generator import fake

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
    title: str = Field(default_factory=fake.sentence)
    max_score: int = Field(alias='maxScore', strict=True, default_factory=fake.max_score)
    min_score: int = Field(alias='minScore', strict=True, default_factory=fake.min_score)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias='estimatedTime', default_factory=fake.estimated_time)
    preview_file_id: str = Field(alias='previewFileId', default_factory=fake.uuid4)           # ⚠️Default value for NEGATIVE test ONLY
    created_by_user_id: str = Field(alias='createdByUserId', default_factory=fake.user_id)    # ⚠️️Default value for NEGATIVE test ONLY

#---------------------------------------------------- Update Course ----------------------------------------------------
class UpdateCourseRequestSchema(BaseModel):
    """
    Схема запроса на частичное обновление курса

    .
    """
    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: int | None = Field(alias='minScore', default_factory=fake.min_score)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias='estimatedTime', default_factory=fake.estimated_time)


#================================================= ⬆︎RESPONSE Schema ===================================================
#---------------------------------------------------- Get Courses ------------------------------------------------------


#--------------------------------------------------- Create Course -----------------------------------------------------
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
    preview_file: FileSchema = Field(alias='previewFile')
    estimated_time: str = Field(alias='estimatedTime')
    created_by_user: UserSchema = Field(alias='createdByUser')

class CreateCourseResponseSchema(BaseModel):
    """
    Схема ответа на создание нового курса

    .
    """
    course: CourseSchema

#--------------------------------------------------- Update Course -----------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------
"""================================== Courses Full Schema (⬆︎Request + ⬇Response) ✨================================"""
class CoursesFullSchema(BaseModel):
    """
    Объединенная схема курса из ⬆︎Request + ⬇Response

    Request  -> Data from CreateCourseRequestSchema
    Response -> Data from CreateCourseResponseSchema
    """
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema
    #------------------------------------- Методы для прямого доступа к данным -----------------------------------------
    # Course ID
    @property
    def course_id(self):
        return self.response.course.id


#-----------------------------------------------------------------------------------------------------------------------
