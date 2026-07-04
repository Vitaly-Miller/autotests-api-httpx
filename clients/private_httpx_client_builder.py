"""
🔒Private httpx.Client builder
(Для методов, требующих авторизации)
"""
import allure
import httpx
from clients.auth_client import get_auth_client
from schemas.auth_schema import AuthDataSchema
from tools.event_hooks import curl_command, api_request_body
from functools import lru_cache



#============================================== Private httpx.Client (Private) =========================================
BASE_URL = 'http://localhost:8000/api/v1'

#@lru_cache()                                                             # Кэшируем (требуется frozen=True для Schema)
@allure.step('Get Private httpx.Client')                                  # Allure step title
def get_private_httpx_client(auth_data: AuthDataSchema) -> httpx.Client:  # Принимает данные для аутентификации (Email и Password)
    """
    Функция создаёт экземпляр httpx.Client (с Base URL + Token + Event hooks)

    :param auth_data: Pydantic-model с данными для аутентификации (Email и Password)
    :return: httpx.Client (с Base URL + Token + Event hooks)
    """
    auth_client = get_auth_client()                                       # Получаем экземпляр AuthClient
    response = auth_client.login_pydantic(auth_data=auth_data)            # ▶ Запрос на аутентификацию через Pydantic-метод
    headers = {'Authorization': f'Bearer {response.token.access_token}'}  # Формируем заголовок c токеном
    private_httpx_client = httpx.Client(                                  # Создаём экземпляр httpx.Client() с передачей:...
        base_url=BASE_URL,                                                # ...Base URL
        headers=headers,                                                  # ...Headers c Token
        event_hooks={                               # Event hooks:
            'request': [                            # ...for Request:
                curl_command,                       # - сURL command (TEXT) - callback
                api_request_body                    # - API Request body (JSON) - callback
            ]
        }
    )
    return private_httpx_client                                           # httpx.Client (с Base URL + Token + Event hooks)

#-----------------------------------------------------------------------------------------------------------------------
