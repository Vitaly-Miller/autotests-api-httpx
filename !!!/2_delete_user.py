"""
Delete User http://localhost:8000/docs#/users/delete_user_view_api_v1_users__user_id__delete
🟥DELETE
"""
import httpx
import faker

#=======================================================================================================================
BASE_URL = 'http://localhost:8000/api/v1'

#-----------------------------------------------------------------------------------------------------------------------
# 1. [Pre-conditions] Create User
create_user_payload = {
  "email": faker.Faker().email(),                  # Генерируем email нового пользователя
  "password": faker.Faker().password(),            # Генерируем password нового пользователя
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user_response = httpx.post(                 # 🟨POST запрос на создание нового пользователя
    url=f'{BASE_URL}/users',                       # URL (BASE_URL + endpoint)
    json=create_user_payload                       # Передаем create_user_payload c данными нового пользователя
)

created_user_data = create_user_response.json()    # Получаем все данные из create_user_response   -> {'user': {'id': '9e660f17-d670-448a-98ca-0de40b43fa29', 'email': 'user_1775801784.19539@email.com', 'lastName': 'string', 'firstName': 'string', 'middleName': 'string'}}
user_id = created_user_data['user']['id']          # Вытаскиваем ID пользователя по индексу []     -> 9e660f17-d670-448a-98ca-0de40b43fa29

#-----------------------------------------------
# 2. [Pre-conditions] Authentication (Log in) для получения токена
login_payload = {
  'email': create_user_payload['email'],           # Берем email из create_user_payload по индексу []
  'password': create_user_payload['password']      # Берем password из create_user_payload по индексу []
}


login_response = httpx.post(                       # 🟨POST запрос (Создание пользователя)
    url=f'{BASE_URL}/authentication/login', # URL
    json=login_payload                             # Передаем login_payload
)

login_response_data = login_response.json()        # Получаем все данные из login_response
auth_headers = {'Authorization': f'Bearer {login_response_data['token']['accessToken']}'} # Вытаскиваем по индексу [] токен из login_response_data

#-----------------------------------------------------------------------------------------------------------------------
# 3. Delete User
delete_user_response = httpx.delete(               # 🟥DELETE запрос на удаление пользователя
    url=f'{BASE_URL}/users/{user_id}',             # URL + endpoint c User ID
    headers=auth_headers)                          # Передаем auth_headers c токеном авторизации

print(delete_user_response.status_code)            # 200  <-User удален

#=======================================================================================================================
