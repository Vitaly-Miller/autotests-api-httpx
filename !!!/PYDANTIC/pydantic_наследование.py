"""
Pydantic Наследование
"""
from pydantic import BaseModel

#=======================================================================================================================
#----------------------------------------------------- Schemas ---------------------------------------------------------
class ShortUserSchema(BaseModel):          # Короткая схема
    id: str
    email: str

class FullUserSchema(ShortUserSchema):     # Полная схема (наследует короткую)
    first_name: str
    last_name: str

#-----------------------------------------------------------------------------------------------------------------------
user_short_data = ShortUserSchema(
    id='111',
    email='john@emal.com'
)

user_full_data = FullUserSchema(
    id='222',                        # ┬ Наследуемые поля из короткой схемы
    email='sarag@emal.com',          # ┘
    first_name='Sarah',              # ┬ Новые поля
    last_name='Connor'               # ┘
)

print(user_short_data.model_dump())  # {'id': '111', 'email': 'john@emal.com'}
print(user_full_data.model_dump())   # {'id': '222', 'email': 'sarag@emal.com', 'first_name': 'Sarah', 'last_name': 'Connor'}

#=======================================================================================================================
