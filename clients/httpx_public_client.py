"""
Public httpx.Client builder
(Для методов, НЕ требующих авторизации)
"""
import httpx
import allure

#============================================= Public httpx.Client (Builder) ===========================================
BASE_URL = 'http://localhost:8000/api/v1'

@allure.step('Get Public httpx.Client')
def get_httpx_public_client() -> httpx.Client:
    """
    Функия создает экземпляр httpx.Client (с Base URL)

    :return: httpx.Client (с Base URL)
    """
    public_httpx_client = httpx.Client(base_url=BASE_URL)       # Создаём экземпляр httpx.Client() с передачей Base URL
    return public_httpx_client                                  # httpx.Client (с Base URL)

#-----------------------------------------------------------------------------------------------------------------------
