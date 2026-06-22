"""
Allure Tag

Для создания перечислений — наборов именованных констант
"""
from enum import Enum, StrEnum

#=======================================================================================================================
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

#=======================================================================================================================
