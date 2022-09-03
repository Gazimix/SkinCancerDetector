from pathlib import Path
import pandas as pd
import imageio
import os
import logging

from tqdm import tqdm

from src.Logger import get_logger

HAM10000_METADATA = "HAM10000_metadata.csv"
HMNIST_IMG_DIRS_FULL_QUALITY = ["HAM10000_images_part_1", "HAM10000_images_part_2"]
HMNIST_IMG_8_8_L = "hmnist_8_8_L.csv"
HMNIST_IMG_8_8_RGB = "hmnist_8_8_RGB.csv"
HMNIST_IMG_28_28_L = "hmnist_28_28_L.csv"
HMNIST_IMG_28_28_RGB = "hmnist_28_28_RGB.csv"



def skin_cancer_detector_parse_dataset_full_quality(archive_path_str: str):
    """
    Parse the full_quality_dataset.csv file.

    :param archive_path_str: The path to the archive dataset directory.
    :return:
    """
    logger = get_logger("DataUtils")

    archive_path = Path(archive_path_str)
    metadata_df = pd.read_csv(archive_path / HAM10000_METADATA)
    images_paths = []
    for i in range(len(HMNIST_IMG_DIRS_FULL_QUALITY)):
        images_dir = HMNIST_IMG_DIRS_FULL_QUALITY[i]
        for img_name in os.listdir(archive_path / images_dir):
            img_path = archive_path / images_dir / img_name
            images_paths.append(img_path)

    images = {}
    for img_path in tqdm(images_paths):
        if logger.isEnabledFor(logging.INFO):
            logger.info(f"Loaded image: {img_path}")
        images[img_path.stem] = imageio.imread_v2(img_path)
    return images, metadata_df


def skin_cancer_detector_parse_dataset_8_8_L(archive_path):
    pass


def skin_cancer_detector_parse_dataset_8_8_RGB(archive_path):
    pass


def skin_cancer_detector_parse_dataset_28_28_L(archive_path):
    pass


def skin_cancer_detector_parse_dataset_28_28_RGB(archive_path):
    pass


def skin_cancer_detector_parse_dataset_(archive_path):
    pass

