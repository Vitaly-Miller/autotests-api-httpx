"""
Delete User http://localhost:8000/docs#/users/delete_user_view_api_v1_users__user_id__delete
🟥DELETE
"""
import httpx
import faker

fake = faker.Faker()
#=======================================================================================================================
BASE_URL = 'http://localhost:8000/api/v1'

#-------------------------------------------- 1.[Pre-conditions] Create User -------------------------------------------

create_user_data = {
  "email": fake.email(),                          # Генерируем email нового пользователя
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user_response = httpx.post(                 # 🟨POST запрос на создание нового пользователя
    url=f'{BASE_URL}/users',                       # URL (BASE_URL + endpoint)
    json=create_user_data                          # Передаем данные нового пользователя
)

created_user_data = create_user_response.json()    # Сохраняем JSON-ответ в переменную
user_id = created_user_data['user']['id']          # Вытаскиваем ID пользователя по индексу []


#----------------------------- 2.[Pre-conditions] Authentication (Log in) для получения токена -------------------------

auth_data = {
  'email': create_user_data['email'],              # Берем email из create_user_data по индексу []
  'password': create_user_data['password']         # Берем password из create_user_data по индексу []
}

login_response = httpx.post(                       # 🟨POST запрос (Создание пользователя)
    url=f'{BASE_URL}/authentication/login',        # Base URL + endpoint
    json=auth_data                                 # Передаем данные для авторизации (Email + Password)
)

login_response_data = login_response.json()        # Сохраняем JSON-ответ в переменную
auth_headers = {'Authorization': f'Bearer {login_response_data['token']['accessToken']}'} # Вытаскиваем токен из login_response_data по индексу []


#--------------------------------------------------- 3. Delete User ----------------------------------------------------
delete_user_response = httpx.delete(               # 🟥DELETE запрос на удаление пользователя
    url=f'{BASE_URL}/users/{user_id}',             # URL + endpoint c User-ID
    headers=auth_headers)                          # Передаем auth_headers c токеном авторизации

print(delete_user_response.status_code)            # 200  <-User удален

#=======================================================================================================================
