from ._dispatch_wrapper import DispatchWrapper
from ._litho_pattern import LithoPattern


class LithoDictionary(DispatchWrapper):
    """A dictionary containing patterns used to represent lithologies.

    You can find more information on your defined lithologies in your LithCAD library.

    Example
    -------
    >>> log = borehole.log("Lithology")
    >>> dict = log.litho_dictionary
    >>> dict.name
    'Sst'
    >>> dict.nb_of_patterns
    12
    """

    _DISPATCH_METHODS = ("LithoPattern", "AddPattern", "RemovePattern")

    @property
    def name(self):
        """str: The name of the dictionary."""
        return self._dispatch.Name

    @name.setter
    def name(self, value):
        self._dispatch.Name = value

    @property
    def nb_of_patterns(self):
        """int: The number of patterns in the dictionary."""
        return self._dispatch.NbOfPatterns

    def is_pattern(self, code):
        """Checks if the dictionary contains a pattern with the specified code.

        Parameters
        ----------
        code : str
            The code of the pattern.

        Returns
        -------
        bool
            True if successful, False otherwise.
        """
        return self._dispatch.IsPattern(code)

    def litho_pattern(self, index_or_code):
        """Gets a pattern by index or by code.

        Parameters
        ----------
        index_or_code : int or str
            The index or the code of the pattern

        Returns
        -------
        LithoPattern
            The LithoPattern object.
        """
        return LithoPattern(self._dispatch.LithoPattern(index_or_code))

    def add_pattern(self):
        """Adds and returns a new pattern using default settings.
        Default settings:
        * Code: #x (x >= 1)
        * Color: black
        * Pattern: none
        * Description:

        Returns
        -------
        LithoPattern
            The new LithoPattern object.
        """
        return LithoPattern(self._dispatch.AddPattern())

    def remove_pattern(self, index_or_code):
        """Removes the pattern corresponding to the index or code.

        Parameters
        ----------
        index_or_code : int or str
            The index or the code of the pattern

        Returns
        -------
        BOOL
            Whether the targeted pattern has been removed from the dictionary or not.
        """
        return self._dispatch.RemovePattern(index_or_code)



