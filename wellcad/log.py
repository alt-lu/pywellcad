class Log:
    def __init__(self, log_dispatch):
        """
        Creates the log object.

        Use the insert_new_log, convert_log_to and add_log methods
        from the Borehole object to retrieve a log.
        """
        self.dispatch = log_dispatch

# log general

    def file_export(self, file_name, prompt_user=True, config="", logfile=""):
        """Exports the document to the specified file. Please refer to the WellCAD help file
        for a description of the export parameters to be used in the configuration file and
        parameter string.

        Parameters
        ----------
        file_name : str
            Path and name of the file to export.
        prompt_user : bool
            If set to False no dialog box will be displayed.
        config : str
            Path and name of the .ini file containing the export parameters.
        logfile : str
            Format of the saved file. LAS, DLIS, EMF, CGM, JPG, PNG, TIF, BMP, WCL and PDF are supported.
        """
        self.dispatch.FileExport(file_name, prompt_user, config, logfile)

    def nb_of_data(self):
        """Gets the number of data points in a log."""
        return self.dispatch.NbOfData

    """
    @property
    def name(self):
        return self.dispatch.Name

    @name.setter
    def name(self, text):
        Sets the title of a log.

        Parameters
        ----------
        text : str
            The new name of the log.
        
        self.dispatch.Name = name
        """

    def set_name(self, name):
        """Sets the title of a log.

        Parameters
        ----------
        text : str
            The new name of the log.
        """

        self.dispatch.Name = name

    def get_name(self):
        """Gets the title of a log.

        Parameters
        ----------
        text : str
            The new name of the log."""
        return self.dispatch.Name

    def set_title_comment(self, comment):
        """Sets the comment in a log title.

        Parameters
        ----------
        comment : str
            The new comment of the log title.
        """

        self.dispatch.TitleComment = comment

    def get_title_comment(self):
        """Gets the comment in a log title.

        Parameters
        ----------
        comment : str
            The new comment of the log title."""
        return self.dispatch.TitleComment

    """
    @property
    def title_comment(self):
        return self.dispatch.TitleComment

    @title_comment.setter
    def title_comment(self, comment):
        Sets the comment in a log title.

        Parameters
        ----------
        comment : str
            The new comment of the log title.
        
        self.dispatch.TitleComment = comment
    """

    def top_depth(self):
        """Gets the depth of the first data point in the log using the current depth reference units."""
        return self.dispatch.TopDepth

    def bottom_depth(self):
        """Gets the depth of the of the last (deepest) data point in the log using the current depth reference units."""
        return self.dispatch.BottomDepth

    def do_settings_dlg(self):  # Is it obsolete ? Should we keep it?
        """Opens the main settings dialog box corresponding to the log. Please note that
        since WellCAD v5.0 Properties Bars are used. The dialog boxes displayed with this
        method may not show all settings anymore."""
        return self.dispatch.DoSettingsDlg

    def get_data_table(self):
        """Gets the entire data table from/for a log. The first row in the
        data table is reserved for the log title (e.g. for a Well Log the fist row
        in the data table contains the column titles “Depth” and the actual log title).
        The data format for each log equals the data displayed in the Tabular Editor."""
        return self.dispatch.DataTable

    def set_data_table(self, data):
        """Sets the entire data table from/for a log. The first row in the
        data table is reserved for the log title (e.g. for a Well Log the fist row
        in the data table contains the column titles “Depth” and the actual log title).
        The data format for each log equals the data displayed in the Tabular Editor.

        Parameters
        ----------
        data : array
            ...
        """
        self.dispatch.DataTable = data

    def data_min(self):
        """Gets the minimum data value of the Well, Mud or Interval Log)."""
        return self.dispatch.DataMin

    def data_max(self):
        """Gets the maximum data value of the log (Well-, Mud-, Interval Log)."""
        return self.dispatch.DataMax

    def set_log_unit(self, unit):
        '''Sets the unit of a log. Restricted to log types having a unit in the log title.

        Parameters
        ----------
        unit : str
            The unit of the log.'''
        self.dispatch.LogUnit = unit

    def get_log_unit(self):
        '''Gets the unit of a log. Restricted to log types having a unit in the log title.

        Parameters
        ----------
        unit : str
            The unit of the log.'''
        return self.dispatch.LogUnit

    '''
    @property
    def log_unit(self):
        """Gets the unit of a log. Restricted to log types having a unit in the log title."""
        return self.dispatch.LogUnit

    @log_unit.setter
    def log_unit(self, unit):
        Sets the unit of a log. Restricted to log types having a unit in the log title.

        Parameters
        ----------
        unit : str
            The unit of the log.
        
        self.dispatch.LogUnit = unit
    '''

    '''
    @property
    def left_position(self):
        """Sets the left position of the log column in percent of the document width."""
        return self.dispatch.LeftPosition

    @left_position.setter
    def left_position(self, position):
        """Sets the left position of the log column in percent of the document width.
         
        Parameters
        ----------
        position : float
            Value between 0 and 1.
        """
        self.dispatch.LeftPosition = position
    '''

    def set_left_position(self, position):
        """Sets the left position of the log column in percent of the document width.

        Parameters
        ----------
        position : float
            Value between 0 and 1.
        """
        self.dispatch.LeftPosition = position

    def get_left_position(self):
        """Gets the left position of the log column in percent of the document width.

        Parameters
        ----------
        position : float
            Value between 0 and 1.
        """
        return self.dispatch.LeftPosition

    '''
    @property
    def right_position(self):
        """Sets the right position of the log column in percent of the document width."""
        return self.dispatch.RightPosition

    @right_position.setter
    def right_position(self, position):
        """Sets the right position of the log column in percent of the document width.

        Parameters
        ----------
        position : float
            Value between 0 and 1.
        """
        self.dispatch.RightPosition = position
    '''

    def set_right_position(self, position):
        """Sets the right position of the log column in percent of the document width.

        Parameters
        ----------
        position : float
            Value between 0 and 1.
        """
        self.dispatch.RightPosition = position

    def get_right_position(self):
        """Gets the right position of the log column in percent of the document width.

        Parameters
        ----------
        position : float
            Value between 0 and 1.
        """
        return self.dispatch.RightPosition

    def set_position(self, left, right):
        """Sets the left and right position of a log column in percentage of the document width.

        Parameters
        ----------
        left : float
            Value between 0 and 1.

        right : float
            Value between 0 and 1.
        """
        self.dispatch.SetPosition(left, right)

    def type(self):  # new lineation log should be added
        """Gets the log type index.

        Parameters
        ----------
        log_type : float
            Undefined = 0
            Well log = 1
            Formula log = 2
            Mud log = 3
            FWS log = 4
            Image log = 5
            Structure log = 6
            Litho log = 7
            Comment log = 8
            Engineering log = 9
            RGB log = 10
            Image Float 2 log = 11
            Image float 4 log = 12
            Interval log = 13
            Analysis log = 14
            Percentage log = 15
            Coredesc log = 16
            Depth log = 17
            Strata log = 18
            Stack log = 19
            Polar & Rose log = 20
            Cross log = 21
            OLE log = 22
            Shading log = 23
            Marker log = 24
            Breakout log = 25
            Bio log = 26
        """
        return self.dispatch.Type

    #@property # is this one necessary ? the setter option requires an argument. Not working with bool.
    #def hide_log_title(self):
    #    """Lets you know if the log title is hidden or not"""
    #    return self.dispatch.HideLogTitle

    def hide_log_title(self):
        """Hides the log title."""
        self.dispatch.HideLogTitle = True

    #@property # is this one necessary ? the setter option requires an argument. Not working with bool.
    #def hide_log_data(self):
     #   """Lets you know if the log data is hidden or not"""
     #   return self.dispatch.HideLogData

    def hide_log_data(self):
        """Hides the log data."""
        self.dispatch.HideLogData = True

    @property
    def log_background_color_int(self):
        """Gets the background color for a log column as an integer of the RGB color."""
        return self.dispatch.LogBackgroundColor

    @log_background_color_int.setter
    def log_background_color_int(self, value):
        """Sets the background color for a log column as an RGB integer value.

        Parameters
        ----------
        value : int
            RGB tuple value.
        """
        self.dispatch.LogBackgroundColor = value

    def log_background_color_rgb(self, r, g, b):
        """Sets the background color for a log column as an RGB tuple.

        Parameters
        ----------
        r : int
            Value between 0 and 255.
        g : int
            Value between 0 and 255.
        b : int
            Value between 0 and 255.
        """
        colorInt = r + (g*256) + (b*256*256)
        self.dispatch.LogBackgroundColor = colorInt

    #@property
    #def border_style(self):
    #    """Gets the background color for a log column as an RGB color value."""
    #    return self.dispatch.BorderStyle

    def get_border_style(self):
        """Gets the background color for a log column as an RGB color value."""
        return self.dispatch.BorderStyle

    def set_border_style(self, style):
        """Sets the border style of the log column.

        Parameters
        ----------
        style : int
            Solid = 0
            Dashed = 1
            Dotted = 2
            Dash-Dot = 3
            Dash-dot-dot = 4
        """
        self.dispatch.BorderStyle = style


    @property
    def border_color_int(self):
        """Gets the background color for a log column as an RGB color value."""
        return self.dispatch.BorderColor

    @border_color_int.setter
    def border_color_int(self, value):
        """Sets the color used for the log border as an RGB integer value.

        Parameters
        ----------
        value : int
            RGB tuple value.
        """
        self.dispatch.BorderColor = value

    def border_color_rgb(self, r, g, b):
        """Sets the background color for a log column as an RGB tuple.

        Parameters
        ----------
        r : int
            Value between 0 and 255.
        g : int
            Value between 0 and 255.
        b : int
            Value between 0 and 255.
        """
        colorInt = r + (g * 256) + (b * 256 * 256)
        self.dispatch.LogBackgroundColor = colorInt


    def display_border(self):
        """Displays the log border."""
        self.dispatch.DisplayBorder = True

    def clear_history(self):
        """Removes all entries from the log history."""
        self.dispatch.ClearHistory()

    def nb_of_history_item(self):
        """Gets the number of entries in the history (audit trail) of a log."""
        return self.dispatch.NbOfHistoryItem

    def history_item_date(self, index):
        """Gets the date of the history item at the specified index.

        Parameters
        ----------
        index : int
            Zero based index of the history entry.
        """
        return self.dispatch.HistoryItemDate(index)

    def history_item_description(self, index):
        """Gets the description of the history item at the specified index.

        Parameters
        ----------
        index : int
            Zero based index of the history entry."""
        return self.dispatch.HistoryItemDescription(index)

    '''
    @property
    def null_value(self):
        """Get the No Data value of a log."""
        return self.dispatch.NullValue

    @null_value.setter
    def null_value(self, value):
        """Sets the No Data value of a log.

        Parameters
        ----------
        value : float
            numerical value which will represent No Data
        """
        self.dispatch.NullValue = value
        
    '''

    def get_null_value(self):
        """Get the No Data value of a log."""
        return self.dispatch.NullValue

    def set_null_value(self, value):
        """Sets the No Data value of a log.

        Parameters
        ----------
        value : float
            numerical value which will represent No Data
        """
        self.dispatch.NullValue = value

    #@property # is this one necessary ? the setter option requires an argument. Not working with bool.
    #def mask_contacts(self):
    #    """Lets you know if the contact lines within the log column are masked or not."""
    #    return self.dispatch.MaskContacts

    #@mask_contacts.setter
    def mask_contacts(self):
        """Masks the contact lines (e.g. from formation tops) within the log column."""
        self.dispatch.MaskContacts = True

    #@property
    #def mask_horizontal_grid(self):
    #    """Lets you know if the horizontal (depth) grid of a log are masked or not."""
    #    return self.dispatch.MaskHorizontalGrid

    #@mask_horizontal_grid.setter
    def mask_horizontal_grid(self):
        """Masks the horizontal (depth) grid of a log."""
        self.dispatch.MaskHorizontalGrid = True

    '''
    @property
    def sample_rate(self):
        """Lets you know the sample interval of a log in current master depth units."""
        return self.dispatch.SampleRate

    @sample_rate.setter
    def sample_rate(self, rate):
        """Sets the sample interval of a log in current master depth units.

        Parameters
        ----------
        rate : float
            numerical value which represents sample rate
        """
        self.dispatch.SampleRate = rate
    '''

    def get_sample_rate(self):
        """Lets you know the sample interval of a log in current master depth units."""
        return self.dispatch.SampleRate

    def set_sample_rate(self, rate):
        """Sets the sample interval of a log in current master depth units.

        Parameters
        ----------
        rate : float
            numerical value which represents sample rate
        """
        self.dispatch.SampleRate = rate

    def scale_low(self, scale):
        """Sets the low scale value of the log.

        Parameters
        ----------
        scale : float
            number which will represent the scale lowest value
        """
        self.dispatch.ScaleLow = scale

    def scale_high(self, scale):
        """Sets the high scale value of the log.

        Parameters
        ----------
        scale : float
            number which will represent the scale highest value
        """
        self.dispatch.ScaleHigh = scale

    '''
    @property
    def scale_mode(self):
        """Gets the scale type for the data display of a Well or Mud Logs."""
        return self.dispatch.ScaleMode

    @scale_mode.setter
    def scale_mode(self, mode):
        """Sets the scale mode for the data display of a Well or Mud Logs.

        Parameters
        ----------
        mode : int
            linear = 0
            logarithmic = 1
        """
        self.dispatch.ScaleMode = mode
    '''

    def get_scale_mode(self):
        """Gets the scale type for the data display of a Well or Mud Logs."""
        return self.dispatch.ScaleMode

    def set_scale_mode(self, mode):
        """Sets the scale mode for the data display of a Well or Mud Logs.

        Parameters
        ----------
        mode : int
            linear = 0
            logarithmic = 1
        """
        self.dispatch.ScaleMode = mode

    #@property
    #def scale_reversed(self):
    #    """Lets you know if the flag is set to reverse the data display scale or not."""
    #    return self.dispatch.ScaleReversed

    #scale_reversed.setter

    def scale_reversed(self):
        """Sets the flag to reverse the data display scale of Well or Mud Logs."""
        self.dispatch.ScaleReversed = True

    #@property
    #def use_log_colored_background(self):
    #    """Lets you know if the background color of a log is displayed or not."""
    #    return self.dispatch.UseLogColoredBackground

    #@use_log_colored_backgroung.setter
    def use_log_colored_background(self):
        """Sets the information whether the background color of a log is displayed or not."""
        self.dispatch.UseLogColoredBackground = True

    #@property
    #def grid_enable(self):
    #    """Lets you know if the flag to display the vertical grid is enabled or not."""
    #    return self.dispatch.GridEnable

    #@grid_enable.setter
    def grid_enable(self):
        """Sets the flag to display the vertical grid in Well or Mud Logs."""
        self.dispatch.GridEnable = True

    def maj_grid_spacing(self, spacing):
        """Sets the vertical (major) grid for Well or Mud Logs.

        Parameters
        ----------
        spacing : float
            value of the spacing between each grid
        """
        self.dispatch.MajGridSpacing = spacing

    def min_grid_spacing(self, spacing):
        """Sets the vertical (minor) grid for Well or Mud Logs.

        Parameters
        ----------
        spacing : float
            value of the spacing between each grid
        """
        self.dispatch.MinGridSpacing = spacing

    #@property
    #def lock_log_data(self):
    #    """Lets you know if the option to lock log data and protect it from editing is enable or not."""
    #    return self.dispatch.LockLogData

    #@lock_log_data.setter
    def lock_log_data(self):
        """Sets the option to lock log data and protect it from editing."""
        self.dispatch.LockLogData = True


