"""
Allure autouse-fixture
"""

import pytest
from tools.allure.environment import create_allure_environment_file

#=======================================================================================================================
@pytest.fixture(scope='session', autouse=True)   # Автоматически запускается на каждую тестовую сессию
def save_allure_environment_file():
    """
    Autouse-фикстура создает файл <environment.properties> в папке <allure-results>

    :return:
    """
    # До начала автотестов ничего не делаем
    yield                                        # Запускаются тесты...
    create_allure_environment_file()             # После завершения тестов создаем файл environment.properties


#=======================================================================================================================
