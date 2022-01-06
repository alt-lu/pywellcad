from ._dispatch_wrapper import DispatchWrapper


class Page(DispatchWrapper):
    """ The Page class manages properties for the document print out.

    Example
    -------
    >>> import wellcad.com
    >>> app = wellcad.com.Application()
    >>> app.new_borehole()
    <wellcad.com._borehole.Borehole object at 0x0000018B3DAF9D30>
    >>> borehole = app.get_active_borehole()
    >>> page = borehole.page
    """

    @property
    def depth_range(self):
        """int : Identify the depth range mode

        The available modes are the following:

        * 0 = depth range not defined (maximum depth range to be printed)
        * 1 = depth range defined by the user
        """
        return self._dispatch.DepthRange

    @depth_range.setter
    def depth_range(self, mode):
        self._dispatch.DepthRange = mode

    @property
    def document_height(self):
        """float: The document height in mm."""
        return self._dispatch.DocumentHeight

    @property
    def document_width(self):
        """float: The document width in mm."""
        return self._dispatch.DocumentWidth

    @document_width.setter
    def document_width(self, value):
        self._dispatch.DocumentWidth = value

    @property
    def nb_of_depth_range(self):
        """double: The number of defined depth ranges."""
        return self._dispatch.NbOfDepthRange

    @property
    def paper_mode(self):
        """int: 0 for page-by-page and 1 for fanfold."""
        return self._dispatch.PaperMode

    @paper_mode.setter
    def paper_mode(self, mode):
        self._dispatch.PaperMode = mode

    @property
    def print_titles_on_top(self):
        """bool: Show the log titles at the top of the printout."""
        return self._dispatch.PrintTitlesOnTop

    @print_titles_on_top.setter
    def print_titles_on_top(self, show):
        self._dispatch.PrintTitlesOnTop = show

    @property
    def print_titles_on_bottom(self):
        """bool: Show the log titles at the bottom of the printout."""
        return self._dispatch.PrintTitlesOnBottom

    @print_titles_on_bottom.setter
    def print_titles_on_bottom(self, show):
        self._dispatch.PrintTitlesOnBottom = show

    @property
    def print_titles_on_bottom_on_each_page(self):
        """bool: Repeat the log titles at the bottom of each printed page."""
        return self._dispatch.PrintTitlesOnBottomOnEachPage

    @print_titles_on_bottom_on_each_page.setter
    def print_titles_on_bottom_on_each_page(self, show):
        self._dispatch.PrintTitlesOnBottomOnEachPage = show

    @property
    def print_titles_on_top_on_each_page(self):
        """bool: Repeat the log titles at the top of each printed page."""
        return self._dispatch.PrintTitlesOnTopOnEachPage

    @print_titles_on_top_on_each_page.setter
    def print_titles_on_top_on_each_page(self, flag):
        self._dispatch.PrintTitlesOnTopOnEachPage = flag

    @property
    def top_margin(self):
        """int: The top margin of the page to print in mm."""
        return self._dispatch.TopMargin

    @top_margin.setter
    def top_margin(self, value):
        self._dispatch.TopMargin = value

    @property
    def bottom_margin(self):
        """int: The bottom margin of the page to print in mm."""
        return self._dispatch.BottomMargin

    @bottom_margin.setter
    def bottom_margin(self, value):
        self._dispatch.BottomMargin = value

    @property
    def left_margin(self):
        """int: The left margin of the page to print in mm."""
        return self._dispatch.LeftMargin

    @left_margin.setter
    def left_margin(self, value):
        self._dispatch.LeftMargin = value

    @property
    def right_margin(self):
        """int: The right margin of the page to print in mm."""
        return self._dispatch.RightMargin

    @right_margin.setter
    def right_margin(self, value):
        self._dispatch.RightMargin = value

    @property
    def numbering(self):
        """int: The page numbering mode

        The available modes are the following:

        * 0 = none
        * 1 = left
        * 2 = right
        * 3 = center
        * 4 = alternating
        """
        return self._dispatch.Numbering

    @numbering.setter
    def numbering(self, mode):
        self._dispatch.Numbering = mode

    @property
    def print_header(self):
        """bool: Option to print the document header or not."""
        return self._dispatch.PrintHeader

    @print_header.setter
    def print_header(self, flag):
        self._dispatch.PrintHeader = flag

    def add_depth_range(self, top, bottom):
        """Adds a new depth range to be printed in current master depth units.
        
        Parameters
        ----------
        top : float
            Top depth of the interval that will be added to the print list.
        bottom : float
            Bottom depth of the interval that will be added to the print list.
        """
        return self._dispatch.AddDepthRange(top, bottom)

    def remove_depth_range(self, index):
        """Remove an entry from the list of depth ranges.
        
        Parameters
        ----------
        index : int
            Zero based index of the entry to be removed from the list.
        """
        return self._dispatch.RemoveDepthRange(index)
