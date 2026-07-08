"""
httpx.Client (Public) builder
(Для методов, НЕ требующих авторизации)
"""
import httpx
import allure
from config import settings
from tools.event_hooks.event_hooks import (
    log_request_event_hook,
    log_response_event_hook,
    api_report_event_hook,
    curl_command_event_hook
)

#============================================ httpx.Client (Public) builder ============================================
@allure.step('◉ Get httpx.Client (Public)')           # Allure step title
def get_httpx_client_public() -> httpx.Client:
    """
    Функия создает настроенный экземпляр httpx.Client (Public)

    :return: Настроенный httpx.Client (Public)
    """
    httpx_client_public = httpx.Client(             # Создаём экземпляр httpx.Client() с передачей:
        base_url=settings.httpx_client.base_url,    # Base URL (from .env)
        timeout=settings.httpx_client.timeout,      # Timeout  (from .env)
        event_hooks={                               # Event hooks:
            'request': [                            #  Before Request:
                log_request_event_hook              #  - Logging Request  (optional)
            ],
            'response': [                           #  After Response:
                api_report_event_hook,              #  - API-reports
                curl_command_event_hook,            #  - cURL-command
                log_response_event_hook             #  - Logging Response  (optional)
            ]
        }
    )
    return httpx_client_public                      # httpx.Client (настроенный)

#-----------------------------------------------------------------------------------------------------------------------
