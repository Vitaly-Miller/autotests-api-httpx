"""
Create File http://localhost:8000/docs#/files/create_file_view_api_v1_files_post
🟨POST
"""
import httpx
import faker
from pathlib import Path

fake = faker.Faker()
#=======================================================================================================================
BASE_URL = 'http://localhost:8000/api/v1'

#-------------------------------------------- 1.[Pre-conditions] Create User -------------------------------------------
create_user_data = {
  "email": fake.email(),                             # Генерируем email нового пользователя
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user_response = httpx.post(                  # 🟨POST запрос на создание нового пользователя
    url=f'{BASE_URL}/users',                        # URL (BASE_URL + endpoint)
    json=create_user_data                           # Передаем create_user_payload c данными нового пользователя
)

created_user_json = create_user_response.json()     # Сохраняем JSON-ответ в переменную
user_id = created_user_json['user']['id']           # Вытаскиваем User ID из created_user_data по индексу []


#--------------------------- 2.[Pre-conditions] Authentication (Log in) для получения токена ---------------------------
auth_data = {
  'email': create_user_data['email'],              # Берем email из auth_data по индексу []
  'password': create_user_data['password']         # Берем password из auth_data по индексу []
}

login_response = httpx.post(                        # 🟨POST запрос на авторизацию (Login)
    url=f'{BASE_URL}/authentication/login',         # URL (BASE_URL + endpoint)
    json=auth_data                                  # Передаем auth_data c email & password
)

login_response_data = login_response.json()         # Сохраняем JSON-ответ в переменную
token = login_response_data['token']['accessToken'] # Вытаскиваем токен из login_response_data по индексу []
auth_headers = {'Authorization': f'Bearer {token}'} # Формируем авторизационный headers c токеном для дальнейших запросов


#--------------------------------------------------- 4. Create File ----------------------------------------------------
# 3. Путь к файлу относительно текущего файла -> .parents[3] - на 3 уровня вверх
file_path = Path(__file__).parents[3]/'testdata'/'files'/'test_image.png'
#file_path = "testdata/my_files/my_image.png"       # <- если ПУСКОВОЙ файл в корне

# (⚠️Через контекстный менеджер <with> - для закрытия после запроса)
with open(file_path, 'rb') as f:                                  # open('путь к файлу', бинарный режим чтения) as <переменная>
    create_file_response = httpx.post(                            # 🟨POST запрос на отправку файла
        url=f'{BASE_URL}/files',                                  # URL (BASE_URL + endpoint)
        data={'filename': 'image.png', 'directory': 'Uploaded'},  # ⚠ Параметры из Swagger: Имя сохранения файла,  Директория сохранения
        files={'upload_file': f},                                 # ⚠ Параметры из Swagger: f - переменная прочитанного файла
        headers=auth_headers                                      # Передаем auth_headers с токеном
    )


create_file_response_data = create_file_response.json()           # Сохраняем JSON-ответ в переменную
file_id = create_file_response_data['file']['id']                 # Вытаскиваем File ID из тела ответа по индексу []

print(f"""
Create File Response Data: {create_file_response_data}   
                  File ID: {file_id} - - ✅ФАЙЛ ЗАЛИТ НА СЕРВЕР!'
""")

#-----------------------------------------------------------------------------------------------------------------------
# 5. Delete file by File ID
delete_file_response = httpx.delete(                              # 🟥DELETE запрос на удаление файла
    url=f'{BASE_URL}/files/{file_id}',                            # URL (BASE_URL + endpoint с file_id)
    headers=auth_headers                                          # Передаем auth_headers с токеном
)

#------------------------------------------------------  Output --------------------------------------------------------
print(f"""
    User email: {create_user_data['email']}                    
User password': {create_user_data['password']} 
       User ID: {user_id}
    User Token: {token}
  Auth Headers: {auth_headers}
""")

print(f'Delete File Response: {delete_file_response} - 🚫ФАЙЛ УДАЛЕН!')      # <Response [200 OK]> - файл удален

#=======================================================================================================================
