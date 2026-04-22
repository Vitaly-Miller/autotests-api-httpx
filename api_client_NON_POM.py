"""
API Client (NON POM)
(ВСЕ В ОДНОМ)
"""

import httpx
import faker

fake = faker.Faker()

#=======================================================================================================================
BASE_URL = 'http://localhost:8000/api/v1'
#------------------------------------------------- 1. Create User ------------------------------------------------------
# 1.1 Генерируем данные нового пользователя
email = fake.email()                                          # Генерируем email нового пользователя
password = fake.password()                                    # Генерируем password нового пользователя

# 1.2 Payload с данными создаваемого пользователя (User credentials)
create_user_payload = {
  "email": email,
  "password": password,
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
# 1.3 Создаем пользователя
create_user_response = httpx.post(                            # 🟨POST запрос на создание пользователя
    url=f'{BASE_URL}/users',                                  # URL (Base URL + endpoint)
    json=create_user_payload                                  # Передаем данные нового пользователя (User credentials)
)                                                             # User создан!

#--------------------------------------------- 2. Authentication (Lig in) ----------------------------------------------
# 2.1 Payload с данными для авторизации созданного пользователя
login_payload = {
  'email': email,
  'password': password
}
# 2.2 Логиним созданного пользователя для получения Токена
login_response = httpx.post(                                  # 🟨POST запрос на авторизацию (Log in) пользователя
    url=f'{BASE_URL}/authentication/login',                   # URL (Base URL + endpoint)
    json=login_payload                                        # Передаем данные с Login и Password
)
# 2.2 Вытаскиваем Access Token из тела ответа
access_token = login_response.json()['token']['accessToken']  # Вытаскиваем по индексу []

# 2.3 Создаем заголовки для авторизации на основе вытащенного Access Token
auth_headers = {'Authorization': f'Bearer {access_token}'}    # 🔑Bearer - тип токена + сам Access Token

#================================================= 3. ✨API client =====================================================
# 3.1 ✨Создаем API client-сессию
client = httpx.Client(
    base_url=BASE_URL,                                        # BASE URL
    headers=auth_headers                                      # Headers c токеном
)
#=======================================================================================================================

#---------------------------------------------- 4. ✅ Рабочий Request --------------------------------------------------
# 4.1 Применяем API client отправляя запрос с готовыми авторизационными данными
response = client.get('/users/me')        # 🟩GET рабочий запрос + endpoint
print(response.json())                    # {'user': {'id': '77ea510e-af3f-4ac4-94ed-6d29b71a67be', 'email': 'jjones@example.com', 'lastName': 'string', 'firstName': 'string', 'middleName': 'string'}}

#-----------------------------------------------------------------------------------------------------------------------
