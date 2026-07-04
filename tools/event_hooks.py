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
#-------------------------------------------- API Reports (for event_hooks) --------------------------------------------
def api_report(response: httpx.Response):
    """
    Функция-callback для event_hooks, прикрепляющая API-Reports к Allure отчету

    :param response: httpx.Response, переданный автоматически public/privet httpx-клиентом (builder)
        """
    response.read()  # Дочитываем тело ответа — иначе .elapsed/.text/.json() недоступны внутри response event hook
    #-------------------------------------------------------------------------------------------------------------------
    # API Base
    api_base = \
        (f'         Request URL: {response.request.url}\n'
         f'      Request Method: {response.request.method}\n'
         f'Response Status Code: {response.status_code}-{response.reason_phrase}')

    # Allure attachment
    allure.attach(
        body=api_base,                                 # - Прикрепляемый объект
        name='API Base',                               # - Allure attachment title
        attachment_type=allure.attachment_type.TEXT    # - Тип отображения объекта в отчете
    )

    #-------------------------------------------------------------------------------------------------------------------
    # API Request Body =>
    request_body_json = 'None'                         # Default Body for GET-requests
    try:
        if response.request.content:                   # Если есть Request body
            request_body_json_dict = json.loads(response.request.content)  # JSON-string (bytes) —> Dict
            request_body_json = json.dumps(            # Dict —> JSON-string (pretty):
                obj=request_body_json_dict,            # - Объект сериализации
                indent=2,                              # - Отступы
                ensure_ascii=False)                    # - Не заменять не-ASCII (не-латинские) символы на Unicode-последовательности
    except httpx.RequestNotRead:                       # Если multipart/stream исключение, то ...
        request_body_json = '<multipart/stream>'       # ... Body for <multipart/stream> requests

    # Allure attachment
    allure.attach(
        body=request_body_json,                        # - Прикрепляемый объект
        name='API Request Body =>',                    # - Allure attachment title
        attachment_type=allure.attachment_type.JSON    # - Тип отображения объекта в отчете
    )
    # ------------------------------------------------------------------------------------------------------------------
    # API Response Body <=
    try:
        response_body_dict = response.json()           # JSON-string —> Dict
        response_body_json = json.dumps(               # Dict —> JSON-string (pretty):
            obj=response_body_dict,                    # - Объект сериализации
            indent=2,                                  # - Отступы
            ensure_ascii=False)                        # - Не заменять не-ASCII (не-латинские) символы на Unicode-последовательности
    except Exception as e:                             # Если исключение, то сохранить в <e>,...
        response_body_json = f' ⚠️ {e}'                # ... Response Body with Exception

    allure.attach(
        body=response_body_json,                       # - Прикрепляемый объект
        name='API Response Body <=',                   # - Allure attachment title
        attachment_type=allure.attachment_type.JSON    # - Тип отображения объекта в отчете
    )


#------------------------------------------- cURL command  (for event_hooks) -------------------------------------------
# cURL command to Allure report
def curl_command(response: httpx.Response):                  # Функция для event_hooks
    """
    Функция-callback для event_hooks, прикрепляющая cURL-команду к Allure отчету

    :param response: httpx.Response, переданный автоматически public/privet httpx-клиентом (builder)
    """
    curl_command = make_curl_from_request(response.request)   # Сохраняем работу функции - cURL command generator

    # cURL command Allure attachment
    allure.attach(
        body=curl_command,                                   # - Прикрепляемый объект
        name='cURL command',                                 # - Allure attachment title
        attachment_type=allure.attachment_type.TEXT          # - Тип отображения отчете
    )


#=======================================================================================================================
    #response.read()                            # Дочитываем тело ответа — иначе .elapsed/.text/.json() недоступны внутри response event hook
