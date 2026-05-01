"""
Валидация JSON Schema - get_user.json()
Validate JSON Schema - get_user.json()
"""
from clients.auth.auth_schema import AuthUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validation_json_schema
from tools.data_generator import generate_password, generate_email

#=======================================================================================================================
#------------------------------------- 1. Create User (через метод .create_user) ---------------------------------------

# Инициализация Pydantic Model
create_user_payload = CreateUserRequestSchema(   # Модель с данными о новом пользователе
    email=generate_email(),                      # Генерируем email
    password=generate_password(),                # Генерируем password
    lastName="string",
    firstName="string",
    middleName="string"
)
# Инициализация клиента (public)
users_client = get_public_users_client()

# 🟨POST запрос на создание пользователя методом .create_user 👈 (на выходе ->  Pydantic-модель)
create_user_response = users_client.create_user(payload=create_user_payload)  # 👈 через .метод _api, чтобы получить - raw JSON для дальнейшего использования

# User ID
create_user_id = create_user_response.user.id    # ⚠ Обращение через .атрибут - Для валидированной Pydantic-Model


# Check
print(create_user_id)                            # 4848865f-bcb5-49c2-8351-bf5c040247bd

#---------------------------------------------- 2. Get User (API-метод) ------------------------------------------------
# Инициализация Pydantic Model
auth_data = AuthUserSchema(                      # Валидация данных через схему
    email=create_user_payload.email,             # Берем email из create_user_payload модели
    password=create_user_payload.password        # Берем password из create_user_payload модели
)

# Инициализация клиента (private)
users_client = get_private_users_client(auth_data=auth_data)

# 🟩GET запрос на получение данных пользователя методом .get_user_api 👈 (на выходе ->  http.Response)
get_user_response = users_client.get_user_api(create_user_id)

get_user_response_json = get_user_response.json() # Сохраняем JSON-ответ

# User ID
get_user_response_user_id = get_user_response_json['user']['id']    # ⚠ Обращение по [] индексу  - Для JSON-ответа без валидации

# Check
print(get_user_response_user_id)                 # 4848865f-bcb5-49c2-8351-bf5c040247bd

#---------------------------------------------- 5. Генерация JSON-схемы ------------------------------------------------
get_user_response_json_schema = GetUserResponseSchema.model_json_schema()

# Check
print(get_user_response_json_schema)  # {'$defs': {'UserSchema': {'description': 'Базовая схема ключа "user": {}', 'properties': {'id': {'title': 'Id', 'type': 'string'}, 'email': {'format': 'email', 'title': 'Email', 'type': 'string'}, 'lastName': {'title': 'Lastname', 'type': 'string'}, 'firstName': {'title': 'Firstname', 'type': 'string'}, 'middleName': {'title': 'Middlename', 'type': 'string'}}, 'required': ['id', 'email', 'lastName', 'firstName', 'middleName'], 'title': 'UserSchema', 'type': 'object'}}, 'description': 'Схема ответа при получении данных пользователя по User ID', 'properties': {'user': {'$ref': '#/$defs/UserSchema'}}, 'required': ['user'], 'title': 'GetUserResponseSchema', 'type': 'object'}

#---------------------------------------------- 6. Валидация JSON-ответа -----------------------------------------------
# Через свою функцию валидации
validation_json_schema(
    instance=get_user_response_json,
    schema=get_user_response_json_schema
)                                               # ✅Данные соответствуют схеме



#============================================ ❌Invalid JSON (NO 'id' key) =============================================
del get_user_response_json['user']['id']        # Удаляем ключ 'id' из JSON-ответа

validation_json_schema(
    instance=get_user_response_json,
    schema=get_user_response_json_schema
)                                               # ❌Ошибка JSON-Schema валидации: 'id' is a required property ...

#-----------------------------------------------------------------------------------------------------------------------
