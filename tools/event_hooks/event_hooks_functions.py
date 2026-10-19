"""
Event Hooks Functions

events_hooks — an httpx.Client parameter that allows performing additional actions before a Request or after a Response
"""
import httpx
import json
import shlex

#========================================================= API =========================================================
# Get API Base <=>
def get_api_base(response: httpx.Response) -> str:
    """
    Function that gets the API Base (URL, Method, Status Code) when making an HTTP request

    :param response: response: httpx.Response
    :return: api_base: API-Base (URL, Method, Status Code)
    """
    api_base = \
        (f'         Request URL: {response.request.url}\n'
         f'      Request Method: {response.request.method}\n'
         f'Response Status Code: {response.status_code}-{response.reason_phrase}\n'
         f'        Response URL: {response.url}')
    return api_base

#-----------------------------------------------------------------------------------------------------------------------
# Get API Request Body =>
def get_api_request_body(response: httpx.Response):
    """
    Function that gets the API Request Body (pretty) when making an HTTP request

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
    Function that gets the API Response Body (pretty) when making an HTTP request

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
# Get API Request Headers =>
def get_api_request_headers(response: httpx.Response):
    """
    Function that gets the API Request Headers (pretty) when making an HTTP request

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
# Get API Response Headers <=
def get_api_response_headers(response: httpx.Response):
    """
    Function that gets the API Response Headers (pretty) when making an HTTP request

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


#========================================================= cURL ========================================================
# cURL-command generator (без транспортных заголовков)
def make_curl(request: httpx.Request, all_headers: bool = False) -> str:
    """
    Function that generates a cURL command when making an HTTP request

    - Request Method
    - Request URL
    - ⚠️WITHOUT TRANSPORT HEADERS
    - accept-encoding: (header)
    - Request Body (if any)


    :param request: HTTP request from which the cURL command will be built
    :param all_headers: Whether to include auto-computed transport headers in the cURL command (False - default)
    :return: String with the cURL command
    """
    # HTTP-заголовки, которые не нужно переносить в cURL.
    # Они автоматически рассчитываются самим HTTP-клиентом (curl/Postman).
    # Например, Content-Length может стать неверным после изменения тела запроса.
    auto_headers = {'host', 'content-length', 'connection', 'accept-encoding', 'accept', 'user-agent'}

    # Формируем список с основной командой cURL, включая Метод и URL:
    # + shlex.quote() - экранирует URL для безопасного использования
    result: list[str] = [f'curl -X {request.method}', shlex.quote(str(request.url))]   # Генерируем сроковый список

    # Формируем HTTP-заголовки:
    for header, value in request.headers.items():   # Итерация по заголовкам и значениям headers
        if not all_headers:                         # Если параметр <all_headers> = False, то ...
            if header.lower() in auto_headers:      # ... если есть автоматически вычисляемые транспортные заголовки, то ...
                continue                            # ... проигнорировать их

        result.append(f'-H {shlex.quote(f"{header}: {value}")}')   # Добавление заголовков и значений в <result>

    # Формируем BODY:
    try:
        if request.content:                # Если запрос содержит тело (например, для POST, PUT, UPDATE)...
            body = request.content.decode( # ... сохраняем в <body>
                encoding='utf-8',          # bytes → str (декодируем)
                errors='replace'           # Некорректные символы заменяем, чтобы генерация cURL не завершилась ошибкой
            )
            result.append(f'-d {shlex.quote(body)}')   # Добавляем тело запроса в <result>

    except httpx.RequestNotRead:                       # Для stream/multipart-запросов ...
        pass                                           # ... пропускаем

    # Объединение списка строк result в одну строку (через склеивание .join()) с разделителями
    return ' \\\n  '.join(result)  # <пробел>, разделитель-<\> (экранированный), перенос сроки-<\n>, <пробел>, <пробел>


#======================================================= Logging =======================================================
# Log Request =>
def get_log_request(request: httpx.Request) -> str:
    """
    Function that builds a log string with data from httpx.Request (Method + Request-URL)

    ex. GET-request to https://wwww.example.com

    :param request: httpx.Request from which the log string will be built
    :return: Built string with data for the Request log (Method + Request-URL)
    """
    log_request = f'{request.method}-request to {request.url}'   # Формируем сроку c данными для лога
    return log_request


# Log Response <=
def get_log_response(response: httpx.Response) -> str:
    """
     Function that builds a log string with data from httpx.Response (Status code + Response-URL)

     ex. Status code: 200-OK from https://wwww.example.com

     :param response: httpx.Response from which the log string will be built
     :return: Built string with data for the Response log (Status code + Response-URL)
     """
    log_response = f'Status code: {response.status_code}-{response.reason_phrase} from {response.url}' # Формируем сроку c данными для лога
    return log_response


#=======================================================================================================================
