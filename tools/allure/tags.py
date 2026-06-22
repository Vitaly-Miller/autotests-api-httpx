"""
Allure Tag

Для создания перечислений — наборов именованных констант
"""
from enum import Enum

#=======================================================================================================================
class Tag(str, Enum):
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
