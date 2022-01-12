from ._dispatch_wrapper import DispatchWrapper


class IntervalItem(DispatchWrapper):
    """ Stores a value that spans a depth interval.

    Interval items are part of an Interval Log and store a single data value.
    Only numerical values are supported and depth intervals may overlap.

    Example
    -------
    >>> interval_log = borehole.log("Test")
    >>> data = interval_log.interval_item_at_depth(10.5)
    >>> data.value
    23.45
    >>> data.top_depth
    9.0
    """

    @property
    def top_depth(self):
        """float: The top depth of the interval item in current
        depth reference units"""
        return self._dispatch.TopDepth

    @property
    def bottom_depth(self):
        """float: The bottom depth of the interval item in current
        depth reference units"""
        return self._dispatch.BottomDepth

    @property
    def value(self):
        """float: The value of the interval item."""
        return self._dispatch.Value

    @value.setter
    def value(self, value):
        self._dispatch.Value = value


