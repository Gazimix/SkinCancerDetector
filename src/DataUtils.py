from pathlib import Path
import pandas as pd
import numpy as np
import imageio
import os
import logging

from matplotlib import pyplot as plt
from tqdm import tqdm

from src.Logger import get_logger

HAM10000_METADATA = "HAM10000_metadata.csv"
HMNIST_IMG_DIRS_FULL_QUALITY = ["HAM10000_images_part_1", "HAM10000_images_part_2"]
HMNIST_IMG_8_8_L = "hmnist_8_8_L.csv"
HMNIST_IMG_8_8_RGB = "hmnist_8_8_RGB.csv"
HMNIST_IMG_28_28_L = "hmnist_28_28_L.csv"
HMNIST_IMG_28_28_RGB = "hmnist_28_28_RGB.csv"


def extract_images_from_csv(path_to_csv: Path, img_channels):
    df = pd.read_csv(path_to_csv)
    df_to_numpy = df.to_numpy()
    labels: np.ndarray = df_to_numpy[:, -1]
    images: np.ndarray = df_to_numpy[:, :-1]
    if img_channels == 1:
        img_dim = int(math.sqrt(images.shape[1]))
        images = images.reshape((len(labels), img_dim, img_dim))
    else:
        img_dim = int(math.sqrt(images.shape[1] // img_channels))
        images = images.reshape((len(labels), img_dim, img_dim, img_channels))
    return images, labels


def skin_cancer_detector_parse_dataset_full_quality(archive_path_str: str):
    """
    Parse the full_quality_dataset.csv file.

    :param archive_path_str: The path to the archive dataset directory.
    :return:
    """
    logger = get_logger("DataUtils")
    sample_counter = 0

    archive_path = Path(archive_path_str)
    metadata_df = pd.read_csv(archive_path / HAM10000_METADATA)
    images_paths = []
    for i in range(len(HMNIST_IMG_DIRS_FULL_QUALITY)):
        images_dir = HMNIST_IMG_DIRS_FULL_QUALITY[i]
        for img_name in os.listdir(archive_path / images_dir):
            if sample_counter == n_samples:
                break
            img_path = archive_path / images_dir / img_name
            images_paths.append(img_path)
            sample_counter += 1

    images = []
    for img_path in tqdm(images_paths):
        if logger.isEnabledFor(logging.INFO):
            logger.info(f"Loaded image: {img_path}")
        images.append(imageio.imread_v2(img_path))
    return images, metadata_df


def skin_cancer_detector_parse_dataset_8_8_L(archive_path_str: str):
    archive_path = Path(archive_path_str)
    path_to_csv = archive_path / HMNIST_IMG_8_8_L
    return extract_images_from_csv(path_to_csv, 1)


def skin_cancer_detector_parse_dataset_8_8_RGB(archive_path_str):
    archive_path = Path(archive_path_str)
    path_to_csv = archive_path / HMNIST_IMG_8_8_RGB
    return extract_images_from_csv(path_to_csv, 3)


def skin_cancer_detector_parse_dataset_28_28_L(archive_path_str: str):
    archive_path = Path(archive_path_str)
    path_to_csv = archive_path / HMNIST_IMG_28_28_L
    return extract_images_from_csv(path_to_csv, 1)

def skin_cancer_detector_parse_dataset_28_28_RGB(archive_path_str: str):
    archive_path = Path(archive_path_str)
    path_to_csv = archive_path / HMNIST_IMG_28_28_RGB
    return extract_images_from_csv(path_to_csv, 3)
