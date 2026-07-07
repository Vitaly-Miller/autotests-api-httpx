"""
Public httpx.Client builder
(Для методов, НЕ требующих авторизации)
"""
import httpx
import allure
from config import settings
from tools.event_hooks.event_hooks_callback import api_report, curl_command

#============================================= Public httpx.Client (builder) ===========================================
@allure.step('◉ Get Public httpx.Client')           # Allure step title
def get_public_httpx_client() -> httpx.Client:
    """
    Функия создает настроенный экземпляр httpx.Client

    :return: httpx.Client (настроенный)
    """
    public_httpx_client = httpx.Client(             # Создаём экземпляр httpx.Client() с передачей:
        base_url=settings.httpx_client.base_url,    # - Base URL (from .env)
        timeout=settings.httpx_client.timeout,      # - Timeout  (from .env)
        event_hooks={                               # - Event hooks:...
            'response': [                           #   - After Response:
                api_report,                         #   - API-reports  - callback function
                curl_command                        #   - cURL-command - callback function
            ]
        }
    )
    return public_httpx_client                      # httpx.Client (настроенный)

#-----------------------------------------------------------------------------------------------------------------------
