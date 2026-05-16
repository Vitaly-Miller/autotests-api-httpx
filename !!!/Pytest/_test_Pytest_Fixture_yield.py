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

#======================================================= yield✨========================================================
# Фикстура с yield - возвращает результат функции и продолжить выполнение этой функции
@pytest.fixture
def user_data():
    print('\n1 [ДО Теста] - Функция ✅СОЗДАНИЯ пользователя (setup)')                     # 1 [ДО Теста] - Функция ✅СОЗДАНИЯ пользователя (setup)
    yield {'username': 'john_connor', 'email': 'john_connor@email.com'}                   # 👈[Передача данных в тест] - {'username': 'john_connor', 'email': 'john_connor@email.com'}
    print('\n3 [ПОСЛЕ Теста] - Функция 🚫 УДАЛЕНИЯ пользователя после теста (teardown)')  # 3 [ПОСЛЕ Теста] - Функция 🚫 УДАЛЕНИЯ пользователя после теста (teardown)


# Тест
def test_username(user_data):                           # 1 [ДО Теста] - Функция ✅СОЗДАНИЯ пользователя (setup)
    print(user_data)                                    # {'username': 'john_connor', 'email': 'john_connor@email.com'}
    assert user_data['username'] == 'john_connor'       # PASSED
                                                        # 3 [ПОСЛЕ Теста] - Функция 🚫 УДАЛЕНИЯ пользователя после теста (teardown)

#-----------------------------------------------------------------------------------------------------------------------
