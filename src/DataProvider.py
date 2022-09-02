from gc import callbacks
from typing import Callable
from sklearn.model_selection import train_test_split


class DataProvider:
    def __init__(self, callback: Callable):
        """
        Ctor for the data provider class which prepares testing, validation & training datasets.

        Args:
            callback (Callable): a ptr to a function that returns a tuple: (images: np.ndarray, metadata: pandas)
        """
        self.process_cb = callback
        self._training_images = []
        self._training_metadata = []
        self._test_images = []
        self._test_metadata = []
        
    def prepare_data(self):
        pass

    def get_validation_dataset(self):
        pass

    def get_test_dataset(self):
        # Inside one x there is an image and the sex and the place and the ... 
        # Inside one y there is is "mel or benign" for that x.
        return self.x_test, self.y_test
        pass

    def get_training_dataset(self):
        pass