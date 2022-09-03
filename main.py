from src.DataProvider import DataProvider
from src.DataUtils import *
import matplotlib.pyplot as plt

ARCHIVE_DIR = "archive"


def plot_2_first_imgs(images, dim=8):
    image = images[0]
    plt.imshow(image)
    plt.show()
    image = images[1]
    plt.imshow(image)
    plt.show()


if __name__ == "__main__":
    dp = DataProvider(None)
    images, labels = skin_cancer_detector_parse_dataset_28_28_RGB(ARCHIVE_DIR)
    plot_2_first_imgs(images, 28)
