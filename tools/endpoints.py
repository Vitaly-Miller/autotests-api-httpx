"""
Endpoints + Enum
"""
from enum import StrEnum

#=======================================================================================================================
class Endpoint(StrEnum):
    prefix = '/api/v1'

    USERS = f'{prefix}/users'
    AUTH = f'{prefix}/authentication'
    FILES = f'{prefix}/files'
    COURSES = f'{prefix}/courses'
    EXERCISES = f'{prefix}/exercises'

#=======================================================================================================================
