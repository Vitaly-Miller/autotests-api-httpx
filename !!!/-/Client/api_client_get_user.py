"""
API Client - Get User
"""
from schemas.auth_schema import AuthDataSchema
from clients.users_client_private import get_users_client_private
from clients.users_client_public import get_users_client_public
from schemas.users_schema import CreateUserRequestSchema

#=======================================================================================================================
#-----------------------------------------------  Create User [PRECONDITION] -------------------------------------------
# Инициализация Pydantic Model
create_user_data = CreateUserRequestSchema()    # Инициализация данных через схему c fake данными

# Инициализация UsersClientPublic (экземпляр класса через Helper)
users_client_public = get_users_client_public()

# 🟨POST запрос на создание пользователя методом create_user (на выходе -> Pydantic-Model)
create_user_response = users_client_public.create_user(create_user_data=create_user_data)

user_id = create_user_response.user.id       # Сохранение User-ID для последующего использования

# Авторизационные данные
auth_data = AuthDataSchema(                  # Инициализация модели / Валидация данных через схему
    email=create_user_data.email,            # Вытаскиваем email из create_user_data модели
    password=create_user_data.password       # Вытаскиваем password из create_user_data модели
)
#------------------------------------------------------ Get User -------------------------------------------------------
# Инициализация UsersClientPrivate (экземпляр класса через Helper)
users_client = get_users_client_private(auth_data=auth_data)


# 🟩GET запрос на получение данных пользователя методом get_user
get_user_response = users_client.get_user_pydantic(user_id)


#------------------------------------------------------ Output ---------------------------------------------------------
print(f'Create User: {create_user_response}')   # {'user': {'id': '07dc57a3-630d-42e3-b901-d4290ee533f3', 'email': 'ybaker@example.net', 'lastName': 'string', 'firstName': 'string', 'middleName': 'string'}}
print(f'   Get User: {get_user_response}')      # {'user': {'id': '07dc57a3-630d-42e3-b901-d4290ee533f3', 'email': 'ybaker@example.net', 'lastName': 'string', 'firstName': 'string', 'middleName': 'string'}}
#-----------------------------------------------------------------------------------------------------------------------
