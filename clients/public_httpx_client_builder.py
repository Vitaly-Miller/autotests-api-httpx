"""
Public httpx.Client builder
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

#============================================= Public httpx.Client (builder) ===========================================
@allure.step('◉ Get Public httpx.Client')           # Allure step title
def get_public_httpx_client() -> httpx.Client:
    """
    Функия создает настроенный экземпляр httpx.Client

    :return: httpx.Client (настроенный)
    """
    public_httpx_client = httpx.Client(             # Создаём экземпляр httpx.Client() с передачей:
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
    return public_httpx_client                      # httpx.Client (настроенный)

#-----------------------------------------------------------------------------------------------------------------------
