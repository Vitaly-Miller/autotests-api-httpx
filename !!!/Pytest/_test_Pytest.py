"""
Pytest info

"""

#===================================================== >_Terminal ========================================================
"""
python -m pytest -v -s -k create_user 

-- Запуск ВСЕХ тестов --
python -m pytest                - запуск всех тестов
python -m pytest -v             - запуск всех тестов с подробным выводом
python -m pytest -vv            - запуск всех тестов с Очень подробным выводом
python -m pytest -s             - запуск всех тестов с выводом print
python -m pytest -v -s          - 👍 запуск всех тестов с подробным выводом + выводом print
...

-- По названию --
pytest tests/test_users.py::test_create_user     - запуск конкретного теста
pytest tests/test_users.py::TestUserAuth         - запуск конкретного тестового класса (TestUserAuth)

-- По названию, содержащему ... --
python -m pytest -k create_user                            - запуск тестов, содержащих "*create_user*"
python -m pytest -k TestUserAuth                           - запуск тестов, содержащихся в классе "TestUserAuth"

-- По названию, содержащему ... c логическими операторами --
python -m pytest -k create and user                        - запуск тестов, содержащих "*create*" И "*user*"
python -m pytest -k create or user                         - запуск тестов, содержащих "*create*" ИЛИ "*user*"
python -m pytest -k create and not user                    - запуск тестов, содержащих "*create*" и НЕТ "*user*"

-- По маркерам ---
python -m pytest -m smoke
python -m pytest -m "smoke and not regression"

-- По маркерам ▷ PyCharm --- 👍
Добавить конфигурацию запуска -> + -> pytest -> Переименовать название -> Поле <Дополнительные аргументы>: -m smoke


-- Контроль падений ---
python -m pytest -x                        - Остановиться на первой ошибке
python -m pytest --maxfail=3               - Максимум падений

python -m pytest --tb=short                - Короткий traceback
python -m pytest --tb=long                 - Полный traceback

...
python -m python -m pytest -h              - info (help)
"""

#======================================================= Структура =====================================================
# Тест
def test_user_login_pydantic():
    pass

# Тестовый класс
class TestUserAuth:               # NO __init__ конструктор! Допускаются только атрибуты класса (a = 100, ...)
    def test_create_user(self):   # Тестовый .метод
        pass

    def test_update_user_pydantic(self):   # Тестовый .метод
        pass


#======================================================== Tests ========================================================
def test_hello():
    print('Hello, World!')          # pytest -s (для вывода print)

# Positive test
def test_assert_positive():
    assert 2 + 4 == 6               # ✅Pass

# Negative test
def test_assert_negative():
    assert 2 + 4 == 5               # E   assert (2 + 4) == 5

# Negative test (c кастомным описанием ошибки)
def test_assert_negative_plus():
    assert 2 + 4 == 5, '❌Кастомное описание ошибки!'  # E   AssertionError: ❌Кастомное описание ошибки!
                                                       # E   assert (2 + 4) == 4
