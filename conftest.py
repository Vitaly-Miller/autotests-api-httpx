"""
conftest.py (via Pytest Plugins)
"""
"""
Используется pytest_plugins - dсе фикстуры в отдельных модулях-файлах
"""
from pathlib import Path            # for <Auto Plugins path>

#================================================ Plugins path (Manual) ================================================
# Ручной путь к plugins (модулям-файлам с фикстурами) ⚠ БЕЗ расширения .py
pytest_plugins = (
    'fixtures.users_public_fixtures',     # ┐
    'fixtures.users_private_fixtures',    # │
    'fixtures.auth_fixtures',             # │ Client's
    'fixtures.files_fixtures',            # │ fixtures
    'fixtures.courses_fixtures',          # │
    'fixtures.exercises_fixtures',        # ┘

    'fixtures.allure_fixtures'            # Allure's fixture
)

#================================================ Plugins path (✨Auto) ================================================
# Автоматически подключает все модули-файлы из папки fixtures/ (кроме __init__.py)
# pytest_plugins = [
#     f'fixtures.{file.stem}'
#     for file in Path(__file__).parent.glob('fixtures/*.py')
#     if file.name != '__init__.py'
# ]
#=======================================================================================================================
