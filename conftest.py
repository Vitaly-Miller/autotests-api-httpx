"""
conftest.py
"""
"""
Используется pytest_plugins
Все фикстуры - в отдельных модулях-файлах
"""
from pathlib import Path            # for <Auto Plugins path>

#================================================ Plugins path (Manual) ================================================
# Ручной путь к plugins (модулям-файлам с фикстурами) ⚠ БЕЗ расширения .py
pytest_plugins = (
    'fixtures.public_users_fixtures',
    'fixtures.private_users_fixtures',
    'fixtures.auth_fixtures',
    'fixtures.files_fixtures',
    'fixtures.courses_fixtures',
    'fixtures.exercises_fixtures',
)

#================================================ Plugins path (✨Auto) ================================================
# Автоматически подключает все модули-файлы из папки fixtures/ (кроме __init__.py)
# pytest_plugins = [
#     f'fixtures.{file.stem}'
#     for file in Path(__file__).parent.glob('fixtures/*.py')
#     if file.name != '__init__.py'
# ]
#=======================================================================================================================
