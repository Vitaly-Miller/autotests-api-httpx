"""
Pydantic Default Values
"""
from pydantic import BaseModel, Field

#=======================================================================================================================
class CourseSchema(BaseModel):
    id: str = 'P_1'                                                       # default value
    title: str = 'Python_1'                                               # default value
    max_score: int = Field(alias='maxScore', default=1000)                # default value (if alias)
    description: str = 'QA'                                               # default value
    estimated_time: str = Field(alias='estimatedTime', default='1 week')  # default value (if alias)

#-----------------------------------------------------------------------------------------------------------------------
course_default = CourseSchema()   # Full default values (берет все default значения из CourseSchema)

course_custom = CourseSchema(
    id='P_2',                     # Передаем своё значения (custom)
    title='Python_2',             # Передаем своё значения (custom)
    maxScore=1001,                # Передаем своё значения (custom)
    #description=  ,              # 👈Не передаем          (default - QA)
    #estimatedTime=               # 👈Не передаем          (default - 1 week)
)
#-----------------------------------------------------------------------------------------------------------------------
# Output
print(course_default)    # id='P_1' title='Python_1' max_score=1000 description='QA' estimated_time='1 week'
print(course_custom)     # id='P_2' title='Python_2' max_score=1001 description='QA' estimated_time='1 week'
