from ._dispatch_wrapper import DispatchWrapper


class ClassifierItem(DispatchWrapper):
    """Represents a classifier item associated to a log.
    Example
    -------
    log = borehole.log("Lithology from GR Classification")
    dictionary = log.classifier_dictionary
    classifier = dictionary.classifier_item(0)
    """

    @property
    def name(self):
        """str: The name of the classifier."""
        return self._dispatch.Name

    @property
    def low_value(self):
        """float: The low value of the classifier item."""
        return self._dispatch.LowValue

    @low_value.setter
    def low_value(self, value):
        self._dispatch.LowValue = value

    @property
    def high_value(self):
        """float: The high value of the classifier item."""
        return self._dispatch.HighValue

    @high_value.setter
    def high_value(self, value):
        self._dispatch.HighValue = value

    @property
    def color(self):
        """int: The color associated to the classifier item.

        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values.
        """
        return self._dispatch.Color

    @color.setter
    def color(self, color):
        self._dispatch.Color = color
