"""
Pytest fixture (Вложенность фикстур)
"""
"""
⚠️Вложенная фикстура должна быть РАВНА или ВЫШЕ по scope
"""
import pytest

#=======================================================================================================================
@pytest.fixture
def user_data():
    return {'username': 'john_connor', 'email': 'john_connor@email.com'}

@pytest.fixture
def user_email(user_data):            # 👈ВЛОЖЕННАЯ фикстура в фикстуру
    return user_data['email']         # john_connor@email.com


#------------------------------------------------------- Test ----------------------------------------------------------
def test_1(user_email):                              # Передаем фикстуру в тест
    assert user_email == 'john_connor@email.com'     # PASSED

#-----------------------------------------------------------------------------------------------------------------------
