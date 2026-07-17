"""
Allure Environment
"""
from config import settings
import platform

#=======================================================================================================================
def create_allure_environment_file() -> None:
    """
    Создает файл environment.properties в папке allure-results

    Собирает информацию об окружении теста (base_url, timeout, ОС, версия Python, хост)
    и записывает ее в формате key=value — Allure отобразит эти данные на вкладке "Environment"

    :return: None
    """
    properties = {                                                                    # Dict
        'Base_URL': settings.httpx_client.base_url_str,                               # str, а не HttpUrl
        'Timeout': settings.httpx_client.timeout,                                     # Timeout
        'OS': platform.platform(terse=True),                                          # macOS-26.5.2
        'Lang': f'{platform.python_implementation()}, {platform.python_version()}',   # CPython, 3.14.3
        'Host_name': platform.node()                                                  # MacBookPro.local
    }

    content = '\n'.join(f'{key}={value}' for key, value in properties.items())   # Итерация <properties> и склеивание в строку с переносами
    file_path = settings.allure_results_dir / 'environment.properties'           # Путь
    file_path.write_text(content, encoding='utf-8')                              # Запись в файл

#=======================================================================================================================
