"""
Event Hooks Functions
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
    request_body_json = 'None'
    try:
        if response.request.content:
            request_body_dict = json.loads(response.request.content)
            request_body_json = json.dumps(
                obj=request_body_dict,
                indent=2,
                ensure_ascii=False)
    except httpx.RequestNotRead:
        request_body_json = '<multipart/stream>'
    return request_body_json

#-----------------------------------------------------------------------------------------------------------------------
# API Response Body <=
def get_api_response_body(response: httpx.Response):
    """
    Function that gets the API Response Body (pretty) when making an HTTP request

    :param response: httpx.Response
    :return: API Response Body <=
    """
    try:
        response_body_dict = response.json()
        response_body_json = json.dumps(
            obj=response_body_dict,
            indent=2,
            ensure_ascii=False)
    except Exception as e:
        response_body_json = f'⚠️\n{e}'
    return response_body_json

#-----------------------------------------------------------------------------------------------------------------------
# Get API Request Headers =>
def get_api_request_headers(response: httpx.Response):
    """
    Function that gets the API Request Headers (pretty) when making an HTTP request

    :param response: httpx.Response
    :return: API Request Headers =>
    """
    request_headers_dict = dict(response.request.headers)
    request_headers_json = json.dumps(
        obj=request_headers_dict,
        indent=2,
        ensure_ascii=False
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
    response_headers_dict = dict(response.headers)
    response_headers_json = json.dumps(
        obj=response_headers_dict,
        indent=2,
        ensure_ascii=False
    )
    return response_headers_json


#========================================================= cURL ========================================================
# cURL-command generator (without transport headers)
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
    auto_headers = {'host', 'content-length', 'connection', 'accept-encoding', 'accept', 'user-agent'}

    # Build a list with the main cURL command, including Method and URL:
    result: list[str] = [f'curl -X {request.method}', shlex.quote(str(request.url))]

    # Build HTTP headers:
    for header, value in request.headers.items():
        if not all_headers:
            if header.lower() in auto_headers:
                continue

        result.append(f'-H {shlex.quote(f"{header}: {value}")}')

    # Build BODY:
    try:
        if request.content:
            body = request.content.decode(
                encoding='utf-8',
                errors='replace'
            )
            result.append(f'-d {shlex.quote(body)}')

    except httpx.RequestNotRead:
        pass

    # Join the result list into one string (via .join()) with separators
    return ' \\\n  '.join(result)


#======================================================= Logging =======================================================
# Log Request =>
def get_log_request(request: httpx.Request) -> str:
    """
    Function that builds a log string with data from httpx.Request (Method + Request-URL)

    ex. GET-request to https://wwww.example.com

    :param request: httpx.Request from which the log string will be built
    :return: Built string with data for the Request log (Method + Request-URL)
    """
    log_request = f'{request.method}-request to {request.url}'
    return log_request


# Log Response <=
def get_log_response(response: httpx.Response) -> str:
    """
     Function that builds a log string with data from httpx.Response (Status code + Response-URL)

     ex. Status code: 200-OK from https://wwww.example.com

     :param response: httpx.Response from which the log string will be built
     :return: Built string with data for the Response log (Status code + Response-URL)
     """
    log_response = f'Status code: {response.status_code}-{response.reason_phrase} from {response.url}'
    return log_response


#=======================================================================================================================
