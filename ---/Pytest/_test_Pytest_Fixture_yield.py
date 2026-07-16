"""
Pytest fixture + yield✨
"""

"""
yield - возвращает результат функции и продолжить выполнение этой функции

@pytest.fixture
def my_func():
    my_func_action    # 1-Выполнение логики функции [Create user]
    yield             # 2-Возврат результата        [Передача user data]
    other_action      # 3-Действия ПОСЛЕ возврата   [Delete user]

"""

import pytest

#======================================================= yield ✨=======================================================
# Фикстура с yield - возвращает результат функции и продолжает выполнение после yield
@pytest.fixture
def user_data():
    print('\n[ДО Теста] - ✅ СОЗДАНИЕ пользователя (setup)')              # [ДО Теста]    - логика
    yield {'username': 'john_connor', 'email': 'john_connor@email.com'}   # [Передача данных в тест]
    print('[ПОСЛЕ Теста] - 🚫 УДАЛЕНИЯ пользователя (teardown)')          # [ПОСЛЕ Теста] - логика


# Тест
def test_username(user_data):                           # Выполняется фикстура:  [ДО Теста]    - ✅ СОЗДАНИЕ пользователя (setup)
    print(user_data)                                    # {'username': 'john_connor', 'email': 'john_connor@email.com'}
    assert user_data['username'] == 'john_connor'       # PASSED
                                                        # Выполняется фикстура:  [ПОСЛЕ Теста] - 🚫 УДАЛЕНИЯ пользователя (teardown)

#-----------------------------------------------------------------------------------------------------------------------
