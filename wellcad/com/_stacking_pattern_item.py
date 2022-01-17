from ._dispatch_wrapper import DispatchWrapper


class StackingPatternItem(DispatchWrapper):
    """Stores a stacking pattern over an interval.

    StackingPattern items are part of a StackingPattern Log and stores the top and bottom widths
    over a depth interval.
    Width values are between 0.0 and 1.0 and depth intervals can not overlap.

    Example
    -------
    >>> stack_log = borehole.log("Test")
    >>> stack_box = stack_box.insert_new_stack_item(10.5, 12.5, 0.5, 0.8)
    >>> stack_box.top_depth
    10.5
    >>> stack_box.top_depth
    12.5
    """

    @property
    def top_depth(self):
        """float: The top depth of the item in current depth
        units."""
        return self._dispatch.TopDepth

    @property
    def bottom_depth(self):
        """float: The bottom depth of the item in current depth
        units."""
        return self._dispatch.BottomDepth

    @property
    def top_width(self):
        """float: The top width of the item.
        
        This should be a value between 0.0 and 1.0. Setting it out of these
        bounds will clamp the value.
        """
        return self._dispatch.TopWidth

    @top_width.setter
    def top_width(self, value):
        self._dispatch.TopWidth = value

    @property
    def bottom_width(self):
        """float: The bottom width of the item.
        
        This should be a value between 0.0 and 1.0. Setting it out of these
        bounds will clamp the value.
        """
        return self._dispatch.BottomWidth

    @bottom_width.setter
    def bottom_width(self, value):
        self._dispatch.BottomWidth = value
