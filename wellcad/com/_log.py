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
from ._classifier_dictionary import ClassifierDictionary
from ._contact_dictionary import ContactDictionary
from ._attribute_dictionary import AttributeDictionary

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
        """int: The background style for the Engineering Log and for the Depth Column Log.

        Available styles are:
        For the Engineering Log:
        * 0: none
        * 1: solid
        * 2: hatch
        For the Depth Column Log:
        * 0: opaque
        * 1: transparent

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

    def set_caliper_component(self, caliper_log):
        """caliper_log: The index or the title of the caliper log"""
        return self._dispatch.SetCaliperComponent(caliper_log)

    def set_amplitude_component(self, amplitude_log):
        """amplitude_log: The index or the title of the amplitude log"""
        return self._dispatch.SetAmplitudeComponent(amplitude_log)

    def set_structure_component(self, structure_log):
        """structure_log: The index or the title of the structure log"""
        return self._dispatch.SetStructureComponent(structure_log)

    def set_lineation_component(self, lineation_log):
        """lineation_log: The index or the title of the lineation log"""
        return self._dispatch.SetLineationComponent(lineation_log)

    @property
    def maj_grid_color(self):
        """int: The background color of the major vertical grid.

        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values.
        """
        return self._dispatch.MajGridColor

    @maj_grid_color.setter
    def maj_grid_color(self, color):
        self._dispatch.MajGridColor = color

    @property
    def min_grid_color(self):
        """int: The background color of the minor vertical grids.

        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values.
        """
        return self._dispatch.MinGridColor

    @min_grid_color.setter
    def min_grid_color(self, color):
        self._dispatch.MinGridColor = color

    @property
    def maj_grid_width(self):
        """int: The width of the major vertical grid lines (in mm/10)."""
        return self._dispatch.MajGridWidth

    @maj_grid_width.setter
    def maj_grid_width(self, width):
        self._dispatch.MajGridWidth = width

    @property
    def min_grid_width(self):
        """int: The width of the minor vertical grid lines (in mm/10)."""
        return self._dispatch.MinGridWidth

    @min_grid_width.setter
    def min_grid_width(self, width):
        self._dispatch.MinGridWidth = width

    @property
    def maj_grid_style(self):
        """int: The pen style of the major vertical grid lines.

        Styles are specified as an integer:

        * Solid = 0
        * Dashed = 1
        * Dotted = 2
        * Dash-Dot = 3
        * Dash-dot-dot = 4
        """
        return self._dispatch.MajGridStyle

    @maj_grid_style.setter
    def maj_grid_style(self, style):
        self._dispatch.MajGridStyle = style

    @property
    def min_grid_style(self):
        """int: The pen style of the minor vertical grid lines.

        Styles are specified as an integer:

        * Solid = 0
        * Dashed = 1
        * Dotted = 2
        * Dash-Dot = 3
        * Dash-dot-dot = 4
        """
        return self._dispatch.MinGridStyle

    @min_grid_style.setter
    def min_grid_style(self, style):
        self._dispatch.MinGridStyle = style

    @property
    def overwrite_depth_grids(self):
        """bool: Whether the depth grids shall be overwritten or not."""
        return self._dispatch.OverwriteDepthGrids

    @overwrite_depth_grids.setter
    def overwrite_depth_grids(self, overwrite):
        self._dispatch.OverwriteDepthGrids = overwrite

    @property
    def overflow_type(self):
        """int: The type of overflow."""
        return self._dispatch.OverflowType

    @overflow_type.setter
    def overflow_type(self, type):
        self._dispatch.OverflowType = type

    @property
    def decades(self):
        """int: The number of decades for the logarithmic scale."""
        return self._dispatch.Decades

    @decades.setter
    def decades(self, dec):
        self._dispatch.Decades = dec

    @property
    def cardinal_points_color(self):
        """int: The color of the cardinal points.

        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values.
        """
        return self._dispatch.CardinalPointsColor

    @cardinal_points_color.setter
    def cardinal_points_color(self, color):
        self._dispatch.CardinalPointsColor = color

    @property
    def left_shading_color(self):
        """int: The color of the left shading.

        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values.
        """
        return self._dispatch.LeftShadingColor

    @left_shading_color.setter
    def left_shading_color(self, color):
        self._dispatch.LeftShadingColor = color

    @property
    def right_shading_color(self):
        """int: The color of the right shading.

        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values.
        """
        return self._dispatch.RightShadingColor

    @right_shading_color.setter
    def right_shading_color(self, color):
        self._dispatch.RightShadingColor = color

    @property
    def curves_count(self):
        """int: The index multiplier of the displayed traces."""
        return self._dispatch.CurvesCount

    @curves_count.setter
    def curves_count(self, count):
        self._dispatch.CurvesCount = count

    @property
    def shading_type(self):
        """int: The type of shading."""
        return self._dispatch.ShadingType

    @shading_type.setter
    def shading_type(self, type):
        self._dispatch.ShadingType = type

    def get_attribute_dictionary(self, name):
        """CFracDatabase: The dictionary of the selected attribute."""
        return AttributeDictionary(self._dispatch.GetAttributeDictionary(name))

    @property
    def text_format(self):
        """int: The index corresponding to the text format.
        0 = Plain Text
        1 = Rich Text
        """
        return self._dispatch.TextFormat

    @text_format.setter
    def text_format(self, format_index):
        self._dispatch.TextFormat = format_index

    @property
    def horz_text_align(self):
        """
        int: The index corresponding to the horizontal text alignment.
        0 = Left
        1 = Center
        2 = Right
        """
        return self._dispatch.HorzTextAlignment

    @horz_text_align.setter
    def horz_text_align(self, align_index):
        self._dispatch.HorzTextAlignment = align_index

    @property
    def vert_text_align(self):
        """
        int: The index corresponding to the vertical text alignment.
        0 = Top
        1 = Center
        2 = Bottom
        """
        return self._dispatch.VertTextAlignment

    @vert_text_align.setter
    def vert_text_align(self, align_index):
        self._dispatch.VertTextAlignment = align_index

    @property
    def text_orientation(self):
        """
        int: The index corresponding to the text orientation.
        0 = Normal
        1 = Left
        2 = Right
        3 = Reverse (only for Comment Log)
        """
        return self._dispatch.TextOrientation

    @text_orientation.setter
    def text_orientation(self, orientation_index):
        self._dispatch.TextOrientation = orientation_index

    @property
    def repeat_text(self):
        """bool: Whether the text will be repeated in a text box or not."""
        return self._dispatch.RepeatText

    @repeat_text.setter
    def repeat_text(self, repeat):
        self._dispatch.RepeatText = repeat

    @property
    def repeat_text_spacing(self):
        """int: The spacing (in mm/10) between each repeated text box."""
        return self._dispatch.RepeatTextSpacing

    @repeat_text_spacing.setter
    def repeat_text_spacing(self, spacing):
        self._dispatch.RepeatTextSpacing = spacing

    @property
    def top_depth_indicator(self):
        """
        int: The index corresponding to the top depth indicator.
        0 = None
        1 = Left
        2 = Center
        3 = Right
        """
        return self._dispatch.TopDepthIndicator

    @top_depth_indicator.setter
    def top_depth_indicator(self, indicator_index):
        self._dispatch.TopDepthIndicator = indicator_index

    @property
    def bottom_depth_indicator(self):
        """
        int: The index corresponding to the bottom depth indicator.
        0 = None
        1 = Left
        2 = Center
        3 = Right
        """
        return self._dispatch.BottomDepthIndicator

    @bottom_depth_indicator.setter
    def bottom_depth_indicator(self, indicator_index):
        self._dispatch.BottomDepthIndicator = indicator_index

    @property
    def depth_font(self):
        """Gets the font used in a Comment Log for the depth."""
        return Font(self._dispatch.DepthFont)

    @depth_font.setter
    def depth_font(self, font):
        self._dispatch.DepthFont = font._dispatch

    @property
    def depth_digits(self):
        """int: The number of digits used for the depth."""
        return self._dispatch.DepthDigits

    @depth_digits.setter
    def depth_digits(self, nb_digits):
        self._dispatch.DepthDigits = nb_digits

    @property
    def pinches_position(self):
        """
        int: The index corresponding to the position of the pinches.
        1 = Left
        2 = Right
        3 = Center
        4 = None
        """
        return self._dispatch.PinchesPosition

    @pinches_position.setter
    def pinches_position(self, position_index):
        self._dispatch.PinchesPosition = position_index

    @property
    def allow_pinches(self):
        """bool: Whether pinches are allowed (height of the box optimized) or not (height of the box corresponding to the depth interval)."""
        return self._dispatch.AllowPinches

    @allow_pinches.setter
    def allow_pinches(self, allow):
        self._dispatch.AllowPinches = allow

    @property
    def classifier_dictionary(self):
        """ClassifierDictionary: The classifier library used by the log (Well/Mud/Interval)."""
        return ClassifierDictionary(self._dispatch.ClassifierDictionary)

    @classifier_dictionary.setter
    def classifier_dictionary(self, dictionary):
        self._dispatch.ClassifierDictionary = dictionary._dispatch

    def attach_classifier_dictionary(self, dictionary_name):
        """Attaches a new classifier dictionary to the Well/Mud/Interval Log.

        Parameters
        ----------
        dictionary : str
            path and name of the file to attach

        Returns
        -------
            ClassifierDictionary
                The ClassifierDictionary object
        """
        return ClassifierDictionary(self._dispatch.AttachClassifierDictionary(dictionary_name))

    @property
    def display_depth(self):
        """bool: Whether or not the markers' depths are displayed."""
        return self._dispatch.DisplayDepth

    @display_depth.setter
    def display_depth(self, display):
        self._dispatch.DisplayDepth = display

    @property
    def display_name(self):
        """bool: Whether or not the markers' names are displayed."""
        return self._dispatch.DisplayName

    @display_name.setter
    def display_name(self, display):
        self._dispatch.DisplayName = display

    @property
    def name_font(self):
        """Gets the font used in a Marker Log for the names."""
        return Font(self._dispatch.NameFont)

    @name_font.setter
    def name_font(self, font):
        self._dispatch.NameFont = font._dispatch

    @property
    def display_comment(self):
        """bool: Whether or not the markers' comments are displayed."""
        return self._dispatch.DisplayComment

    @display_comment.setter
    def display_comment(self, display):
        self._dispatch.DisplayComment = display

    @property
    def shading_color_up(self):
        """int: The color of the shading used for the upper amplitudes.

        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values.
        """
        return self._dispatch.ShadingColorUp

    @shading_color_up.setter
    def shading_color_up(self, color):
        self._dispatch.ShadingColorUp = color

    @property
    def shading_color_down(self):
        """int: The color of the shading used for the lower amplitudes.

        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values.
        """
        return self._dispatch.ShadingColorDown

    @shading_color_down.setter
    def shading_color_down(self, color):
        self._dispatch.ShadingColorDown = color

    @property
    def zero_line(self):
        """float: The amplitude corresponding to the zero line."""
        return self._dispatch.ZeroLine

    @zero_line.setter
    def zero_line(self, value):
        self._dispatch.ZeroLine = value

    @property
    def scale_factor(self):
        """float: The scale factor of the amplitude."""
        return self._dispatch.ScaleFactor

    @scale_factor.setter
    def scale_factor(self, value):
        self._dispatch.ScaleFactor = value

    @property
    def use_associated_color(self):
        """BOOL: Specifies whether the beds will be filled with the associated colors instead of the patterns."""
        return self._dispatch.UseAssociatedColor

    @use_associated_color.setter
    def use_associated_color(self, enable):
        self._dispatch.UseAssociatedColor = enable

    @property
    def hide_symbol_background(self):
        """BOOL: Specifies whether or not the symbols' background will be transparent."""
        return self._dispatch.HideSymbolBackground

    @hide_symbol_background.setter
    def hide_symbol_background(self, hide):
        self._dispatch.HideSymbolBackground = hide

    @property
    def symbol_scale(self):
        """float: The scale factor for the symbols' size.
        1.0 corresponds to 100%."""
        return self._dispatch.SymbolScale

    @symbol_scale.setter
    def symbol_scale(self, value):
        self._dispatch.SymbolScale = value

    @property
    def display_contact(self):
        """BOOL: Specifies whether or not the contacts are displayed on the log."""
        return self._dispatch.DisplayContact

    @display_contact.setter
    def display_contact(self, display):
        self._dispatch.DisplayContact = display

    @property
    def display_text(self):
        """BOOL: Specifies whether or not the text will be displayed."""
        return self._dispatch.DisplayText

    @display_text.setter
    def display_text(self, display):
        self._dispatch.DisplayText = display

    @property
    def label_mode(self):
        """int: The index of the text displaying mode.
        0: Code only
        1: Description
        2: Code and description.
        """
        return self._dispatch.LabelMode

    @label_mode.setter
    def label_mode(self, mode):
        self._dispatch.LabelMode = mode

    @property
    def drawing_mode(self):
        """int: The index of the drawing mode.
        0: All slices in interval superimposed
        1: Interval average slice
        """
        return self._dispatch.DrawingMode

    @drawing_mode.setter
    def drawing_mode(self, mode):
        self._dispatch.DrawingMode = mode

    @property
    def display_internal_circle(self):
        """BOOL: Specifies whether or not we display the internal circle."""
        return self._dispatch.DisplayInternalCircle

    @display_internal_circle.setter
    def display_internal_circle(self, display):
        self._dispatch.DisplayInternalCircle = display

    @property
    def internal_radius(self):
        """float: The radius of the internal circle."""
        return self._dispatch.InternalRadius

    @internal_radius.setter
    def internal_radius(self, radius):
        self._dispatch.InternalRadius = radius

    @property
    def internal_shading_position(self):
        """int: The index of the internal shading position.
        0: None
        1: Inside
        2: Outside
        3: Both
        """
        return self._dispatch.InternalShadingPosition

    @internal_shading_position.setter
    def internal_shading_position(self, pos):
        self._dispatch.InternalShadingPosition = pos

    @property
    def internal_shading_color(self):
        """int: The color of the internal shading.

        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values.
        """
        return self._dispatch.InternalShadingColor

    @internal_shading_color.setter
    def internal_shading_color(self, color):
        self._dispatch.InternalShadingColor = color

    @property
    def internal_shading_style(self):
        """int: The index of the internal shading's style.
        0: None
        1: Solid
        2: Horizontal Hatch
        3: Vertical Hatch
        4: Downward Diagonal Hatch
        5: Upward Diagonal Hatch
        6: Cross Hatch
        7: Diagonal Cross Hatch
        """
        return self._dispatch.InternalShadingStyle

    @internal_shading_style.setter
    def internal_shading_style(self, style):
        self._dispatch.InternalShadingStyle = style

    @property
    def display_external_circle(self):
        """BOOL: Specifies whether or not we display the external circle."""
        return self._dispatch.DisplayExternalCircle

    @display_external_circle.setter
    def display_external_circle(self, display):
        self._dispatch.DisplayExternalCircle = display

    @property
    def external_radius(self):
        """float: The radius of the external circle."""
        return self._dispatch.ExternalRadius

    @external_radius.setter
    def external_radius(self, radius):
        self._dispatch.ExternalRadius = radius

    @property
    def external_shading_position(self):
        """int: The index of the external shading position.
        0: None
        1: Inside
        2: Outside
        3: Both
        """
        return self._dispatch.ExternalShadingPosition

    @external_shading_position.setter
    def external_shading_position(self, pos):
        self._dispatch.ExternalShadingPosition = pos

    @property
    def external_shading_color(self):
        """int: The color of the external shading.

        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values.
        """
        return self._dispatch.ExternalShadingColor

    @external_shading_color.setter
    def external_shading_color(self, color):
        self._dispatch.ExternalShadingColor = color

    @property
    def external_shading_style(self):
        """int: The index of the external shading's style.
        0: None
        1: Solid
        2: Horizontal Hatch
        3: Vertical Hatch
        4: Downward Diagonal Hatch
        5: Upward Diagonal Hatch
        6: Cross Hatch
        7: Diagonal Cross Hatch
        """
        return self._dispatch.ExternalShadingStyle

    @external_shading_style.setter
    def external_shading_style(self, style):
        self._dispatch.ExternalShadingStyle = style

    @property
    def display_azimuth(self):
        """BOOL: Specifies whether or not we display the azimuth grid."""
        return self._dispatch.DisplayAzimuth

    @display_azimuth.setter
    def display_azimuth(self, display):
        self._dispatch.DisplayAzimuth = display

    @property
    def azimuth_spacing(self):
        """int: The step (in degree) between two azimuth tick marks."""
        return self._dispatch.AzimuthSpacing

    @azimuth_spacing.setter
    def azimuth_spacing(self, spacing):
        self._dispatch.AzimuthSpacing = spacing

    @property
    def display_caliper(self):
        """BOOL: Specifies whether or not we display the caliper grid."""
        return self._dispatch.DisplayCaliper

    @display_caliper.setter
    def display_caliper(self, display):
        self._dispatch.DisplayCaliper = display

    @property
    def caliper_spacing(self):
        """float: The step (in degree) between two concentric circles of the caliper grid."""
        return self._dispatch.CaliperSpacing

    @caliper_spacing.setter
    def caliper_spacing(self, spacing):
        self._dispatch.CaliperSpacing = spacing

    @property
    def display_labels(self):
        """BOOL: Specifies whether or not we display the labels."""
        return self._dispatch.DisplayLabels

    @display_labels.setter
    def display_labels(self, display):
        self._dispatch.DisplayLabels = display

    @property
    def retrogradation_color(self):
        """int: The color of the retrogradation patterns.

        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values.
        """
        return self._dispatch.RetrogradationColor

    @retrogradation_color.setter
    def retrogradation_color(self, color):
        self._dispatch.RetrogradationColor = color

    @property
    def progradation_color(self):
        """int: The color of the progradation patterns.

        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values.
        """
        return self._dispatch.ProgradationColor

    @progradation_color.setter
    def progradation_color(self, color):
        self._dispatch.ProgradationColor = color

    @property
    def aggradation_color(self):
        """int: The color of the aggradation patterns.

        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values.
        """
        return self._dispatch.AggradationColor

    @aggradation_color.setter
    def aggradation_color(self, color):
        self._dispatch.AggradationColor = color

    @property
    def display_limits(self):
        """BOOL: Specifies if the limits of the intervals are displayed."""
        return self._dispatch.DisplayLimits

    @display_limits.setter
    def display_limits(self, display):
        self._dispatch.DisplayLimits = display

    @property
    def display_structure_aperture(self):
        """BOOL: Specifies if the aperture of the structures is displayed on the 3D Log."""
        return self._dispatch.DisplayStructureAperture

    @display_structure_aperture.setter
    def display_structure_aperture(self, display):
        self._dispatch.DisplayStructureAperture = display

    @property
    def projection_type(self):
        """int: The index of the projection type.
        0: Perspective
        1: 3rd Angle
        2: None
        """
        return self._dispatch.Projection

    @projection_type.setter
    def projection_type(self, projection_index):
        self._dispatch.Projection = projection_index

    @property
    def frame_type(self):
        """int: The index of the frame type.
        0: No Frame
        1: Frame Only
        2: Frame & Surface
        """
        return self._dispatch.Frame

    @frame_type.setter
    def frame_type(self, frame_index):
        self._dispatch.Frame = frame_index

    @property
    def min_cylinder_faces(self):
        """int: The minimum number of faces rendered for each slice."""
        return self._dispatch.MinCylinderFaces

    @min_cylinder_faces.setter
    def min_cylinder_faces(self, min_faces):
        self._dispatch.MinCylinderFaces = min_faces

    @property
    def ambient_intensity(self):
        """float: The intensity of the ambient light, between 0 and 1."""
        return self._dispatch.AmbientIntensity

    @ambient_intensity.setter
    def ambient_intensity(self, intensity):
        self._dispatch.AmbientIntensity = intensity

    @property
    def spot_intensity(self):
        """float: The intensity of the spotlight."""
        return self._dispatch.SpotIntensity

    @spot_intensity.setter
    def spot_intensity(self, intensity):
        self._dispatch.SpotIntensity = intensity

    @property
    def spot_vert_pos(self):
        """float: The angle of the spotlight (between 5° and 175°)."""
        return self._dispatch.SpotVerticalPos

    @spot_vert_pos.setter
    def spot_vert_pos(self, angle):
        self._dispatch.SpotVerticalPos = angle

    @property
    def view_angle(self):
        """float: The angular position of the user's point of view."""
        return self._dispatch.ViewAngle

    @view_angle.setter
    def view_angle(self, angle):
        self._dispatch.ViewAngle = angle

    @property
    def caliper_low(self):
        """float: The low scale value of the caliper component."""
        return self._dispatch.CaliperLow

    @caliper_low.setter
    def caliper_low(self, value):
        self._dispatch.CaliperLow = value

    @property
    def caliper_high(self):
        """float: The high scale value of the caliper component."""
        return self._dispatch.CaliperHigh

    @caliper_high.setter
    def caliper_high(self, value):
        self._dispatch.CaliperHigh = value

    @property
    def caliper_from_log(self):
        """BOOL: Specifies whether we extract the caliper values from the caliper log or not (then we use the fixed value)."""
        return self._dispatch.CaliperFromLog

    @caliper_from_log.setter
    def caliper_from_log(self, enable):
        self._dispatch.CaliperFromLog = enable

    @property
    def depth_of_img_from_log(self):
        """BOOL: Specifies whether we extract the DoI values from the DoI log or not (then we use the fixed value)."""
        return self._dispatch.DepthOfImgFromLog

    @depth_of_img_from_log.setter
    def depth_of_img_from_log(self, enable):
        self._dispatch.DepthOfImgFromLog = enable

    @property
    def caliper_value(self):
        """float: The caliper fixed value."""
        return self._dispatch.CaliperValue

    @caliper_value.setter
    def caliper_value(self, value):
        self._dispatch.CaliperValue = value

    @property
    def depth_of_img_value(self):
        """float: The depth of image fixed value."""
        return self._dispatch.DepthOfImgValue

    @depth_of_img_value.setter
    def depth_of_img_value(self, value):
        self._dispatch.DepthOfImgValue = value

    @property
    def slabcore_azimuth(self):
        """float: The slabcore azimuth of the structure log."""
        return self._dispatch.SlabCoreAzimuth

    @slabcore_azimuth.setter
    def slabcore_azimuth(self, value):
        self._dispatch.SlabCoreAzimuth = value

    @property
    def slabcore_style(self):
        """int: The index of the slabcore style.
        0: Full Size
        1: Fixed Size
        """
        return self._dispatch.SlabCoreStyle

    @slabcore_style.setter
    def slabcore_style(self, style_index):
        self._dispatch.SlabCoreStyle = style_index

    @property
    def display_full_partial_picks(self):
        """BOOL: Specifies whether or not the sinusoids are entirely drawn when dealing with partial picks (with a dotted line for parts not included in the offsets of the fracture)."""
        return self._dispatch.DisplayFullPartialPicks

    @display_full_partial_picks.setter
    def display_full_partial_picks(self, display):
        self._dispatch.DisplayFullPartialPicks = display

    @property
    def display_nodes(self):
        """BOOL: Specifies whether the nodes of a structure log are displayed or not."""
        return self._dispatch.DisplayNodes

    @display_nodes.setter
    def display_nodes(self, display):
        self._dispatch.DisplayNodes = display

    @property
    def display_opening(self):
        """BOOL: Specifies for a breakout log using a symbol style whether the opening angles are displayed or not."""
        return self._dispatch.DisplayOpening

    @display_opening.setter
    def display_opening(self, display):
        self._dispatch.DisplayOpening = display

    def set_caliper_log(self, caliper_log):
        """caliper_log: The index or the title of the caliper log"""
        self._dispatch.SetCaliperLog(caliper_log)

    def set_depth_of_img_log(self, depth_of_img_log):
        """depth_of_img_log: The index or the title of the depth of image log"""
        self._dispatch.SetDepthOfImgLog(depth_of_img_log)

    @property
    def shading_style(self):
        """int: The index of the shading style.
        0: None
        1: Solid
        2: Horizontal Hatch
        3: Vertical Hatch
        4: Downward Diagonal Hatch
        5: Upward Diagonal Hatch
        6: Cross Hatch
        7: Diagonal Cross Hatch
        """
        return self._dispatch.ShadingStyle

    @shading_style.setter
    def shading_style(self, style):
        self._dispatch.ShadingStyle = style

    @property
    def shading_color(self):
        """int: The color of the shading.

        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values.
        """
        return self._dispatch.ShadingColor

    @shading_color.setter
    def shading_color(self, color):
        self._dispatch.ShadingColor = color

    @property
    def opacity(self):
        """int: The opacity of the shading, between 0 (transparent) and 100 (opaque)."""
        return self._dispatch.Opacity

    @opacity.setter
    def opacity(self, value):
        self._dispatch.Opacity = value

    @property
    def top_arrow_shape(self):
        """int: The index of the top arrow shape.
        0: None
        1: Flat
        2: Semi Flat Left
        3: Semi Flat Right
        4: Arrow
        5: Semi Arrow Left
        6: Semi Arrow Right
        7: Empty Triangle
        8: Fill Triangle
        9: Empty Rounded Triangle
        10: Fill Rounded Triangle
        11: Empty Rectangle
        12: Fill Rectangle
        13: Empty Circle
        14: Fill Circle
        15: Empty Lozenge
        16: Fill Lozenge
        """
        return self._dispatch.TopArrowShape

    @top_arrow_shape.setter
    def top_arrow_shape(self, shape):
        self._dispatch.TopArrowShape = shape

    @property
    def top_arrow_width(self):
        """int: Top arrow width, between 0 and 1000."""
        return self._dispatch.TopArrowWidth

    @top_arrow_width.setter
    def top_arrow_width(self, width):
        self._dispatch.TopArrowWidth = width

    @property
    def top_arrow_height(self):
        """int: Top arrow height, between 0 and 1000."""
        return self._dispatch.TopArrowHeight

    @top_arrow_height.setter
    def top_arrow_height(self, height):
        self._dispatch.TopArrowHeight = height

    @property
    def bottom_arrow_shape(self):
        """int: The index of the bottom arrow shape.
        0: None
        1: Flat
        2: Semi Flat Left
        3: Semi Flat Right
        4: Arrow
        5: Semi Arrow Left
        6: Semi Arrow Right
        7: Empty Triangle
        8: Fill Triangle
        9: Empty Rounded Triangle
        10: Fill Rounded Triangle
        11: Empty Rectangle
        12: Fill Rectangle
        13: Empty Circle
        14: Fill Circle
        15: Empty Lozenge
        16: Fill Lozenge
        """
        return self._dispatch.BottomArrowShape

    @bottom_arrow_shape.setter
    def bottom_arrow_shape(self, shape):
        self._dispatch.BottomArrowShape = shape

    @property
    def bottom_arrow_width(self):
        """int: Bottom arrow width, between 0 and 1000."""
        return self._dispatch.BottomArrowWidth

    @bottom_arrow_width.setter
    def bottom_arrow_width(self, width):
        self._dispatch.BottomArrowWidth = width

    @property
    def bottom_arrow_height(self):
        """int: Bottom arrow height, between 0 and 1000."""
        return self._dispatch.BottomArrowHeight

    @bottom_arrow_height.setter
    def bottom_arrow_height(self, height):
        self._dispatch.BottomArrowHeight = height

    @property
    def classified(self):
        """BOOL: Whether or not the log (well, mud or interval) is classified."""
        return self._dispatch.Classified

    @classified.setter
    def classified(self, classified):
        self._dispatch.Classified = classified

    @property
    def symbol_style(self):
        """int: The index of the symbol style.
        0: Circle
        1: Disk
        2: Square
        3: Box
        4: Triangle
        5: Pyramid
        6: Lozenge
        7: Diamond
        8: Cross
        9: Star
        """
        return self._dispatch.SymbolStyle

    @symbol_style.setter
    def symbol_style(self, style):
        self._dispatch.SymbolStyle = style

    @property
    def symbol_color(self):
        """int: The color of the symbols.

        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values.
        """
        return self._dispatch.SymbolColor

    @symbol_color.setter
    def symbol_color(self, color):
        self._dispatch.SymbolColor = color

    @property
    def symbol_size(self):
        """int: The size of the symbol (in mm/10)."""
        return self._dispatch.SymbolSize

    @symbol_size.setter
    def symbol_size(self, size):
        self._dispatch.SymbolSize = size

    @property
    def attach_depth_to(self):
        """int: The index indicating if the depth is attached to the top, the middle or the bottom of the bar.
        1: Attach to top
        2: Attach to middle
        3: Attach to bottom
        """
        return self._dispatch.AttachDepthTo

    @attach_depth_to.setter
    def attach_depth_to(self, size):
        self._dispatch.AttachDepthTo = size

    @property
    def digits(self):
        """int: The number of displayed digits."""
        return self._dispatch.Digits

    @digits.setter
    def digits(self, nb):
        self._dispatch.Digits = nb

    def attach_palette(self, palette_name):
        """Attaches an existing palette to the log.

        Parameters
        ----------
        palette_name : str
            path and name of the palette file to attach
        """
        self._dispatch.AttachPalette(palette_name)

    @property
    def scale(self):
        """float: The scale factor of a depth log."""
        return self._dispatch.Scale

    @scale.setter
    def scale(self, value):
        self._dispatch.Scale = value

    @property
    def paper_scale_unit(self):
        """int: The index of the unit used by the plot paper.
        0: meter
        1: foot
        2: inch
        3: cm
        4: mm
        """
        return self._dispatch.PaperScaleUnit

    @paper_scale_unit.setter
    def paper_scale_unit(self, index):
        self._dispatch.PaperScaleUnit = index

    @property
    def data_scale_unit(self):
        """int: The index of the data scale unit. This parameters will always be equal to the
        log unit and can't be changed, except when unit the Date/Time format. In this case,
        the unit can be chosen between option 5 and option 9.
        Possible options :
        0: meters
        1: feet
        2: inch
        3: cm
        4: mm
        5: days
        6: hours
        7: minutes
        8: seconds
        9: milliseconds
        """
        return self._dispatch.DataScaleUnit

    @data_scale_unit.setter
    def data_scale_unit(self, value):
        self._dispatch.DataScaleUnit = value

    @property
    def display_data(self):
        """int: The index of the data display mode.
        0: Standard Depth Scale
        1: Data Spacing
        """
        return self._dispatch.DisplayData

    @display_data.setter
    def display_data(self, index):
        self._dispatch.DisplayData = index

    @property
    def data_spacing(self):
        """int: The rank multiplier of the data that will be displayed. If it's equal to 1, all data points will be displayed. If it's equal to 2, every 2nd point will be displayed and so on."""
        return self._dispatch.DataSpacing

    @data_spacing.setter
    def data_spacing(self, value):
        self._dispatch.DataSpacing = value

    @property
    def date_format(self):
        """int: The index of the date format.
        0: Date not displayed
        1: DD/MM/YY (default format)
        2: DD/MM/YYYY
        3: DD-MMM-YY
        4: DD-MMM-YYYY
        5: MM/DD/YY
        6: MM/DD/YYYY
        7: DD-MMM
        8: DD/MM
        """
        return self._dispatch.DateFormat

    @date_format.setter
    def date_format(self, index):
        self._dispatch.DateFormat = index

    @property
    def date_stamp(self):
        """int: The frequency (in minutes) at which a date stamp will be displayed."""
        return self._dispatch.DateStamp

    @date_stamp.setter
    def date_stamp(self, value):
        self._dispatch.DateStamp = value

    @property
    def time_format(self):
        """int: The index of the date format.
        0: Date not displayed
        1: HH:MM:SS (default format)
        2: HH:MM:SS.0
        3: HH:MM
        4: MM:SS.0
        5: SS.0
        6: UNIX Time
        7: seconds since Time Zero
        """
        return self._dispatch.TimeFormat

    @time_format.setter
    def time_format(self, index):
        self._dispatch.TimeFormat = index

    @property
    def gmt_offset(self):
        """int: The value (in minutes) of the GMT correction."""
        return self._dispatch.GMTOffset

    @gmt_offset.setter
    def gmt_offset(self, value):
        self._dispatch.GMTOffset = value

    @property
    def indicators_per_spacing(self):
        """int: The number of depth strings per spacing."""
        return self._dispatch.IndicatorsPerSpacing

    @indicators_per_spacing.setter
    def indicators_per_spacing(self, value):
        self._dispatch.IndicatorsPerSpacing = value

    @property
    def ticks_position(self):
        """int: The index corresponding to the position of the ticks.
        0: None
        1: Left
        2: Right
        3: Both
        """
        return self._dispatch.TicksPosition

    @ticks_position.setter
    def ticks_position(self, value):
        self._dispatch.TicksPosition = value

    @property
    def min_grid_number(self):
        """int: The number of minor lines per spacing."""
        return self._dispatch.MinGridNumber

    @min_grid_number.setter
    def min_grid_number(self, value):
        self._dispatch.MinGridNumber = value

    @property
    def maj_grid_number(self):
        """int: The number of major lines per spacing."""
        return self._dispatch.MajGridNumber

    @maj_grid_number.setter
    def maj_grid_number(self, value):
        self._dispatch.MajGridNumber = value

    @property
    def min_grid_tick_style(self):
        """int: The index corresponding to the tick style of the minor grid's lines.
        0: Small Line
        1: Large Line
        2: Small Triangle
        3: Large Triangle
        """
        return self._dispatch.MinGridTickStyle

    @min_grid_tick_style.setter
    def min_grid_tick_style(self, value):
        self._dispatch.MinGridTickStyle = value

    @property
    def maj_grid_tick_style(self):
        """int: The index corresponding to the tick style of the major grid's lines.
        0: Small Line
        1: Large Line
        2: Small Triangle
        3: Large Triangle
        """
        return self._dispatch.MajGridTickStyle

    @maj_grid_tick_style.setter
    def maj_grid_tick_style(self, value):
        self._dispatch.MajGridTickStyle = value

    def attach_contact_dictionary(self, dictionary):
        """Attaches a new contact library (\*.ctd file) to a Litho, Strata or Marker Log.

        Parameters
        ----------
        dictionary : str
            path and name of the .CTD file to attach

        Returns
        -------
            ContactDictionary
                The ContactDictionary object
        """
        return ContactDictionary(self._dispatch.AttachContactDictionary(dictionary))

    @property
    def contact_dictionary(self):
        """ContactDictionary: The contact database used by the log (Litho/Strata/Marker Log)."""
        return ContactDictionary(self._dispatch.ContactDictionary)

    @contact_dictionary.setter
    def contact_dictionary(self, dictionary):
        self._dispatch.ContactDictionary = dictionary._dispatch

    @property
    def limit_contact_to_column(self):
        """BOOL: Whether or not the contacts are limited to non empty columns."""
        return self._dispatch.LimitContactToColumn

    @limit_contact_to_column.setter
    def limit_contact_to_column(self, enable):
        self._dispatch.LimitContactToColumn = enable

    @property
    def display_background(self):
        """BOOL: Whether or not the background is filled with a pattern/color."""
        return self._dispatch.DisplayBackground

    @display_background.setter
    def display_background(self, enable):
        self._dispatch.DisplayBackground = enable

    @property
    def time_zero(self):
        """int: The initial time of the Date/Time column in seconds with 0 corresponding to the 01/01/1970 at 00:00:00.
        For example, choosing 90130 will make it start on the 02/01/1970 at 01:02:10."""
        return self._dispatch.TimeZero

    @time_zero.setter
    def time_zero(self, enable):
        self._dispatch.TimeZero = enable

    def remove_attribute(self, name):
        """Remove the chosen attribute from a Breakout/Lineation/Structure Log.

        Parameters
        ----------
        name : str
            Name of the attribute to delete.
        """
        self._dispatch.RemoveAttribute(name)

    @property
    def nb_of_attributes(self):
        """int: The number of attributes associated to the Structure/Breakout/Lineation Log."""
        return self._dispatch.NbOfAttributes


    def set_left_right_border(self, left_border, right_border):
        """Selects the left and right borders of the zone where the shading will be painted.

        Parameters
        ----------
        left_border : str or float
            Can be a constant value, the name of a log or the left border of the shading log (if the log's right border has not already been selected.


        right_border : str or float
            Can be a constant value, the name of a log or the right border of the shading log (if the log's left border has not already been selected).
        """
        self._dispatch.SetLeftRightBorder(left_border, right_border)

    @property
    def get_left_border(self):
        """str: The name of the left border. It can be the name of a log, the left border of the shading log or a string containing a number."""
        return self._dispatch.LeftBorder

    @property
    def get_right_border(self):
        """str: The name of the right border. It can be the name of a log, the right border of the shading log or a string containing a number."""
        return self._dispatch.RightBorder

    def remove_component(self, index):
        """Remove the component of a Percentage/Analysis Log.

        Parameters
        ----------
        index : int
            Index of the component to delete.
        """
        self._dispatch.RemoveComponent(index)

    @property
    def nb_of_columns(self):
        """int: The number of columns in the Strata Log."""
        return self._dispatch.NbOfColumns

    def insert_new_strata_column(self, name):
        """Insert a new column (comment log) into a strata log.

        Parameters
        ----------
        name : str
            The name of the new column.

        Returns
        -------
        CommentLog
            The CommentLog corresponding to the newly created column.
        """
        return Log(self._dispatch.InsertNewStrataColumn(name))
