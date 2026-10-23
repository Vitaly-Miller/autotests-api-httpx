"""
Logger (via logging)
"""
import logging

#=======================================================================================================================
def get_logger(name: str, console: bool = False) -> logging.Logger:
    """
    Creates and configures a Logger via logging

    :param name: Logger name
    :param console: Whether to output the log to the console (default = False)
    :return: logging.Logger
    """
    # 1.Logger
    logger = logging.getLogger(name)         # Create Logger and give it a dynamic name (from the function)
    logger.setLevel(logging.DEBUG)           # Logging level (depth) - DEBUG and above (all)

    # 2.Handler
    handler = logging.StreamHandler()        # Create Handler - StreamHandler
    handler.setLevel(logging.DEBUG)          # Logging level (depth) - DEBUG and above (all)

    # 3.Formatter                     time         name        level         message
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')   # Log formatting

    # 4.ADD
    handler.setFormatter(formatter)          # Set Formatter on Handler

    if console:                              # If console=True (default - False)
        logger.addHandler(handler)           # Output log to console

    return logger


#=======================================================================================================================
