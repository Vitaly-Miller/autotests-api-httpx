"""
🅰🅿︎🅸 🆁🅴🅿︎🅾🆁🆃 to console (✨Pretty)
"""
import json
from tools.formatting.colors import ANSI

#=======================================================================================================================
class Report:
    #-------------------------------------------------- Base -----------------------------------------------------------
    # Title
    @staticmethod
    def api_title():
        text = f'{ANSI.B_CYAN} 🅰🅿︎🅸 🆁🅴🅿︎🅾🆁🆃 {ANSI.GRAY} '
        print(f'\n\n\n{text.center(64,  " ")}')

    # URL
    @staticmethod
    def api_url(response):
        obj = response.request.url
        print(f'\n{ANSI.B_CYAN}┌╴{ANSI.RESET}Request URL:\t  {obj}{ANSI.RESET}')

    # Method
    @staticmethod
    def api_method(response):
        obj = response.request.method
        if obj == 'GET':       color = ANSI.B_GREEN
        elif obj == 'POST':    color = ANSI.BEIGE
        elif obj == 'PUT':     color = ANSI.B_BLUE
        elif obj == 'PATCH':   color = ANSI.B_PURPLE
        elif obj == 'DELETE':  color = ANSI.B_RED
        elif obj == 'OPTIONS': color = ANSI.PINK
        else: color = ANSI.RESET
        print(f'{ANSI.B_CYAN}├╴{ANSI.RESET}HTTP Method:\t  {color}{obj}{ANSI.RESET}')

    # Status code
    @staticmethod
    def api_status_code(response):
        obj = response.status_code
        if obj < 200:   color = ANSI.SUNRISE       # 1xx
        elif obj < 300: color = ANSI.BRIGHT_GREEN  # 2xx
        elif obj < 400: color = ANSI.SUNRISE       # 3xx
        elif obj < 500: color = ANSI.RED           # 4xx
        elif obj < 600: color = ANSI.ORANGE        # 5xx
        else: color = ANSI.RESET
        print(f'{ANSI.B_CYAN}├╴{ANSI.RESET}Status code:\t  {color}{obj}{ANSI.RESET}')

    # Response time
    @staticmethod
    def api_response_time(response, max_sec=5):    # ⚠️секунды
        obj = response.elapsed.total_seconds()
        round_response_time = round(obj, 3)   # 0.12345 -> 0.123
        if round_response_time < max_sec:
            color = ANSI.DARK_GREEN
        else:
            color = ANSI.RED
        print(f'{ANSI.B_CYAN}└╴{ANSI.RESET}Response time:  {color}{round_response_time}{ANSI.GRAY}/{max_sec} sec{ANSI.RESET}\n')


    #---------------------------------------------- REQUEST / RESPONSE -------------------------------------------------
    # REQUEST Body ⮕
    @staticmethod
    def api_request_body(response):
        print(f'{ANSI.GRAY}{'|'*17}{ANSI.GREEN} REQUEST Body{ANSI.GRAY}: ⮕ {'|'*17}')

        if response.request.content:
            obj = json.loads(response.request.content)
            obj_json = json.dumps(obj, indent=4, ensure_ascii=False)
            print(f'{obj_json}{ANSI.RESET}')
        else:
            print(f'{{\n\t<None>\n}}{ANSI.RESET}')

    # RESPONSE Body ⬅︎
    @staticmethod
    def api_response_body(response):
        print(f'{ANSI.GRAY}{'|'*17}{ANSI.BLUE} RESPONSE Body{ANSI.GRAY}: ⬅︎ {'|'*16}')
        obj = response.json()
        obj_json = json.dumps(obj, indent=4, ensure_ascii=False)
        print(f'{obj_json}{ANSI.RESET}')

    # REQUEST Headers ⮕
    @staticmethod
    def api_request_headers(response):
        print(f'{ANSI.GRAY}{'|'*16}{ANSI.BROWN} REQUEST Headers{ANSI.GRAY}: ⮕ {'|'*15}')
        obj = dict(response.request.headers)
        obj_json = json.dumps(obj, indent=4, ensure_ascii=False)
        print(f'{obj_json}{ANSI.RESET}')

    # RESPONSE Headers ⬅︎
    @staticmethod
    def api_response_headers(response):
        print(f'{ANSI.GRAY}{'|'*15}{ANSI.BROWN_ORANGE} RESPONSE Headers{ANSI.GRAY}: ⬅︎ {'|'*15}')
        obj = dict(response.headers)
        obj_json = json.dumps(obj, indent=4, ensure_ascii=False)
        print(f'{obj_json}{ANSI.RESET}')

#-----------------------------------------------------------------------------------------------------------------------
