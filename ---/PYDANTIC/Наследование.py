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

#---------------------------------------------- Инициализация моделей --------------------------------------------------
short_data = ShortUserSchema(
    id='111',
    email='john@emal.com'
)

full_data = FullUserSchema(
    id='222',                        # ┬ Наследуемые поля из короткой схемы
    email='sarah@emal.com',          # ┘
    first_name='Sarah',              # ┬ Новые поля
    last_name='Connor'               # ┘
)


#----------------------------------------------------- Output ----------------------------------------------------------
print(short_data.model_dump())  # {'id': '111', 'email': 'john@emal.com'}
print(full_data.model_dump())   # {'id': '222', 'email': 'sarah@emal.com', 'first_name': 'Sarah', 'last_name': 'Connor'}

#=======================================================================================================================
