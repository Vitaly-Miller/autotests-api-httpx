"""
API Client Get User
"""
from clients.auth.auth_schema import AuthUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.data_generator import generate_email, generate_password

#=======================================================================================================================
# Инициализация
public_users_client = get_public_users_client()


# 1. Запрос на создание пользователя
create_user_request = CreateUserRequestSchema(
  email=generate_email(),                  # Генерируем email нового пользователя
  password=generate_password(),            # Генерируем password нового пользователя
  firstName='string',
  middleName="string",
  lastName="string"
)

create_user_response = public_users_client.create_user_api(request=create_user_request)
user_id = create_user_response.json()['user']['id']   # Вытаскиваем user_id
print(f'Create User Data:\n{create_user_response.json()}')


#2. Запрос на аутентификацию пользователя
authentication_user = AuthUserSchema(
  email=create_user_request.email,
  password=create_user_request.password
)
private_users_client = get_private_users_client(user=authentication_user)
user_response = private_users_client.get_user_api(user_id)

print(f'User Data:\n{user_response.json()}')
