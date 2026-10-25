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
    response.read()

    # API Base <=>
    allure.attach(
        body=get_api_base(response),
        name='API Base <=>',
        attachment_type=allure.attachment_type.TEXT
    )

    # API Request Body =>
    allure.attach(
        body=get_api_request_body(response),
        name='API Request Body =>',
        attachment_type=allure.attachment_type.JSON
    )

    # API Response Body <=
    allure.attach(
        body=get_api_response_body(response),
        name='API Response Body <=',
        attachment_type=allure.attachment_type.JSON
    )

    # API Request Headers =>
    allure.attach(
        body=get_api_request_headers(response),
        name='API Request Headers =>',
        attachment_type=allure.attachment_type.JSON
    )

    # API Response Headers <=
    allure.attach(
        body=get_api_response_headers(response),
        name='API Response Headers <=',
        attachment_type=allure.attachment_type.JSON
    )


#---------------------------------------------------- cURL-command -----------------------------------------------------
# cURL-command
def curl_command_event_hook(response: httpx.Response):
    """
    Callback function for event_hooks that attaches a cURL command to the Allure report

    :param response: httpx.Response, passed automatically by the public/private httpx client (builder)
    """
    allure.attach(
        body=make_curl(response.request),
        name='cURL command',
        attachment_type=allure.attachment_type.TEXT
    )


#------------------------------------------------------- Logging -------------------------------------------------------
# Log Request =>
def log_request_event_hook(request: httpx.Request):
    """
    Callback function for event_hooks that logs httpx.Request

    ex. Make GET-request to https://wwww.example.com

    :param request: httpx.Request
    """
    logger.info(get_log_request(request))


# Log Response <=
def log_response_event_hook(response: httpx.Response):
    """
    Callback function for event_hooks that logs httpx.Response

    ex. Got response status code: 200-OK from https://wwww.example.com

    :param response: httpx.Response
    """
    logger.info(get_log_response(response))


#=======================================================================================================================
