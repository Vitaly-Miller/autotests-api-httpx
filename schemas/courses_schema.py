"""
Courses (Pydantic Schema)
"""
from pydantic import BaseModel, Field
from schemas.files_schema import FileSchema
from schemas.users_schema import UserSchema
from tools.data_generator import fake

"""================================================ ⬆︎REQUEST Schema ================================================"""
#---------------------------------------------------- Create Course ----------------------------------------------------
class CreateCourseRequestSchema(BaseModel):
    title: str = Field(default_factory=fake.sentence)
    max_score: int = Field(alias='maxScore', strict=True, default_factory=fake.max_score)
    min_score: int = Field(alias='minScore', strict=True, default_factory=fake.min_score)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias='estimatedTime', default_factory=fake.estimated_time)
    preview_file_id: str = Field(alias='previewFileId', default_factory=fake.uuid4)           # ⚠️Default value for NEGATIVE test ONLY
    created_by_user_id: str = Field(alias='createdByUserId', default_factory=fake.user_id)    # ⚠️️Default value for NEGATIVE test ONLY

#---------------------------------------------------- Get Course -------------------------------------------------------



#----------------------------------------------------- Get Courses -----------------------------------------------------
class GetCoursesQwerySchema(BaseModel):  # (?qwery)
    user_id: str = Field(alias='userId')


#---------------------------------------------------- Update Course ----------------------------------------------------
class UpdateCourseRequestSchema(BaseModel):
    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: int | None = Field(alias='minScore', default_factory=fake.min_score)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias='estimatedTime', default_factory=fake.estimated_time)


"""=============================================== ⬆︎RESPONSE Schema ================================================"""
#--------------------------------------------------- Create Course -----------------------------------------------------
class CourseSchema(BaseModel):
    id: str
    title: str
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    description: str
    preview_file: FileSchema = Field(alias='previewFile')       # {}
    estimated_time: str = Field(alias='estimatedTime')
    created_by_user: UserSchema = Field(alias='createdByUser')  # {}

class CreateCourseResponseSchema(BaseModel):
    course: CourseSchema

#---------------------------------------------------- Get Course -------------------------------------------------------



#---------------------------------------------------- Get Courses ------------------------------------------------------
class GetCoursesResponseSchema(BaseModel):
    courses: list[CourseSchema]


#--------------------------------------------------- Update Course -----------------------------------------------------
class UpdateCourseResponseSchema(BaseModel):
    course: CourseSchema


#-----------------------------------------------------------------------------------------------------------------------
"""====================================== Full Schema (⬆︎Request + ⬇Response) ✨====================================="""
#---------------------------------------------------- Create Course ----------------------------------------------------
class CreateCourseSchema(BaseModel):
    request: CreateCourseRequestSchema    # ┐
    response: CreateCourseResponseSchema  # ┘

#---------------------------------------------------- Update Course ----------------------------------------------------
class UpdateCourseSchema(BaseModel):
    request: UpdateCourseRequestSchema    # ┐
    response: UpdateCourseResponseSchema  # ┘


#-----------------------------------------------------------------------------------------------------------------------
