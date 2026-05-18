"""
Test Get User Me 1
(Фикстура create_user + manual)
"""
import pytest
from clients.auth.auth_schema import AuthUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.users_schema import UserFullSchema
from tools.assertions.users_assert import assert_user_data_fields
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.regression
@pytest.mark.users
def test_get_user_me(create_user: UserFullSchema):            # Передача фикстуры СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ
    auth_data = create_user.auth_data                         # Вытаскиваем авторизационные данные через .свойство UserFullSchema
    get_user_me_client = get_private_users_client(auth_data)  # Получаем экземпляр PrivateUsersClient c уже настроенным HTTP-клиентом с Base URL и авторизированным пользователем
    response = get_user_me_client.get_user_me_api()           # 🟩Get-запрос на получение данных ТЕКУЩЕГО пользователя через .метод

    #---------------------------------------------------- Assertions ---------------------------------------------------



#=======================================================================================================================
    Tool.api_report(response)
