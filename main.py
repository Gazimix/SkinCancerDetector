from src.DataProvider import DataProvider
from src.DataUtils import skin_cancer_detector_parse_dataset_full_quality, extract_images_from_csv, \
    skin_cancer_detector_parse_dataset_8_8_L, skin_cancer_detector_parse_dataset_28_28_RGB
from src.Logger import set_loggers_level

if __name__ == "__main__":
    set_loggers_level()     # Keep this line first.

    dp = DataProvider(None)
    images, labels = skin_cancer_detector_parse_dataset_28_28_RGB("archive")  # TODO-Sahar: del.


