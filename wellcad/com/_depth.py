from ._dispatch_wrapper import DispatchWrapper


class Depth(DispatchWrapper):
    """ The reference/master vertical axis. Can be in depth or time.

    Depth objects allow setting properties for the master depth axis
    such as scale, unit, decimals, ….

    Example
    -------
    >>> import wellcad.com
    >>> app = wellcad.com.Application()
    >>> app.new_borehole()
    <wellcad.com._borehole.Borehole object at 0x0000018B3DAF9D30>
    >>> borehole = app.get_active_borehole()
    >>> depth = borehole.depth
    """

    @property
    def decimals(self):
        """int: the number of decimals displayed in the depth string of the master depth axis."""
        return self._dispatch.Decimals

    @decimals.setter
    def decimals(self, decimals):
        self._dispatch.Decimals = decimals

    @property
    def horizontal_grid_spacing(self):
        """float: The depth grid spacing for the master depth axis"""
        return self._dispatch.HorizontalGridSpacing

    @horizontal_grid_spacing.setter
    def horizontal_grid_spacing(self, grid_spacing):
        self._dispatch.HorizontalGridSpacing = grid_spacing

    @property
    def scale(self):
        """float: The depth scale used for the master depth axis.
        
        The resulting scale is 1:``scale``.
        
        Example
        -------
        >>> depth.scale = 100 # Scale is 1:100
        """
        return self._dispatch.Scale

    @scale.setter
    def scale(self, scale):
        self._dispatch.Scale = scale

    @property
    def used_as_depth_scale(self):
        """bool: Whether this depth scale is used as the current reference axis."""
        return self._dispatch.UsedAsDepthScale

    @used_as_depth_scale.setter
    def used_as_depth_scale(self, enable):
        self._dispatch.UsedAsDepthScale = enable

    @property
    def horizontal_grid(self):
        """int: The depth grid type.

        The available types are the following:

        * 0 = none
        * 1 = major grid lines only
        * 2 = major & minor grid lines
        """
        return self._dispatch.HorizontalGrid

    @horizontal_grid.setter
    def horizontal_grid(self, grid_type):
        self._dispatch.HorizontalGrid = grid_type

    @property
    def left_position(self):
        """float: The left position of the master depth column border
        relative to the document width (value between 0 and 1)."""
        return self._dispatch.LeftPosition

    @left_position.setter
    def left_position(self, left_pos):
        self._dispatch.LeftPosition = left_pos

    @property
    def right_position(self):
        """float: The right position of the master depth column border
        relative to the document width (value between 0 and 1)."""
        return self._dispatch.RightPosition

    @right_position.setter
    def right_position(self, right_pos):
        self._dispatch.RightPosition = right_pos

    @property
    def unit(self):
        """int: The depth unit

        The available units are the following:

        * 0 = meter
        * 1 = feet
        """
        return self._dispatch.Unit

    @unit.setter
    def unit(self, unit):
        self._dispatch.Unit = unit



    def set_position(self, left_pos, right_pos):
        """Set the left and right position of the master depth
        column border relative to the document width (value between 0 and 1).
        
        Parameters
        ----------
        left_pos : float
            A value between 0 and 1 indicating the left depth
            column border relative to the document width.
        right_pos : float
            A value between 0 and 1 indicating the right
            depth column border relative to the document width.
        """
        self._dispatch.SetPosition(left_pos, right_pos)

