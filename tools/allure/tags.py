"""
Allure tag

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
    # -----------------------
    CREATE = 'CREATE'
    GET = 'GET'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'
    VALIDATE = 'VALIDATE'
    # -----------------------
    PARAMETRIZE = 'PARAMETRIZE'
