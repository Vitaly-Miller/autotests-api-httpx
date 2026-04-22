"""
Pydantic (дополнительная схема для поля)
"""
from pydantic import BaseModel, Field

#=======================================================================================================================
#-------------------------------------------------- Pydantic Schema-----------------------------------------------------
# Дополнительная схема для поля <user_address> в <UserUserSchema> (👉 ВСЕГДА ⬆︎ВЫШЕ ОСНОВНОЙ)
class AddressSchema(BaseModel):
    city: str
    zip: str

# ОСНОВНАЯ схема
class UserSchema(BaseModel):
    name: str
    user_address: AddressSchema = Field(alias='userAddress')



#=========================================== MODEL INITIALIZATION & VALIDATION =========================================
# Инициализация модели (Классическая = прописываем параметры модели вручную)                 * типа экземпляр класса
user_model = UserSchema(
    name='John',
    userAddress={'city': 'LA', 'zip': '90210'}  # noqa
)
#--------------------------------------------------  API Objects -------------------------------------------------------

# Dict
user_dict = {
    'name': 'John',
    'userAddress': {'city': 'LA', 'zip': '90210'}
}
#--------------------------------------------------
# JSON-строка
user_json = """
{
    "name": "John",
    "userAddress": {"city": "LA", "zip": "90210"}
}
"""
#===================================== DESERIALIZATION from <...> —> Model (validate ⬅︎) ===============================
# Dict —> Model                     ┌──────┐
user_model_from_dict = UserSchema.model_validate(user_dict)       # name='John' user_address=AddressSchema(city='LA', zip='90210')

# JSON —> Model                     ┌──────┬──────┐
user_model_from_json = UserSchema.model_validate_json(user_json)  # name='John' user_address=AddressSchema(city='LA', zip='90210')


#====================================== SERIALIZATION from Model —> <...> (dump ⮕) ====================================
# Model —> Dict                     ┌────┐
user_dict_from_model = user_model.model_dump()                    # {'name': 'John', 'userAddress': {'city': 'LA', 'zip': '90210'}}

# Model —> JSON                     ┌────┬────┐
user_json_from_model = user_model.model_dump_json()               # {"name":"John","user_address":{"city":"LA","zip":"90210"}}


#------------------------------------------------------ Output ---------------------------------------------------------
print()
print(f'User_Model (manual)   | {user_model}')
print()
print('---- Serialization ----')
print(f'User_Model_from_Dict  | {user_model_from_dict}')
print(f'User_Model_from_JSON  | {user_model_from_json}')
print()
print('---- Serialization ----')
print(f'User_Dict_from_Model  | {user_dict_from_model}')
print(f'User_JSON_from_Model  | {user_json_from_model}')



#-----------------------------------------------------------------------------------------------------------------------
#
