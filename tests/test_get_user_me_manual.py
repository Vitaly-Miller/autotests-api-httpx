"""
Test Get User Me
"""
import pytest
from clients.auth.auth_schema import AuthUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.smoke
@pytest.mark.users
def test_get_user_me():  # Передача фикстур СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ и АВТОРИЗАЦИИ
    #---------------------------------------------- Pre-conditions -----------------------------------------------------
    # 1. Create User (Создаем пользователя)
    public_users_client = get_public_users_client()          # Получаем экземпляр PublicUsersClient c уже настроенным HTTP-клиентом с Base URL
    create_user_payload = CreateUserRequestSchema()          # Инициализируем-генерируем данные для создания пользователя через схему
    public_users_client.create_user(payload=create_user_payload) # 🟨Post-запрос на создание пользователя

    auth_data = AuthUserSchema(                              # Инициализируем данные для авторизации через схему. Сохраняем в переменную Email и Pass
        email=create_user_payload.email,                     # Вытаскиваем .Email из модели
        password=create_user_payload.password)               # Вытаскиваем .Password из модели


    # 2. Login (НЕ НУЖЕН. АВТОРИЗИРУЕТСЯ ДАЛЕЕ В ОСНОВНОМ ЗАПРОСЕ)

    # ------------------------------------------------------------------------------------------------------------------
    # 3. Get User Me
    get_user_me_client = get_private_users_client(auth_data) # Получаем экземпляр PrivateUsersClient c уже настроенным HTTP-клиентом с Base URL
    response = get_user_me_client.get_user_me_api()          # 🟩Get-запрос на получение данных ТЕКУЩЕГО пользователя

    #---------------------------------------------------- Assertions ---------------------------------------------------



#=======================================================================================================================
    Tool.api_report(response)
