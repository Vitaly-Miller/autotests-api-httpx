"""
http.Client Builder (Public/Private)

⚠️Вызывает конфликт импортов. ДОПИЛИТЬ!
"""
import httpx
from clients.auth.auth_schema import AuthUserSchema, LoginRequestSchema

#------------------------------------------ http.Client Builder (Public/Private) ---------------------------------------
BASE_URL = 'http://localhost:8000/api/v1'

def get_http_client(auth_data: AuthUserSchema = None) -> httpx.Client:
    """
    Универсальная функция создаёт экземпляр httpx.Client (Public/Private):

    🔒PRIVATE - Если auth_data передан. (Для методов, требующих авторизации)
    PUBLIC - Если auth_data НЕ передан. (Для методов, НЕ требующих авторизации)

    :param auth_data: Данные для аутентификации пользователя (Email, Password) в формате Pydantic-model
    :return: 🔒PRIVATE httpx.Client с установленным заголовком Authorization
    :return: PUBLIC httpx.Client
    """
    if auth_data:
        from clients.auth.auth_client import get_auth_client      # ⚠️КОСТЫЛЬ - иначе конфликт импортов
        auth_client = get_auth_client()                           # Инициализируем AuthenticationClient для аутентификации
        login_payload = LoginRequestSchema(                       # Инициализируем payload для аутентификации
            email=auth_data.email,
            password=auth_data.password)
        login_response = auth_client.login(payload=login_payload) # ▶︎ POST запрос и аутентифицируемся
        #token = login_response["token"]["accessToken"]           # ⚠ Обращение по [] индексу   - Для JSON-ответа без валидации      (Вытаскиваем токен из отела ответа)
        token = login_response.token.access_token                 # ⚠ Обращение через .атрибут  - Для валидированной Pydantic-Model  (Вытаскиваем токен из отела ответа)
        auth_headers = {'Authorization': f'Bearer {token}'}       # Сформируем заголовок для аутентификации
        return httpx.Client(base_url=BASE_URL, headers=auth_headers)    # 🔒PRIVATE - Если auth_data передан
    return httpx.Client(base_url=BASE_URL)                              # PUBLIC - Если auth_data НЕ передан
