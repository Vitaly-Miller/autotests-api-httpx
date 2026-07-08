"""
🔒Private httpx.Client builder
(Для методов, требующих авторизации)
"""
import allure
import httpx
from config import settings
from clients.auth_client import get_auth_client
from schemas.auth_schema import AuthDataSchema
from tools.event_hooks.event_hooks import (
    log_request_event_hook,
    log_response_event_hook,
    api_report_event_hook,
    curl_command_event_hook
)

#============================================== Private httpx.Client (builder) =========================================
#@lru_cache()                                                             # Кэшируем (требуется frozen=True для Schema)
@allure.step('◉ Get Private httpx.Client')                                # Allure step title
def get_private_httpx_client(auth_data: AuthDataSchema) -> httpx.Client:  # Принимает данные для аутентификации (Email и Password)
    """
    Функция создаёт настроенный экземпляр httpx.Client

    :param auth_data: Pydantic-model с данными для аутентификации (Email и Password)
    :return: httpx.Client (настроенный)
    """
    auth_client = get_auth_client()                                       # Получаем экземпляр AuthClient
    response = auth_client.login_pydantic(auth_data=auth_data)            # ▶ Запрос на аутентификацию через Pydantic-метод
    headers = {'Authorization': f'Bearer {response.token.access_token}'}  # Формируем заголовок c Bearer-токеном
    private_httpx_client = httpx.Client(                                  # Создаём экземпляр httpx.Client() с передачей:...
        base_url=settings.httpx_client.base_url,                          # Base URL (from .env)
        timeout=settings.httpx_client.timeout,                            # Timeout  (from .env)
        headers=headers,                                                  # Headers c Token
        event_hooks={                                                     # Event hooks:
            'request': [                                                  #  Before Request:
                log_request_event_hook                                    #  - Logging Request  (optional)
            ],
            'response': [                                                 #  After Response:
                api_report_event_hook,                                    #  - API-reports  - callback function
                curl_command_event_hook,                                  #  - cURL-command - callback function
                log_response_event_hook                                   #  - Logging Response  (optional)
            ]
        }
    )
    return private_httpx_client                                           # httpx.Client (настроенный)

#-----------------------------------------------------------------------------------------------------------------------
