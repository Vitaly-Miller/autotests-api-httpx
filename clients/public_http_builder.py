"""
PUBLIC http Builder
(Для методов, НЕ требующих авторизации)
"""
from httpx import Client

#=======================================================================================================================
#----------------------------------------------- http Builder (Public) -------------------------------------------------
BASE_URL = 'http://localhost:8000/api/v1'

def get_public_http_client() -> Client:
    """
    Функия создает экземпляр httpx.Client с базовыми настройками.

    :return: Готовый к использованию объект httpx.Client.
    """
    return Client(base_url=BASE_URL)