# Well, Formula, Mud and Interval logs

    def data(self, index):
        """Gets the data value at the specified index from a Well, Mud, Interval or Depth Log.

        Parameters
        ----------
        index : int
            Zero based index of the data point to be retrieved.
        """
        return self.dispatch.Data(index)

    def data_at_depth(self, depth):
        """Gets the data value at the specified depth from a Well, Mud, Interval or Depth Log.

        Parameters
        ----------
        depth : float
            Depth value at current units at which the data value will be returned
        """
        return self.dispatch.DataAtDepth(depth)

    def data_depth(self, index):
        """Gets the depth at the specified index of the data point. Valid for Mud, Well, Depth,
        Percent, Analysis, FWS, Image and RGB Logs. For logs requiring a constant sample step
        (Well, Image, RGB, Analysis Logs) the index 0 corresponds to the Bottom Depth.

        Parameters
        ----------
        index : int
            Zero based index of the depth point to be retrieved.
        """
        return self.dispatch.DataDepth(index)

    def insert_data(self, index, value):
        """Inserts a new data value at the specified index of a Well Log.

        Parameters
        ----------
        index : int
            Zero based index at which the new data point will be inserted.
            If necessary existing data points will be shifted.
            The index must be lower or equal to the number of data points in the log.
        value : float
            new data value
        """
        self.dispatch.InsertData(index, value)

    def insert_data_at_depth(self, depth, value):
        """Inserts a new data value at the specified depth of a Well Log.

        Parameters
        ----------
        depth : float
            Depth in current units at which the new data point should be inserted.
            If necessary existing data points will be shifted.
            The function fails if the added depth does not respect the constant sample rate of the Well Log.
        value : float
            new data value
        """
        self.dispatch.InsertDataAtDepth(depth, value)

    '''
    @property
    def formula(self):
        """Lets you know the formula used in a Formula log."""
        return self.dispatch.Formula

    @formula.setter
    def formula(self, formula):
        """Sets the formula to be used in a Formula Log.
        The formula should not include the equal sign.

        Parameters
        ----------
        formula : str
            equation using standard math symbols
        """
        self.dispatch.Formula(formula)
    '''

    def get_formula(self):
        """Lets you know the formula used in a Formula log."""
        return self.dispatch.Formula

    def set_formula(self, formula):
        """Sets the formula to be used in a Formula Log.
        The formula should not include the equal sign.

        Parameters
        ----------
        formula : str
            equation using standard math symbols
        """
        self.dispatch.Formula(formula)

    '''
    @property
    def filter(self):
        """Lets you know the width (in samples) of the display filter used for Well Logs."""
        return self.dispatch.Filter

    @filter.setter
    def filter(self, width):
        """Sets the width (in samples) of the display filter used for Well Logs.

        Parameters
        ----------
        width : int
            number of samples which corresponds to the filter width
        """
        self.dispatch.Filter = width
    '''

    def get_filter(self):
        """Lets you know the width (in samples) of the display filter used for Well Logs."""
        return self.dispatch.Filter

    def set_filter(self, width):
        """Sets the width (in samples) of the display filter used for Well Logs.

        Parameters
        ----------
        width : int
            number of samples which corresponds to the filter width
        """
        self.dispatch.Filter = width

    '''   
    @property
    def fixed_bar_width(self):
        """Lets you know the fixed bar width in 1/10 mm for Mud Logs."""
        return self.dispatch.FixedBarWidth

    @fixed_bar_width.setter
    def fixed_bar_width(self, width):
        """Sets the fixed bar width in 1/10 mm for Mud Logs.

        Parameters
        ----------
        width : int
            number of millimeters
        """
        self.dispatch.FixedBarWidth = width
        
    '''

    def get_fixed_bar_width(self):
        """Lets you know the fixed bar width in 1/10 mm for Mud Logs."""
        return self.dispatch.FixedBarWidth

    def set_fixed_bar_width(self, width):
        """Sets the fixed bar width in 1/10 mm for Mud Logs.

        Parameters
        ----------
        width : int
            number of millimeters
        """
        self.dispatch.FixedBarWidth = width

    def insert_new_interval_item (self, top_depth, bottom_depth, value):
        """Inserts a new interval in an interval log.

        Parameters
        ----------
        top_depth : float
            top depth of the new interval in current depth units
        bottom_depth : float
            bottom depth of the new interval in current depth units
        value : float
            the new data value
        """
        self.dispatch.InsertNewIntervalItem(top_depth, bottom_depth, value)

    def interval_item(self, index):
        """Gets an interval item object from an Interval Log at the specified index.

        Parameters
        ----------
        index : int
            zero based index at which to retrieve the interval item.
        """
        return self.dispatch.IntervalItem(index)

    def interval_item_at_depth(self, depth):
        """Gets an interval item object from an Interval Log at the specified depth in current
        depth units.

        Parameters
        ----------
        depth : float
            depth value at which to retrieve the interval item.
        """
        return self.dispatch.IntervalItemAtDepth(depth)

    def pen_color(self, r, g, b): # RGB as a hole, maybe have to use a python method to convert R,G and B as one number
        """Sets the pen color used in a Well or Mud Log as RGB color value.

        Parameters
        ----------
        r : int
            Value between 0 and 255.
        g : int
            Value between 0 and 255.
        b : int
            Value between 0 and 255.
        """
        colorInt = r + (g * 256) + (b * 256 * 256)
        self.dispatch.BackgroundColor = colorInt

    @property
    def pen_style(self):
        """Lets you know the pen style used in a Well or Mud Log."""
        return self.dispatch.PenStyle

    @pen_style.setter
    def pen_style(self, style):
        """Sets the pen style used in a Well or Mud Log.

        Parameters
        ----------
        style : int
            Solid = 0
            Dashed = 1
            Dotted = 2
            Dash-Dot = 3
            Dash-dot-dot = 4
        """
        self.dispatch.PenStyle = style

    @property
    def pen_width(self):
        """Lets you know the pen width used in a Well or Mud Log in 1/10 mm."""
        return self.dispatch.PenWidth

    @pen_width.setter
    def pen_width(self, width):
        """Sets the pen width used in a Well or Mud Log in 1/10 mm.

        Parameters
        ----------
        width : int
            number of millimeters
        """
        self.dispatch.PenWidth = width

    def remove_data(self, index):
        """Removes the data point at the specified index from a Mud or Well Log.
         For Well Logs the data value will be set to NULL.

        Parameters
        ----------
        index : int
            zero based index at which the data point will be removed
        """
        self.dispatch.RemoveData(index)

    def remove_data_at_depth(self, depth):
        """Removes the data point at the specified depth from a Mud or Well Log.
         For Well Logs the data value will be set to NULL.

        Parameters
        ----------
        depth : float
            depth value in current units at which the data point will be removed
        """
        self.dispatch.RemoveDataAtDepth(depth)

    def remove_interval_item(self, index):
        """Removes a data interval from an Interval Log at the specified index.

        Parameters
        ----------
        index : int
            zero based index at which the data interval that will be removed
        """
        self.dispatch.RemoveIntervalItem(index)

    def remove_interval_item_at_depth(self, depth):
        """Removes a data interval from an Interval Log at the specified depth.

        Parameters
        ----------
        depth : float
            depth value in current units at which the data point will be removed
        """
        self.dispatch.RemoveIntervalItemAtDepth(depth)

    @property
    def shading(self):
        """Lets you know the shading position used in a Well or Mud Log (0 = none, 1 = left, 2 = right)."""
        return self.dispatch.Shading

    @shading.setter
    def shading(self, position):
        """Sets the the shading position used in a Well or Mud Log.

        Parameters
        ----------
        position : int
            None = 0
            Left = 1
            Right = 2
        """
        self.dispatch.Shading = position

    @property
    def style(self):
        """Lets you know the for Mud Logs (1 = fixed bar, 2 = dynamic bar, 3 = line)
        and Engineering Logs (0 = full, 1 = left, 2 = right)."""
        return self.dispatch.Style

    @style.setter
    def style(self, style_number):
        """Sets the data display style for Mud Logs and Engineering Logs.

        Parameters
        ----------
        style_number : int

            Mud Logs :
            fixed bar = 1
            dynamic bar = 2
            line = 3

            Engineering Log :
            full = 0
            left = 1 = left,
            right = 2
        """

        self.dispatch.Style = style_number


