"""
🔒Private httpx.Client builder
(Для методов, требующих авторизации)
"""
import httpx
from clients.auth_client import get_auth_client
from schemas.auth_schema import AuthDataSchema
from functools import lru_cache

#============================================== Private httpx.Client (Private) =========================================
BASE_URL = 'http://localhost:8000/api/v1'

#@lru_cache()  # ✨Кэшируем (требуется frozen=True для Schema)
def get_httpx_private_client(auth_data: AuthDataSchema) -> httpx.Client:
    """
    Функция создаёт экземпляр httpx.Client (с Base URL + Token)

    :param auth_data: Pydantic-model с данными для аутентификации (Email и Password)
    :return: httpx.Client (с Base URL + Token)
    """
    auth_client = get_auth_client()                     # Получаем экземпляр AuthClient
    response = auth_client.login_pydantic(auth_data=auth_data)   # ▶ Запрос на аутентификацию через Pydantic-метод
    headers = {'Authorization': f'Bearer {response.token.access_token}'}  # Формируем заголовок c токеном
    private_httpx_client = httpx.Client(                # Создаём экземпляр httpx.Client() с передачей Base URL + Token
        base_url=BASE_URL,
        headers=headers
    )
    return private_httpx_client                         # httpx.Client (с Base URL + Token)

#-----------------------------------------------------------------------------------------------------------------------
