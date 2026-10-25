"""
conftest.py (via Pytest Plugins)
Uses pytest_plugins - all fixtures are in separate module files
"""
from pathlib import Path

#================================================ Plugins path (Manual) ================================================
pytest_plugins = (
    'fixtures.users_public_fixtures',     # ┐
    'fixtures.users_private_fixtures',    # │
    'fixtures.auth_fixtures',             # │ Client's
    'fixtures.files_fixtures',            # │ fixtures
    'fixtures.courses_fixtures',          # │
    'fixtures.exercises_fixtures',        # ┘

    'fixtures.allure_fixtures'            # Allure's fixture
)

#================================================ Plugins path (Auto) ==================================================
# pytest_plugins = [
#     f'fixtures.{file.stem}'
#     for file in Path(__file__).parent.glob('fixtures/*.py')
#     if file.name != '__init__.py'
# ]


#=======================================================================================================================
