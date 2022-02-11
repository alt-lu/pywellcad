from ._dispatch_wrapper import DispatchWrapper
from ._font import Font
from ._drill_item import DrillItem
from ._structure import Structure
from ._litho_bed import LithoBed
from ._polar_and_rose_box import PolarAndRoseBox
from ._interval_item import IntervalItem
from ._fossil_item import FossilItem
from ._equipment_item import EquipmentItem
from ._comment_box import CommentBox
from ._marker_item import MarkerItem
from ._stacking_pattern_item import StackingPatternItem
from ._cross_section_box import CrossSectionBox
from ._litho_dictionary import LithoDictionary


class Log(DispatchWrapper):
    """The Log class represents a depth or time referenced set of data displayed as a column in a borehole document.
    Logs can be added/removed/manipulated from the borehole document itself.

    >>> import wellcad.com
    >>> app = wellcad.com.Application()
    >>> borehole = app.new_borehole()
    >>> log = borehole.insert_new_log(1) # Create a new well log
    """
    
    _DISPATCH_METHODS = ("Structure",)
    _DISPATCH_ATTRIBUTES = ("Style",)

    def file_export(self, directory, file_title=None, extension=None, prompt_user=None, config_filename=None):
        """Exports the data of the log in the specified format (TXT, CSV, ASC,
        WA* for all log types, BMP, TIF, GIF, JPG, PNG in addition for RGB and
        Image Logs).

        Parameters
        ----------
        directory : str
            Path to the location where the file should be stored.
        file_title : str, optional
            Name of the file that will be created. By default the log title
            will be taken.
        extension : str, optional
            The file extension to be used.
        prompt_user: bool, optional
            If set to ``True`` any warning messages during the graphic file
            export will be shown.
        config_filename : str, optional
            Configuration file used for ASCII (TXT, CSV, ASC, WA*) export only.
        
        Returns
        -------
        bool
            Whether the log was successfully exported.
        """
        return self._dispatch.FileExport(directory, file_title, extension, prompt_user, config_filename)

    @property
    def nb_of_data(self):
        """int: The number of data points in a log."""
        return self._dispatch.NbOfData

    @property
    def name(self):
        """str: The title of the log."""
        return self._dispatch.Name

    @name.setter
    def name(self, value):
        self._dispatch.Name = value

    @property
    def title_comment(self):
        """str: The title comment for this log."""
        return self._dispatch.TitleComment

    @title_comment.setter
    def title_comment(self, comment):
        self._dispatch.TitleComment = comment

    @property
    def top_depth(self):
        """float: The depth of the first top-most (shallowest) data point in
        the log using the current depth reference units."""
        return self._dispatch.TopDepth

    @property
    def bottom_depth(self):
        """float: The depth of the of the bottom-most (deepest) data point in
        the log using the current depth reference units."""
        return self._dispatch.BottomDepth


    @property
    def data_table(self):
        """tuple of tuples: The data table for a log. The first row in the data
        table is reserved for the log titles (e.g. for a Well Log the fist row
        in the data table contains the column titles "Depth" and the actual log
        title). The data format for each log equals the data displayed in the
        Tabular Editor."""
        return self._dispatch.DataTable

    @data_table.setter
    def data_table(self, data):
        self._dispatch.DataTable = data

    @property
    def data_min(self):
        """float: The minimum data value of the Well, Mud or Interval Log."""
        return self._dispatch.DataMin

    @property
    def data_max(self):
        """float: The maximum data value of the Well, Mud or Interval Log."""
        return self._dispatch.DataMax

    @property
    def log_unit(self):
        """str: The unit of a log. Restricted to log types having a unit in the log title."""
        return self._dispatch.LogUnit

    @log_unit.setter
    def log_unit(self, unit):
        self._dispatch.LogUnit = unit

    @property
    def left_position(self):
        """float: The position of the left side of the log column as a fraction
        of the document width.
        
        In the case that this is set to be a value higher than
        ``right_position``, the two attributes will swap. Values will be
        clamped in the range [0.0, 1.0].
        """
        return self._dispatch.LeftPosition

    @left_position.setter
    def left_position(self, position):
        self._dispatch.LeftPosition = position

    @property
    def right_position(self):
        """float: The position of the right side of the log column as a
        fraction of the document width.
        
        In the case that this is set to be a value lower than
        ``left_position``, the two attributes will swap. Values will be
        clamped in the range [0.0, 1.0].
        """
        return self._dispatch.RightPosition

    @right_position.setter
    def right_position(self, position):
        self._dispatch.RightPosition = position

    def set_position(self, left, right):
        """Sets the position and width of the log.

        Values given outside the range of [0.0, 1.0] will be clamped. If
        ``left`` > ``right``, the arguments are swapped.

        Parameters
        ----------
        left : float
            The position of the left side of the log column as a fraction of
            the document width.

        right : float
            The position of the right side of the log column as a fraction of
            the document width.
        """
        self._dispatch.SetPosition(left, right)

    @property
    def type(self):
        """int: The log type index.

        Log types are one of the below:

        * Undefined = 0
        * Well log = 1
        * Formula log = 2
        * Mud log = 3
        * FWS log = 4
        * Image log = 5
        * Structure log = 6
        * Litho log = 7
        * Comment log = 8
        * Engineering log = 9
        * RGB log = 10
        * Image Float 2 log = 11
        * Image float 4 log = 12
        * Interval log = 13
        * Analysis log = 14
        * Percentage log = 15
        * Coredesc log = 16
        * Depth log = 17
        * Strata log = 18
        * Stack log = 19
        * Polar & Rose log = 20
        * Cross log = 21
        * OLE log = 22
        * Shading log = 23
        * Marker log = 24
        * Breakout log = 25
        * Bio log = 26
        * Lineation log = 27
        """
        return self._dispatch.Type

    @property
    def hide_log_title(self):
        """bool: Whether the log title is hidden."""
        return self._dispatch.HideLogTitle

    @hide_log_title.setter
    def hide_log_title(self, value):
        self._dispatch.HideLogTitle = value

    @property
    def hide_log_data(self):
        """bool: Whether the log data is hidden."""
        return self._dispatch.HideLogData

    @hide_log_data.setter
    def hide_log_data(self, value):
        self._dispatch.HideLogData = value

    @property
    def log_background_color(self):
        """int: The background color of the log column.
        
        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values. Other allowed values are : 0xFFFFFFFF (None) and 0xFF000000 (automatic color).
        """
        return self._dispatch.LogBackgroundColor

    @log_background_color.setter
    def log_background_color(self, value):
        self._dispatch.LogBackgroundColor = value

    @property
    def border_style(self):
        """int: The border line style of the log column.
        
        Styles are specified as an integer:

        * Solid = 0
        * Dashed = 1
        * Dotted = 2
        * Dash-Dot = 3
        * Dash-dot-dot = 4
        """
        return self._dispatch.BorderStyle

    @border_style.setter
    def border_style(self, style):
        self._dispatch.BorderStyle = style

    @property
    def border_width(self):
        """float: The width for the log column border in 1/10 mm."""
        return self._dispatch.BorderWidth

    @border_width.setter
    def border_width(self, width):
        self._dispatch.BorderWidth = width

    @property
    def border_color(self):
        """int: The border color of the log column.
        
        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values. Other allowed values are : 0xFFFFFFFF (None) and 0xFF000000 (automatic color).
        """
        return self._dispatch.BorderColor

    @border_color.setter
    def border_color(self, value):
        self._dispatch.BorderColor = value

    @property
    def display_border(self):
        """bool: Whether the log column border is displayed."""
        return self._dispatch.DisplayBorder

    @display_border.setter
    def display_border(self, value):
        self._dispatch.DisplayBorder = value

    def clear_history(self):
        """Removes all entries from the log history."""
        self._dispatch.ClearHistory()

    @property
    def nb_of_history_item(self):
        """int: The number of entries in the history (audit trail) of a log."""
        return self._dispatch.NbOfHistoryItem

    def history_item_date(self, index):
        """Gets the date of the history item at the specified index.

        Parameters
        ----------
        index : int
            Zero based index of the history entry.
        
        Returns
        -------
        pywintypes.datetime
            The timezone-aware datetime of the history item.
        """
        return self._dispatch.HistoryItemDate(index).replace(tzinfo=None).astimezone()

    def history_item_description(self, index):
        """Gets the description of the history item at the specified index.

        Parameters
        ----------
        index : int
            Zero based index of the history entry.
        
        Returns
        -------
        str
            The description of the specified history entry.
        """
        return self._dispatch.HistoryItemDescription(index)

    @property
    def null_value(self):
        """float: The value that is treated as ``Null`` (not displayed) in a log."""
        return self._dispatch.NullValue

    @null_value.setter
    def null_value(self, value):
        self._dispatch.NullValue = value

    @property
    def mask_contacts(self):
        """bool: Whether contact lines within the log column are masked or not."""
        return self._dispatch.MaskContacts

    @mask_contacts.setter
    def mask_contacts(self, value):
        self._dispatch.MaskContacts = value

    @property
    def mask_horizontal_grid(self):
        """bool: Whether the horizontal (depth) gridlines of a log are masked or not."""
        return self._dispatch.MaskHorizontalGrid

    @mask_horizontal_grid.setter
    def mask_horizontal_grid(self, value):
        self._dispatch.MaskHorizontalGrid = value

    @property
    def sample_rate(self):
        """float: The sample interval of a log in current master depth units."""
        return self._dispatch.SampleRate

    @sample_rate.setter
    def sample_rate(self, rate):
        self._dispatch.SampleRate = rate

    @property
    def scale_low(self):
        """float: The low value of the log scale."""
        return self._dispatch.ScaleLow

    @scale_low.setter
    def scale_low(self, scale):
        self._dispatch.ScaleLow = scale

    @property
    def scale_high(self):
        """float: The high value of the log scale."""
        return self._dispatch.ScaleHigh

    @scale_high.setter
    def scale_high(self, scale):
        self._dispatch.ScaleHigh = scale

    @property
    def scale_mode(self):
        """int: The horizontal scale mode (linear or logarithmic) of a log.

        This property is only available for Well or Mud logs, and can have the
        following values:

        * Linear = 0
        * Logarithmic = 1
        """
        return self._dispatch.ScaleMode

    @scale_mode.setter
    def scale_mode(self, mode):
        self._dispatch.ScaleMode = mode

    @property
    def scale_reversed(self):
        """bool: Whether the data display scale is reversed."""
        return self._dispatch.ScaleReversed

    @scale_reversed.setter
    def scale_reversed(self, value):
        self._dispatch.ScaleReversed = value

    @property
    def use_log_colored_background(self):
        """bool: Whether the background color of a log is displayed."""
        return self._dispatch.UseLogColoredBackground

    @use_log_colored_background.setter
    def use_log_colored_background(self, value):
        self._dispatch.UseLogColoredBackground = value

    @property
    def maj_grid_enable(self):
        """bool: Whether to display major vertical gridlines."""
        return self._dispatch.MajGridEnable

    @maj_grid_enable.setter
    def maj_grid_enable(self, value):
        self._dispatch.MajGridEnable = value

    @property
    def min_grid_enable(self):
        """bool: Whether to display minor vertical gridlines."""
        return self._dispatch.MinGridEnable

    @min_grid_enable.setter
    def min_grid_enable(self, value):
        self._dispatch.MinGridEnable = value

    @property
    def maj_grid_spacing(self):
        """float: The spacing between major vertical gridlines."""
        return self._dispatch.MajGridSpacing

    @maj_grid_spacing.setter
    def maj_grid_spacing(self, spacing):
        self._dispatch.MajGridSpacing = spacing

    @property
    def min_grid_spacing(self):
        """float: The spacing between minor vertical gridlines."""
        return self._dispatch.MinGridSpacing

    @min_grid_spacing.setter
    def min_grid_spacing(self, spacing):
        self._dispatch.MinGridSpacing = spacing

    @property
    def lock_log_data(self):
        """bool: Whether the log data is protected from editing."""
        return self._dispatch.LockLogData

    @lock_log_data.setter
    def lock_log_data(self, value):
        self._dispatch.LockLogData = value

    def get_data(self, index):
        """Gets the data value for the specified index.

        This method is only applicable for a Well, Mud, Interval or Depth Log.

        Parameters
        ----------
        index : int
            Zero based index of the data to be retrieved.
        
        Returns
        -------
        float
            The value of the log data at the specified index.
        """
        return self._dispatch.GetData(index)

    def set_data(self, index, value):
        """Sets the data value for the specified index.

        This method is only applicable for a Well, Mud, Interval or Depth Log.

        Parameters
        ----------
        index : int
            Zero based index of the data to be retrieved.
        value : float
            The value you want to set the data to.
        """
        self._dispatch.SetData(index, value)

    def get_data_at_depth(self, depth):
        """Gets the log data value at the specified depth.
        
        This method is only applicable for a Well, Mud, Interval or Depth Log.

        Parameters
        ----------
        depth : float
            Depth value in current master depth units.
        
        Returns
        -------
        float
            The value of the log data at the specified depth.
        """
        return self._dispatch.GetDataAtDepth(depth)

    def set_data_at_depth(self, depth, value):
        """Sets the log data value at the specified depth.

        This method is only applicable for a Well, Mud, Interval or Depth Log.

        Parameters
        ----------
        depth : float
            Depth value in current master depth units.
        value : float
            The value you want to set the data to.
        """
        self._dispatch.SetDataAtDepth(depth, value)

    def data_depth(self, index):
        """Gets the log data depth for the specified index.
        
        This method can be called for Mud, Well, Depth, Percent, Analysis, FWS,
        Image and RGB Logs. For logs with a constant sample step (Well, Image,
        RGB, Analysis Logs), the index 0 corresponds to the Bottom Depth.

        Parameters
        ----------
        index : int
            Zero based index of the data to be retrieved.
        
        Returns
        -------
        float
            The depth of the log data at the specified index. If the index is
            out of bounds, this will be 0.0 for a Mud Log, and an extrapolated
            value for a Well Log.
        """
        return self._dispatch.DataDepth(index)

    def insert_data(self, index, value):
        """Inserts a new data value at the specified index.

        If necessary existing data points will be shifted.

        Parameters
        ----------
        index : int
            Zero based index at which the new data point will be inserted. The
            index must be lower or equal to the number of data points in the
            log.
        value : float
            The new data value.
        
        Raises
        ------
        pywintypes.com_error
            If the data couldn't be inserted (out-of-bounds index or other)
        """
        self._dispatch.InsertData(index, value)

    def insert_data_at_depth(self, depth, value):
        """Inserts a new data value at the specified depth.

        Data points above (shallower depth) will be shifted upward to
        accomodate the newly inserted point in a Well Log.

        Parameters
        ----------
        depth : float
            Depth in current master units at which the new data point should be
            inserted. Depth is rounded to the nearest sample for Well Logs.
        value : float
            The new data value
        """
        self._dispatch.InsertDataAtDepth(depth, value)

    @property
    def formula(self):
        """str: The mathematical formula used for a Formula log.
        
        Raises
        ------
        pywintypes.com_error
            If, during setting, the supplied formula is invalid.
        """
        return self._dispatch.Formula

    @formula.setter
    def formula(self, value):
        self._dispatch.Formula = value

    @property
    def filter(self):
        """int: The width (in samples) of the display filter used for Well Logs."""
        return self._dispatch.Filter

    @filter.setter
    def filter(self, value):
        self._dispatch.Filter = value

    @property
    def fixed_bar_width(self):
        """int: The fixed bar width, in units of 1/10 mm, for Mud Logs."""
        return self._dispatch.FixedBarWidth

    @fixed_bar_width.setter
    def fixed_bar_width(self, width):
        self._dispatch.FixedBarWidth = width

    def insert_new_interval_item(self, top_depth, bottom_depth, value):
        """Inserts a new interval in an Interval log.

        Parameters
        ----------
        top_depth : float
            The top depth of the new interval in current depth units.
        bottom_depth : float
            The bottom depth of the new interval in current depth units.
        value : float
            The value of the new interval item.
        
        Returns
        -------
        IntervalItem
            The newly inserted interval item.
        """
        return IntervalItem(self._dispatch.InsertNewIntervalItem(top_depth, bottom_depth, value))

    def interval_item(self, index):
        """Gets an interval item object from an Interval Log.

        Items are ordered by ascending top depth.

        Parameters
        ----------
        index : int
            Zero based index of the interval item.
        
        Returns
        -------
        IntervalItem or None
            The interval item at the specified index, or None if the index
            is out of range.
        """
        return IntervalItem(self._dispatch.IntervalItem(index))

    def interval_item_at_depth(self, depth):
        """Gets an interval item object from an Interval Log at the specified depth.

        Parameters
        ----------
        depth : float
            Depth value of the interval item, in current master depth units.
        
        Returns
        -------
        IntervalItem or None
            The interval item at the specified depth, or None if no interval
            item exists at the specified depth.
        """
        return IntervalItem(self._dispatch.IntervalItemAtDepth(depth))

    @property
    def pen_color(self):
        """int: The pen color for a Well or Mud log.
        
        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values.  Other allowed values are : 0xFFFFFFFF (None) and 0xFF000000 (automatic color).
        """
        return self._dispatch.PenColor

    @pen_color.setter
    def pen_color(self, color):
        self._dispatch.PenColor = color

    @property
    def pen_style(self):
        """int: The pen style for the Well or Mud log.
        
        Styles are specified as an integer:

        * Solid = 0
        * Dashed = 1
        * Dotted = 2
        * Dash-Dot = 3
        * Dash-dot-dot = 4
        """
        return self._dispatch.PenStyle

    @pen_style.setter
    def pen_style(self, style):
        self._dispatch.PenStyle = style

    @property
    def pen_width(self):
        """int: The pen width used in a Well or Mud Log in units of 1/10 mm."""
        return self._dispatch.PenWidth

    @pen_width.setter
    def pen_width(self, width):
        self._dispatch.PenWidth = width

    def remove_data(self, index):
        """Removes a data point from a Mud or Well Log.
        
        For Well Logs the data value will be set to ``Null``.

        Parameters
        ----------
        index : int
            Zero based index for the data point to be removed
        """
        self._dispatch.RemoveData(index)

    def remove_data_at_depth(self, depth):
        """Removes a data point from a Mud or Well Log.
        
        All data points above (shallower depth) the removed point will be
        shifted downward (deeper) when data is removed from a Well Log.

        Parameters
        ----------
        depth : float
            The depth value (in current master units) at which the data point.
            will be removed.
        """
        self._dispatch.RemoveDataAtDepth(depth)

    def remove_interval_item(self, index):
        """Removes a data interval from an Interval log.

        Parameters
        ----------
        index : int
            Zero based index to specify which data interval will be removed.
        """
        self._dispatch.RemoveIntervalItem(index)

    def remove_interval_item_at_depth(self, depth):
        """Removes a data interval from an Interval log.

        Parameters
        ----------
        depth : float
            Depth value in current master units to specify which interval item
            will be removed.
        """
        self._dispatch.RemoveIntervalItemAtDepth(depth)

    @property
    def shading(self):
        """int: The shading position used in a Well or Mud Log.
        
        * None = 0
        * Left = 1
        * Right = 2
        * Full = 3
        """
        return self._dispatch.Shading

    @shading.setter
    def shading(self, position):
        self._dispatch.Shading = position

    @property
    def style(self):
        """int: The data display style for a log.
        
        For Mud logs:

        * Fixed Bar = 1
        * Dynamic Bar = 2
        * Line = 3
        
        For Engineering logs:

        * Full = 0
        * Left = 1
        * Right = 2
        """
        return self._dispatch.Style

    @style.setter
    def style(self, style):
        self._dispatch.Style = style

    def attach_litho_dictionary(self, dictionary):
        """Attaches a new symbol or pattern library (\*.LTH file) to Litho, CoreDesc,
        Strata, Analysis or Percentage Log.

        Parameters
        ----------
        dictionary : str
            path and name of the LTH file to attach

        Returns
        -------
            LithoDictionary
                The LithoDictionary object
        """
        return LithoDictionary(self._dispatch.AttachLithoDictionary(dictionary))

    def get_component_name(self, column):
        """Gets the name (i.e. litho code) for the component used in
        the specified data column of a Percentage or Analysis Log.

        Parameters
        ----------
        column : int
            Zero based index of the data column in the tabular editor for
            which the component name should be set or retrieved.

        Returns
        -------
        str
            The code of the component used in the specified data
            column of a Percentage or Analysis Log.
        """
        return self._dispatch.GetComponentName(column)

    def set_component_name(self, column, code):
        """Sets the name (i.e. litho code) for the component used in
        the specified data column of a Percentage or Analysis Log.

        Parameters
        ----------
        column : int
            Zero based index of the data column in the tabular editor for
            which the component name should be set or retrieved.
        code : str
            Code of the component to be used in the specified data
            column of a Percentage or Analysis Log.
        """
        self._dispatch.SetComponentName(column, code)

    def fossil_item(self, index):
        """Gets a Fossil Item object from the CoreDesc Log at the specified index.

        Items are ordered by ascending top depth.

        Parameters
        ----------
        index : int
            Zero based index of the item to be retrieved.

        Returns
        -------
        FossilItem or None
            The FossilItem at the desired index or none if index is out of range.
        """
        return FossilItem(self._dispatch.FossilItem(index))

    def fossil_item_at_depth(self, depth):
        """Gets a fossil item object from the CoreDesc Log at the specified depth.

        Parameters
        ----------
        depth : float
            depth value in current depth units at which the item will be retrieved

        Returns
        -------
        FossilItem or None
            The FossilItem at the desired depth or None if depth is out of range.
        """
        return FossilItem(self._dispatch.FossilItemAtDepth(depth))

    def insert_new_fossil_item(self, top_depth, bottom_depth, litho_code, abundance, dominance, position):
        """Inserts a new data point or interval into a Core Description Log.

        Parameters
        ----------
        top_depth : float
            Top depth of the new data interval in current depth units.
        bottom_depth : float
            Bottom depth of the new data interval in current depth units.
        litho_code : str
            Code of the symbol representing the feature as defined in the symbol library of the log.
        abundance : int
            The abundance value associated with the symbol (e.g. between 0 and 9).
        dominance : int
            The dominance value associated with the symbol
            undiff = 0
            minor = 1
            major = 2
        position : float
            A value between 0 and 1 determining the horizontal position of the symbol within the log column.

        Returns
        -------
        FossilItem
            The newly created FossilItem.
        """
        return FossilItem(self._dispatch.InsertNewFossilItem(top_depth, bottom_depth, litho_code, abundance, dominance, position))

    def insert_new_litho_bed(self, top_depth, bottom_depth, litho_code, value, position):
        """Inserts a new lithology bed into a Litho Log.

        Parameters
        ----------
        top_depth : float
            Top depth of the new data interval in current depth units.
        bottom_depth : float
            Bottom depth of the new data interval in current depth units.
        litho_code : str
            Code of the symbol representing the feature as defined in the symbol library of the log.
        value : float
            Hardness value between 0 and 1.
        position : float
            A value between 0 and 1 determining the horizontal position of a non repeated symbol
            in percent of the track width.

        Returns
        -------
        LithoBed
            The newly created LithoBed.
        """
        return LithoBed(self._dispatch.InsertNewLithoBed(top_depth, bottom_depth, litho_code, value, position))

    def get_litho_bed(self, index):
        """Gets a LithoBed object at the specified index from a Lithology Log.

        Items are ordered by ascending top depth.

        Parameters
        ----------
        index : int
            Zero based index of the LithoBed to retrieve.

        Returns
        -------
        LithoBed
            The LithoBed at the desired index.
        """
        return LithoBed(self._dispatch.GetLithoBed(index))

    def set_litho_bed(self, index, litho_bed):
        """Sets a LithoBed object at the specified index from another
        LithoBed object.

        Parameters
        ----------
        index : int
            Zero based index of the LithoBed to retrieve.
        litho_bed : LithoBed
            The LithoBed object to copy.
        """
        self._dispatch.SetLithoBed(index, litho_bed._dispatch)

    def get_litho_bed_at_depth(self, depth):
        """Gets a LithoBed object at the specified depth from a Lithology Log.

        Parameters
        ----------
        depth : float
            Depth value in current depth units at which the item will be retrieved.

        Returns
        -------
        LithoBed
            The LithoBed at the desired depth.
        """
        return LithoBed(self._dispatch.GetLithoBedAtDepth(depth))

    def set_litho_bed_at_depth(self, depth, litho_bed):
        """Sets a LithoBed object at the specified depth from another
        LithoBed object.

        Parameters
        ----------
        depth : float
            Depth value in current depth units at which the item will be retrieved.
        litho_bed : LithoBed
            The LithoBed object to copy.
        """
        self._dispatch.SetLithoBedAtDepth(depth, litho_bed._dispatch)

    @property
    def litho_dictionary(self):
        """LithoDictionary: The symbol library used by the log as LithoDictionary object."""
        return LithoDictionary(self._dispatch.LithoDictionary)

    @litho_dictionary.setter
    def litho_dictionary(self, dictionary):
        self._dispatch.LithoDictionary = dictionary._dispatch

    def remove_fossil_item(self, index):
        """Removes an item at the specified index from a CoreDesc Log.

        Parameters
        ----------
        index : int
            Zero based index of the fossil item to be removed.
        """
        self._dispatch.RemoveFossilItem(index)

    def remove_fossil_item_at_depth(self, depth):
        """Removes an item at the specified index from a CoreDesc Log.

        Parameters
        ----------
        depth : float
            the depth value of the symbol in current depth units at which it will be removed.
        """
        self._dispatch.RemoveFossilItemAtDepth(depth)

    def remove_litho_bed(self, index):
        """Removes a lithology bed from the Lithology log at the specified index.

        Parameters
        ----------
        index : int
            Zero based index of the lithology bed item to be removed.
        """
        self._dispatch.RemoveLithoBed(index)

    def remove_litho_bed_at_depth(self, depth):
        """Removes a lithology bed from the Lithology log at the specified depth.

        Parameters
        ----------
        depth : float
            the depth value in current depth units at which the lithological bed will be removed.
        """
        self._dispatch.RemoveLithoBedAtDepth(depth)

    def insert_trace(self, index):
        """Inserts a new data trace into an Image, FWS or Analysis Log at the specified index.

        Columns for the newly inserted trace are filled with No-Data
        value. Edit them with set_trace_data or set_trace_data_at_depth.

        Parameters
        ----------
        index : int
            Zero based index at which the trace should be added.
            Index zero represents the deepest trace.
            The maximum allowed index is (number of traces + 1).
            For Image and Analysis logs, existing traces will be shifted upwards depth wise.
        """
        self._dispatch.InsertTrace(index)

    def insert_trace_at_depth(self, depth):
        """Inserts a new data trace into an Image, FWS or Analysis or Percent Log at the specified depth.

        Columns for the newly inserted trace are filled with No-Data
        value. Edit them with set_trace_data or set_trace_data_at_depth.

        Parameters
        ----------
        depth : float
            The depth value in current depth units at which the new
            data trace will be inserted.
            For Image and Analysis logs:
            Insertion depth is rounded to the nearest sample.
            Value must be within the depth range of the existing
            traces or contiguous to that range (± 1.5 * sampling rate).
            If necessary existing traces will be shifted upwards.
            For Percent and FWS logs, if there is already data at that
            depth, it is replaced with No-Data value, otherwise a trace
            is inserted at the desired depth without shifting other
            traces depth wise.

        """
        self._dispatch.InsertTraceAtDepth(depth)

    def remove_trace(self, index):
        """Remove an entire data trace from an Image, FWS, Analysis
        or Percentage Log.

        For Image logs, if the trace is the first or
        the last, it is removed. Otherwise, it sets all values of that
        trace to No-Data value.
        For Analysis, it is the same as for Image logs, but the
        replacement value is 0.
        For FWS logs, it removes the trace and shifts down all above
        traces.

        Parameters
        ----------
        index : int
            Zero based index of the trace (0 = bottom depth).
        """
        self._dispatch.RemoveTrace(index)

    def remove_trace_at_depth(self, depth):
        """Remove an entire data trace from an Image, FWS, Analysis or
        Percentage Log.

        For Image logs, if the trace is the first or
        the last, it is removed. Otherwise, it sets all values of that
        trace to No-Data value.
        For Analysis, it is the same as for Image logs, but the
        replacement value is 0.
        For FWS logs and Percent, it removes the trace and shifts down
        all above traces.

        Parameters
        ----------
        depth : float
            The depth value in current depth units at which the trace
            will be removed or set to No-Data value.
        """
        self._dispatch.RemoveTraceAtDepth(depth)

    def get_trace_data(self, depth_index, trace_index):
        """Gets the data value at the specified row index and position within the trace
        (column index) of an Analysis, Percentage, FWS, Image or RGB Log.

        Parameters
        ----------
        depth_index : int
            zero based index of the depth (0 = bottom depth for FWS,
            Image, RGB and Analysis logs, top depth for Percent logs).
        trace_index : int
            zero based index of the column.

        Returns
        -------
        float
            The data value at the specified index and column.
            The current No-Data value (e.g. -999) will be returned if
            the depth or trace index refers to a non-existent (out of
            index range) data point.
        """
        return self._dispatch.GetTraceData(depth_index, trace_index)

    def set_trace_data(self, depth_index, trace_index, value):
        """Sets the data value at the specified row index and position within the trace
        (column index) of an Analysis, Percentage, FWS, Image or RGB Log.

        Parameters
        ----------
        depth_index : int
            zero based index of the depth (0 = bottom depth).
        trace_index : int
            zero based index of the column.
        value : float
            The value you want to set the data to.
        """
        self._dispatch.SetTraceData(depth_index, trace_index, value)

    def get_trace_data_at_depth(self, depth, trace_position):
        """Gets the data value at the specified depth and position within the trace of an Analysis,
        Percentage, FWS, Image or RGB Log.

        Parameters
        ----------
        depth : float
            The depth value at which you would like to retrieve the
            data value in the current depth units.
        trace_position : float
            The position within the trace (time or angle as shown in
            the column header of the tabular editor, not the index)
            at which you would like to retrieve the data value.

        Returns
        -------
        float
            The data value at the specified depth and column.
            The current No-Data value (e.g. -999) will be returned if
            the depth or trace index refers to a non-existent (out of
            index range) data point.
        """
        return self._dispatch.GetTraceDataAtDepth(depth, trace_position)

    def set_trace_data_at_depth(self, depth, trace_position, value):
        """set the data value at the specified depth and position within
        the trace of an Analysis, Percentage, FWS, Image or RGB Log

        Parameters
        ----------
        depth : float
            The depth value at which you would like to retrieve the data value in the current depth units.
        trace_position : float
            The position within the trace (time or angle as shown in the column header of the tabular editor,
            not the index) at which you would like to retrieve the data value.
        value : float
            The value you want to set the data to.
        """
        self._dispatch.SetTraceDataAtDepth(depth, trace_position, value)

    @property
    def trace_length(self):
        """int: The length of a data trace in Image, RGB and FWS Logs.

        For FWS, Analysis and Percent logs:
        If trace_length is set to a lower value than the current one,
        all the trace columns past the desired length are discared.
        If trace_length is set to a higher value than the current one,
        additional columns are filled with No-data values.
        For Image and RGB logs:
        If trace_length is set to a lower value than the current one,
        trace value are resampled and averaged.
        If trace_length is set to a higher value than the current one,
        TODO determine behaviour here.
        """
        return self._dispatch.TraceLength

    @trace_length.setter
    def trace_length(self, length):
        self._dispatch.TraceLength = length

    @property
    def trace_offset(self):
        """float: The offset of a data trace in the FWS Log."""
        return self._dispatch.TraceOffset

    @trace_offset.setter
    def trace_offset(self, offset):
        self._dispatch.TraceOffset = offset

    @property
    def trace_sample_rate(self):
        """float: The trace sample interval for a FWS Logs."""
        return self._dispatch.TraceSampleRate

    @trace_sample_rate.setter
    def trace_sample_rate(self, rate):
        self._dispatch.TraceSampleRate = rate

    def get_column_name(self, column):
        """Gets set the name of a Strata Log column.

        Parameters
        ----------
        column : int
            Zero based index of the column to be retrieved

        Returns
        -------
        str
            The name of the column.
        """
        return self._dispatch.GetColumnName(column)

    def set_column_name(self, column, name):
        """Sets set the name of a Strata Log column.

        Parameters
        ----------
        column : int
            Zero based index of the column to be retrieved
        name : str
            New name of the column.
        """
        self._dispatch.SetColumnName(column, name)

    def comment_box(self, index):
        """Gets the Comment Box object from the Comment Log at the specified index.

        Parameters
        ----------
        index : int
            Zero based index at which the box will be retrieved.

        Returns
        -------
        CommentBox or None
            The CommentBox at the desired index or None if index is out of range.
        """
        return CommentBox(self._dispatch.CommentBox(index))

    def comment_box_at_depth(self, depth):
        """Gets the Comment Box object from the Comment Log at the specified depth.

        Parameters
        ----------
        depth : float
            The depth value in current depth units at which the comment box will be retrieved.

        Returns
        -------
        CommentBox or None
            The CommentBox at the desired depth or None if depth is out of range.
        """
        return CommentBox(self._dispatch.CommentBoxAtDepth(depth))

    def insert_new_comment_box(self, top_depth, bottom_depth, text):
        """Sets a new box with the specified text into a Comment Log.

        Parameters
        ----------
        top_depth : float
            The top of the box in current depth units.
        bottom_depth : float
            The bottom of the box in current depth units.
        text : str
            The text to be displayed in the new box.

        Returns
        -------
        CommentBox
            The newly created CommentBox.
        """
        return CommentBox(self._dispatch.InsertNewCommentBox(top_depth, bottom_depth, text))

    def marker(self, index):
        """Gets the marker with the specified index.

        Parameters
        ----------
        index : int
            Zero based index of the marker.

        Returns
        -------
        MarkerItem
            The marker with the specified index.
        """
        return MarkerItem(self._dispatch.Marker(index))

    def marker_by_name(self, name):
        """Gets the marker with the specified name.

        Parameters
        ----------
        name : str
            Name of the marker to be retrieved.

        Returns
        -------
        MarkerItem
            The marker with the specified name.
        """
        return MarkerItem(self._dispatch.MarkerByName(name))

    def insert_new_marker(self, depth, name, comment, contact):
        """Inserts a new marker at the specified depth into a Marker Log

        Parameters
        ----------
        depth : float
            The depth value in current depth units at which the marker will be added.
        name : str
            The name (or identifier) of the marker.
        comment : str
            The optional comment for the marker.
        contact : str
            Name of a contact style to be used and available in the contact dictionary of the Marker Log.

        Returns
        -------
        MarkerItem
            The Marker object at the desired depth with the specified attributes.
        """
        return MarkerItem(self._dispatch.InsertNewMarker(depth, name, comment, contact))

    def remove_comment_box(self, index):
        """Removes a comment box from the Comment log at the specified index.

        Parameters
        ----------
        index : int
            Zero based index at which the comment box will be removed.
        """
        self._dispatch.RemoveCommentBox(index)

    def remove_comment_box_at_depth(self, depth):
        """Removes a comment box from the Comment log at the specified depth.

        Parameters
        ----------
        depth : float
            The depth value in current depth units at which the comment box will be removed.
        """
        self._dispatch.RemoveCommentBoxAtDepth(depth)

    def remove_marker(self, index):
        """Removes the marker from a Marker Log at the specified index.

        Parameters
        ----------
        index : int
            Zero based index at which the marker box will be removed.
        """
        self._dispatch.RemoveMarker(index)

    def strata_column(self, index):
        """Gets a column from a Strata Log as Comment Log object.

        Parameters
        ----------
        index : int
            Zero based index  of the column to be returned.

        Returns
        -------
        Log
            A comment log object.
        """
        return Log(self._dispatch.StrataColumn(index))

    def remove_strata_column(self, index):
        """Removes the the specified column from a Strata Log at the specified index.

        Parameters
        ----------
        index : int
            Zero based index of the column to be removed.
        """
        self._dispatch.RemoveStrataColumn(index)

    @property
    def font(self):
        """Gets the font used in a Comment Log as Font Object."""
        return Font(self._dispatch.Font)

    @font.setter
    def font(self, font):
        self._dispatch.Font = font._dispatch

    def attach_attribute_dictionary(self, attribute, file):
        """Attaches a new attribute library (\*.TAD file) to a
        Breakout, Lineation or Structure Log.

        Parameters
        ----------
        attribute : str
            Name of the classification column.
        file : str
            Path to the TAD file to attach.

        Raises
        ------
        pywintypes.com_error
            If the classification column doesn't exist, an exception is raised.
        """
        self._dispatch.AttachAttributeDictionary(attribute, file)

    def insert_new_attribute(self, attribute_name):
        """Inserts a new blank classification column to a Breakout,
        Lineation or Structure Log.

        Parameters
        ----------
        attribute_name : str
            Name of the new class.
        """
        self._dispatch.InsertNewAttribute(attribute_name)

    def get_attribute_name(self, index):
        """Gets the name of the attribute class (i.e. classification
        column) in a Breakout, Lineation or Structure Log.

        Parameters
        ----------
        index : str
            Zero based index of the column.

        Returns
        -------
        str
            The name of the attribute class (classification column)

        Raises
        ------
        pywintypes.com_error
            If the column index points to a non existent column (out
            of index range) an exception will be raised.
        """
        return self._dispatch.GetAttributeName(index)

    def set_attribute_name(self, index, name):
        """Sets the name of the attribute class (i.e. classification
        column) in a Breakout, Lineation or Structure Log.

        Parameters
        ----------
        index : str
            Zero based index of the column.
        name : str
            New name of the classification column.

        Raises
        ------
        pywintypes.com_error
            If the column index points to a non existent column (out
            of index range) an exception will be raised.
        """
        self._dispatch.SetAttributeName(index, name)

    def structure(self, index):
        """Gets a Structure object from the Structure Log at the
        specified index.

        Parameters
        ----------
        index : int
            Zero based index of the structure object to be retrieved.

        Returns
        -------
        Structure or None
            The structure at the specified index. If the index is outside the valid range no exception
            will be raised and ``None`` will be returned.
        """
        return Structure(self._dispatch.Structure(index))

    def structure_at_depth(self, depth):
        """Gets the closest Structure object from the Structure Log
        to the specified depth in current depth units.

        Parameters
        ----------
        depth : float
            The depth value in current depth units at which the
            structure object will be retrieved.

        Returns
        -------
        Structure or None
            The feature closest to the specified depth will be returned.
            If the depth is outside the valid range no exception
            will be raised and ``None`` will be returned.
        """
        return Structure(self._dispatch.StructureAtDepth(depth))

    def insert_new_structure_ex(self, depth, azimuth, dip, aperture):
        """Sets a new structure in a Structure Log.

        Parameters
        ----------
        depth : float
            The depth value in the current units of the breakout structure to
            be inserted.
        azimuth : float
            The azimuth angle of the structure measured in degrees.
        dip : float
            The tilt angle of the structure measured in degrees.
        aperture : float
            The aperture of the structure in meters.

        Returns
        -------
        Structure
            The newly created structure object.
        """
        return Structure(self._dispatch.InsertNewStructureEx(depth, azimuth, dip, aperture))

    def remove_structure(self, index):
        """Removes a structure from the Structure Log at the
        specified index.

        Parameters
        ----------
        index : int
            Zero based index of the structure to be removed.
        """
        self._dispatch.RemoveStructure(index)

    def remove_structure_at_depth(self, depth):
        """Removes a structure from the Structure Log at the
        specified depth in current depth units.

        Parameters
        ----------
        depth : float
            The depth value in current depth units at which the
            structure will be removed.
        """
        self._dispatch.RemoveStructureAtDepth(depth)

    def breakout(self, index):
        """Gets a breakout structure from the Breakout Log at the specified
        index.

        Parameters
        ----------
        index : int
            Zero based index of the breakout to be retrieved.

        Returns
        -------
        Structure or None
            The breakout at the specified index. If the index is
            outside the valid range no exception will be raised and
            ``None`` will be returned.

        """
        return Structure(self._dispatch.Breakout(index))

    def breakout_at_depth(self, depth):
        """Gets a breakout structure from the Breakout Log at the specified
        depth in current depth units.

        Parameters
        ----------
        depth : float
            The depth value in current depth units at which the
            breakout will be retrieved.

        Returns
        -------
        Structure or None
            The feature closest to the specified depth will be returned.
            If the depth is outside the valid range no exception
            will be raised and ``None`` will be returned.
        """
        return Structure(self._dispatch.BreakoutAtDepth(depth))

    def insert_new_breakout_ex(self, depth, azimuth, tilt, length, opening):
        """Sets a new breakout structure in a Breakout Log.

        If the mirror option is active, a second breakout structure object is
        added 180° degrees apart.

        Parameters
        ----------
        depth : float
            The depth value of the breakout structure in current depth units.
        azimuth : float
            The azimuth angle of the breakout structure measured in degrees.
        tilt : float
            The tilt angle of the breakout structure measured in degrees.
        length : float
            The length of the breakout structure in meters.
        opening : float
            The opening (or aperture) angle of the breakout structure in degrees.

        Returns
        -------
        Structure
            The newly created breakout structure.
        """
        return Structure(self._dispatch.InsertNewBreakoutEx(depth, azimuth, tilt, length, opening))

    def remove_breakout(self, index):
        """Removes a breakout structure from the Breakout Log at the specified
        index.

        Parameters
        ----------
        index : int
            Zero based index of the breakout structure to be removed.
        """
        self._dispatch.RemoveBreakout(index)

    def remove_breakout_at_depth(self, depth):
        """Removes a breakout structure from the Breakout Log at the specified
        depth in current depth units.

        Parameters
        ----------
        depth : float
            The depth value in current depth units at which the
            breakout structure will be removed.
        """
        self._dispatch.RemoveBreakoutAtDepth(depth)
    
    def lineation(self, index):
        """Gets a lineation pick from the Lineation Log at the specified
        index.

        Parameters
        ----------
        index : int
            Zero based index of the lineation to be retrieved.

        Returns
        -------
        Structure or None
            The lineation at the specified index. If the index is
            outside the valid range no exception will be raised and
            ``None`` will be returned.
        """
        return Structure(self._dispatch.Lineation(index))

    def lineation_at_depth(self, depth):
        """Gets a lineation structure from the Lineation Log at the specified
        depth in current depth units.

        Parameters
        ----------
        depth : float
            The depth value in current depth units at which the
            lineation will be retrieved.

        Returns
        -------
        Structure or None
            The feature closest to the specified depth will be returned.
            If the depth is outside the valid range no exception
            will be raised and ``None`` will be returned.
        """
        return Structure(self._dispatch.LineationAtDepth(depth))

    def insert_new_lineation_ex(self, depth, trend, plunge, eccentricity):
        """Sets a new linear structure in a Lineation Log.

        Parameters
        ----------
        depth : float
            Depth of the mid-point of the fitted line in current depth units.
        trend : float
            Trend direction of the vector in degrees.
        plunge : float
            "Dip" angle of the vector in degrees.
        eccentricity : float
            Offset of the lineation from the center of the borehole.
            A value between -1 and 1 can be set. An eccentricity of 0
            corresponds to a line going straight through the center
            of the borehole.

        Returns
        -------
        Structure
            The newly created lineation structure.
        """
        return Structure(self._dispatch.InsertNewLineationEx(depth, trend, plunge, eccentricity))

    def remove_lineation(self, index):
        """Removes a lineation from the Lineation Log at the
        specified index.

        Parameters
        ----------
        index : int
            Zero based index of the lineation to be removed.
        """
        self._dispatch.RemoveLineation(index)

    def remove_lineation_at_depth(self, depth):
        """Removes a lineation from the Lineation Log at the
        specified depth in current depth units.

        Parameters
        ----------
        depth : float
            The depth value in current depth units at which the
            lineation will be removed.
        """
        self._dispatch.RemoveLineationAtDepth(depth)

    @property
    def length_unit(self):
        """float: The conversion factor (from meters) for the
        breakout structure length measured in the breakout log

        Set it to 0.001 when measured in mm and to 0.0254 when
        measured in inches."""
        return self._dispatch.LengthUnit

    @length_unit.setter
    def length_unit(self, factor):
        self._dispatch.LengthUnit = factor

    @property
    def caliper_unit(self):
        """float: The conversion factor (from meters) for the caliper
        value in a structure log.

        Set it to 0.001 when measured in mm and to 0.0254 when
        measured in inches."""
        return self._dispatch.CaliperUnit

    @caliper_unit.setter
    def caliper_unit(self, factor):
        self._dispatch.CaliperUnit = factor

    @property
    def aperture_unit(self):
        """float: The conversion factor (from meters) for the 
        aperture value in a structure log.  

        Set it to 0.001 when measured in mm and to 0.00254 when
        measured in 1/10th inches."""
        return self._dispatch.ApertureUnit

    @aperture_unit.setter
    def aperture_unit(self, factor):
        self._dispatch.ApertureUnit = factor

    def insert_new_schmit_box(self, top_depth, bottom_depth, text):
        """Inserts a new box into a Polar & Rose Log.

        Parameters
        ----------
        top_depth : float
            The top depth value of the interval in the current depth units.
        bottom_depth : float
            The bottom depth value of the interval in the current depth units.
        text : string
            A text description which is only shown in the tabular editor display.

        Returns
        -------
        PolarAndRoseBox
            The newly created Polar & Rose box.
        """
        return PolarAndRoseBox(self._dispatch.InsertNewSchmitBox(top_depth, bottom_depth, text))

    def schmit_box(self, index):
        """Gets a box object from the Polar & Rose Log at the
        specified index.

        Parameters
        ----------
        index : int
            Zero based index of the box to be returned.

        Returns
        -------
        PolarAndRoseBox
            The Polar & Rose box at the desired index.
        """
        return PolarAndRoseBox(self._dispatch.SchmitBox(index))

    def schmit_box_at_depth(self, depth):
        """Gets a box object from the Polar & Rose Log
        at the specified depth in current depth units.

        Parameters
        ----------
        depth : float
            The depth of the box to be returned in current depth units.

        Returns
        -------
        PolarAndRoseBox
            The Polar & Rose box at the desired depth.
        """
        return PolarAndRoseBox(self._dispatch.SchmitBoxAtDepth(depth))

    def remove_schmit_box(self, index):
        """Removes a box from the Polar & Rose Log at the
        specified index.

        Parameters
        ----------
        index : int
            Zero based index of the Polar & Rose box to be removed.
        """
        self._dispatch.RemoveSchmitBox(index)

    def remove_schmit_box_at_depth(self, depth):
        """Removes a box from the Polar & Rose log at the specified
        depth in current depth units.

        Parameters
        ----------
        depth : float
            The depth of the Polar & Rose box to be removed in
            current depth units.
        """
        self._dispatch.RemoveSchmitBoxAtDepth(depth)

    def cross_box(self, index):
        """Gets a Cross Box object from the Cross Section Log at the specified index.

        Parameters
        ----------
        index : int
            Zero based index of the box to be retrieved.

        Returns
        -------
        CrossSectionBox or None
            The CrossSectionBox at the desired index or None if index is out of range.
        """
        return CrossSectionBox(self._dispatch.CrossBox(index))

    def cross_box_at_depth(self, depth):
        """Gets a Cross Box object from the Cross Section Log at the specified depth in current depth units.

        Parameters
        ----------
        depth : float
            The depth of the box to be retrieved in current depth units.

        Returns
        -------
        CrossSectionBox or None
            The CrossSectionBox at the desired index or None if the index is out of range.
        """
        return CrossSectionBox(self._dispatch.CrossBoxAtDepth(depth))

    def insert_new_cross_box(self, top_depth, bottom_depth):
        """Inserts a new box into the Cross Section Log.

        Parameters
        ----------
        top_depth : float
            The top depth value of the cross section box in current depth units.
        bottom_depth : float
            The bottom depth value of the cross section box in current depth units.

        Returns
        -------
        CrossSectionBox
            The newly created CrossSectionBox.
        """
        return CrossSectionBox(self._dispatch.InsertNewCrossBox(top_depth, bottom_depth))

    def remove_cross_box(self, index):
        """Removes a box from the Cross Section Log at the specified index.

        Parameters
        ----------
        index : int
            Zero based index of the box to be removed.
        """
        self._dispatch.RemoveCrossBox(index)

    def remove_cross_box_at_depth(self, depth):
        """Removes a box from the Cross Section Log at the specified depth.

        Parameters
        ----------
        depth : float
            The depth in current units at which the box will be removed.
        """
        self._dispatch.RemoveCrossBoxAtDepth(depth)

    def insert_new_stack_item(self, top_depth, bottom_depth, top_width, bottom_width):
        """Inserts a new data interval into a Stacking Pattern Log.

        Parameters
        ----------
        top_depth : float
            The top depth value of the interval in the current depth units.
        bottom_depth : float
            The bottom depth value of the interval in the current depth units.
        top_width : float
           Width value at the top of the new interval.
        bottom_width : float
            Width value at the bottom of the new interval.

        Returns
        -------
        StackingPatternItem
            The newly created StackingPatternItem.
        """
        return StackingPatternItem(self._dispatch.InsertNewStackItem(top_depth, bottom_depth, top_width, bottom_width))

    def stack_item(self, index):
        """Gets a Stack Item object from the Stacking Pattern Log at the specified depth index.

        Items are ordered by ascending top depth.

        Parameters
        ----------
        index : int
            Zero based index of the item to be retrieved.

        Returns
        -------
        StackingPatternItem or None
            The StackingPatternItem at the desired index or None if the index is out of range.
        """
        return StackingPatternItem(self._dispatch.StackItem(index))

    def stack_item_at_depth(self, depth):
        """Gets a Stack Item object from the Stacking Pattern Log at the specified depth in current depth units.

        Parameters
        ----------
        depth : float
            The depth of the item to be retrieved in current depth units.

        Returns
        -------
        StackingPatternItem or None
            The StackingPatternItem at the desired depth or None if depth is out of range.
        """
        return StackingPatternItem(self._dispatch.StackItemAtDepth(depth))

    def remove_stack_item(self, index):
        """Removes an item from the Stacking Pattern Log at the specified index.

        Parameters
        ----------
        index : int
            Zero based index  of the stacking pattern box to be removed.
        """
        self._dispatch.RemoveStackItem(index)

    def remove_stack_item_at_depth(self, depth):
        """Removes an item from the Stacking Pattern Log at the specified depth.

        Parameters
        ----------
        depth : float
            The depth of the stack item to be removed in current depth units.
        """
        self._dispatch.RemoveStackItemAtDepth(depth)

    @property
    def used_as_depth_scale(self):
        """bool: Whether the Depth Log is used as the current depth
        reference axis."""
        return self._dispatch.UsedAsDepthScale

    @used_as_depth_scale.setter
    def used_as_depth_scale(self, mode):
        self._dispatch.UsedAsDepthScale = mode

    def insert_new_ole_box_from_file(self, file_name, allow_picture, top_depth, bottom_depth):
        """Inserts a new OLE object between the specified interval
        into an OLE Log.

        OLE objects can be files such as images, Excel charts,
        Word documents or pdfs.

        Parameters
        ----------
        file_name : str
            Path and name of the file to be loaded.
        allow_picture : bool
            Set to True to allow graphic files to be displayed using
            an internal viewer.
        top_depth : float
            Top depth of the OLE object in current depth units.
        bottom_depth : float
            Bottom depth of the OLE object in current depth units.
        """
        self._dispatch.InsertNewOleBoxFromFile(file_name, allow_picture, top_depth, bottom_depth)

    def drill_item(self, index):
        """Gets a Drill Item object from the Engineering Log at the
        specified index.

        Parameters
        ----------
        index : int
            Zero based index at which the drill item will be retrieved.

        Returns
        -------
        DrillItem
            The drill item at the specified index.
        """
        return DrillItem(self._dispatch.DrillItem(index))

    def drill_item_at_depth(self, depth):
        """Gets a Drill Item object from the Engineering Log at the
        specified depth.

        Parameters
        ----------
        depth : float
            The depth of the item to be retrieved in current depth
            units.

        Returns
        -------
        DrillItem
            The drill item at the specified depth.
        """
        return DrillItem(self._dispatch.DrillItemAtDepth(depth))

    def eqp_item(self, index):
        """Gets an Equipment Item object at the specified index from
        the Engineering Log.

        Parameters
        ----------
        index : int
            Zero based index at which the item will be retrieved.

        Returns
        -------
        EquipmentItem
            The equipment item at the specified index.
        """
        return EquipmentItem(self._dispatch.EqpItem(index))

    @property
    def comment_style(self):
        """int: The position of the comment associated with an engineering log.

        The following styles are available:

            * 0 = None, comment is not displayed
            * 1 = Left, comment displayed on the left of the engineering log
            * 2 = Right, comment displayed on the right of the engineering log
        """
        return self._dispatch.CommentStyle

    @comment_style.setter
    def comment_style(self, style):
        self._dispatch.CommentStyle = style

    @property
    def ground_depth(self):
        """float: The starting point (reference datum) of the
        borehole."""
        return self._dispatch.GroundDepth

    @ground_depth.setter
    def ground_depth(self, starting_point):
        self._dispatch.GroundDepth = starting_point

    @property
    def diameter_high(self):
        """float: The maximum diameter scaling value
        (width of the log column) for an Engineering Log."""
        return self._dispatch.DiameterHigh

    @diameter_high.setter
    def diameter_high(self, diameter):
        self._dispatch.DiameterHigh = diameter

    def insert_new_drill_item(self, bottom_depth, diameter):
        """Inserts a new drill item into the Engineering Log.

        Item index are ordered by depth value in the stack of drill
        items.

        Parameters
        ----------
        bottom_depth : float
            The bottom depth of the borehole in current depth units.
            (The top depth is either the ground_depth or the former
            bottom depth).
        diameter : float
            The diameter of the borehole.

        Returns
        -------
        DrillItem
            The inserted DrillItem
        """
        return DrillItem(self._dispatch.InsertNewDrillItem(bottom_depth, diameter))

    def insert_new_eqp_item(self, top_depth, bottom_depth, name):
        """Inserts a new equipment item of the specified name and
        depth interval into the Engineering Log.

        The new item is given the last index in the list of equipment
        items.

        Parameters
        ----------
        top_depth : float
            The top depth of the equipment item interval
            in current units.
        bottom_depth : float
            The bottom depth of the equipment item interval
            in current units.
        name : str
            The name (code) of the equipment item to be inserted.
            Base available equipments names are listed below, but you
            can modify or add your own in the Equipment dictionary.

                * PlainCasing
                * WireWoundCasing
                * SlottedCasing
                * PerforatedCasing
                * Centralizer
                * Shoe
                * Packer
                * Water
                * Wedge
                * HeadWorks
                * Transducer
                * Gauge
                * Cement
                * Gravel
                * NormalThread
                * ReverseThread
                * Plug

            If an invalid name is provided, no item will be inserted.

        Returns
        -------
        EqpItem
            The inserted EqpItem
        """
        return EquipmentItem(self._dispatch.InsertNewEqpItem(top_depth, bottom_depth, name))

    @property
    def nb_of_drill_item(self):
        """int: The number of drill items in an Engineering Log."""
        return self._dispatch.NbOfDrillItem

    @property
    def nb_of_eqp_item(self):
        """int: The number of equipment items in an Engineering Log."""
        return self._dispatch.NbOfEqpItem

    def remove_drill_item(self, index):
        """Removes the drill item at the specified index from an
        Engineering Log.

        Parameters
        ----------
        index : int
            Zero based index at which the item will be removed.
        """
        self._dispatch.RemoveDrillItem(index)

    def remove_eqp_item(self, index):
        """Removes an equipment item at the specified depth index
        from an Engineering Log.

        Parameters
        ----------
        index : int
            Zero based index at which the item will be removed.
        """
        self._dispatch.RemoveEqpItem(index)

    @property
    def background_color(self):
        """int: The background color of the engineering log.

        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values.
        """
        return self._dispatch.BackgroundColor

    @background_color.setter
    def background_color(self, value):
        self._dispatch.BackgroundColor = value


    @property
    def background_hatch_style(self):
        """int: The background hatch style for the Engineering Log.

        Available styles are:

        * 0: horizontal
        * 1: vertical
        * 2: forward diagonal
        * 3: backward diagonal
        * 4: cross
        * 5: diagonal cross

        If an invalid style is set, nothing will happen.
        """
        return self._dispatch.BackgroundHatchStyle

    @background_hatch_style.setter
    def background_hatch_style(self, code):
        self._dispatch.BackgroundHatchStyle = code

    @property
    def background_style(self):
        """int: The background style for the Engineering Log.

        Available styles are:

        * 0: none
        * 1: solid
        * 2: hatch

        If an invalid style is set, nothing will happen.
        """
        return self._dispatch.BackgroundStyle

    @background_style.setter
    def background_style(self, code):
        self._dispatch.BackgroundStyle = code

    def allow_export_attribute_dictionary(self, index, export, password):
        """When dealing with a protected document you can use this method to enable/disable the option
        to export the tadpole dictionary (\*.TAD) from a specific classification column of a Structure or
        Breakout Log. This assumes you are in possession of the password.

        Parameters
        ----------
        index : int
            Zero based index of the classification column for which the protection level should eb changed.
        export : bool
            Set this boolean to True to allow an export as \*.tad file. Set it to False to protect the dictionary.
        password : str
            the password needed to make changes to the protection level.
        """
        self._dispatch.AllowExportAttributeDictionary(index, export, password)

    def allow_export_litho_dictionary(self, export, password):
        """When dealing with a protected document you can use this method to enable / disable the option
        to export the symbol dictionary (\*.LTH) of a log. This assumes you are in possession of the password.

        Parameters
        ----------
        export : bool
            Set this boolean to True to allow the dictionary export. Set it to False to protect the dictionary.
        password : str
            the password needed to make changes to the protection level.
        """
        self._dispatch.AllowExportLithoDictionary(export, password)

    def allow_modify_log_data(self, export, password):
        """When dealing with a protected document you can use this method to enable / disable the option
        to edit the data of a log. This assumes you are in possession of the password.

        Parameters
        ----------
        export : bool
            Set this boolean to True to allow the modification of log data. Set it to False to protect the data.
        password : str
            the password needed to make changes to the protection level.
        """
        self._dispatch.AllowModifyLogData(export, password)

    def allow_modify_log_settings(self, export, password):
        """When dealing with a protected document you can use this method to enable / disable the option
        to change the settings of a log. This assumes you are in possession of the password.

        Parameters
        ----------
        export : bool
            Set this boolean to True to allow access to the log settings. Set it to False to protect the log settings.
        password : str
            the password needed to make changes to the protection level.
        """
        self._dispatch.AllowModifyLogSettings(export, password)

    def allow_use_formula(self, export, password):
        """When dealing with a protected document you can use this method to enable / disable the option
        to access and use the formula in a Formula Log. This assumes you are in possession of the password.

        Parameters
        ----------
        export : bool
            Set this boolean to True to allow access the formula. Set it to False to protect the formula.
        password : str
            the password needed to make changes to the protection level.
        """
        self._dispatch.AllowUseFormula(export, password)

    def allow_view_formula(self, export, password):
        """When dealing with a protected document you can use this method to enable / disable the option
        to see the formula used in a Formula Log. This assumes you are in possession of the password.

        Parameters
        ----------
        export : bool
            Set this boolean to True to see the formula. Set it to False to protect the formula.
        password : str
            the password needed to make changes to the protection level.
        """
        self._dispatch.AllowViewFormula(export, password)

    def allow_view_log_history(self, export, password):
        """When dealing with a protected document you can use this method to enable / disable the option
        to view the log history. This assumes you are in possession of the password.

        Parameters
        ----------
        export : bool
            Set this boolean to True to access the log history. Set it to False to protect the log history.
        password : str
            the password needed to make changes to the protection level.
        """
        self._dispatch.AllowViewLogHistory(export, password)
