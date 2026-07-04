"""
API REPORT to console (✨Pretty)
"""
import httpx
import json
from tools.formatting.colors import ANSI

#=======================================================================================================================
class Report:
    def __init__(self, response: httpx.Response):
        self.response = response
    #-------------------------------------------------- Base -----------------------------------------------------------
    # Title
    @staticmethod
    def api_title():
        print(f'\n\n{ANSI.GRAY}{'—'*12}{ANSI.B_CYAN} API REPORT {ANSI.GRAY}{'—'*12}{ANSI.RESET}')


    # URL
    def api_url(self):
        url = self.response.request.url
        print(f'\n{ANSI.B_CYAN}┌╴{ANSI.RESET}Request URL:\t  {url}{ANSI.RESET}')


    # Method
    def api_method(self):
        method = self.response.request.method
        if method == 'GET':       color = ANSI.B_GREEN
        elif method == 'POST':    color = ANSI.BEIGE
        elif method == 'PUT':     color = ANSI.B_BLUE
        elif method == 'PATCH':   color = ANSI.B_PURPLE
        elif method == 'DELETE':  color = ANSI.B_RED
        elif method == 'OPTIONS': color = ANSI.PINK
        else: color = ANSI.RESET
        print(f'{ANSI.B_CYAN}├╴{ANSI.RESET}HTTP Method:\t  {color}{method}{ANSI.RESET}')


    # Status code
    def api_status_code(self):
        code = self.response.status_code            # Код            (например: 200)
        reason = self.response.reason_phrase        # Описание кода  (например: OK)
        if code < 200:   color = ANSI.SUNRISE       # 1xx
        elif code < 300: color = ANSI.BRIGHT_GREEN  # 2xx
        elif code < 400: color = ANSI.SUNRISE       # 3xx
        elif code < 500: color = ANSI.RED           # 4xx
        elif code < 600: color = ANSI.ORANGE        # 5xx
        else: color = ANSI.RESET
        print(f'{ANSI.B_CYAN}├╴{ANSI.RESET}Status code:\t  {color}{code}-{reason}{ANSI.RESET}')


    # Response time
    def api_response_time(self, max_sec=5.0):                    # Max sec limit = ⚠️default value
        response_time = self.response.elapsed.total_seconds()    # 0.12345
        round_response_time = round(response_time, 3)            # 0.12345 —> 0.123 (округление)
        if round_response_time < max_sec:
            color = ANSI.DARK_GREEN
        else:
            color = ANSI.RED
        print(f'{ANSI.B_CYAN}└╴{ANSI.RESET}Response time:  {color}{round_response_time}{ANSI.GRAY}/{max_sec} sec{ANSI.RESET}\n')


    #------------------------------------------------- Body (Content) --------------------------------------------------
    # REQUEST Body ⮕
    def api_request_body(self):
        print(f'\n{ANSI.GREEN} REQUEST Body{ANSI.GRAY}: ⮕')
        try:
            if self.response.request.content:
                request_body_dict = json.loads(self.response.request.content)
                request_body_json = json.dumps(request_body_dict, indent=2, ensure_ascii=False)
                print(request_body_json)
            else:
                print(f'{{\n\t<none>\n}}')
        except Exception:     # NOQA <— ⚠️Заменить на except httpx.RequestNotRead:
            print(f'{{\n\t<multipart/stream>\n}}')


    # RESPONSE Body ⬅︎
    def api_response_body(self):
        print(f'\n{ANSI.BLUE} RESPONSE Body{ANSI.GRAY}: ⬅︎')
        try:
            response_body_dict = self.response.json()
            response_body_json = json.dumps(response_body_dict, indent=2, ensure_ascii=False)
            print(response_body_json)
        except Exception as e:
            print(f' ⚠️ {e}')

    #----------------------------------------------------- Headers -----------------------------------------------------
    # REQUEST Headers ⮕
    def api_request_headers(self):
        print(f'\n{ANSI.BROWN} REQUEST Headers{ANSI.GRAY}: ⮕')
        request_headers_dict = dict(self.response.request.headers)
        request_headers_json = json.dumps(request_headers_dict, indent=2, ensure_ascii=False)
        print(request_headers_json)


    # RESPONSE Headers ⬅︎
    def api_response_headers(self):
        print(f'\n{ANSI.BROWN_ORANGE} RESPONSE Headers{ANSI.GRAY}: ⬅︎')
        response_headers_dict = dict(self.response.headers)
        response_headers_json = json.dumps(response_headers_dict, indent=2, ensure_ascii=False)
        print(response_headers_json)
        print(f'{'—'*36}{ANSI.RESET}')

#=======================================================================================================================
