"""
🔒PRIVATE http Builder
(Для методов, требующих авторизации)
"""
from httpx import Client
from clients.auth.auth_client import get_auth_client
from clients.auth.auth_schema import LoginRequestSchema, AuthUserSchema

#=======================================================================================================================
#------------------------------------------------ http Builder (Private) -----------------------------------------------
BASE_URL = 'http://localhost:8000/api/v1'

def get_private_http_client(auth_data: AuthUserSchema) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param auth_data: Данные для аутентификации пользователя (Email, Password).
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    auth_client = get_auth_client()                          # Инициализируем AuthenticationClient для аутентификации
    login_request = LoginRequestSchema(                      # Инициализируем запрос на аутентификацию
        email=auth_data.email,
        password=auth_data.password)
    login_response = auth_client.login(login_request)        # Выполняем POST запрос и аутентифицируемся
    #token = login_response["token"]["accessToken"]          # ⚠ Обращение по [] индексу   - Для JSON-ответа без валидации      (Вытаскиваем токен из отела ответа)
    token = login_response.token.access_token                # ⚠ Обращение через .атрибут  - Для валидированной Pydantic-Model  (Вытаскиваем токен из отела ответа)
    auth_headers = {'Authorization': f'Bearer {token}'}      # Сформируем заголовок для аутентификации
    return Client(
        base_url=BASE_URL,
        headers=auth_headers)

#-----------------------------------------------------------------------------------------------------------------------
