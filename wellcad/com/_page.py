from ._noneable_wrapper import NoneableWrapper

class Page(NoneableWrapper):
    @property
    def length(self):
        """Returns the document height in mm."""
        return self._dispatch.DocumentHeight
    

    @property
    def width(self):
        """Returns the document width in mm."""
        return self._dispatch.DocumentHeight


    @width.setter
    def width(self, value):
        """Sets the width of the borehole document in mm.
        
        Arguments:
            value -- E.g. set it to 190 for a 190mm wide document.

        """

        self._dispatch.DocumentWidth = value


    @property
    def nb_depth_ranges(self):
        """Returns the number of defined depth ranges defined."""
        return self._dispatch.NbOfDepthRanges


    @property
    def depth_range_mode(self):
        """Returns 0 for max range and 1 for custom range."""
        return self._dispatch.DepthRange 


    @depth_range_mode.setter
    def depth_range_mode(self, mode):
        """Sets the depth range mode for printing.
        
        Arguments:
            mode -- Set it to 0 for the max depth range and to 1 to
                    print the custom depth ranges.

        """

        self._dispatch.DepthRange = mode


    def add_depth_range(self, top, base):
        """Adds a new custom depth range.
        
        Arguments:
        top -- Top depth of the interval in units of the
               master depth axis
        base -- Bottom depth of the interval in units of
                the master depth axis

        """

        return self._dispatch.DepthRange(top, base)


    def remove_depth_range(self, index):
        """Removes a custom custom depth range.
        
        Arguments:
        index -- Zero based index of the list of depth ranges

        """

        return self._dispatch.RemoveDepthRange (index)


    @property	
    def paper_mode(self):
        """Returns 0 for page-by-page and 1 for fanfold."""
        return self._dispatch.PaperMode  


    @paper_mode.setter
    def paper_mode(self, mode):
        """Sets the page mode for printing.
        
        Arguments:
            mode -- Set it to 0 for page-by-page and to 1 for
                    fanfold(continuos) printing.

        """

        self._dispatch.PaperMode = mode


    @property	
    def numbering_mode(self):
        """0 = none, 1 = left, 2 = right, 3 = center, 4 = alternating."""
        return self._dispatch.Numbering  


    @numbering_mode.setter
    def numbering_mode(self, mode):
        """Sets the page numbering mode.
        
        Arguments:
            mode -- Set 0 = none, 1 = left, 2 = right,
            3 = center, 4 = alternating.

        """

        self._dispatch.Numbering = mode


    @property	
    def left_margin(self):
        """Get the left margin of the page to print in mm."""
        return self._dispatch.LeftMargin   


    @left_margin.setter
    def left_margin(self, value):
        """Sets the left margin of the page to print.
        
        Arguments:
            value -- integer specifying the left margin in mm 

        """

        self._dispatch.LeftMargin = value


    @property	
    def right_margin(self):
        """Get the right margin of the page to print in mm."""
        return self._dispatch.RightMargin   


    @right_margin.setter
    def right_margin(self, value):
        """Sets the right margin of the page to print.
        
        Arguments:
            value -- integer specifying the right margin in mm 

        """

        self._dispatch.RightMargin = value


    @property	
    def top_margin(self):
        """Get the top margin of the page to print in mm."""
        return self._dispatch.TopMargin   


    @top_margin.setter
    def top_margin(self, value):
        """Sets the top margin of the page to print.
        
        Arguments:
            value -- integer specifying the top margin in mm 

        """

        self._dispatch.TopMargin = value



    @property	
    def bottom_margin(self):
        """Get the bottom margin of the page to print in mm."""
        return self._dispatch.BottomMargin   


    @bottom_margin.setter
    def bottom_margin(self, value):
        """Sets the bottom margin of the page to print.
        
        Arguments:
            value -- integer specifying the bottom margin in mm 

        """

        self._dispatch.BottomMargin = value


    @property	
    def print_header(self):
        """Returns True if the header is going to be printed."""
        return self._dispatch.PrintHeader   


    @print_header.setter
    def print_header(self, flag):
        """Set to True if the header should be printed.
        
        Arguments:
            flag -- boolean specifiying whether the page header
                    is printed (True) or not (False) 

        """

        self._dispatch.PrintHeader = flag



    @property	
    def print_bottom_titles(self):
        """Returns True if the log titles are printed at the bottom."""
        return self._dispatch.PrintTitlesOnBottom    


    @print_bottom_titles.setter
    def print_bottom_titles(self, flag):
        """Set to True if the titles should be printed at the bottom.
        
        Arguments:
            flag -- boolean specifiying whether the log titles are
                    printed at the plot bottom (True) or not (False) 

        """

        self._dispatch.PrintTitlesOnBottom  = flag



    @property	
    def print_top_titles(self):
        """Returns True if the log titles are printed at the top."""
        return self._dispatch.PrintTitlesOnTop    


    @print_top_titles.setter
    def print_top_titles(self, flag):
        """Set to True if the titles should be printed at the top.
        
        Arguments:
            flag -- boolean specifiying whether the log titles are
                    printed at the plot top (True) or not (False) 

        """

        self._dispatch.PrintTitlesOnTop  = flag



    @property	
    def repeat_top_titles(self):
        """Returns True if titles are repeated at the top of each page."""
        return self._dispatch.PrintTitlesOnTopOnEachPage    


    @repeat_top_titles.setter
    def repeat_top_titles(self, flag):
        """Set to True if the titles should be repeated at each page top.
        
        Arguments:
            flag -- boolean specifiying whether the log titles are
                    repeated at the top of each page (True) or not (False) 

        """

        self._dispatch.PrintTitlesOnTopOnEachPage  = flag



    @property	
    def repeat_bottom_titles(self):
        """Returns True if titles are repeated at each page bottom."""
        return self._dispatch.PrintTitlesOnBottomOnEachPage    


    @repeat_bottom_titles.setter
    def repeat_bottom_titles(self, flag):
        """Set to True if the titles should be repeated at each page bottom.
        
        Arguments:
            flag -- boolean specifiying whether the log titles are
                    repeated at the bottom of each page (True) or not (False) 

        """

        self._dispatch.PrintTitlesOnBottomOnEachPage  = flag