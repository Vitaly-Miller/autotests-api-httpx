"""
Get User http://localhost:8000/docs#/users/get_user_view_api_v1_users__user_id__get
🟦GET
"""
import httpx
import faker

#=======================================================================================================================
BASE_URL = 'http://localhost:8000/api/v1'

#-------------------------------------------- 1.[Pre-conditions] Create User -------------------------------------------
create_user_data = {
  "email": faker.Faker().email(),                  # Генерируем email нового пользователя
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user_response = httpx.post(                   # 🟨POST запрос на создание нового пользователя
    url=f'{BASE_URL}/users',                         # URL (BASE_URL + endpoint)
    json=create_user_data                            # Передаем данные нового пользователя
)

created_user_data = create_user_response.json()      # Сохраняем JSON-ответ в переменную             -> {'user': {'id': '9e660f17-d670-448a-98ca-0de40b43fa29', 'email': 'user_1775801784.19539@email.com', 'lastName': 'string', 'firstName': 'string', 'middleName': 'string'}}
user_id = created_user_data['user']['id']            # Вытаскиваем ID пользователя по индексу []     -> 9e660f17-d670-448a-98ca-0de40b43fa29


#--------------------------- 2.[Pre-conditions] Authentication (Log in) для получения токена ---------------------------
auth_data = {
  'email': create_user_data['email'],                # Берем email из create_user_data по индексу []
  'password': create_user_data['password']           # Берем password из create_user_data по индексу []
}

login_response = httpx.post(                         # 🟨POST запрос на авторизацию (Login)
    url=f'{BASE_URL}/authentication/login',          # URL (BASE_URL + endpoint)
    json=auth_data                                   # Передаем auth_data c email & password
)

login_response_data = login_response.json()          # Сохраняем JSON-ответ в переменную
token = login_response_data['token']['accessToken']  # Вытаскиваем токен из login_response_data по индексу []
auth_headers = {'Authorization': f'Bearer {token}'}  # Формируем авторизационный headers


#---------------------------------------------------- 3. Get User ------------------------------------------------------
get_user_me_response = httpx.get(                    # 🟩GET запрос на получение данных пользователя
    url=f'{BASE_URL}/users/{user_id}',               # URL (BASE_URL + endpoint c user_id)
    headers=auth_headers)                            # Передаем auth_headers c токеном авторизации

get_user_response_data = get_user_me_response.json() # Сохраняем JSON-ответ в переменную


#------------------------------------------------------- Output --------------------------------------------------------
print(auth_data)                                     # {'email': 'rachel13@example.net', 'password': 'string'}
print(get_user_response_data)                        # {'user': {'id': '434f7183-3323-415a-8377-2c6b8fdad93d', 'email': 'rachel13@example.net', 'lastName': 'string', 'firstName': 'string', 'middleName': 'string'}}

#=======================================================================================================================
