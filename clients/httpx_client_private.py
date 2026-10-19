"""
httpx.Client (🔒Private) (builder)
(For methods that require authorization)
"""
import allure
import httpx
from config import settings
from clients.auth_client import get_auth_client
from schemas.auth_schema import AuthDataSchema
from tools.event_hooks.event_hooks import (
    log_request_event_hook,
    log_response_event_hook,
    api_report_event_hook,
    curl_command_event_hook
)

#=========================================== httpx.Client (Private) builder ============================================
@allure.step('◉ Get httpx.Client (Private)')
def get_httpx_client_private(auth_data: AuthDataSchema) -> httpx.Client:
    """
    Creates a configured httpx.Client instance (Private)

    :param auth_data: Pydantic model with authentication data (email and password)
    :return: Configured httpx.Client (Private)
    """
    auth_client = get_auth_client()
    response = auth_client.login_pydantic(auth_data=auth_data)
    headers = {'Authorization': f'Bearer {response.token.access_token}'}
    httpx_client_private = httpx.Client(
        base_url=settings.httpx_client.base_url,
        timeout=settings.httpx_client.timeout,
        headers=headers,
        event_hooks={
            'request': [
                log_request_event_hook
            ],
            'response': [
                api_report_event_hook,
                curl_command_event_hook,
                log_response_event_hook
            ]
        }
    )
    return httpx_client_private


#=======================================================================================================================
