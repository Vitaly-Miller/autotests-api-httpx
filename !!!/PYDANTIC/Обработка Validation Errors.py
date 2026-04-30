"""
Обработка Validation Errors
"""
from pprint import pprint

from pydantic import BaseModel, Field, ValidationError

#==================================================== Schema ===========================================================
"""Цифры"""
class UserSchema(BaseModel):
    id: str | int = Field(gt=10)        # (> 10)  greater than     (gt)
    books: str | int = Field(ge=10)     # (>= 10) greater or equal (ge)
    age: str | int = Field(lt=10)       # (< 10)  less than        (lt)
    score: str | int = Field(le=10)     # (<= 10) less or equal    (le)

#--------------------------------------------------- ✅Valid model -----------------------------------------------------
valid_user = UserSchema(
    id=11,
    books=10,
    age=9,
    score=10
)

print(valid_user)               # id=11 books=10 age=9 score=10

#-------------------------------------------------- ❌Invalid model ----------------------------------------------------
try:
    invalid_user = UserSchema(
        id=11,
        books=10,
        age=10,                 # 👈Передаем ошибочный аргумент
        score=10
    )
except ValidationError as e:     # Перехват ошибки типа ValidationError и сохранения описания в переменную <e>
    # Вывод описания исключения
    print(e)                     # 1 validation error for UserSchema
                                 # age
                                 #  Input should be less than 10 [type=less_than, input_value=10, input_type=int]
                                 #    For further information visit https://errors.pydantic.dev/2.13/v/less_than

    # Подробный вывод исключения:
    print(e.errors())            # [{'type': 'less_than', 'loc': ('age',), 'msg': 'Input should be less than 10', 'input': 10, 'ctx': {'lt': 10}, 'url': 'https://errors.pydantic.dev/2.13/v/less_than'}]

#-----------------------------------------------------------------------------------------------------------------------
