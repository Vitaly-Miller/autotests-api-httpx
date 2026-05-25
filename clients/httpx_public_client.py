"""
Public httpx.Client builder
(Для методов, НЕ требующих авторизации)
"""
import httpx

#============================================= httpx.Client Builder (Public)  ===========================================
BASE_URL = 'http://localhost:8000/api/v1'

def get_httpx_public_client() -> httpx.Client:
    """
    Функия создает экземпляр httpx.Client (с Base URL)

    :return: httpx.Client (с Base URL)
    """
    public_httpx_client = httpx.Client(base_url=BASE_URL)        # Создаём экземпляр httpx.Client с Base URL
    return public_httpx_client

#-----------------------------------------------------------------------------------------------------------------------
