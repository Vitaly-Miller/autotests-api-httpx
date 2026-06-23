"""
Allure Annotations + Enum
"""
from enum import Enum, StrEnum

#=======================================================================================================================

#------------------------------------------------------- Suites --------------------------------------------------------
class Tag(str, Enum):                    # ⚠️Python 3.11+ ⮕ class Tag(StrEnum):
    USERS = 'USERS'
    AUTHENTICATION = 'AUTHENTICATION'    # Auth (Login)
    FILES = 'FILES'
    COURSES = 'COURSES'
    EXERCISES = 'EXERCISES'
    #-----------------------
    REGRESSION = 'REGRESSION'
    SMOKE = 'SMOKE'
    NEGATIVE = 'NEGATIVE'
    VALIDATE = 'VALIDATE'
    # -----------------------
    CREATE = 'CREATE'
    GET = 'GET'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'
    # -----------------------
    PARAMETRIZE = 'PARAMETRIZE'

#------------------------------------------------------ Behaviors ------------------------------------------------------
class Epic(StrEnum):
    API = 'API'
    STUDENT = 'Student service'
    ADMIN = 'Admin service'

class Feature(StrEnum):
    USERS = 'Users'
    AUTHENTICATION = 'Authentication'    # Auth (Login)
    FILES = 'Files'
    COURSES = 'Courses'
    EXERCISES = 'Exercises'

class Story(StrEnum):
    LOGIN = 'Login'                      # Auth (Authentication)
    CREATE = 'Create'
    GET = 'Get'
    UPDATE = 'Update'
    DELETE = 'Delete'
    NEGATIVE = 'Negative'
    VALIDATE = 'Validate'





#=======================================================================================================================
