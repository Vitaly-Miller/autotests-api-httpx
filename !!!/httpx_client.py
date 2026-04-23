"""
HTTPX Client
"""

import httpx

#=======================================================================================================================
# 1. Проходим аутентификацию (обычный httpx)
login_payload = {                                                # Данные зарегистрированного пользователя
    'email': 'user@example.com',
    'password': 'string'
}
# Выполняем обычный httpx запрос
login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)

#-------------------------------------------------------
# 2. Инициализируем httpx.Client клиент-сессию с Base URL и headers-авторизацией 👈
client = httpx.Client(
    base_url='http://localhost:8000/api/v1',
    headers={'Authorization': f'Bearer {login_response.json()['token']['accessToken']}'}
)

# Выполняем client запрос с авторизацией
get_user_me_response = client.get(url='/users/me')                  # Просто добавили endpoint. Всё остальное из client

#-----------------------------------------------------------------------------------------------------------------------
# Output
print(login_response.json())        # {'token': {'tokenType': 'bearer', 'accessToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmUiOiIyMDI2LTA0LTIyVDA1OjMwOjIxLjYwMDI5MyIsInVzZXJfaWQiOiI3MjFjYjg4NS0xY2E4LTQ3OTEtYjA4YS03OGMxZGNhYTFiNmIifQ.juy1nlk004FXR7GE8laKPSBpHUrMdby-A3LlWid2In8', 'refreshToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmUiOiIyMDI2LTA2LTIxVDA1OjAwOjIxLjYwMDM4MSIsInVzZXJfaWQiOiI3MjFjYjg4NS0xY2E4LTQ3OTEtYjA4YS03OGMxZGNhYTFiNmIifQ.l_qD2jztuThll-cyS1IlRwiMeRIs8QNt4WOQok5EZFE'}}
print(get_user_me_response.json())  # {'user': {'id': '721cb885-1ca8-4791-b08a-78c1dcaa1b6b', 'email': 'user@example.com', 'lastName': 'string', 'firstName': 'string', 'middleName': 'string'}}
#-----------------------------------------------------------------------------------------------------------------------
