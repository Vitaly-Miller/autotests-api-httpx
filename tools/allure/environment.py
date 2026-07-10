"""
Allure environment
"""
from config import settings
import platform

#=======================================================================================================================
# v.1
# def create_allure_environment_file() -> None:
#     items = [f'{key}={value}' for key, value in settings.model_dump().items()]  # Создаем список из элементов в формате {key}={value}
#     properties = '\n'.join(items)                                               # Собираем все элементы в единую строку с переносами
#
#     # Открываем файл ./allure-results/environment.properties на запись
#     with open(settings.allure_results_dir.joinpath('environment.properties'), 'w') as file:
#         file.write(properties)                                                  # Записываем переменные в файл

#=======================================================================================================================
# v.2
def create_allure_environment_file() -> None:
    """
    Создает файл environment.properties в папке allure-results.

    Собирает информацию об окружении теста (base_url, timeout, ОС, версия Python, хост)
    и записывает ее в формате key=value — Allure отобразит эти данные на вкладке "Environment".

    :return: None
    """
    properties = {                                                                    # Dict
        'Base_URL': settings.httpx_client.base_url_str,                               # str, а не HttpUrl
        'Timeout': settings.httpx_client.timeout,                                     # Timeout
        'OS': platform.platform(terse=True),                                          # macOS-26.5.2
        'Lang': f'{platform.python_implementation()}, {platform.python_version()}',   # CPython, 3.14.3
        'Host_name': platform.node()                                                  # MacBookPro.local
    }
    """
    Явно перечисляем, какие поля из settings хотим увидеть в Allure-отчете.
    Именно поэтому это обычный dict, а не settings.model_dump().
    - model_dump() вернул бы вложенные модели (httpx_client, test_data) целиком,
    и в файл попали бы Python-словари вида "httpx_client={'base_url': ..., 'timeout': None}",
    что Allure не сможет нормально распарсить.

    """
    content = '\n'.join(f'{key}={value}' for key, value in properties.items())        # Итерация <properties> и склеивание в строку с переносами
    """
    Превращаем dict в текст формата key=value, по одной паре на строку —
    именно такой формат ожидает Allure в файле environment.properties.
    f'{key}={value}'  — строка вида 'base_url=https://...'
    '\n'.join(...)    — склеивает все строки через перенос строки
    """
    file_path = settings.allure_results_dir / 'environment.properties'
    """
    settings.allure_results_dir — это Path (DirectoryPath из pydantic),
    поэтому можно просто "делить" его на имя файла через оператор /
    (аналог os.path.join, но в стиле pathlib)
    """
    file_path.write_text(content, encoding='utf-8')                                   # Запись в файл
    """
    write_text() сам открывает файл на запись, пишет content и закрывает файл —
    не нужно вручную делать open(..., 'w') / file.write(...) / закрывать файл
    """
#=======================================================================================================================
