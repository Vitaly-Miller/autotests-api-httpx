"""
HTTPX Client
"""

import httpx

#=======================================================================================================================
# 1. Проходим аутентификацию (обычный httpx)
auth_data = {                                          # Данные уже зарегистрированного в системе пользователя в виде словаря
    'email': 'user@example.com',
    'password': 'string'
}
# Выполняем обычный httpx запрос
login_response = httpx.post(url='http://localhost:8000/api/v1/authentication/login', json=auth_data)

# 2. Вытаскиваем токен из тела ответа по индексу []
login_response_json = login_response.json()             # Сохраняем JSON-ответ в переменную
token = login_response_json['token']['accessToken']     # Вытаскиваем токен из login_response_json по индексу []
#----------------------------------------------------
# 3. Инициализируем httpx.Client клиент-сессию с настроенными Base URL и headers-авторизацией 👈
client = httpx.Client(
    base_url='http://localhost:8000/api/v1',
    headers={'Authorization': f'Bearer {token}'}
)

# Выполняем client GET-запрос, в котором уже хранятся base_url и headers с токеном авторизации.
get_user_me_response = client.get(url='/users/me')      # Просто добавили endpoint.

#-----------------------------------------------------------------------------------------------------------------------
# Output
print(login_response_json)          # {'token': {'tokenType': 'bearer', 'accessToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmUiOiIyMDI2LTA0LTIyVDA1OjMwOjIxLjYwMDI5MyIsInVzZXJfaWQiOiI3MjFjYjg4NS0xY2E4LTQ3OTEtYjA4YS03OGMxZGNhYTFiNmIifQ.juy1nlk004FXR7GE8laKPSBpHUrMdby-A3LlWid2In8', 'refreshToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmUiOiIyMDI2LTA2LTIxVDA1OjAwOjIxLjYwMDM4MSIsInVzZXJfaWQiOiI3MjFjYjg4NS0xY2E4LTQ3OTEtYjA4YS03OGMxZGNhYTFiNmIifQ.l_qD2jztuThll-cyS1IlRwiMeRIs8QNt4WOQok5EZFE'}}
print(get_user_me_response.json())  # {'user': {'id': '721cb885-1ca8-4791-b08a-78c1dcaa1b6b', 'email': 'user@example.com', 'lastName': 'string', 'firstName': 'string', 'middleName': 'string'}}
#-----------------------------------------------------------------------------------------------------------------------
