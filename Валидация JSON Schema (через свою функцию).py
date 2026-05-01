"""
Валидация JSON Schema - create_user_response.json()
"""


from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.schema import validation_json_schema
from tools.data_generator import generate_email, generate_password


#=======================================================================================================================
#-------------------------------------------------- 1. Create User -----------------------------------------------------
# Инициализация Pydantic Model
create_user_payload = CreateUserRequestSchema(               # Модель с данными о новом пользователе
    email=generate_email(),                                  # Генерируем email
    password=generate_password(),                            # Генерируем password
    lastName="string",
    firstName="string",
    middleName="string"
)
# Инициализация клиента (public)
users_client = get_public_users_client()

# 🟨POST запрос на создание пользователя методом create_user_api 👈
create_user_response = users_client.create_user_api(payload=create_user_payload)  # 👈 через .метод _api, чтобы получить - raw JSON для дальнейшего использования

create_user_response_json = create_user_response.json()      # сохраняем JSON-ответ

#--------------------------------------------- 2. Генерация JSON Schema ------------------------------------------------
# Pydantic Schema -> JSON Schema
create_user_response_json_schema = CreateUserResponseSchema.model_json_schema()


#------------------------------------------------- 3. Валидация JSON ---------------------------------------------------
# Через свою функцию валидации
validation_json_schema(
    instance=create_user_response_json,
    schema=create_user_response_json_schema
)                                                       # ✅Данные соответствуют схеме



#============================================ ❌Invalid JSON-data (email) ==============================================
create_user_response_json['user']['email'] = 'hello'    # Меняем в ответе email на невалидный (⚠️НЕ ЗАБУДЬ! - в схеме ответа email: EmailStr)

#------------------------------------------------ Валидация JSON (invalid)  --------------------------------------------
# Через свою функцию валидации
validation_json_schema(
    instance=create_user_response_json,
    schema=create_user_response_json_schema
)                                                       # ❌Ошибка JSON-Schema валидации: 'hello' is not a 'email'
