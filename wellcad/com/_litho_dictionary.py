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

    _DISPATCH_METHODS = ("LithoPattern",)

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