# litho, Coredesc, and percentage logs

    def attach_litho_dictionary(self, dictionary):
        """Attaches a new symbol or pattern library (\*.LTH file) to Litho, CoreDesc,
        Strata, Analysis or Percentage Log.

        Parameters
        ----------
        dictionary : str
            path and name of the LTH file to attach
        """
        self.dispatch.AttachLithoDictionary(dictionary)


    def component_name(self, column, code):
        """Sets the color used for the log border as an RGB color value.

        Parameters
        ----------
        column : int
            Zero based index of the data column in the tabular editor for
            which the component name should be set or retrieved.
        code : str
            Code of the component to be used as specified in the litho library of the log.
        """
        self.dispatch.ComponentName(column, code)

    def fossil_item(self, index):
        """Gets a Fossil Item object from the CoreDesc Log at the specified index.

        Parameters
        ----------
        index : int
            Zero based index of the item to be retrieved.
        """
        return self.dispatch.FossilItem(index)

    def fossil_item_at_depth(self, depth):
        """Gets a fossil item object from the CoreDesc Log at the specified depth.

        Parameters
        ----------
        depth : float
            depth value in current depth units at which the item will be retrieved
        """
        return self.dispatch.FossilItemAtDepth(depth)

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
        """
        self.dispatch.InsertNewFossilItem(top_depth, bottom_depth, litho_code, abundance, dominance, position)

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
            A value between 0 and 1 determining the horizontal position Position of a non repeated symbol
            in percent of the track width.
        """
        self.dispatch.InsertNewLithoBed(top_depth, bottom_depth, litho_code, value, position)

    def litho_bed(self, index):
        """Gets a LithoBed object at the specified index from a Lithology Log.

        Parameters
        ----------
        index : int
            Zero based index of the LithoBed to be retrieved.
        """
        return self.dispatch.LithoBed(index)

    def litho_bed_at_depth(self, depth):
        """Gets a LithoBed object at the specified depth from a Lithology Log.

        Parameters
        ----------
        depth : float
            depth value in current depth units at which the item will be retrieved
        """
        return self.dispatch.LithoBedAtDepth(depth)

    @property
    def litho_dictionary(self):
        """Gets the symbol library used by the log as LithoDictionary object."""
        return self.dispatch.LithoDictionary

    @litho_dictionary.setter
    def litho_dictionary(self, dictionary):
        """Sets the symbol library used by the log as LithoDictionary object.

        Parameters
        ----------
        dictionary : str
            path and name of the LTH file to attach
        """
        self.dispatch.LithoDictionary(dictionary)

    def remove_fossil_item(self, index):
        """Removes an item at the specified index from a CoreDesc Log.

        Parameters
        ----------
        index : int
            Zero based index of the fossil item to be removed.
        """
        self.dispatch.RemoveFossilItem(index)

    def remove_fossil_item_at_depth(self, depth):
        """Removes an item at the specified index from a CoreDesc Log.

        Parameters
        ----------
        depth : float
            the depth value of the symbol in current depth units at which it will be removed.
        """
        self.dispatch.RemoveFossilItemAtDepth(depth)

    def remove_litho_bed(self, index):
        """Removes a lithology bed from the Lithology log at the specified index.

        Parameters
        ----------
        index : int
            Zero based index of the lithology bed item to be removed.
        """
        self.dispatch.RemoveLithoBed(index)

    def remove_litho_bed_at_depth(self, depth):
        """Removes a lithology bed from the Lithology log at the specified depth.

        Parameters
        ----------
        depth : float
            the depth value in current depth units at which the lithological bed will be removed.
        """
        self.dispatch.RemoveLithoBedAtDepth(depth)

