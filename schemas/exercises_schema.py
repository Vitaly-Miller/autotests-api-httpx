"""
Exercises (Pydantic Schema)
"""
from pydantic import BaseModel, Field
from tools.data_generator import fake

"""================================================ ⬆︎REQUEST Schema ================================================"""
#--------------------------------------------------- Create Exercise ---------------------------------------------------
class CreateExerciseRequestSchema(BaseModel):
    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias='courseId', default_factory=fake.uuid4)    # ⚠️Default value for NEGATIVE tests only    (Но сервер не проверяет наличие course_id в системе. Валидация только по формату UUID)
    max_score: int = Field(alias='maxScore', strict=True, default_factory=fake.max_score)
    min_score: int = Field(alias='minScore', strict=True, default_factory=fake.min_score)
    order_index: int = Field(alias='orderIndex', default_factory=fake.random_int)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias='estimatedTime', default_factory=fake.estimated_time)

#---------------------------------------------------- Get Exercise ----------------------------------------------------
class GetExerciseRequestSchema(BaseModel):
    exercise_id: str

#---------------------------------------------------- Get Exercises ----------------------------------------------------
class GetExercisesRequestSchema(BaseModel):
    course_id: str = Field(alias='courseId')  # (?query)


#--------------------------------------------------- Update Exercise ---------------------------------------------------
class UpdateExerciseRequestSchema(BaseModel):
    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: int | None = Field(alias='minScore', default_factory=fake.min_score)
    order_index: int | None = Field(alias='orderIndex', default_factory=fake.random_int)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias='estimatedTime', default_factory=fake.estimated_time)


#-----------------------------------------------------------------------------------------------------------------------

"""================================================ ⬇︎RESPONSE Schema ==============================================="""
#---------------------------------------------------- "exercise": {} ---------------------------------------------------
class ExerciseSchema(BaseModel):
    id: str
    title: str
    course_id: str = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')

#--------------------------------------------------- Create Exercise ---------------------------------------------------
class CreateExerciseResponseSchema(BaseModel):
    exercise: ExerciseSchema

#---------------------------------------------------- Get Exercise -----------------------------------------------------
class GetExerciseResponseSchema(BaseModel):
    exercise: ExerciseSchema

#---------------------------------------------------- Get Exercises ----------------------------------------------------
class GetExercisesResponseSchema(BaseModel):
    exercise: ExerciseSchema

#--------------------------------------------------- Update Exercise ---------------------------------------------------
class UpdateExerciseResponseSchema(BaseModel):
    exercise: ExerciseSchema

#--------------------------------------------------- Delete Exercise ---------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------
"""====================================== Full Schema (⬆︎Request + ⬇Response) ✨====================================="""
class CreateExerciseSchema(BaseModel):
    request: CreateExerciseRequestSchema    # ┐
    response: CreateExerciseResponseSchema  # ┘

    #--- Методы прямого доступа к данным ---
    # Exercise ID
    @property
    def exercise_id(self):
        return self.response.exercise.id


#-----------------------------------------------------------------------------------------------------------------------
