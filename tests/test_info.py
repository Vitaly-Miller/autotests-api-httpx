"""
Pytest info

"""

#===================================================== Terminal ========================================================
"""

-- Запуск ВСЕХ тестов --
pytest                - запуск всех тестов
pytest -v             - запуск всех тестов с подробным выводом
pytest -vv            - запуск всех тестов с Очень подробным выводом
pytest -s             - запуск всех тестов с выводом print
pytest -v -s          - 👍 запуск всех тестов с подробным выводом + выводом print

(⚠️без .venv)
python -m pytest      - запуск всех тестов
...

-- По названию --
pytest tests/test_users.py::test_create_user     - запуск конкретного теста
pytest tests/test_users.py::TestUserAuth         - запуск конкретного тестового класса (TestUserAuth)

-- По названию, содержащему ... --
pytest -k create_user                            - запуск тестов, содержащих "*create_user*"
pytest -k TestUserAuth                           - запуск тестов, содержащихся в классе "TestUserAuth"

-- По названию, содержащему ... c логическими операторами --
pytest -k create and user                        - запуск тестов, содержащих "*create*" И "*user*"
pytest -k create or user                         - запуск тестов, содержащих "*create*" ИЛИ "*user*"
pytest -k create and not user                    - запуск тестов, содержащих "*create*" и НЕТ "*user*"

-- По маркерам ---
pytest -m smoke
pytest -m "smoke and not regression"

-- Контроль падений ---
pytest -x                        - Остановиться на первой ошибке
pytest --maxfail=3               - Максимум падений

pytest --tb=short                - Короткий traceback
pytest --tb=long                 - Полный traceback

...
python -m pytest -h            - info (help)
"""

#======================================================= Структура =====================================================
# Тест
def test_user_login():
    pass

# Тестовый класс
class TestUserAuth:               # NO __init__ конструктор! Допускаются только атрибуты класса (a = 100, ...)
    def test_create_user(self):   # Тестовый .метод
        pass

    def test_update_user(self):   # Тестовый .метод
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
