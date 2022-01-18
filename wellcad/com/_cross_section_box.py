from ._dispatch_wrapper import DispatchWrapper


class CrossSectionBox(DispatchWrapper):
    """ Stores a depth interval over which a cross section from an image log is created.

    CrossSection boxes are part of a CrossSection Log and stores a depth interval.
    Top and bottom depths of the intervals can be the same.

    Example
    -------
    >>> cross_log = borehole.log("Test")
    >>> cross_box = cross_log.insert_new_cross_box(10.5, 12.5)
    >>> data.top_depth
    10.5
    >>> data.top_depth
    12.5
    """

    @property
    def top_depth(self):
        """float : The top depth of the box in current
        depth reference units."""
        return self._dispatch.TopDepth

    @property
    def bottom_depth(self):
        """float : The bottom depth of the box in current
        depth reference units."""
        return self._dispatch.BottomDepth


