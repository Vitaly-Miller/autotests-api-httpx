"""
Create User http://localhost:8000/docs#/users/create_user_view_api_v1_users_post
🟨POST
"""
import httpx
import faker

faker = faker.Faker()
#=======================================================================================================================
BASE_URL = 'http://localhost:8000/api/v1'

create_user_payload = {
  "email": faker.email(),                 # Генерируем email нового пользователя
  "password": faker.password(),           # Генерируем password нового пользователя
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user_response = httpx.post(        # 🟨POST запрос на создание нового пользователя
    url=f'{BASE_URL}/users',              # URL (BASE_URL + endpoint)
    json=create_user_payload              # Передаем create_user_payload c данными нового пользователя
)

print(create_user_response.status_code)   # 200
print(create_user_response.json())        # {"user":{"id":"eff6ae4c-c3c8-43e7-83b8-a30abbcf4e6f","email":"user_1775797475.5296519@email.com","lastName":"string","firstName":"string","middleName":"string"}}

#=======================================================================================================================
