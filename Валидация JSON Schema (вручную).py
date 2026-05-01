"""
Валидация JSON Schema - create_user_response.json()
"""
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.data_generator import generate_email, generate_password
import jsonschema

#=======================================================================================================================
#-------------------------------------------------- 1. Create User -----------------------------------------------------
# Инициализация Pydantic Model
create_user_payload = CreateUserRequestSchema(              # Модель с данными о новом пользователе
    email=generate_email(),                                 # Генерируем email
    password=generate_password(),                           # Генерируем password
    lastName="string",
    firstName="string",
    middleName="string"
)
# Инициализация клиента (public)
users_client = get_public_users_client()

# 🟨POST запрос на создание пользователя методом create_user_api 👈
create_user_response = users_client.create_user_api(payload=create_user_payload)  # 👈 через .метод _api, чтобы получить - raw JSON для дальнейшего использования

create_user_response_json = create_user_response.json()     # сохраняем JSON-ответ


#--------------------------------------------- 2. Генерация JSON Schema ------------------------------------------------
# Pydantic Schema -> JSON Schema
create_user_response_json_schema = CreateUserResponseSchema.model_json_schema()


#------------------------------------------------ 3. Валидация JSON  ---------------------------------------------------
try:
    jsonschema.validate(
        instance=create_user_response_json,                 # Данные для валидации
        schema=create_user_response_json_schema,            # JSON-схема
        format_checker=jsonschema.FormatChecker()           # Валидация форматов (⚠️НЕ ЗАБУДЬ! - в схеме ответа email: EmailStr)
    )
    print('✅Данные соответствуют схеме.')
except jsonschema.ValidationError as e:
    print(f'❌Ошибка JSON-Schema валидации: {e.message}')   # ✅Данные соответствуют схеме.



#============================================= ❌Invalid JSON-data (NO 'email') ========================================
del create_user_response_json['user']['email']              # Удаляем ключ 'email' из JSON- ответа

#--------------------------------------------------- Валидация JSON (invalid)  -----------------------------------------
try:
    jsonschema.validate(
        instance=create_user_response_json,                 # Данные для валидации
        schema=create_user_response_json_schema,            # JSON-схема
        format_checker=jsonschema.FormatChecker()           # Валидация форматов (⚠️НЕ ЗАБУДЬ! - в схеме ответа email: EmailStr)
    )
    print('✅Данные соответствуют схеме.')
except jsonschema.ValidationError as e:
    print(f'❌Ошибка JSON-Schema валидации: {e.message}')   # ❌Ошибка JSON-Schema валидации: 'email' is a required property

#-----------------------------------------------------------------------------------------------------------------------
