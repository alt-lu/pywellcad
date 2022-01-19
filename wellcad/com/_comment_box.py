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

