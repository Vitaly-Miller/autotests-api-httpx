"""
Event hooks (хуки событий)
— параметр httpx.Client, позволяющий выполнять дополнительные действия перед Request запроса или после Response
"""
import json

import httpx
import allure
from tools.curl_generator import make_curl_from_request
from tools.tool import Tool

#=======================================================================================================================
#--------------------------------------------------------- API ---------------------------------------------------------
# API Request Body to Allure report
def api_request_body(request: httpx.Request):              # Функция для event_hooks
    """
    Функция-callback для event_hooks, прикрепляющая API Request Body к Allure отчету

    ... с игнорированием пустых GET- и <multipart/stream> - запросов

    :param request: httpx.Request, переданный автоматически public/privet httpx-клиентом (builder)
    """
    body_json = 'None'                                 # Default Body for GET-requests
    try:
        if request.content:
            body_dict = json.loads(request.content)    # JSON-string (bytes) —> Dict
            body_json = json.dumps(                    # Dict —> JSON-string (pretty):
                body_dict,                         # - Объект сериализации
                indent=2,                              # - Отступы
                ensure_ascii=False)                    # - Не заменять не-ASCII (не-латинские) символы на Unicode-последовательности
    except httpx.RequestNotRead:                       # Если multipart/stream исключение, то ...
        body_json = '<multipart/stream>'               # ... Body for <multipart/stream> requests

    # Allure attachment
    allure.attach(
        body=body_json,                                # - Прикрепляемый объект
        name='API Request Body ⮕',                     # - Allure attachment title
        attachment_type=allure.attachment_type.JSON    # - Тип отображения объекта в отчете
    )




#---------------------------------------------------- cURL command -----------------------------------------------------
# cURL command to Allure report
def curl_command(request: httpx.Request):             # Функция для event_hooks
    """
    Функция-callback для event_hooks, прикрепляющая cURL-команду к Allure отчету

    :param request: httpx.Request, переданный автоматически public/privet httpx-клиентом (builder)
    """
    curl_command = make_curl_from_request(request)       # Сохраняем работу функции - cURL command generator

    # cURL command Allure attachment
    allure.attach(
        body=curl_command,                               # - Прикрепляемый объект
        name='cURL command',                             # - Allure attachment title
        attachment_type=allure.attachment_type.TEXT      # - Тип отображения отчете
    )


#=======================================================================================================================
    #response.read()                            # Дочитываем тело ответа — иначе .elapsed/.text/.json() недоступны внутри response event hook
