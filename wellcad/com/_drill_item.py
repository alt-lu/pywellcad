from ._dispatch_wrapper import DispatchWrapper


class DrillItem(DispatchWrapper):
    """ A Drill Item found in an engineering log gives information about the dimensions of the drilled borehole.

    The drill item gives information about the diameter and length of the borehole. You can have multiple drill items
    in a borehole if the diameter varies at certain depths. Only a bottom depth is specified: it will range from the
    top of the borehole (at depth 0) to the specified bottom_depth OR if another drill item is present above,
    it will range from the bottom of the other drill to the bottom_depth of the current drill.

    Example
    -------
    >>> log = borehole.log("Well Sketch")
    >>> drill_item = log.drill_item(0)
    >>> drill_item.diameter
    300
    >>> drill_item.comment
    'Drill
    0.00-15.00
    diameter:300'
    """
    @property
    def bottom_depth(self):
        """float: The bottom depth of the drill in current depth units."""
        return self._dispatch.BottomDepth

    @bottom_depth.setter
    def bottom_depth(self, value):
        self._dispatch.BottomDepth = value

    @property
    def diameter(self):
        """float: The diameter of the drill in arbitrary units.

        Note that some other dimensions in an engineering log are
        relative to this measure."""
        return self._dispatch.Diameter

    @diameter.setter
    def diameter(self, value):
        self._dispatch.Diameter = value

    @property
    def comment(self):
        """str: The comment associated with the drill item."""
        return self._dispatch.Comment

    @comment.setter
    def comment(self, value):
        self._dispatch.Comment = value
