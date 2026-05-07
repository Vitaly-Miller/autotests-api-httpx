"""
Create User http://localhost:8000/docs#/users/create_user_view_api_v1_users_post
🟨POST
"""
import httpx
import faker                               # Для генерации данных
import json                                # ✨для красивого вывода JSON

fake = faker.Faker()
#=======================================================================================================================
BASE_URL = 'http://localhost:8000/api/v1'

create_user_payload = {
  "email": fake.email(),                  # Генерируем email нового пользователя
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user_response = httpx.post(        # 🟨POST запрос на создание нового пользователя
    url=f'{BASE_URL}/users',              # URL (BASE_URL + endpoint)
    json=create_user_payload              # Передаем create_user_payload c данными нового пользователя в формате JSON
)

create_user_response_data = create_user_response.json()   # Сохраняем JSON-ответ в переменную


#----------------------------------------------------- Output ----------------------------------------------------------
print(create_user_response.status_code)                         # 200
print(create_user_response_data['user']['id'])                  # 51e14a1c-8d92-46e0-83ba-0cd6e6516828
print(json.dumps(create_user_response.json(), indent=4))    # {
                                                                #    "user": {
                                                                #        "id": "51e14a1c-8d92-46e0-83ba-0cd6e6516828",
                                                                #        "email": "jamesgreen@example.org",
                                                                #        "lastName": "string",
                                                                #        "firstName": "string",
                                                                #        "middleName": "string"
                                                                #    }
                                                                # }


#=======================================================================================================================
