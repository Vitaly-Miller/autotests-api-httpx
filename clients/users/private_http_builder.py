"""
🔒Private http Builder
(Для методов, требующих авторизации)
"""
from httpx import Client
from clients.auth.auth_client import get_auth_client
from clients.auth.auth_schema import LoginRequestSchema, AuthUserSchema

#=======================================================================================================================
#--------------------------------------------------- http Builder ------------------------------------------------------
BASE_URL = 'http://localhost:8000/api/v1'

def get_private_http_client(user: AuthUserSchema) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    auth_client = get_auth_client()                                                      # Инициализируем AuthenticationClient для аутентификации
    login_request = LoginRequestSchema(email=user.email, password=user.password)         # Инициализируем запрос на аутентификацию
    login_response = auth_client.login(login_request)                                    # Выполняем POST запрос и аутентифицируемся
    auth_headers = {'Authorization': f'Bearer {login_response["token"]["accessToken"]}'} # Вытаскиваем токен из ответа

    return Client(base_url=BASE_URL, headers=auth_headers)