# Image and FWS logs

    def insert_trace(self, index):
        """Inserts a new data trace into an Image, FWS or Analysis Log at the specified index.

        Parameters
        ----------
        index : int
            Zero based index at which the trace should be added.
            Must be lower or equal the number of data traces within the log.
            If necessary, existing traces will be shifted.
        """
        self.dispatch.InsertTrace(index)

    def insert_trace_at_depth(self, depth):
        """Inserts a new data trace into an Image, FWS or Analysis Log at the specified depth.

        Parameters
        ----------
        depth : float
            The depth value in current depth units at which the new data trace will be inserted.
            If necessary existing traces will be shifted.
            The function fails if the specified depth lies without the constant sample rate of the log
            (use InsertTrace instead).
        """
        self.dispatch.InsertTraceAtDepth(depth)

    def remove_trace(self, index):
        """Remove an entire data trace from an Image, FWS, Analysis or Percentage Log.
        Removing a trace from a log means setting all trace values to NULL.

        Parameters
        ----------
        index : int
            Zero based index of the trace to be set to NULL.
        """
        self.dispatch.RemoveTrace(index)

    def remove_trace_at_depth(self, depth):
        """Remove an entire data trace from an Image, FWS, Analysis or Percentage Log.
        Removing a trace from a log means setting all trace values to NULL.

        Parameters
        ----------
        depth : float
            The depth value in current depth units at which the trace will be set to NULL.
        """
        self.dispatch.InsertTraceAtDepth(depth)

    def trace_data(self, depth_index, trace_index):
        """set the data value at the specified row index and position within the trace
         (column index) of an Analysis, Percentage, FWS, Image or RGB Log.

        Parameters
        ----------
        depth_index : int
            zero based index of the depth (0 = bottom depth).
        trace_index : int
            zero based index of the column.
        """
        self.dispatch.TraceData(depth_index, trace_index)

    @property
    def trace_data_at_depth(self):
        """Gets the data value at the specified depth and position within the trace of an Analysis,
        Percentage, FWS, Image or RGB Log."""
        return self.dispatch.TraceDataAtDepth

    @trace_data_at_depth.setter
    def trace_data_at_depth(self, depth, trace_position):
        """set the data value at the specified depth and position within
         the trace of an Analysis, Percentage, FWS, Image or RGB Log

        Parameters
        ----------
        depth : float
            The depth value at which you would like to retrieve the data value in the current depth units.
        trace_position : float
            The position within the trace (time or angle as shown in the column header of the tabular editor,
            not the index) at which you would like to retrieve the data value.
        """
        self.dispatch.TraceDataAtDepth(depth, trace_position)

    @property
    def trace_length(self):
        """Gets the length of a data trace in Image, RGB and FWS Logs."""
        return self.dispatch.TraceLength

    @trace_length.setter
    def trace_length(self, length):
        """Sets  the length of a data trace in Image, RGB and FWS Logs.

        Parameters
        ----------
        length : str
            numerical value corresponding to the length of the trace
        """
        self.dispatch.TraceLength(length)

    @property
    def trace_offset(self):
        """Gets the offset of a data trace in the FWS Log."""
        return self.dispatch.TraceOffset

    @trace_offset.setter
    def trace_offset(self, offset):
        """Sets the offset of a data trace in the FWS Log.

        Parameters
        ----------
        offset : float
            numerical value representing the offset
        """
        self.dispatch.TraceOffset(offset)

    @property
    def trace_sample_rate(self):
        """Gets the trace sample interval in Image, RGB and FWS Logs."""
        return self.dispatch.TraceSampleRate

    @trace_sample_rate.setter
    def trace_sample_rate(self, rate):
        """Sets the trace sample interval in Image, RGB and FWS Logs.

        Parameters
        ----------
        rate : float
            numerical value representing the sample rate or interval
        """
        self.dispatch.TraceSampleRate(rate)

    @property
    def column_name(self):
        """Gets the name of a Strata Log column."""
        return self.dispatch.ColumnName

    @column_name.setter
    def column_name(self, column, name):
        """Sets set the name of a Strata Log column.

        Parameters
        ----------
        column : int
            Zero based index of the column to be retrieved
        name : str
            New name of the column.
        """
        self.dispatch.ColumnName(column, name)

    def comment_box(self, index):
        """Gets the Comment Box object from the Comment Log at the specified index.

        Parameters
        ----------
        index : int
            Zero based index at which the box will be retrieved.
        """
        return self.dispatch.CommentBox(index)

    def comment_box_at_depth(self, depth):
        """Gets the Comment Box object from the Comment Log at the specified depth.

        Parameters
        ----------
        depth : float
            The depth value in current depth units at which the comment box will be retrieved.
        """
        return self.dispatch.CommentBoxAtDepth(depth)

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
        """
        self.dispatch.InsertNewCommentBox(top_depth, bottom_depth, text)

    def marker(self, index):
        """Gets the marker object of the specified index from the Marker Log.

        Parameters
        ----------
        index : int
            Zero based index at which the marker object will be retrieved.
        """
        return self.dispatch.Marker(index)

    def marker_by_name(self, name):
        """Gets the marker object of the specified name from the Marker Log.

        Parameters
        ----------
        name : str
            Text of the marker object to be retrieved.
        """
        return self.dispatch.MarkerByName(name)

    def insert_new_marker(self, depth, name, comment, contact):
        """Sets a new marker at the specified depth into a Marker Log

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
        """
        self.dispatch.InsertNewMarker(depth,name, comment, contact)

    def removes_comment_box(self, index):
        """Removes a comment box from the Comment log at the specified index.

        Parameters
        ----------
        index : int
            Zero based index at which the comment box will be removed.
        """
        self.dispatch.RemoveCommentBox(index)

    def removes_comment_box_at_depth(self, depth):
        """Removes a comment box from the Comment log at the specified depth.

        Parameters
        ----------
        depth : float
            The depth value in current depth units at which the comment box will be removed.
        """
        self.dispatch.RemoveCommentBoxAtDepth(depth)

    def remove_marker(self, index):
        """Removes the marker from a Marker Log at the specified index.

        Parameters
        ----------
        index : int
            Zero based index at which the marker box will be removed.
        """
        self.dispatch.RemoveMarker(index)

    def strata_column(self, index):
        """Gets a column from a Strata Log as Comment Log object.

        Parameters
        ----------
        index : int
            Zero based index  of the column to be returned.
        """
        return self.dispatch.StrataColumn(index)

    def remove_strata_column(self, index):
        """Removes the the specified column from a Strata Log at the specified index.

        Parameters
        ----------
        index : int
            Zero based index of the column to be removed.
        """
        self.dispatch.RemoveStrataColumn(index)

    @property
    def font(self):
        """Gets the font used in a Comment Log as Font Object."""
        return self.dispatch.Font

    @font.setter
    def font(self, name):
        """Sets the font used in a Comment Log as Font Object.

        Parameters
        ----------
        name : str
            name of the font to be used.
        """
        self.dispatch.Font(name)

#Structure and Borehole

    def attach_attribute_dictionary(self, attribute, file):
        """Attaches a new attribute library (\*.TAD file) to a Structure / Breakout Log.

        Parameters
        ----------
        attribute : str
            Name of the classification column (see column_name).
        file : str
            Path and name of the TAD file to attach.
        """
        self.dispatch.AttachAttributeDictionary(attribute, file)


    def attribute_name(self):
        """Gets the name of the attribute class (i.e. classification column) in a Breakout Log or a Structure Log."""
        return self.dispatch.AttributeName

    def set_attribute_name(self, index, name):
        """Sets the name of the attribute class (i.e. classification column) in a Breakout Log or a Structure Log.

        Parameters
        ----------
        index : str
            Zero based index of the column.
        name : str
            New name of the classification column.
        """
        self.dispatch.AttributeName(index, name)

    def structure(self, index):
        """Gets a Structure object from the Structure Log at the specified depth index.

        Parameters
        ----------
        index : int
            Zero based index  of the structure object to be retrieved.
        """
        return self.dispatch.Structure(index)

    def structure_at_depth(self, depth):
        """Gets a Structure object from the Structure Log at the specified depth in current depth units.

        Parameters
        ----------
        depth : float
            The depth value in current depth units at which the structure object will be retrieved.
            Feature closest to specified depth will be returned.
        """
        self.dispatch.StructureAtDepth(depth)

    def breakout(self, index):
        """Gets a breakout from the Breakout Log at the specified depth index.

        Parameters
        ----------
        index : int
            Zero based index  of the breakout to be retrieved.
        """
        return self.dispatch.Breakout(index)

    def breakout_at_depth(self, depth):
        """Gets a breakout from the Breakout Log at the specified depth in current depth units.

        Parameters
        ----------
        depth : float
            The depth value in current depth units at which the breakout will be retrieved.
        """
        return self.dispatch.BreakoutAtDepth(depth)

    def insert_new_breakout_ex(self, depth, azimuth, tilt, length, opening):
        """Sets a new breakout in a Breakout Log.

        Parameters
        ----------
        depth : float
            The depth value in the current units of the breakout to be inserted.
        azimuth : float
            The azimuth angle of the breakout measured in degrees.
        tilt : float
            The tilt angle of the breakout measured in degrees.
        length : float
            The length of the breakout in meters.
        opening : float
            The opening angle of the breakout in degrees.
        """
        self.dispatch.InsertNewBreakoutEx(depth, azimuth, tilt, length, opening)

    def insert_new_structure_ex(self, depth, azimuth, dip, aperture):
        """Sets a new structure in a Structure Log.

        Parameters
        ----------
        depth : float
            The depth value in the current units of the breakout to be inserted.
        azimuth : float
            The azimuth angle of the structure measured in degrees.
        dip : float
            The tilt angle of the structure measured in degrees.
        aperture : float
            The aperture of the structure in meters.
        """
        self.dispatch.InsertNewStructureEx(depth, azimuth, dip, aperture)

    def remove_breakout(self, index):
        """Removes a breakout from the Breakout Log at the specified index.

        Parameters
        ----------
        index : int
            Zero based index  of the breakout to be removed.
        """
        self.dispatch.RemoveBreakout(index)

    def remove_breakout_at_depth(self, depth):
        """Removes a breakout from the Breakout Log at the specified depth in current depth units.

        Parameters
        ----------
        depth : float
            The depth value in current depth units at which the breakout will be removed.
        """
        self.dispatch.RemoveBreakoutAtDepth(depth)

    def remove_structure(self, index):
        """Removes a structure from the Structure Log at the specified index.

        Parameters
        ----------
        index : int
            Zero based index  of the structure to be removed.
        """
        self.dispatch.RemoveStructure(index)

    def remove_structure_at_depth(self, depth):
        """Removes a structure from the Structure Log at the specified depth in current depth units.

        Parameters
        ----------
        depth : float
            The depth value in current depth units at which the structure will be removed.
        """
        self.dispatch.RemoveStructureAtDepth(depth)

    @property
    def length_unit(self):
        """Gets the unit of the breakout length measured in the breakout log
        (0.001 when measured in mm and 0.0254 when measured in inches) """
        return self.dispatch.LengthUnit

    @length_unit.setter
    def length_unit(self, code):
        """Sets the unit of the breakout length measured in the breakout log.

        Parameters
        ----------
        code : float
            0.001 when measured in mm or 0.0254 when measured in inches.
        """
        self.dispatch.LengthUnit(code)

    @property
    def caliper_unit(self):
        """Gets the unit of the caliper used in the structure log.
        (0.001 when measured in mm and 0.0254 when measured in inches) """
        return self.dispatch.CaliperUnit

    @caliper_unit.setter
    def caliper_unit(self, code):
        """Sets the unit of the caliper used in the structure log.

        Parameters
        ----------
        code : float
            0.001 when measured in mm or 0.0254 when measured in inches.
        """
        self.dispatch.CaliperUnit(code)

    @property
    def aperture_unit(self):
        """Gets the aperture value in a structure log.
        (0.001 when measured in mm and 0.0254 when measured in inches) """
        return self.dispatch.ApertureUnit

    @aperture_unit.setter
    def aperture_unit(self, code):
        """Sets the aperture value in a structure log.

        Parameters
        ----------
        code : float
            0.001 when measured in mm or 0.0254 when measured in inches.
        """
        self.dispatch.ApertureUnit(code)

#Polar & Rose Logs

    def insert_new_schmit_box(self, topdepth, bottomdepth, text):
        """Inserts a new box into a Polar & Rose Log.

        Parameters
        ----------
        topdepth : float
            The top depth value of the interval in the current depth units.
        bottomdepth : float
            The bottom depth value of the interval in the current depth units.
        text : string
            A text description which is only shown in the tabular editor display.
        """
        self.dispatch.InsertNewSchmitBox(topdepth, bottomdepth, text)

    def schmit_box(self, index):
        """Gets a Schmidt Box object from the Polar & Rose Log at the specified index.

        Parameters
        ----------
        index : int
            Zero based index  of the box to be returned.
        """
        return self.dispatch.SchmitBox(index)

    def schmit_box_at_depth(self, depth):
        """Gets a Schmit Box object from the Polar & Rose Log at the specified depth in current depth units.

        Parameters
        ----------
        depth : float
            The depth of the box to be returned in current depth units.
        """
        self.dispatch.SchmitBoxAtDepth(depth)

    def remove_schmidt_box(self, index):
        """Removes a Schmit Box object from the Polar & Rose Log at the index.

        Parameters
        ----------
        index : int
            Zero based index  of the box to be removed.
        """
        self.dispatch.RemoveSchmitBox(index)

    def remove_schmit_box_at_depth(self, depth):
        """Removes a box from the Polar & Rose log at the specified depth in current depth units.

        Parameters
        ----------
        depth : float
            The depth of the box to be removed in current depth units.
        """
        self.dispatch.RemoveSchmitBoxAtDepth(depth)

#Cross Section Log

    def cross_box(self, index): # the example in the Automation module is wrong
        """Gets a Cross Box object from the Cross Section Log at the specified index.

        Parameters
        ----------
        index : int
            Zero based index of the box to be retrieve.
        """
        return self.CrossBox(index)

    def cross_box_at_depth(self, depth):
        """Gets a Cross Box object from the Cross Section Log at the specified depth in current depth units.

        Parameters
        ----------
        depth : float
            The depth of the box to be retrieved in current depth units.
        """
        return self.dispatch.CrossBoxAtDepth(depth)

    def insert_new_cross_box(self, topdepth, bottomdepth):
        """Inserts a new box into the Cross Section Log.

        Parameters
        ----------
        topdepth : float
            The top depth value of the cross section box in current depth units.
        bottomdepth : float
            The bottom depth value of the cross section box in current depth units.
        """
        self.dispatch.InsertNewCrossBox(topdepth, bottomdepth)

    def remove_cross_box(self, index):
        """Removes a box from the Cross Section Log at the specified index.

        Parameters
        ----------
        index : int
            Zero based index of the box to be removed.
        """
        self.dispatch.RemoveCrossBox(index)

    def remove_cross_box_at_depth(self, depth):
        """Removes a box from the Cross Section Log at the specified depth.

        Parameters
        ----------
        depth : float
            The depth in current units at which the box will be removed.
        """
        self.dispatch.RemoveCrossBoxAtDepth(depth)

#Stacking Pattern Log

    def insert_new_stack_item(self, topdepth, bottomdepth, topwidth, bottomwidth):
        """Inserts a new data interval into a Stacking Pattern Log.

        Parameters
        ----------
        topdepth : float
            The top depth value of the interval in the current depth units.
        bottomdepth : float
            The bottom depth value of the interval in the current depth units.
        topwidth : float
           Width value at the top of the new interval.
        bottomwidth : float
            Width value at the bottom of the new interval.
        """
        self.dispatch.InsertNewStackItem(topdepth, bottomdepth, topwidth, bottomwidth)

    def stack_item(self, index):
        """Gets a Stack Item object from the Stacking Pattern Log at the specified depth index.

        Parameters
        ----------
        index : int
            Zero based index of the item to be retrieve.
        """
        return self.dispatch.StackItem(index)

    def stack_item_at_depth(self, depth):
        """Gets a Stack Item object from the Stacking Pattern Log at the specified depth in current depth units.

        Parameters
        ----------
        depth : float
            The depth of the item to be retrieved in current depth units.
        """
        return self.dispatch.StackItemAtDepth(depth)

    def remove_stack_item(self, index):
        """Removes an item from the Stacking Pattern Log at the specified index.

        Parameters
        ----------
        index : int
            Zero based index  of the stacking pattern box to be removed.
        """
        self.dispatch.RemoveStackItem(index)

    def remove_stack_item_at_depth(self, depth):
        """Removes an item from the Stacking Pattern Log at the specified depth.

        Parameters
        ----------
        depth : float
            The depth of the stack item to be removed in current depth units.
        """
        self.dispatch.RemoveStackItemAtDepth(depth)

# depth log

    def used_as_depth_scale (self):
        """Sets the Depth Log as current depth reference axis."""

        self.dispatch.UsedAsDepthScale = True

#OLE log

    def insert_new_ole_box_from_file(self, file_name, allowpicture, topdepth, bottomdepth):
        """Inserts a new interval into an OLE Log.

        Parameters
        ----------
        file_name : str
            Path and name of the file to export.
        allowpicture : bool
            Set to True to allow graphic files to be displayed using an internal viewer.
        topdepth : float
            Top depth of the interval in current depth units.
        bottomdepth : float
            Bottom depth of the interval in current depth units.
        """
        self.dispatch.InsertNewOleBoxFromFile(file_name, allowpicture, topdepth, bottomdepth)

# Engineering Log

    def drill_item(self, index):
        """Gets a Drill Item object from the Engineering Log at the specified index.

        Parameters
        ----------
        index : int
            Zero based index at which the drill item will be retrieved.
        """
        return self.dispatch.DrillItem(index)

    def drill_item_at_depth(self, depth):
        """Gets a Drill Item object from the Engineering Log at the specified depth.

        Parameters
        ----------
        depth : float
            The depth of the item to be retrieved in current depth units.
        """
        return self.dispatch.DrillItemAtDepth(depth)

    def eqp_item(self, index):
        """Gets an Equipment Item object at the specified index from the Engineering Log.

        Parameters
        ----------
        index : int
            Zero based index at which the item will be retrieved.
        """
        return self.dispatch.EqpItem(index)

    def ground_depth(self, depth):
        """Sets the starting point (reference datum) of the borehole.

        Parameters
        ----------
        depth : float
            The depth value in current unit corresponding to the starting point of the borehole.
        """
        self.dispatch.GroundDepth(depth)

    @property
    def diameter_high(self):
        """Gets the maximum diameter scaling value (width of the log column) for an Engineering Log. """
        return self.dispatch.DiameterHigh

    @diameter_high.setter
    def diameter_high(self, diameter):
        """Sets the maximum diameter scaling value (width of the log column) for an Engineering Log.

        Parameters
        ----------
        diameter : float
            Width value of the log column.
        """
        self.dispatch.DiameterHigh(diameter)

    def insert_new_drill_item(self, depth, diameter):
        """Inserts a new drill item into the Engineering Log.

        Parameters
        ----------
        bottom depth : float
            The bottom depth of the borehole in current depth units.
            (The top depth is either the ground_depth or the former bottom depth).
        """
        self.dispatch.InsertNewDrillItem(depth, diameter)

    def insert_new_eqp_item(self, topdepth, bottomdepth, name):
        """Inserts a new equipment item of the specified name and depth interval into the Engineering Log.

        Parameters
        ----------
        topdepth : float
            The top depth of the equipment item interval in current units.
        bottomdepth : float
            The bottom depth of the equipment item interval in current units.
        name : str
            The name (code) of the equipment item to be inserted.
            Possible item are :
            -PlainCasing
            -WireWoundCasing
            -SlottedCasing
            -PerforatedCasing
            -Centralizer
            -Shoe
            -Packer
            -Water
            -Wedge
            -HeadWorks
            -Transducer
            -Gauge
            -Cement
            -Gravel
            -NormalThread
            -ReverseThread
            -Plug

        """
        self.dispatch.InsertNewEqpItem(topdepth, bottomdepth, name)

    def nb_of_drill_item(self):
        """Gets the number of drill items in an Engineering Log."""
        return self.dispatch.NbOfDrillItem

    def nb_of_eqp_item(self):
        """Gets the number of equipment items in an Engineering Log."""
        return self.dispatch.NbOfEqpItem

    def remove_drill_item(self, index):
        """Removes the drill item at the specified index from an Engineering Log.

        Parameters
        ----------
        index : int
            Zero based index at which the item will be removed.
        """
        self.dispatch.RemoveDrillItem(index)

    def remove_eqp_item(self, index):
        """Removes an equipment item at the specified depth index from an Engineering Log.

        Parameters
        ----------
        index : int
            Zero based index at which the item will be removed.
        """
        self.dispatch.RemoveEqpItem(index)

    @property
    def background_color_int(self):
        """Gets the color used in the background of the Engineering Log as an integer of the RGB color."""
        return self.dispatch.BackgroundColor

    @background_color_int.setter
    def background_color_int(self, value):
        """Sets the color used in the background of the Engineering Log as an RGB integer value.

        Parameters
        ----------
        value : int
            RGB tuple value.
        """
        self.dispatch.BackgroundColor = value

    def background_color_rgb(self, r, g, b):
        """Sets the Engineering Log background color as an RGB tuple.

        Parameters
        ----------
        r : int
            Value between 0 and 255.
        g : int
            Value between 0 and 255.
        b : int
            Value between 0 and 255.
        """
        colorInt = r + (g * 256) + (b * 256 * 256)
        self.dispatch.BackgroundColor = colorInt

    @property
    def background_hatch_style(self):
        """Gets the background hatch style for the Engineering Log  """
        return self.dispatch.BackgroundHatchStyle

    @background_hatch_style.setter # code number 4 is missing
    def background_hatch_style(self, code):
        """Sets the background hatch style for the Engineering Log.

        Parameters
        ----------
        code : int
            horizontal = 0
            vertical = 1
            forward diagonal = 2
            backward diagonal = 3
            cross = 5
            diagonal cross = 6
        """
        self.dispatch.BackgroundHatchStyle = code

    @property
    def background_style(self):
        """Gets the background style for the Engineering Log."""
        return self.dispatch.BackgroundStyle

    @background_style.setter
    def background_style(self, code):
        """Sets the background style for the Engineering Log.

        Parameters
        ----------
        code : int
            none = 0
            solid = 1
            hatch = 2
        """
        self.dispatch.BackgroundStyle = code


#Protection


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
        self.dispatch.AllowExportAttributeDictionary(index, export, password)

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
        self.dispatch.AllowExportLithoDictionary(export, password)

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
        self.dispatch.AllowModifyLogData(export, password)

    def allow_modify_log_data(self, export, password):
        """When dealing with a protected document you can use this method to enable / disable the option
        to change the settings of a log. This assumes you are in possession of the password.

        Parameters
        ----------
        export : bool
            Set this boolean to True to allow access to the log settings. Set it to False to protect the log settings.
        password : str
            the password needed to make changes to the protection level.
        """
        self.dispatch.AllowModifyLogSettings(export, password)

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
        self.dispatch.AllowUseFormula(export, password)

    def allow_use_formula(self, export, password):
        """When dealing with a protected document you can use this method to enable / disable the option
        to see the formula used in a Formula Log. This assumes you are in possession of the password.

        Parameters
        ----------
        export : bool
            Set this boolean to True to see the formula. Set it to False to protect the formula.
        password : str
            the password needed to make changes to the protection level.
        """
        self.dispatch.AllowViewFormula(export, password)

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
        self.dispatch.AllowViewLogHistory(export, password)