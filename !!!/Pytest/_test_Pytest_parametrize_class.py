"""
Parameterize Test Class
"""
import pytest


#================================= Parametrize class method (Дублирование - НЕ УДОБНО!) ================================
class TestClass1:
    # Hi
    @pytest.mark.parametrize('user', ['User 1', 'User 2'])  # 👈
    def test_hi(self, user: str):                           # передаем параметр (по очереди)
        print(f'Hi, {user}!')                               # [User 1] PASSED   Hi, User 1!
                                                            # [User 2] PASSED   Hi, User 2!
    # Hello
    @pytest.mark.parametrize('user', ['User 1', 'User 2'])  # 👈
    def test_hello(self,user: str):                         # передаем параметр (по очереди)
        print(f'Hello, {user}!')                            # [User 1] PASSED   Hello, User 1!
                                                            # [User 2] PASSED   Hello, User 2!



#================================================= Parametrize Class ===================================================
@pytest.mark.parametrize('user', ['User 1', 'User 2'])  # 👈
class TestClass2:
    # Hi
    def test_hi(self, user: str):                           # передаем класс-параметр (по очереди)
        print(f'Hi, {user}!')                               # [User 1] PASSED   Hi, User 1!
                                                            # [User 2] PASSED   Hi, User 2!
    # Hello
    def test_hello(self,user: str):                         # передаем класс-параметр (по очереди)
        print(f'Hello, {user}!')                            # [User 1] PASSED   Hello, User 1!
                                                            # [User 2] PASSED   Hello, User 2!

#=======================================================================================================================
