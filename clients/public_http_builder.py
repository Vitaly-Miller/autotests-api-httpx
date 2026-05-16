"""
PUBLIC http.Client Builder
(Для методов, НЕ требующих авторизации)
"""
import httpx

#=======================================================================================================================
#----------------------------------------------- http.Client Builder (Public) -------------------------------------------------
BASE_URL = 'http://localhost:8000/api/v1'

def get_public_http_client() -> httpx.Client:
    """
    Функия создает экземпляр httpx.Client с Base URL.

    :return: Готовый к использованию объект httpx.Client с Base URL
    """
    return httpx.Client(base_url=BASE_URL)
