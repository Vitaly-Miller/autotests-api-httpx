"""
Allure Annotations + Enum
"""
from enum import StrEnum

#=======================================================================================================================
# ⚠️Python 3.11- ⮕ class ...(str, Enum):
# ⚠️Python 3.11+ ⮕ class ...(StrEnum):

#-------------------------------------------------------- Tags ---------------------------------------------------------
# @allure.tag()
class Tag(StrEnum):
    USERS = 'USERS'
    AUTH = 'AUTHENTICATION'
    FILES = 'FILES'
    COURSES = 'COURSES'
    EXERCISES = 'EXERCISES'
    #------------------------
    REGRESSION = 'REGRESSION'
    SMOKE = 'SMOKE'
    NEGATIVE = 'NEGATIVE'
    VALIDATE = 'VALIDATE'
    #-------------------
    CREATE = 'CREATE'
    GET = 'GET'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'
    #--------------------------
    PARAMETRIZE = 'PARAMETRIZE'


#------------------------------------------------ Behaviors / Suites ---------------------------------------------------
# @allure.epic() / @allure.parent_suite()
class Epic(StrEnum):
    API = 'API'
    STUDENT = 'Student service'
    ADMIN = 'Admin service'

# @allure.feature() / @allure.suite()
class Feature(StrEnum):
    USERS = 'Users'
    AUTH = 'Authentication'
    FILES = 'Files'
    COURSES = 'Courses'
    EXERCISES = 'Exercises'

# @allure.story() / @allure.sub_suite()
class Story(StrEnum):
    LOGIN = 'Login'
    CREATE = 'Create'
    GET = 'Get'
    UPDATE = 'Update'
    DELETE = 'Delete'
    NEGATIVE = 'Negative'
    VALIDATE = 'Validate'


#=======================================================================================================================
