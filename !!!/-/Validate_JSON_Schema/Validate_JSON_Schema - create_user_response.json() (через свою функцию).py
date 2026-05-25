"""
Валидация JSON Schema - create_user_response.json()
"""


from clients.users.public_users_client import get_public_users_client
from schemas.users import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.schema_assert import validation_json_schema
from tools.data_generator import fake

#=======================================================================================================================
#----------------------------------------------- 1. Create User (API-метод) --------------------------------------------
# Инициализация Pydantic Model
create_user_data = CreateUserRequestSchema(               # Модель с данными о новом пользователе
    email=fake.email(),
    password=fake.password(),
    lastName=fake.last_name(),
    firstName=fake.first_name(),
    middleName=fake.middle_name()
)
# Инициализация клиента (public)
users_client = get_public_users_client()

# 🟨POST запрос на создание пользователя методом create_user_api 👈
create_user_response = users_client.create_user_api(create_user_data=create_user_data)  # 👈 через .метод _api, чтобы получить - raw JSON для дальнейшего использования


#---------------------------------------------- 5. Генерация JSON-схемы ------------------------------------------------
# ПРОПУСКАЮ - Генерацию встроил в функцию валидации JSON-схемы - validation_json_schema() (см. ниже)


#------------------------------------------------- 3. Валидация JSON ---------------------------------------------------
# Через свою функцию валидации
validation_json_schema(
    instance=create_user_response,
    schema=CreateUserResponseSchema
)                                                       # ✅JSON-response schema. Validation success.



#======================================== ❌Invalid JSON (invalid email format) ========================================
create_user_response_data = create_user_response.json()
create_user_response_data['user']['email'] = 'hello'    # Меняем в ответе email на невалидный (⚠️НЕ ЗАБУДЬ! - в схеме ответа email: EmailStr)

#------------------------------------------------ Валидация JSON (invalid)  --------------------------------------------
#Через свою функцию валидации
validation_json_schema(
    instance=create_user_response_data,
    schema=CreateUserResponseSchema
)                                                       # ❌JSON-response schema. Validation error: ['hello' is not a 'email']
