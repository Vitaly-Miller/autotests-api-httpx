"""
Pytest fixture
"""


import pytest



#=======================================================================================================================
"""
Область применения фикстуры:
----------------------------
@pytest.fixture(scope='...')

Выполнить ОДИН раз на каждый(ую):
'function' - Тест-функцию          (Default)
'class'    - Класс
'module'   - Файл
'session'  - Сессию (все тесты запуска)
'package'  - на Директорию с тестами (пакет с __init__.py)

-----------------------------
@pytest.fixture(autouse=True) -> ✨Не требуется передача в тесте. Добавляется АВТОМАТИЧЕСКИ.
autouse=True                  - Для каждого Теста.  
autouse=True, scope='class'   - Для каждого Класса.
autouse=True, scope='class'   - Для каждой Сессии (все тесты запуска).
...
"""
#============================================== файл conftest.py =======================================================
#--------------------------------------- Функции-фикстуры со своей логикой ---------------------------------------------
@pytest.fixture(scope='session')    # Вызывается один раз на ВСЮ СЕССИЮ
def settings():
    print('[SESSION] Один раз на ВСЮ СЕССИЮ')

@pytest.fixture(scope='class')      # Вызывается один раз на КАЖДЫЙ КЛАСС
def user():
    print('[CLASS] Один раз на каждый тестовый КЛАСС')

@pytest.fixture(scope='function')   # Вызывается один раз на КАЖДЫЙ ТЕСТ
def client():
    print('[FUNCTION] Один раз на каждый Тест')


@pytest.fixture(autouse=True)       # Вызывается один раз на КАЖДЫЙ ТЕСТ - ✨Добавляется АВТОМАТИЧЕСКИ в каждый тест!
def send_report():
    print('[AUTOUSE]  Один раз на каждый Тест (АВТО) -> Отчет отправлен!')

#------------------------------------------------------ Tests ----------------------------------------------------------
# Передаем фикстуры в тесты
class TestClass1:
    def test_1(self, settings, user, client):   # [SESSION]  Один раз на ВСЮ СЕССИЮ
        ...                                     # [CLASS]    Один раз на каждый тестовый КЛАСС
                                                # [AUTOUSE]  Один раз на каждый Тест (АВТО) -> Отчет отправлен!
                                                # [FUNCTION] Один раз на каждый Тест
                                                # ✔️PASSED

    def test_2(self, settings, user, client):   # [AUTOUSE]  Один раз на каждый Тест (АВТО) -> Отчет отправлен!
        ...                                     # [FUNCTION] Один раз на каждый Тест
                                                # ✔️PASSED



class TestClass2:
    def test_3(self, settings, user, client):   # [CLASS]    Один раз на каждый тестовый КЛАСС
        ...                                     # [AUTOUSE]  Один раз на каждый Тест (АВТО) -> Отчет отправлен!
                                                # [FUNCTION] Один раз на каждый Тест
                                                # ✔️PASSED


#-----------------------------------------------------------------------------------------------------------------------
@pytest.fixture
def user_data() -> dict:
    return {'username': 'john_connor', 'email': 'john_connor@email.com'}


def test_username(user_data):
    print(user_data)
    assert user_data['username'] == 'john_connor'

def test_user_email(user_data):
    print(user_data)
    assert user_data['email'] == 'john_connor@email.com'
