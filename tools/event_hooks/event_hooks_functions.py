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
    try:                                                     # Try
        if response.request.content:                         # If there is a Request body
            request_body_dict = json.loads(response.request.content)  # JSON-string (bytes) —> Dict
            request_body_json = json.dumps(                  # Dict —> JSON-string (pretty):
                obj=request_body_dict,                       # - Object to serialize
                indent=2,                                    # - Indentation
                ensure_ascii=False)                          # - Do not escape non-ASCII (non-Latin) characters to Unicode
    except httpx.RequestNotRead:                             # If multipart/stream exception, then ...
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
    try:                                                     # Try
        response_body_dict = response.json()                 # JSON-string —> Dict
        response_body_json = json.dumps(                     # Dict —> JSON-string (pretty):
            obj=response_body_dict,                          # - Object to serialize
            indent=2,                                        # - Indentation
            ensure_ascii=False)                              # - Do not escape non-ASCII (non-Latin) characters to Unicode
    except Exception as e:                                   # If exception, save its description in <e>,...
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
        obj=request_headers_dict,                            # - Object to serialize
        indent=2,                                            # - Indentation
        ensure_ascii=False                                   # - Do not escape non-ASCII (non-Latin) characters to Unicode
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
        obj=response_headers_dict,                           # - Object to serialize
        indent=2,                                            # - Indentation
        ensure_ascii=False                                   # - Do not escape non-ASCII (non-Latin) characters to Unicode
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
    # HTTP headers that should not be carried over to cURL.
    # They are calculated automatically by the HTTP client itself (curl/Postman).
    # For example, Content-Length may become wrong after the request body changes.
    auto_headers = {'host', 'content-length', 'connection', 'accept-encoding', 'accept', 'user-agent'}

    # Build a list with the main cURL command, including Method and URL:
    # + shlex.quote() - escapes the URL for safe use
    result: list[str] = [f'curl -X {request.method}', shlex.quote(str(request.url))]   # Generate a list of strings

    # Build HTTP headers:
    for header, value in request.headers.items():   # Iterate over header names and values
        if not all_headers:                         # If <all_headers> = False, then ...
            if header.lower() in auto_headers:      # ... if there are auto-calculated transport headers, then ...
                continue                            # ... skip them

        result.append(f'-H {shlex.quote(f"{header}: {value}")}')   # Append headers and values to <result>

    # Build BODY:
    try:
        if request.content:                # If the request has a body (e.g. for POST, PUT, UPDATE)...
            body = request.content.decode( # ... save to <body>
                encoding='utf-8',          # bytes → str (decode)
                errors='replace'           # Replace invalid characters so cURL generation does not fail
            )
            result.append(f'-d {shlex.quote(body)}')   # Append request body to <result>

    except httpx.RequestNotRead:                       # For stream/multipart requests ...
        pass                                           # ... skip

    # Join the result list into one string (via .join()) with separators
    return ' \\\n  '.join(result)  # <space>, separator-<\> (escaped), line break-<\n>, <space>, <space>


#======================================================= Logging =======================================================
# Log Request =>
def get_log_request(request: httpx.Request) -> str:
    """
    Function that builds a log string with data from httpx.Request (Method + Request-URL)

    ex. GET-request to https://wwww.example.com

    :param request: httpx.Request from which the log string will be built
    :return: Built string with data for the Request log (Method + Request-URL)
    """
    log_request = f'{request.method}-request to {request.url}'   # Build log data string
    return log_request


# Log Response <=
def get_log_response(response: httpx.Response) -> str:
    """
     Function that builds a log string with data from httpx.Response (Status code + Response-URL)

     ex. Status code: 200-OK from https://wwww.example.com

     :param response: httpx.Response from which the log string will be built
     :return: Built string with data for the Response log (Status code + Response-URL)
     """
    log_response = f'Status code: {response.status_code}-{response.reason_phrase} from {response.url}' # Build log data string
    return log_response


#=======================================================================================================================
