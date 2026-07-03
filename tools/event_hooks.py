"""
Event hooks (хуки событий) в httpx
— выполнять дополнительные действия перед Request запроса или после Response
"""
import httpx
import allure
from tools.curl_generator import make_curl_from_request, response
from tools.tool import Tool

#=======================================================================================================================
# Event Hooks for attach cURL command to Allure report
def curl_event_hook(request: httpx.Request):             # Функция принимает Request
    """
    Функция для Event Hooks Event hook для автоматического прикрепления cURL команды к Allure отчету

    :param request: httpx.Request, переданный в public/privet httpx-клиент (builder)
    """
    curl_command = make_curl_from_request(request)       # Сохраняем работу функции (cURL command generator)

    # cURL command Allure attachment
    allure.attach(
        body=curl_command,                               # - Прикрепляемый объект
        name='cURL command',                             # - Allure attachment title
        attachment_type=allure.attachment_type.TEXT      # - Output type (Тип отображения объекта - TEXT)
    )


#-----------------------------------------------------------------------------------------------------------------------
# Функция
def api_report_event_hook(response: httpx.Response):
    response.read()                            # Дочитываем тело ответа — иначе .elapsed/.text/.json() недоступны внутри response event hook

    api_report = Tool.api_report(response)

    # cURL command Allure attachment
    allure.attach(
        body=api_report,                          # - Прикрепляемый объект
        name='API report',                             # - Allure attachment title
        attachment_type=allure.attachment_type.TEXT    # - Output type (Тип отображения объекта - TEXT)
    )


#=======================================================================================================================
