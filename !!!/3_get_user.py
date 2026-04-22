"""
Get User http://localhost:8000/docs#/users/get_user_view_api_v1_users__user_id__get
🟦GET
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
    url=f'{BASE_URL}/authentication/login',        # URL (BASE_URL + endpoint)
    json=login_payload                             # Передаем login_payload c email & password
)

login_response_data = login_response.json()        # Получаем все данные из login_response
auth_headers = {'Authorization': f'Bearer {login_response_data['token']['accessToken']}'} # Вытаскиваем по индексу [] токен из login_response_data

#-----------------------------------------------------------------------------------------------------------------------
# 3. Get User
get_user_me_response = httpx.get(                    # 🟩GET запрос (Получение данных пользователя)
    url=f'{BASE_URL}/users/{user_id}',               # URL (BASE_URL + endpoint c user_id)
    headers=auth_headers)                            # Передаем auth_headers c токеном авторизации

get_user_response_data = get_user_me_response.json() # Получаем все данные из get_user_me_response
print(get_user_response_data)                        # {'user': {'id': '9e660f17-d670-448a-98ca-0de40b43fa29', 'email': 'user_1775801784.19539@email.com', 'lastName': 'string', 'firstName': 'string', 'middleName': 'string'}}

#=======================================================================================================================
