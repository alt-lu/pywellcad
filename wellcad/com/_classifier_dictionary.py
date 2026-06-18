from ._dispatch_wrapper import DispatchWrapper
from ._classifier_item import ClassifierItem

class ClassifierDictionary(DispatchWrapper):
    """A dictionary containing the different classifiers of a Well/Mud/Interval Log.
    Example
    -------
    log = borehole.log("Lithology from GR Classification")
    dict = log.classifier_dictionary
    """

    _DISPATCH_METHODS = ("Classifier", "AddClassifier", "RemoveClassifier")

    @property
    def name(self):
        """str: The name of the dictionary."""
        return self._dispatch.Name

    @name.setter
    def name(self, value):
        self._dispatch.Name = value

    @property
    def nb_of_classifiers(self):
        """int: The number of classifiers in the dictionary."""
        return self._dispatch.NbOfClassifiers

    def classifier_item(self, index_or_name):
        """Gets a classifier item by index or by name.

        Parameters
        ----------
        index_or_name : int or str
            The index or the name of the classifier item

        Returns
        -------
        ClassifierItem
            The ClassifierItem object.
        """
        return ClassifierItem(self._dispatch.Classifier(index_or_name))

    def add_classifier(self):
        """Adds and returns a new classifier item using default settings.
        Default settings:
        * Name: Class
        * Color: black
        * Low value: 0
        * High value: 1

        Returns
        -------
        ClassifierItem
            The new ClassifierItem object.
        """
        return ClassifierItem(self._dispatch.AddClassifier())

    def remove_classifier(self, index_or_name):
        """Removes the classifier item corresponding to the index or code.

        Parameters
        ----------
        index_or_code : int or str
            The index or the code of the classifier item.

        Returns
        -------
        BOOL
            Whether the targeted classifier item has been removed from the dictionary or not.
        """
        return self._dispatch.RemoveClassifier(index_or_name)



