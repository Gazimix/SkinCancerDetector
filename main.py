import numpy as np
from src.DataProvider import DataProvider
from src.DataUtils import skin_cancer_detector_parse_dataset_full_quality

if __name__ == "__main__":
    dp = DataProvider(None)
    skin_cancer_detector_parse_dataset_full_quality("archive")  # TODO-Sahar: del.


