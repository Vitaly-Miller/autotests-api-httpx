"""
Event Hooks Callback functions

events_hooks — параметр httpx.Client, позволяющий выполнять дополнительные действия перед Request запроса или после Response
"""
import httpx
import allure
from tools.event_hooks.event_hooks_functions import (
    get_api_base,
    get_api_request_body,
    get_api_response_body,
    get_api_request_headers,
    get_api_response_headers,
    make_curl_from_request
)

#=======================================================================================================================
#----------------------------------------------------- API-reports -----------------------------------------------------
# API-Reports
def api_report(response: httpx.Response):
    """
    Callback-функция для event_hooks, прикрепляющая API-reports к Allure отчету

    - API Base (URL, Method, Status Code)
    - API Request Body =>
    - API Response Body <=
    - API Request Headers =>
    - API Response Headers <=

    :param response: httpx.Response, переданный автоматически public/privet httpx-клиентом (builder)
        """
    response.read()                                      # Дочитываем тело ответа —
                                                         # — иначе .text/.json() недоступны внутри response event hook

    # API Base <=>
    allure.attach(                                       # Allure attachment:
        body=get_api_base(response),                     # - Прикрепляемый объект (функция)
        name='API Base <=>',                             # - Allure attachment title
        attachment_type=allure.attachment_type.TEXT      # - Тип отображения объекта в отчете
    )

    # API Request Body =>
    allure.attach(                                       # Allure attachment:
        body=get_api_request_body(response),             # - Прикрепляемый объект (функция)
        name='API Request Body =>',                      # - Allure attachment title
        attachment_type=allure.attachment_type.JSON      # - Тип отображения объекта в отчете
    )

    # API Response Body <=
    allure.attach(                                       # Allure attachment:
        body=get_api_response_body(response),            # - Прикрепляемый объект (функция)
        name='API Response Body <=',                     # - Allure attachment title
        attachment_type=allure.attachment_type.JSON      # - Тип отображения объекта в отчете
    )

    # API Request Headers =>
    allure.attach(                                       # Allure attachment:
        body=get_api_request_headers(response),          # - Прикрепляемый объект (функция)
        name='API Request Headers =>',                   # - Allure attachment title
        attachment_type=allure.attachment_type.JSON      # - Тип отображения объекта в отчете
    )

    # API Response Headers <=
    allure.attach(                                       # Allure attachment:
        body=get_api_response_headers(response),         # - Прикрепляемый объект (функция)
        name='API Response Headers <=',                  # - Allure attachment title
        attachment_type=allure.attachment_type.JSON      # - Тип отображения объекта в отчете
    )

#---------------------------------------------------- cURL-command -----------------------------------------------------
# cURL-command
def curl_command(response: httpx.Response):
    """
     Callback-функция для event_hooks, прикрепляющая cURL-команду к Allure отчету

    :param response: httpx.Response, переданный автоматически public/privet httpx-клиентом (builder)
    """
    allure.attach(                                       # Allure attachment:
        body=make_curl_from_request(response.request),   # - Прикрепляемый объект (функция)
        name='cURL command',                             # - Allure attachment title
        attachment_type=allure.attachment_type.TEXT      # - Тип отображения отчете
    )


#=======================================================================================================================
