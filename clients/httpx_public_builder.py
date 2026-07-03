"""
Public httpx.Client builder
(Для методов, НЕ требующих авторизации)
"""
import httpx
import allure
from tools.event_hooks import curl_event_hook

#============================================= Public httpx.Client (Builder) ===========================================
BASE_URL = 'http://localhost:8000/api/v1'

@allure.step('Get Public httpx.Client')
def get_httpx_public_client() -> httpx.Client:
    """
    Функия создает экземпляр httpx.Client (с Base URL)

    :return: httpx.Client (с Base URL)
    """
    public_httpx_client = httpx.Client(             # Создаём экземпляр httpx.Client() с передачей Base URL
        base_url=BASE_URL,
        event_hooks={'request': [curl_event_hook]}  # Event hook (cURL command generator)
    )
    return public_httpx_client                      # httpx.Client (с Base URL)

#-----------------------------------------------------------------------------------------------------------------------
