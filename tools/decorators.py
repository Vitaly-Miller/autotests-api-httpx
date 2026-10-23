"""
Pytest Decorators
(⚠️Does not use in current project)
"""
import time
from loguru import logger
from functools import wraps
from _pytest.outcomes import Failed

#=======================================================================================================================
#------------------------------------------ Test (function) execution time ⏱ ---------------------------------------------
def check_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()   # start |->
        func(*args, **kwargs)      # func()
        end_time = time.time()     # <-| end
        print(f' [⌛️: {round((end_time - start_time), 3)} sec]')
    return wrapper


#------------------------------------------------------- Loguru --------------------------------------------------------
# Error Logger (Loguru)
# Config:
logger.remove()                                                      # removes all previous sinks if the module is re-imported (otherwise records are duplicated)
logger.add(
    sink='logs.log',                                                 # name of the log file to create
    level='INFO',                                                    # level of logs written to the file (TRACE > DEBUG > INFO > SUCCESS > WARNING > ERROR > CRITICAL)
    format='\n{time:MM/DD/YYYY (hh:mm:ss A)}:\n{level} | {message}', # output format (time, level, message)
    rotation='10MB',                                                 # size limit
    retention='10days'                                               # how many days
)
# decorator:
def log(func):                                                       # create a decorator named <log>
    @wraps(func)                                                     # decorator for the decorator (in short - needed)
    def wrapper(*args, **kwargs):                                    # inner function that accepts any arguments
        try:
            return func(*args, **kwargs)                             # try to execute our function

        except Failed as e:                                          # ⚠️ pytest.fail errors
            logger.error(f'{func.__name__}\n{e}')                    # ... write error to file (function name + error)
            raise                                                    # and re-raise the error

        except Exception as e:                                       # ⚠️ system errors
            logger.error(f'{func.__name__}\n{e}')                    # ... write error to file (function name + error)
            raise                                                    # and re-raise the error
    return wrapper                                                   # return the decorator


#=======================================================================================================================
