"""
Logger (by logging)
"""
import logging

#=======================================================================================================================
def get_logger(name: str, console: bool = False) -> logging.Logger:
    """
    Создает и настраивает Logger

    .
    """
    # 1.Logger
    logger = logging.getLogger(name)         # Создаем Logger и присваиваем ему динамическое название name (из функции)
    logger.setLevel(logging.DEBUG)           # Уровень (глубина) логирования - DEBUG и выше (все)

    # 2.Handler
    handler = logging.StreamHandler()        # Создаем Handler (обработчик) - StreamHandler
    handler.setLevel(logging.DEBUG)          # Уровень (глубина) логирования - DEBUG и выше (все)

    # 3.Formatter                     время        имя         уровень       сообщение
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')   # Форматирование логов

    # 4.ADD
    handler.setFormatter(formatter)          # Добавляем Handler (обработчик) в Formatter

    if console:                              # Условие, если console=True (default - False)
        logger.addHandler(handler)           # Выводить log в консоль

    return logger

"""
# Example
logger = get_logger('TEST')                           # Инициализация Logger + Имя
logger.info('Получение клиента')                      # 2026-07-07 20:35:47,164 | TEST | INFO | Получение клиента
logger.info('Выполнение теста')                       # 2026-07-07 20:35:47,167 | TEST | INFO | Выполнение теста
"""
#=======================================================================================================================
