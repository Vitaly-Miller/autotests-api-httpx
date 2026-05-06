"""
Валидация JSON Schema - create_user_response.json()
Validate JSON Schema - create_user_response.json()
"""
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.data_generator import fake
import jsonschema

#=======================================================================================================================
#--------------------------------------------- 1. Create User (API-метод) ----------------------------------------------
# Инициализация Pydantic Model
create_user_payload = CreateUserRequestSchema(              # Модель с данными о новом пользователе
    email=fake.email(),
    password=fake.password(),
    lastName=fake.last_name(),
    firstName=fake.first_name(),
    middleName=fake.middle_name()
)
# Инициализация клиента (public)
users_client = get_public_users_client()

# 🟨POST запрос на создание пользователя методом create_user_api 👈 (на выходе -> http.Response)
create_user_response = users_client.create_user_api(payload=create_user_payload)  # 👈 через .метод _api, чтобы получить - raw JSON для дальнейшего использования

create_user_response_json = create_user_response.json()     # сохраняем JSON-ответ


#--------------------------------------------- 2. Генерация JSON Schema (ручная)------------------------------------------------
# Pydantic Schema -> JSON Schema
create_user_response_json_schema = CreateUserResponseSchema.model_json_schema()  # ⚠ Можно встроить генератор в валидацию (см. функцию в schema.py)


#------------------------------------------------ 3. Валидация JSON  ---------------------------------------------------
try:
    jsonschema.validate(
        instance=create_user_response_json,                 # Данные для валидации в формате JSON
        schema=create_user_response_json_schema,            # JSON-схема (предварительно сгенерированная выше)
        format_checker=jsonschema.FormatChecker()           # Валидация форматов (⚠️НЕ ЗАБУДЬ! - в схеме ответа - email: EmailStr)
    )
    print('✅Данные соответствуют схеме.')
except jsonschema.ValidationError as e:
    print(f'❌Ошибка JSON-Schema валидации: [{e.message}]') # ✅
    raise e                                                 # Упасть с полным Traceback



#============================================ ❌Invalid JSON (NO 'email' key) ==========================================
del create_user_response_json['user']['email']              # Удаляем ключ 'email' из JSON-ответа для невалидности

#--------------------------------------------------- Валидация JSON (invalid)  -----------------------------------------
try:
    jsonschema.validate(
        instance=create_user_response_json,                 # Данные для валидации в формате JSON
        schema=create_user_response_json_schema,            # JSON-схема (предварительно сгенерированная выше)
        format_checker=jsonschema.FormatChecker()           # Валидация форматов (⚠️НЕ ЗАБУДЬ! - в схеме ответа - email: EmailStr)
    )
    print('✅Данные соответствуют схеме.')
except jsonschema.ValidationError as e:
    print(f'❌Ошибка JSON-Schema валидации: {e.message}')   # ❌
    raise e                                                 # Упасть с полным Traceback

#-----------------------------------------------------------------------------------------------------------------------
