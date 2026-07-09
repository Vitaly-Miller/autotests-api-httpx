"""
Allure environment
"""
from config import settings

#=======================================================================================================================
def create_allure_environment_file():
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]  # Создаем список из элементов в формате {key}={value}
    properties = '\n'.join(items)                                               # Собираем все элементы в единую строку с переносами

    # Открываем файл ./allure-results/environment.properties на чтение
    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)                                                  # Записываем переменные в файл

#=======================================================================================================================
