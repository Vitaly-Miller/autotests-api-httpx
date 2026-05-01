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


#--------------------------------------------- 2. Генерация JSON Schema ------------------------------------------------
# Pydantic Schema -> JSON Schema
create_user_response_json_schema = CreateUserResponseSchema.model_json_schema()


#--------------------------------------------- 3. Валидация JSON Schema ------------------------------------------------
try:
    jsonschema.validate(instance=create_user_response.json(), schema=create_user_response_json_schema)
    print('✅Данные соответствуют схеме.')
except jsonschema.ValidationError as e:
    print(f'❌Ошибка JSON-Schema валидации: {e.message}')          # Данные соответствуют схеме


#------------------------------------------------------- Output --------------------------------------------------------
print(f'User ID: {create_user_response.json()['user']['id']}')     # 👈тода обращаемся по [] индексу - для JSON-ответа без валидации
print(create_user_response_json_schema)
"""
{
    '$defs': {
        'UserSchema': {
            'description': 'Базовая схема ключа "user": {}',
            'properties': {
                'id': {'title': 'Id', 'type': 'string'},
                'email': {'title': 'Email', 'type': 'string'},
                'lastName': {'title': 'Lastname', 'type': 'string'},
                'firstName': {'title': 'Firstname', 'type': 'string'},
                'middleName': {'title': 'Middlename', 'type': 'string'}
            },
            'required': ['id', 'email', 'lastName', 'firstName', 'middleName'],
            'title': 'UserSchema', 'type': 'object'
        }
    }, 
    'description': 'Схема ответа при создании нового пользователя',
    'properties': {
        'user': {'$ref': '#/$defs/UserSchema'}
    },
    'required': ['user'],
    'title': 'CreateUserResponseSchema', 'type': 'object'
}
"""
#-----------------------------------------------------------------------------------------------------------------------
