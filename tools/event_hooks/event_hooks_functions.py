"""
Event Hooks Functions

events_hooks — параметр httpx.Client, позволяющий выполнять дополнительные действия перед Request запроса или после Response
"""
import httpx
import json

#=======================================================================================================================
#----------------------------------------------------- API Reports -----------------------------------------------------
# API Base <=>
def get_api_base(response: httpx.Response) -> str:
    """
    Функция для получения API-Base (URL, Method, Status Code) при выполнении HTTP-запроса

    :param response: response: httpx.Response
    :return: api_base: API-Base (URL, Method, Status Code)
    """
    api_base = \
        (f'         Request URL: {response.request.url}\n'
         f'      Request Method: {response.request.method}\n'
         f'Response Status Code: {response.status_code}-{response.reason_phrase}')
    return api_base

#-----------------------------------------------------------------------------------------------------------------------
# API Request Body =>
def get_api_request_body(response: httpx.Response):
    """
    Функция для получения API Request Body (pretty) при выполнении HTTP-запроса

    :param response: httpx.Response
    :return: API Request Body =>
    """
    request_body_json = 'None'                               # Default Body for GET-requests
    try:                                                     # Попытка
        if response.request.content:                         # Если есть Request body
            request_body_dict = json.loads(response.request.content)  # JSON-string (bytes) —> Dict
            request_body_json = json.dumps(                  # Dict —> JSON-string (pretty):
                obj=request_body_dict,                       # - Объект сериализации
                indent=2,                                    # - Отступы
                ensure_ascii=False)                          # - Не заменять не-ASCII (не-латинские) символы на Unicode
    except httpx.RequestNotRead:                             # Если multipart/stream исключение, то ...
        request_body_json = '<multipart/stream>'             # ... Body for <multipart/stream> requests
    return request_body_json

#-----------------------------------------------------------------------------------------------------------------------
# API Response Body <=
def get_api_response_body(response: httpx.Response):
    """
    Функция для получения API Response Body (pretty) при выполнении HTTP-запроса

    :param response: httpx.Response
    :return: API Response Body <=
    """
    try:                                                     # Попытка
        response_body_dict = response.json()                 # JSON-string —> Dict
        response_body_json = json.dumps(                     # Dict —> JSON-string (pretty):
            obj=response_body_dict,                          # - Объект сериализации
            indent=2,                                        # - Отступы
            ensure_ascii=False)                              # - Не заменять не-ASCII (не-латинские) символы на Unicode
    except Exception as e:                                   # Если исключение, то сохранить описание в <e>,...
        response_body_json = f'⚠️\n{e}'                      # ... Response Body with Exception
    return response_body_json

#-----------------------------------------------------------------------------------------------------------------------
# API Request Headers =>
def get_api_request_headers(response: httpx.Response):
    """
    Функция для получения API Request Headers (pretty) при выполнении HTTP-запроса

    :param response: httpx.Response
    :return: API Request Headers =>
    """
    request_headers_dict = dict(response.request.headers)    # JSON-string —> Dict
    request_headers_json = json.dumps(                       # Dict —> JSON-string (pretty):
        obj=request_headers_dict,                            # - Объект сериализации
        indent=2,                                            # - Отступы
        ensure_ascii=False                                   # - Не заменять не-ASCII (не-латинские) символы на Unicode
    )
    return request_headers_json

#-----------------------------------------------------------------------------------------------------------------------
# API Response Headers <=
def get_api_response_headers(response: httpx.Response):
    """
    Функция для получения API Response Headers (pretty) при выполнении HTTP-запроса

    :param response: httpx.Response
    :return: API Response Headers <=
    """
    response_headers_dict = dict(response.headers)           # JSON-string —> Dict
    response_headers_json = json.dumps(                      # Dict —> JSON-string (pretty):
        obj=response_headers_dict,                           # - Объект сериализации
        indent=2,                                            # - Отступы
        ensure_ascii=False                                   # - Не заменять не-ASCII (не-латинские) символы на Unicode
    )
    return response_headers_json

#---------------------------------------------------- cURL command -----------------------------------------------------
# cURL command generator
def make_curl_from_request(request: httpx.Request) -> str:
    """
    Функция генерирует команду cURL при выполнении HTTP-запроса

    :param request: HTTP-запрос, из которого будет сформирована команда cURL.
    :return: Строка с командой cURL, содержащая метод запроса, URL, заголовки и тело (если есть).
    """
    # Создаем список с основной командой cURL, включая Метод и URL
    result: list[str] = [f'curl -X "{request.method}"', f'"{request.url}"']  # Генерируем сроковый список

    # Добавляем заголовки в формате -H "Header: Value"
    for header, value in request.headers.items():         # Итерация по заголовкам и значениям headers
        result.append(f'-H "{header}: {value}"')          # Добавление заголовков и значений в <result>

    # Добавляем body, если оно есть (например, для POST, PUT, UPDATE)
    try:
        if request.content:                                # Если есть request.content (body), то ...  ┐ ИЛИ ОДНОЙ СТРОКОЙ —> if body := request.content:
            body = request.content                         # ... сохраняем в <body>                    ┘
            result.append(f'-d "{body.decode('utf-8')}"')  # Добавление body в <result> c переводом байтов в —> строку
    except httpx.RequestNotRead:                           # Если запрос не прочитан, в случае передачи stream, ...
        pass                                               # ... проигнорировать

    # Объединение списка строк result в одну строку (через склеивание .join())
    return " \\\n  ".join(result)                          # <пробел>, разделитель-<\> (экранированный), перенос сроки-<\n>, <пробел>, <пробел>

#=======================================================================================================================
