from ._dispatch_wrapper import DispatchWrapper


class AttributeCategory(DispatchWrapper):
    """Represents a category belonging to the dictionary of an attribute (AttributeDictionary).

    Example
    -------
    log = borehole.log("Structure")
    dictionary = log.get_attribute_dictionary(log.get_attribute_name(0))
    category = dictionary.attribute_category(0)
    category.code
    """

    @property
    def code(self):
        """str: The code of the attribute category."""
        return self._dispatch.Code

    @property
    def description(self):
        """str: The description of the category."""
        return self._dispatch.Description

    @description.setter
    def description(self, text):
        self._dispatch.Description = text

    @property
    def body_style(self):
        """int: The index corresponding to the style of the tadpole's body.
        * 1: Circle
        * 2: Lozange
        * 3: Square
        * 4: Triangle
        * 5: Breakout
        * 6: Star
        """
        return self._dispatch.BodyStyle

    @body_style.setter
    def body_style(self, index):
        self._dispatch.BodyStyle = index

    @property
    def body_size(self):
        """int: The index corresponding to the size of the body.
        3 options:
        * 0: Small body
        * 1: Medium body
        * 2: Big body
        """
        return self._dispatch.BodySize

    @body_size.setter
    def body_size(self, size):
        self._dispatch.BodySize = size

    @property
    def tail_style(self):
        """int: The index corresponding to the style of the tadpole's tail.
        * 0: Flat
        * 1: Curved
        * 2: Incomplete
        * 3: Bifide
        """
        return self._dispatch.TailStyle

    @tail_style.setter
    def tail_style(self, index):
        self._dispatch.TailStyle = index

    @property
    def tail_size(self):
        """int: The index corresponding to the size of the tadpole's tail.
        * 0: No tail
        * 1: Small tail
        * 2: Medium tail
        * 3: Big tail
        """
        return self._dispatch.TailSize

    @tail_size.setter
    def tail_size(self, size):
        self._dispatch.TailSize = size

    @property
    def tail_color(self):
        """int: The color of the tadpole's tail.

        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values. Other allowed values are : 0xFFFFFFFF (None) and 0xFF000000 (automatic color).
        """
        return self._dispatch.TailColor

    @tail_color.setter
    def tail_color(self, color):
        self._dispatch.TailColor = color

    @property
    def color(self):
        """int: The color of the tadpole's body.

        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values. Other allowed values are : 0xFFFFFFFF (None) and 0xFF000000 (automatic color).
        """
        return self._dispatch.Color

    @color.setter
    def color(self, color):
        self._dispatch.Color = color

    @property
    def sine_style(self):
        """int: The index corresponding to the style of the sinusoid.
        * 0: Solid
        * 1: Dashed
        * 2: Dot
        * 3: Dash-Dot
        * 4: Dash-Dot-Dot
        """
        return self._dispatch.SineStyle

    @sine_style.setter
    def sine_style(self, index):
        self._dispatch.SineStyle = index

    @property
    def sine_width(self):
        """int: The width of the sinusoid (in mm/10)."""
        return self._dispatch.SineWidth

    @sine_width.setter
    def sine_width(self, width):
        self._dispatch.SineWidth = width
