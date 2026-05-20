"""
conftest.py
(pytest_plugins)
"""
from pathlib import Path            # for <Auto Plugins path>

#================================================ Plugins path (Manual) ================================================
# Ручной путь к plugins (модули-файлы с фикстурами) ⚠ БЕЗ расширения .py
pytest_plugins = (
    'fixtures.public_users',
    'fixtures.private_users',
    'fixtures.auth',
    'fixtures.files',
    'fixtures.courses',
    'fixtures.exercises',
)



#================================================ Plugins path (✨Auto) ================================================
# Автоматически подключает все модули-файлы из папки fixtures/ (кроме __init__.py)
# pytest_plugins = [
#     f'fixtures.{f.stem}'
#     for f in Path(__file__).parent.glob('fixtures/*.py')
#     if f.name != '__init__.py'
# ]
#=======================================================================================================================



"""
---------------------- ℹ️️-----------------------
❗️Pydantic-фикстуры - для Pre- Post-conditions ❗️
❗️API-фикстуры      - для Assertions           ❗️
------------------------------------------------
"""
