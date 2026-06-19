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
        """str: The description of the pattern."""
        return self._dispatch.Description

    @description.setter
    def description(self, text):
        self._dispatch.Description = text

    @property
    def width(self):
        """int: The width of the pattern (in 1/10 mm)."""
        return self._dispatch.Width

    @width.setter
    def width(self, value):
        self._dispatch.Width = value

    @property
    def height(self):
        """int: The height of the pattern (in 1/10 mm)."""
        return self._dispatch.Height

    @height.setter
    def height(self, value):
        self._dispatch.Height = value

    @property
    def repeatable(self):
        """bool: The option of the symbol to be repeated
        to fill an entire depth interval or not.
        """
        return self._dispatch.Repeatable

    @repeatable.setter
    def repeatable(self, enable):
        self._dispatch.Repeatable = enable

    @property
    def color(self):
        """int: The color associated to the litho pattern.

        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values.
        """
        return self._dispatch.Color

    @color.setter
    def color(self, color):
        self._dispatch.Color = color
