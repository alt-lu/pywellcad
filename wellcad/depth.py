class Depth:

    def __init__(self, depth_dispatch):
        """Returns a Depth object.
        
        Use the get_depth method of the bore hobject to retrieve the
        Depth object.
        """

        self.dispatch = depth_dispatch
    

    @property
    def unit(self):
        """Returns 0 = meter or 1 = feet."""
        return self.dispatch.Unit


    @unit.setter
    def unit(self, unit):
        """Sets the depth axis unit.
        
        Arguments:
            unit -- Set 0 for meter or 1 for feet.
        """

        self.dispatch.Unit = unit


    @property
    def depth_reference(self):
        """Status of the documents reference axis.

        Returns:
            True if the master depth axis is the current reference scale.
        """

        return self.dispatch.UsedAsDepthScale

    
    @depth_reference.setter
    def depth_reference(self, enable):
        """Sets the documents reference axis scale status.
        
        Arguments:
            enable -- If set to True the master depth axis becomes the
                      reference axis of the document.
        """

        self.dispatch.UsedAsDepthScale = enable


    @property
    def scale(self):
        """Returns 100 for a 1:100 depth scale."""
        return self.dispatch.Scale


    @scale.setter
    def scale(self, scale):
        """Sets the depth axis scale.
        
        Arguments:
            scale -- Set 100 for a scale of 1:100.
        """

        self.dispatch.Scale = scale


    @property
    def decimals(self):
        """Returns the number of decimals displayed for the depth."""
        return self.dispatch.Decimals


    @decimals.setter
    def decimals(self, decimals):
        """Sets the number of decimals displayed in the depth axis.
        
        Arguments:
            decimals -- Set 1 for 0.1, 2 for 0.01, 3 for 0.001 etc..
        """

        self.dispatch.Decimals = decimals
    

    @property
    def horizontal_grid_type(self):
        """Returns the type of horizontal grid used.
        
        Returns:
            0 - No grid
            1 - Major grid only
            2 - Major & Minor grid
        """

        return self.dispatch.HorizontalGrid


    @horizontal_grid_type.setter
    def horizontal_grid_type(self, grid_type):
        """Sets the type of horiz. grid lines displayed.
        
        Arguments:
            grid_type -- 0 = None, 1 = Major, 2 = Major & Minor.
        """

        self.dispatch.HorizontalGrid = grid_type

    
    @property
    def horizontal_grid_spacing(self):
        """Returns the spacing of horizontal grid lines."""
        return self.dispatch.HorizontalGridSpacing


    @horizontal_grid_spacing.setter
    def horizontal_grid_spacing(self, grid_spacing):
        """Sets the spacing of the horiz. grid lines displayed.
        
        Arguments:
            grid_spacing -- E.g. 1 = every meter or ft.
        """

        self.dispatch.HorizontalGridSpacing = grid_spacing

    
    def set_position(self, left_pos, right_pos):
        """Adjusts the left / right border of the depth axis column.
        
        Arguments:
            left_pos -- Value between 0 and 1 (= 100% document width).
            right_pos -- Value between 0 and 1 (= 100% document width).
        """
        self.dispatch.SetPosition(left_pos, right_pos)
        
        
    @property
    def left_position(self):
        """Returns the left border of the depth axis column."""
        return self.dispatch.LeftPosition


    @left_position.setter
    def left_position(self, left_pos):
        """Adjusts the left border of the depth axis column.
        
        Arguments:
            left_pos -- Value between 0 and 1 (= 100% document width).
        """
        self.dispatch.LeftPosition = left_pos


    @property
    def right_position(self):
        """Returns the right border of the depth axis column."""
        return self.dispatch.RightPosition


    @right_position.setter
    def right_position(self, right_pos):
        """Adjusts the right border of the depth axis column.
        
        Arguments:
            right_pos -- Value between 0 and 1 (= 100% document width).
        """
        self.dispatch.RightPosition = right_pos