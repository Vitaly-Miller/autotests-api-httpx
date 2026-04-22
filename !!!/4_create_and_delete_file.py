"""
Create File http://localhost:8000/docs#/files/create_file_view_api_v1_files_post
🟨POST
"""
import httpx
import faker
from pathlib import Path

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

login_response = httpx.post(                       # 🟨POST запрос на авторизацию пользователя (Log in)
    url=f'{BASE_URL}/authentication/login',        # URL (BASE_URL + endpoint)
    json=login_payload                             # Передаем login_payload c email & password
)

login_response_data = login_response.json()        # Получаем все данные из login_response
auth_headers = {'Authorization': f'Bearer {login_response_data['token']['accessToken']}'} # Вытаскиваем по индексу [] токен из login_response_data
#-----------------------------------------------------------------------------------------------------------------------
print(f"""
    User email: {create_user_payload['email']}
User password': {create_user_payload['password']} 
       User ID: {user_id}
    User Token: {login_response_data['token']['accessToken']}
  Auth Headers: {auth_headers}
""")

#-----------------------------------------------------------------------------------------------------------------------
# 3. Create File (Через контекстный менеджер <with> - для закрытия после запроса)
file_path = Path(__file__).parents[1]/'testdata'/'files'/'image.png' # относительный путь к файлу (.parents[1] - на один уровень вверх относительно текущего файла с запросом)
with open(file_path, 'rb') as f:                                     # open('путь к файлу', бинарный режим чтения) as <переменная>
    create_file_response = httpx.post(                               # 🟨POST запрос на отправку файла
        url=f'{BASE_URL}/files',                                     # URL (BASE_URL + endpoint)
        data={'filename': 'image.png', 'directory': 'Uploaded'},     # ⚠Параметры из Swagger: Новое название файла,  Директория сохранения
        files={'upload_file': f},                                    # ⚠Параметры из Swagger: f - переменная прочитанного файла
        headers=auth_headers                                         # Передаем auth_headers с токеном
    )

create_file_response_data = create_file_response.json()
file_id = create_file_response_data['file']['id']

print(f"""
Create File Response Data: {create_file_response_data}   
                  File ID: {file_id}
""")

#-----------------------------------------------------------------------------------------------------------------------
# Delete file by ID
delete_file_response = httpx.delete(                                 # 🟥DELETE запрос на удаление файла
    url=f'{BASE_URL}/files/{file_id}',                               # URL (BASE_URL + endpoint с file_id)
    headers=auth_headers                                             # Передаем auth_headers с токеном
)

print(f'     Delete File Response: {delete_file_response}')          # <Response [200 OK]> - файл удален

#=======================================================================================================================
