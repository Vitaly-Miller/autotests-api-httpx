"""
Event Hooks (Callback functions)

events_hooks — параметр httpx.Client, позволяющий выполнять дополнительные действия перед Request запроса или после Response
"""
import httpx
import allure
from tools.logger import get_logger
from tools.event_hooks.event_hooks_functions import (
    get_api_base,
    get_api_request_body, get_api_response_body,
    get_api_request_headers, get_api_response_headers,
    make_curl,
    get_log_request, get_log_response,
)
#------------- Logger -------------
logger = get_logger('HTTPX-Client')                      # for <log_request_event_hook> / <log_response_event_hook>

#=======================================================================================================================
#----------------------------------------------------- API-reports -----------------------------------------------------
# API-Reports
def api_report_event_hook(response: httpx.Response):
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
def curl_command_event_hook(response: httpx.Response):
    """
    Callback-функция для event_hooks, прикрепляющая cURL-команду к Allure отчету

    :param response: httpx.Response, переданный автоматически public/privet httpx-клиентом (builder)
    """
    allure.attach(                                       # Allure attachment:
        body=make_curl(response.request),                # - Прикрепляемый объект (функция)
        name='cURL command',                             # - Allure attachment title
        attachment_type=allure.attachment_type.TEXT      # - Тип отображения отчете
    )


#------------------------------------------------------- Logging -------------------------------------------------------
# Log Request =>
def log_request_event_hook(request: httpx.Request):
    """
    Callback-функция для event_hooks, логирующая httpx.Request

    ex. Make GET-request to https://wwww.example.com

    :param request: httpx.Request
    """
    logger.info(get_log_request(request))                # Вызываем соответствующую функию


# Log Response <=
def log_response_event_hook(response: httpx.Response):
    """
    Callback-функция для event_hooks, логирующая httpx.Response

    ex. Got response status code: 200-OK from https://wwww.example.com

    :param response: httpx.Response
    """
    logger.info(get_log_response(response))              # Вызываем соответствующую функию


#=======================================================================================================================
