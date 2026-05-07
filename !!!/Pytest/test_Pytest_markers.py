"""
Pytest markers
"""
import pytest

"""
---- >_terminal ----
python -m pytest -v -s -m smoke                        - запустить Smoke тесты
python -m pytest -v -s -m regression                   - запустить Regression тесты
python -m pytest -v -s -m "smoke or regression"        - запустить тесты, промаркированные Smoke ИЛИ Regression
python -m pytest -v -s -m "smoke and regression"       - запустить тесты, ОДНОВРЕМЕННО промаркированные Smoke И Regression
python -m pytest -v -s -m "regression and not slow"    - запустить Regression тесты, ИСКЛЮЧАЯ Slow тесты

---- ▷ PyCharm ----
Добавить конфигурацию запуска -> + -> pytest -> Переименовать название -> Поле <Дополнительные аргументы>: -m smoke


❗️Кастомные названия маркеров .smoke, .regression, ... -
- необходимо добавить в pytest.ini чтоб не вылезало <PytestUnknownMarkWarning ========= warnings summary ========> предупреждение.
"""
#==================================================== Маркеры тестов ===================================================
@pytest.mark.smoke                 # Маркируем тест как smoke (кастомное название)
def test_smoke_case():
    assert 1 + 1 == 2

@pytest.mark.regression            # Маркируем тест как regression (кастомное название)
def test_regression_case():
    assert 2 * 2 == 4

@pytest.mark.fast                  # ...
def test_fast():
    ...
@pytest.mark.slow                  # ...
def test_slow():
    ...

#=============================================== Маркеры тестовых классов ==============================================
@pytest.mark.smoke                # Маркировка тестового Класса применяется ко всем тестовым .методам класса
class TestSuite:
    def test_1(self):             # smoke
        ...
    def test_2(self):             # smoke
        ...
    def test_3(self):             # smoke
        ...


# Вложенность маркировки
@pytest.mark.regression           # Маркировка тестового Класса применяется ко всем тестовым .методам класса
class TestUserAuth:

    @pytest.mark.smoke            # regression and smoke
    def test_login(self):
        ...

    @pytest.mark.slow             # regression and slow
    def test_password_reset(self):
        ...

    def test_logout(self):        # regression
        ...
