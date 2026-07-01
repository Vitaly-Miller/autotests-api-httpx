"""
Валидация JSON Schema - get_user.json()
JSON Schema validation - get_user.json()
"""
from schemas.auth_schema import AuthDataSchema
from clients.private_users_client import get_private_users_client
from clients.public_users_client import get_public_users_client
from schemas.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema_assert import validate_json_schema
from tools.data_generator import fake

#=======================================================================================================================
#------------------------------------- 1. Create User (через метод .create_user) ---------------------------------------
# Инициализация Pydantic Model
create_user_payload = CreateUserRequestSchema(   # Модель с данными о новом пользователе
    email=fake.email(),
    password=fake.password(),
    lastName=fake.last_name(),
    firstName=fake.first_name(),
    middleName=fake.middle_name()
)
# Инициализация клиента (public)
users_client = get_public_users_client()

# 🟨POST запрос на создание пользователя методом .create_user 👈 (на выходе ->  Pydantic-модель)
create_user_response = users_client.create_user(payload=create_user_payload)  # 👈 через .метод _api, чтобы получить - raw JSON для дальнейшего использования

# User-ID
create_user_id = create_user_response.user.id    # 👈 Обращение через .атрибут - Для валидированной Pydantic-Model


# Check
print(create_user_id)                            # 4848865f-bcb5-49c2-8351-bf5c040247bd

#---------------------------------------------- 2. Get User (API-метод) ------------------------------------------------
# Инициализация Pydantic Model
auth_data = AuthDataSchema(                      # Валидация данных через схему
    email=create_user_payload.email,             # Берем email из create_user_payload модели
    password=create_user_payload.password        # Берем password из create_user_payload модели
)

# Инициализация клиента (private)
users_client = get_private_users_client(auth_data=auth_data)

# 🟩GET запрос на получение данных пользователя методом .get_user_api 👈 (на выходе ->  http.Response)
get_user_response = users_client.get_user_api(create_user_id)

get_user_response_json = get_user_response.json() # Сохраняем JSON-ответ

# User-ID
get_user_response_user_id = get_user_response_json['user']['id']    # 👈 Обращение по [] индексу  - Для JSON-ответа без валидации

# Check
print(get_user_response_user_id)                  # 4848865f-bcb5-49c2-8351-bf5c040247bd

#---------------------------------------------- 5. Генерация JSON-схемы ------------------------------------------------
# ПРОПУСКАЮ - Генерацию встроил в функцию валидации JSON-схемы - validate_json_schema() (см. ниже)


#---------------------------------------------- 6. Валидация JSON-схемы -----------------------------------------------
# Через свою функцию валидации
validate_json_schema(
    instance=get_user_response_json,
    schema=GetUserResponseSchema
)                                                # ✅JSON-response schema. Validation success.


#============================================ ❌Invalid JSON (NO 'id' key) =============================================
del get_user_response_json['user']['id']        # Удаляем ключ 'id' из JSON-ответа

validate_json_schema(
    instance=get_user_response_json,
    schema=GetUserResponseSchema
)                                                # ❌JSON-response schema. Validation error: ['id' is a required property]

#-----------------------------------------------------------------------------------------------------------------------
