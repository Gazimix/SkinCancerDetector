from src.DataProvider import DataProvider
from src.DataUtils import *
import matplotlib.pyplot as plt

ARCHIVE_DIR = "archive"


def set_loggers_level():
    get_logger(DATA_UTILS_LOGGER).setLevel(logging.WARN)


def plot_2_first_imgs(images, dim=8):
    image = images[0]
    image = image.reshape([dim, dim])
    plt.imshow(image)
    plt.show()
    image = images[1]
    image = image.reshape([dim, dim])
    plt.imshow(image)
    plt.show()


if __name__ == "__main__":
    dp = DataProvider(None)
    # images = skin_cancer_detector_parse_dataset_8_8_L(ARCHIVE_DIR)  # TODO-Sahar: del.
    # TODO-Sahar: del.
    images, labels = skin_cancer_detector_parse_dataset_28_28_L(ARCHIVE_DIR)
    print(images)
    print(labels)
    plot_2_first_imgs(images, 28)
