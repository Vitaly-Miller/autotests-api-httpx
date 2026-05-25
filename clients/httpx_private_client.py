"""
🔒PRIVATE httpx.Client Builder
(Для методов, требующих авторизации)
"""
import httpx
from clients.auth_client import get_auth_client
from schemas.auth import AuthUserSchema

#================================================ httpx.Client (Private) ================================================
BASE_URL = 'http://localhost:8000/api/v1'

def get_private_httpx_client(auth_data: AuthUserSchema) -> httpx.Client:
    """
    Функция создаёт экземпляр httpx.Client (с Авторизацией)

    :param auth_data: Pydantic-model с данными для аутентификации
    :return: httpx.Client (с Авторизацией)
    """
    auth_client = get_auth_client()                          # Экземпляр AuthClient
    auth_data = AuthUserSchema(                              # Инициализируем Pydantic-model c данными для аутентификации
        email=auth_data.email,                               # Используем email из переданной Pydantic-model (auth_data)
        password=auth_data.password                          # Используем password из переданной Pydantic-model (auth_data)
    )
    auth_response = auth_client.login(auth_data=auth_data)   # ▶ Запрос на аутентификацию через Pydantic-метод
    #token = auth_response["token"]["accessToken"]           # Вытаскиваем токен из тела JSON-ответа аутентификации      - ⚠ Обращение по [] индексу
    token = auth_response.token.access_token                 # Вытаскиваем токен из тела Pydantic-ответа аутентификации  - ⚠ Обращение по .атрибуту
    access_token = {'Authorization': f'Bearer {token}'}      # Формируем заголовок c токеном
    private_httpx_client = httpx.Client(base_url=BASE_URL, headers=access_token) # Создаём экземпляр httpx.Client с авторизацией
    return private_httpx_client
#-----------------------------------------------------------------------------------------------------------------------
