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
    properties = {
        'Base_URL': settings.httpx_client.base_url_str,
        'Timeout': settings.httpx_client.timeout,
        'OS': platform.platform(terse=True),
        'Lang': f'{platform.python_implementation()}, {platform.python_version()}',
        'Host_name': platform.node()
    }

    content = '\n'.join(f'{key}={value}' for key, value in properties.items())
    file_path = settings.allure_results_dir / 'environment.properties'
    file_path.write_text(content, encoding='utf-8')

#=======================================================================================================================
