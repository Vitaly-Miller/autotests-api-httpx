"""
Event hooks (хуки событий) в httpx
— выполнять дополнительные действия перед Request запроса или после Response
"""
import httpx
import allure
from tools.curl_generator import make_curl_from_request

#=======================================================================================================================
# Функция для Event Hooks
def curl_event_hook(request: httpx.Request):             # Функция для Event Hooks принимает Request
    """
    Event hook для автоматического прикрепления cURL команды к Allure отчету

    :param request: httpx.Request, переданный в public/privet httpx-клиент (builder)
    """
    curl_command = make_curl_from_request(request)       # Сохраняем работу функции (cURL command generator)

    allure.attach(                                       # Allure attachment:
        body=curl_command,                               # - Прикрепляемый объект
        name='cURL command',                             # - Allure attachment title
        attachment_type=allure.attachment_type.TEXT      # - Output type (Тип отображения объекта - TEXT)
    )

# Event Hooks
client = httpx.Client(event_hooks={'request': [curl_event_hook]})   # до Request выполнить функцию print_request




#=======================================================================================================================
