"""
Allure Environment
"""
from config import settings
import platform

#=======================================================================================================================
def create_allure_environment_file() -> None:
    """
    Creates the environment.properties file in the allure-results folder

    Collects information about the test environment (base_url, timeout, OS, Python version, host)
    and writes it in key=value format — Allure displays this data on the "Environment" tab

    :return: None
    """
    properties = {                                                                    # Dict
        'Base_URL': settings.httpx_client.base_url_str,                               # str, not HttpUrl
        'Timeout': settings.httpx_client.timeout,                                     # Timeout
        'OS': platform.platform(terse=True),                                          # macOS-26.5.2
        'Lang': f'{platform.python_implementation()}, {platform.python_version()}',   # CPython, 3.14.3
        'Host_name': platform.node()                                                  # MacBookPro.local
    }

    content = '\n'.join(f'{key}={value}' for key, value in properties.items())   # Iterate <properties> and join into a newline-separated string
    file_path = settings.allure_results_dir / 'environment.properties'           # Path
    file_path.write_text(content, encoding='utf-8')                              # Write to file

#=======================================================================================================================
