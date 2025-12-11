from ._dispatch_wrapper import DispatchWrapper


class CommentBox(DispatchWrapper):
    @property
    def top_depth(self):
        """float: The top depth of the comment box in current depth
        units."""
        return self._dispatch.TopDepth

    @property
    def bottom_depth(self):
        """float: The bottom depth of the comment box in current depth
        units."""
        return self._dispatch.BottomDepth

    @property
    def text(self):
        """str: The text of the comment box."""
        return self._dispatch.Text

    @text.setter
    def text(self, value):
        self._dispatch.Text = value

    @property
    def color(self):
        """int: The color of the box.

        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values.
        """
        return self._dispatch.Color

    @color.setter
    def color(self, color):
        self._dispatch.Color = color