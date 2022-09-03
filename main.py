from src.DataProvider import DataProvider
from src.DataUtils import *
import matplotlib.pyplot as plt

ARCHIVE_DIR = "archive"


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
    dp = DataProvider(None)
    # images = skin_cancer_detector_parse_dataset_8_8_L(ARCHIVE_DIR)  # TODO-Sahar: del.
    # TODO-Sahar: del.
    images, labels = skin_cancer_detector_parse_dataset_28_28_L(ARCHIVE_DIR)
    print(images)
    print(labels)
    images, labels = skin_cancer_detector_parse_dataset_28_28_RGB("archive")  # TODO-Sahar: del.


