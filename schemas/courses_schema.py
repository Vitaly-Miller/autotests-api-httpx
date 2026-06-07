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
class GetCoursesQwerySchema(BaseModel):  # ?qwery
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
    estimated_time: str = Field(alias='estimatedTime')
    preview_file: FileSchema = Field(alias='previewFile')       # {}
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

    # --- Методы прямого доступа к данным ---
    @property
    def course_id(self) -> str:
        return self.response.course.id

    @property
    def title(self) -> str:
        return self.request.title

    @property
    def max_score(self) -> int:
        return self.request.max_score

    @property
    def min_score(self) -> int:
        return self.request.min_score

    @property
    def description(self) -> str:
        return self.request.description

    @property
    def estimated_time(self) -> str:
        return self.request.estimated_time

    # preview_file{}
    @property
    def file_id(self) -> str:
        return self.response.course.preview_file.id

    @property
    def filename(self) -> str:
        return self.response.course.preview_file.filename

    @property
    def directory(self) -> str:
        return self.response.course.preview_file.directory

    @property
    def url(self) -> str:
        return self.response.course.preview_file.url

    # created_by_user{}
    @property
    def user_id(self) -> str:
        return self.response.course.created_by_user.id

    @property
    def email(self) -> str:
        return self.response.course.created_by_user.email

    @property
    def last_name(self) -> str:
        return self.response.course.created_by_user.last_name

    @property
    def first_name(self) -> str:
        return self.response.course.created_by_user.first_name

    @property
    def middle_name(self) -> str:
        return self.response.course.created_by_user.middle_name


#---------------------------------------------------- Update Course ----------------------------------------------------
class UpdateCourseSchema(BaseModel):
    request: UpdateCourseRequestSchema    # ┐
    response: UpdateCourseResponseSchema  # ┘


#-----------------------------------------------------------------------------------------------------------------------
