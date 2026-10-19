"""
httpx.Client (Public) builder
(For methods that do NOT require authorization)
"""
import httpx
import allure
from config import settings
from tools.event_hooks.event_hooks import (
    log_request_event_hook,
    log_response_event_hook,
    api_report_event_hook,
    curl_command_event_hook
)

#============================================ httpx.Client (Public) builder ============================================
@allure.step('◉ Get httpx.Client (Public)')
def get_httpx_client_public() -> httpx.Client:
    """
    Creates a configured httpx.Client instance (Public)

    :return: Configured httpx.Client (Public)
    """
    httpx_client_public = httpx.Client(
        base_url=settings.httpx_client.base_url,
        timeout=settings.httpx_client.timeout,
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
    return httpx_client_public


#=======================================================================================================================
