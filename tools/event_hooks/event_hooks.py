"""
Event Hooks (Callback functions)

events_hooks — an httpx.Client parameter that allows performing additional actions before a Request or after a Response
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
    Callback function for event_hooks that attaches API reports to the Allure report

    - API Base (URL, Method, Status Code)
    - API Request Body =>
    - API Response Body <=
    - API Request Headers =>
    - API Response Headers <=

    :param response: httpx.Response, passed automatically by the public/private httpx client (builder)
        """
    response.read()                                      # Read the response body —
                                                         # — otherwise .text/.json() are unavailable inside the response event hook
    # API Base <=>
    allure.attach(                                       # Allure attachment:
        body=get_api_base(response),                     # - Attached object (function)
        name='API Base <=>',                             # - Allure attachment title
        attachment_type=allure.attachment_type.TEXT      # - Object display type in the report
    )

    # API Request Body =>
    allure.attach(                                       # Allure attachment:
        body=get_api_request_body(response),             # - Attached object (function)
        name='API Request Body =>',                      # - Allure attachment title
        attachment_type=allure.attachment_type.JSON      # - Object display type in the report
    )

    # API Response Body <=
    allure.attach(                                       # Allure attachment:
        body=get_api_response_body(response),            # - Attached object (function)
        name='API Response Body <=',                     # - Allure attachment title
        attachment_type=allure.attachment_type.JSON      # - Object display type in the report
    )

    # API Request Headers =>
    allure.attach(                                       # Allure attachment:
        body=get_api_request_headers(response),          # - Attached object (function)
        name='API Request Headers =>',                   # - Allure attachment title
        attachment_type=allure.attachment_type.JSON      # - Object display type in the report
    )

    # API Response Headers <=
    allure.attach(                                       # Allure attachment:
        body=get_api_response_headers(response),         # - Attached object (function)
        name='API Response Headers <=',                  # - Allure attachment title
        attachment_type=allure.attachment_type.JSON      # - Object display type in the report
    )


#---------------------------------------------------- cURL-command -----------------------------------------------------
# cURL-command
def curl_command_event_hook(response: httpx.Response):
    """
    Callback function for event_hooks that attaches a cURL command to the Allure report

    :param response: httpx.Response, passed automatically by the public/private httpx client (builder)
    """
    allure.attach(                                       # Allure attachment:
        body=make_curl(response.request),                # - Attached object (function)
        name='cURL command',                             # - Allure attachment title
        attachment_type=allure.attachment_type.TEXT      # - Display type in the report
    )


#------------------------------------------------------- Logging -------------------------------------------------------
# Log Request =>
def log_request_event_hook(request: httpx.Request):
    """
    Callback function for event_hooks that logs httpx.Request

    ex. Make GET-request to https://wwww.example.com

    :param request: httpx.Request
    """
    logger.info(get_log_request(request))                # Call the corresponding function


# Log Response <=
def log_response_event_hook(response: httpx.Response):
    """
    Callback function for event_hooks that logs httpx.Response

    ex. Got response status code: 200-OK from https://wwww.example.com

    :param response: httpx.Response
    """
    logger.info(get_log_response(response))              # Call the corresponding function


#=======================================================================================================================
