"""
🔒Private http Builder
(Для методов, требующих авторизации)
"""
from httpx import Client
from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema, AuthenticationUserSchema

#=======================================================================================================================
#--------------------------------------------------- http Builder ------------------------------------------------------
BASE_URL = 'http://localhost:8000/api/v1'

def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    authentication_client = get_authentication_client()                                  # Инициализируем AuthenticationClient для аутентификации
    login_request = LoginRequestSchema(email=user.email, password=user.password)         # Инициализируем запрос на аутентификацию
    login_response = authentication_client.login(login_request)                          # Выполняем POST запрос и аутентифицируемся
    auth_headers = {'Authorization': f'Bearer {login_response["token"]["accessToken"]}'} # Вытаскиваем токен из ответа

    return Client(base_url=BASE_URL, headers=auth_headers)
