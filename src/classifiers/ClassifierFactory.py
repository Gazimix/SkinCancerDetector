from typing import List

from src.classifiers.Classifier import Classifier


class ClassifierFactory:
    """
    Factory for creating classifiers.
    """

    @staticmethod
    def create(name: str, **kwargs) -> Classifier:
        """
        Create a classifier.

        :param name: The name of the classifier.
        :param kwargs: The keyword arguments for the classifier.
        """
        pass
        # return Classifier(name, **kwargs)

    def get_all_classifiers(self) -> List[Classifier]:
        """
        Get all classifiers.

        :return: A list of all classifiers.
        """
        return []   # TODO-Sahar: