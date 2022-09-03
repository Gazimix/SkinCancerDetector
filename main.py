import logging

from src.DataProvider import DataProvider
from src.DataUtils import skin_cancer_detector_parse_dataset_full_quality
from src.Logger import get_logger, DATA_UTILS_LOGGER


def set_loggers_level():
    get_logger(DATA_UTILS_LOGGER).setLevel(logging.WARN)


if __name__ == "__main__":
    set_loggers_level()     # Keep this line first.

    dp = DataProvider(None)
    skin_cancer_detector_parse_dataset_full_quality("archive")  # TODO-Sahar: del.


