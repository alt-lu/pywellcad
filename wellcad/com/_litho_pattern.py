from ._dispatch_wrapper import DispatchWrapper


class LithoPattern(DispatchWrapper):
    """Represents a lithological pattern. These are patterns within a litho dictionary (LithoDictionary).

    You can find more information on your defined lithologies in your LithCAD library.

    Example
    -------
    >>> log = borehole.log("Lithology")
    >>> dictionary = log.litho_dictionary
    >>> pattern = dictionary.litho_pattern(0)
    >>> pattern.code
    'Sst'
    """

    @property
    def code(self):
        """str: The lithological code of the pattern.

        You can use the LithCAD tool to see your lithological
        symbols and associated codes."""
        return self._dispatch.Code

    @property
    def description(self):
        """str: The description ot the pattern."""
        return self._dispatch.Description

    @property
    def width(self):
        """int: The width of the pattern (in 1/10 mm)."""
        return self._dispatch.Width

    @property
    def height(self):
        """int: The height of the pattern (in 1/10 mm)."""
        return self._dispatch.Height

    @property
    def repeatable(self):
        """bool: The option of the symbol to be repeated
        to fill an entire depth interval or not.
        """
        return self._dispatch.Repeatable
