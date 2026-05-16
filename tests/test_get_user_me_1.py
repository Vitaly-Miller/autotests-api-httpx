"""
Test Get User Me
(Фикстура get_user_me)
"""
import pytest
from clients.auth.auth_schema import AuthUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.users_schema import UserFullSchema
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.smoke
@pytest.mark.users
def test_get_user_me(create_user: UserFullSchema):   # Передача фикстуры СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ
    #------------------------------------------------ 1.Pre-conditions -------------------------------------------------
    # Авторизационные данные созданного пользователя:
    auth_data = AuthUserSchema(                      # Инициализируем данные для авторизации через схему. Сохраняем в переменную Email и Pass
        email=create_user.email,                     # Вытаскиваем .Email из модели
        password=create_user.password)               # Вытаскиваем .Password из модели

    #------------------------------------------------- 2. Get User Me --------------------------------------------------
    get_user_me_client = get_private_users_client(auth_data)  # Получаем экземпляр PrivateUsersClient c уже настроенным HTTP-клиентом с Base URL
    response = get_user_me_client.get_user_me_api()           # 🟩Get-запрос на получение данных ТЕКУЩЕГО пользователя

    #---------------------------------------------------- Assertions ---------------------------------------------------



#=======================================================================================================================
    Tool.api_report(response)
