"""
Pydantic методы
"""
from pydantic import BaseModel, Field, computed_field

#=======================================================================================================================
# API object
obj_dict = {
    "id": "T-800",
    "email": "john@email.com",
    "firstName": "John",
    "lastName": "Connor"
}

#========================================= ВЫЗЫВАЕМОЕ динамическое поле (метод) ========================================
# Схема
class UserSchema(BaseModel):
    id: str
    email: str
    first_name: str = Field(alias='firstName')
    last_name: str = Field(alias='lastName')

    # Python Метод
    @property                                          # БЕЗ скобок ()
    def username(self) -> str:                         # 👈ВЫЗЫВАЕМОЕ динамическое поле <username> НЕ попадает в схему
        """
        Метод позволяет создать ВЫЗЫВАЕМОЕ динамическое поле, не добавляя его к схеме

        :return: str
        """
        return f'{self.first_name} {self.last_name}'


# Инициализация модели (Dict -> Model)
user = UserSchema.model_validate(obj_dict)

#------------------------------------------------------- Output --------------------------------------------------------

print('\n------------- Python @property -------------')
print(user)                 # id='T-800' email='user@example.com' last_name='Connor' first_name='John'   👈(поле  <username> НЕ попало в схему)
print(user.first_name)      # John
print(user.last_name)       # Connor
print(user.username)        # John Connor  (динамическое поле НЕ попало в схему...,но можно вызвать отдельно, как атрибут)




#======================================== ОБЩЕЕ динамическое поле (@computed_field) ====================================
class UserSchema(BaseModel):
    id: str
    email: str
    first_name: str = Field(alias='firstName')
    last_name: str = Field(alias='lastName')
    #username: str = f'{first_name} {last_name}'      # ❌

    # Pydantic Метод
    @computed_field                                   # 👈✅ (Общее динамическое поле <username> ПОПАДАЕТ в схему + БЕЗ скобок ())
    #@property                                        # БЕЗ скобок () - Работает и без свойства @property при @computed_field. Но могут быть ошибки в других стеках.
    def username(self) -> str:
        return f'{self.first_name} {self.last_name}'


# Инициализация модели (Dict -> Model)
user = UserSchema.model_validate(obj_dict)


#------------------------------------------------------- Output --------------------------------------------------------
print('\n--------- Pydantic @computed_field ----------')
print(user)                 # id='T-800' email='john@email.com' first_name='John' last_name='Connor' username='John Connor' 👈(поле  <username> ПОПАЛО в схему)
print(user.first_name)      # John
print(user.last_name)       # Connor
print(user.username)        # John Connor

#=======================================================================================================================
