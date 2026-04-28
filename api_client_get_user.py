"""
API Client Get User
"""
from clients.auth.auth_schema import AuthUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.data_generator import generate_email, generate_password

#===================================================== PRECONDITION ====================================================
#---------------------------------------------------- 1. Create User ---------------------------------------------------
# Инициализация Pydantic Model
create_user_payload = CreateUserRequestSchema(    # Словарь с данными о новом пользователе
  email=generate_email(),                         # Генерируем email
  password=generate_password(),                   # Генерируем password
  lastName="string",
  firstName="string",
  middleName="string"
)

# Инициализация клиента (public)
public_users_client = get_public_users_client()

# 🟨POST запрос на создание пользователя методом create_user (JSON-объект)
create_user_response = public_users_client.create_user(payload=create_user_payload)

# User ID
user_id = create_user_response['user']['id']      # Вытаскиваем User ID из ответа

#------------------------------------------------------ 2. Get User ----------------------------------------------------
# Инициализация Pydantic Model
auth_data = AuthUserSchema(                       # Словарь с данными для аутентификации
  email=create_user_payload.email,                # Берем email из create_user_payload модели
  password=create_user_payload.password           # Берем password из create_user_payload модели
)
# Инициализация клиента (private)
users_client = get_private_users_client(auth_data=auth_data)

# 🟩GET запрос на получение данных пользователя методом get_user (JSON-объект)
login_user_response = users_client.get_user(user_id)


#------------------------------------------------------ Output ---------------------------------------------------------
print(f'Create User: {create_user_response}')   # {'user': {'id': '07dc57a3-630d-42e3-b901-d4290ee533f3', 'email': 'ybaker@example.net', 'lastName': 'string', 'firstName': 'string', 'middleName': 'string'}}
print(f'   Get User: {login_user_response}')    # {'user': {'id': '07dc57a3-630d-42e3-b901-d4290ee533f3', 'email': 'ybaker@example.net', 'lastName': 'string', 'firstName': 'string', 'middleName': 'string'}}
#-----------------------------------------------------------------------------------------------------------------------
