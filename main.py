import logging

from src.DataProvider import DataProvider
from src.DataUtils import *
from src.Logger import get_logger, DATA_UTILS_LOGGER
import matplotlib.pyplot as plt
import imageio

ARCHIVE_DIR = "archive"


def set_loggers_level():
    get_logger(DATA_UTILS_LOGGER).setLevel(logging.WARN)


def plot_2_first_imgs(images):
    image = images[0]
    image = image.reshape([28, 28])
    plt.imshow(image, cmap='Greys')
    plt.show()
    image = images[1]
    image = image.reshape([28, 28])
    plt.imshow(image, cmap='Greys')
    plt.show()


if __name__ == "__main__":
    set_loggers_level()     # Keep this line first.

    dp = DataProvider(None)
    # images = skin_cancer_detector_parse_dataset_8_8_L(ARCHIVE_DIR)  # TODO-Sahar: del.
    # TODO-Sahar: del.
    images, labels = skin_cancer_detector_parse_dataset_28_28_L(ARCHIVE_DIR)
    print(images)
    print(labels)