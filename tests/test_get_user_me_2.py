"""
Test Get User Me 1
(Фикстура <create_user> + Manual)
"""
from urllib import response

import httpx
import pytest
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.smoke
@pytest.mark.users
def test_get_user_me(get_user_me: httpx.Response):   # Передача фикстуры get_user_me

    response = get_user_me                           # Сохраняем ответ в переменную
    #---------------------------------------------------- Assertions ---------------------------------------------------



#=======================================================================================================================
    Tool.api_report(response)
