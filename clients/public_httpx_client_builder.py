"""
Public httpx.Client builder
(Для методов, НЕ требующих авторизации)
"""
import httpx
import allure
from tools.event_hooks import curl_command, api_request_body

#============================================= Public httpx.Client (Builder) ===========================================
BASE_URL = 'http://localhost:8000/api/v1'

@allure.step('Get Public httpx.Client')             # Allure step title
def get_public_httpx_client() -> httpx.Client:
    """
    Функия создает экземпляр httpx.Client (с Base URL)

    :return: httpx.Client (с Base URL)
    """
    public_httpx_client = httpx.Client(             # Создаём экземпляр httpx.Client() с передачей:
        base_url=BASE_URL,                          # Base URL
        event_hooks={                               # Event hooks:
            'request': [                            # ...for Request:
                curl_command,                       # - сURL command (TEXT) - callback
                api_request_body                    # - API Request body (JSON) - callback
            ]
        }
    )
    return public_httpx_client                      # httpx.Client (с Base URL + Event hooks)

#-----------------------------------------------------------------------------------------------------------------------
