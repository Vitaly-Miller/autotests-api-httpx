"""
Logger (settings)
"""
import logging

#=======================================================================================================================
def get_logger(name: str) -> logging.Logger:
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
    logger.addHandler(handler)               # Добавляем Handler (обработчик) в Logger

    return logger                            # logging.Logger

"""
# Example
logger = get_logger('TEST')                           # Инициализация Logger + Имя
logger.info('Получение клиента')                      # 2026-07-07 20:35:47,164 | TEST | INFO | Получение клиента
logger.info('Выполнение теста')                       # 2026-07-07 20:35:47,164 | TEST | INFO | Выполнение теста
"""
#=======================================================================================================================
