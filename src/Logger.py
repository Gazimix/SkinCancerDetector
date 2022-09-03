import logging
import os
import sys
from functools import lru_cache

LOG_FILENAME = 'logs/logging.log'
# LOG_FORMAT = "[%(levelname)-5s : '%(name)-20s' : %(asctime)20s : %(processName)-10s : %(threadName)-10s : func='%(funcName)-25s'] - %(message)s"
LOG_FORMAT = "[%(levelname)-5s : '%(name)-20s' : %(asctime)20s] - %(message)s"

# Logger names:
DATA_UTILS_LOGGER = "DataUtils"


@lru_cache
def get_logger(logger_name):
    if not os.path.exists('logs'):
        os.mkdir("logs")

    logger = logging.getLogger(logger_name)

    file_handler = logging.FileHandler(LOG_FILENAME)
    file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(file_handler)

    handler_stdout = logging.StreamHandler(sys.stdout)
    handler_stdout.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(handler_stdout)

    return logger


def set_loggers_level():
    get_logger(DATA_UTILS_LOGGER).setLevel(logging.WARN)
