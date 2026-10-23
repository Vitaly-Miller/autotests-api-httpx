"""
Allure autouse-fixture
"""

import pytest
from tools.allure.environment import create_allure_environment_file

#=======================================================================================================================
@pytest.fixture(scope='session', autouse=True)   # Runs automatically once per test session
def save_allure_environment_file():
    """
    Autouse fixture that creates the <environment.properties> file in the <allure-results> folder

    :return:
    """
    # Do nothing before the tests start
    yield                                        # Tests run...
    create_allure_environment_file()             # After tests finish, create the environment.properties file


#=======================================================================================================================
