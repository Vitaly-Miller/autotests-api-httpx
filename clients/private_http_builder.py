"""
🔒PRIVATE http.Client Builder
(Для методов, требующих авторизации)
"""
import httpx
from clients.auth.auth_client import get_auth_client
from clients.auth.auth_schema import AuthUserSchema

#=======================================================================================================================
#------------------------------------------------ http.Client (Private) -----------------------------------------------
BASE_URL = 'http://localhost:8000/api/v1'

def get_private_http_client(auth_data: AuthUserSchema) -> httpx.Client:
    """
    Функция создаёт экземпляр httpx.Client с авторизированным (залогиненным) пользователем

    :param auth_data: Данные для аутентификации (Email, Password) в формате Pydantic-model
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization
    """
    auth_client = get_auth_client()                           # Инициализируем AuthClient для аутентификации
    auth_data = AuthUserSchema(                               # Инициализируем auth_data для аутентификации
        email=auth_data.email,
        password=auth_data.password)
    login_response = auth_client.login(auth_data=auth_data)   # 🟨POST-запрос на аутентификацию (login) -> LoginResponseSchema  (Pydantic-Model)
    #token = login_response["token"]["accessToken"]           # ⚠ Обращение по [] индексу   - Для JSON-ответа без валидации      (Вытаскиваем токен из отела ответа)
    token = login_response.token.access_token                 # ⚠ Обращение через .атрибут  - Для валидированной Pydantic-Model  (Вытаскиваем токен из отела ответа)
    auth_headers = {'Authorization': f'Bearer {token}'}       # Сформируем заголовок для аутентификации
    return httpx.Client(base_url=BASE_URL, headers=auth_headers)

#-----------------------------------------------------------------------------------------------------------------------
