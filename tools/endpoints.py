"""
Endpoints + Enum
"""
from enum import StrEnum

#=======================================================================================================================
class Endpoint(StrEnum):
    route = '/api/v1'

    USERS = f'{route}/users'
    AUTH = f'{route}/authentication'
    FILES = f'{route}/files'
    COURSES = f'{route}/courses'
    EXERCISES = f'{route}/exercises'

#=======================================================================================================================
