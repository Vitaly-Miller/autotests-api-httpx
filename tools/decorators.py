"""
Pytest Decorators
"""
import time
from loguru import logger
from functools import wraps
from _pytest.outcomes import Failed
from httpx import Response
from tools.func import Tool

#=======================================================================================================================

"""--------------------------------------- Время выполнения теста (функции) ⏱ ---------------------------------------"""
def check_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()   # start |->
        func(*args, **kwargs)      # func()
        end_time = time.time()     # <-| end
        print(f' [⌛️: {round((end_time - start_time), 3)} sec]')
    return wrapper


"""----------------------------------------------------- Loguru -----------------------------------------------------"""
# Error Logger (Loguru)
# Config:
logger.remove()                                                      # удаляет все предыдущие sink-и, если модуль импортируется повторно (а то - дублирование записи)
logger.add(
    sink='logs.log',                                                 # название создаваемого файла для хранения логов
    level='INFO',                                                    # уровень логов, которые попадут в файл (TRACE > DEBUG > INFO > SUCCESS > WARNING > ERROR > CRITICAL)
    format='\n{time:MM/DD/YYYY (hh:mm:ss A)}:\n{level} | {message}', # формат вывода (время, уровень, сообщение)
    rotation='10MB',                                                 # какой объем
    retention='10days'                                               # сколько дней
)
# decorator:
def log(func):                                                       # создаем декоратор с именем <log>
    @wraps(func)                                                     # декоратор для декоратора (короче - нужен)
    def wrapper(*args, **kwargs):                                    # вложенная функция, которая принимает любые аргументы
        try:
            return func(*args, **kwargs)                             # пытаемся выполнить нашу функцию

        except Failed as e:                                          # ⚠️ pytest.fail ошибки
            logger.error(f'{func.__name__}\n{e}')                    # ... записываем ошибку в файл (имя функции + ошибка)
            raise                                                    # и вызываем системную ошибку

        except Exception as e:                                       # ⚠️ системные ошибки
            logger.error(f'{func.__name__}\n{e}')                    # ... записываем ошибку в файл (имя функции + ошибка)
            raise                                                    # и вызываем системную ошибку
    return wrapper                                                   # возвращаем декоратор


#---------------------------------------------------- API Report -------------------------------------------------------
# (Декоратор ⚠️НЕ РАБОТАЕТ - Нужен внешний response. Допилить!)
#def api_report(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        response = result or next((v for v in kwargs.values() if isinstance(v, Response)), None)
        if response is not None:
            Tool.api_report(response)
        return result
    return wrapper

#-----------------------------------------------------------------------------------------------------------------------
