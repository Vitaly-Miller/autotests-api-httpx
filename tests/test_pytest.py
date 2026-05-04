"""
Pytest info

"""

#===================================================== Terminal ========================================================
"""
python -m pytest       - запуск всех тестов
python -m pytest -v    - запуск всех тестов с подробным выводом
python -m pytest -vv   - запуск всех тестов с Очень подробным выводом
python -m pytest -s    - запуск всех тестов с выводом print
python -m pytest -v -s - запуск всех тестов с подробным выводом и выводом print

python -m pytest tests/test_users.py::test_create_user     - запуск конкретного теста
python -m pytest -k test_create_user                       - запуск тестов, содержащих test_create_user
python -m pytest tests/test_users.py::TestUsers            - запуск конкретного тестового класса

-- По маркерам ---
python -m pytest -m smoke
python -m pytest -m "smoke and not regression"

-- Контроль падений ---
python -m pytest -x            - Остановиться на первой ошибке
python -m pytest --maxfail=3   - Максимум падений

python -m pytest --tb=short    - Короткий traceback
python -m pytest --tb=long     - Полный traceback

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
#=======================================================================================================================
