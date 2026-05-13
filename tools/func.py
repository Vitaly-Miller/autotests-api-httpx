"""
Tools - ⚠️В РАЗРАБОТКЕ
- Не нравится что в классе
- Не нравится название класса - конфликтует ели файл назвать tools.py
- Не нравится название файла. Логично назвать tools.py
"""
import inspect
import os
import json
from dotenv import set_key, dotenv_values
from tools.formatting.colors import ANSI
from tools.formatting.report import Report

#=======================================================================================================================
class Tool:
    #----------------------------------------------- Get Test name -----------------------------------------------------
    # (⚠️НЕ ИСПОЛЬЗУЕТСЯ)
    @staticmethod
    def name_test():
        stack = inspect.stack()
        file = os.path.basename(stack[2].filename)
        test = stack[2].function
        check = stack[1].function
        return f'👉[{file}] --> [{test}] -> [{check}]\n'

    #-------------------------------------------- 💾Save & Read .env ---------------------------------------------------
    # (⚠️НЕ ИСПОЛЬЗУЕТСЯ)
    # Save KEY-VALUE to .env
    @staticmethod
    def save_env(key, env_key: str):
        try:
            set_key('.env', env_key, key, quote_mode='never')
        except Exception: # NOQA
            print(f'\t{ANSI.RED}⚠️ NOT Saved to .env ⚠️: {ANSI.ORANGE}"{key}"{ANSI.RESET}')

    # (⚠️НЕ ИСПОЛЬЗУЕТСЯ)
    # Read VALUE from .env
    @staticmethod
    def read_env(env_key: str):
        key_value = dotenv_values('.env')      # ← перечитывает файл каждый раз
        return key_value.get(env_key)

    # (⚠️НЕ ИСПОЛЬЗУЕТСЯ)
    # Saving USER DATA to .env (3-in-1)
    @staticmethod
    def save_user_data(response):
        request_body = json.loads(response.request.content)
        response_body = response.json()
        Tool.save_env(request_body['clientName'], 'CLIENT_NAME')
        Tool.save_env(request_body['clientEmail'], 'CLIENT_EMAIL')
        Tool.save_env(response_body['accessToken'], 'ACCESS_TOKEN')

    #----------------------------------------- ✨API REPORT in console -------------------------------------------------
    """ ⚠️USE IN THE FINAL -> Tool.api_report(response)"""

    @staticmethod
    def api_report(response):
        Report.api_title()
        Report.api_url(response)
        Report.api_method(response)
        Report.api_status_code(response)
        Report.api_response_time(response)
        Report.api_request_body(response)
        Report.api_response_body(response)
        Report.api_request_headers(response)
        Report.api_response_headers(response)

    #-------------------------------------------------------------------------------------------------------------------
