from abc import ABC


class Classifier(ABC):
    """
    Base class for classifiers.
    """

    def fit(self, x, y, **kwargs):
        pass

    def predict(self, x, **kwargs):
        pass

    def get_hyperparams(self):  # TODO-Sahar: Check if this is necessary.
        pass