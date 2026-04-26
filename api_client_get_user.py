"""
API Client Get User
"""
from clients.auth.auth_schema import AuthUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.data_generator import generate_email, generate_password

#=======================================================================================================================

#--------------------------------------------------- Create User -------------------------------------------------------
# Инициализация Pydantic Model
create_user_payload = CreateUserRequestSchema(
  email=generate_email(),                                       # Генерируем email нового пользователя
  password=generate_password(),                                 # Генерируем password нового пользователя
  lastName="string",
  firstName="string",
  middleName="string"
)
# Запрос на создание пользователя
public_users_client = get_public_users_client()                 # Инициализация клиента через Public Client Builder
create_user_response = public_users_client.create_user_api(payload=create_user_payload) # Выполняем 🟨POST запрос на создание пользователя
create_user_response_data = create_user_response.json()         # Сохраняем JSON ответ
user_id = create_user_response_data['user']['id']               # Вытаскиваем user_id из ответа


#--------------------------------------------------- Get User ----------------------------------------------------------
# Инициализация Pydantic Model
auth_data = AuthUserSchema(
  email=create_user_payload.email,                              # Берем email из create_user_payload модели
  password=create_user_payload.password                         # Берем password из create_user_payload модели
)
# Запрос на аутентификацию пользователя
private_users_client = get_private_users_client(auth_data=auth_data) # Инициализация клиента через Private Client Builder
user_response = private_users_client.get_user_api(user_id)      # Выполняем 🟩GET запрос на получение данных пользователя


#------------------------------------------------------ Output ---------------------------------------------------------
print(f'Created User: {create_user_response.json()}') # {'user': {'id': '07dc57a3-630d-42e3-b901-d4290ee533f3', 'email': 'ybaker@example.net', 'lastName': 'string', 'firstName': 'string', 'middleName': 'string'}}
print(f'Got User:     {user_response.json()}')        # {'user': {'id': '07dc57a3-630d-42e3-b901-d4290ee533f3', 'email': 'ybaker@example.net', 'lastName': 'string', 'firstName': 'string', 'middleName': 'string'}}
