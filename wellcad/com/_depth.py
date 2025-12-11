from ._dispatch_wrapper import DispatchWrapper
from ._font import Font


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
        """bool: Whether this depth scale is used as the current reference axis.

        Setting this property to True on another depth log changes
        the property to False on this object. If no other depth log
        is used as the depth scale, the main depth log will
        automatically be used as the depth scale."""
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
        """float: The position of the left side of the master depth column as a
        fraction of the document width.
        
        In the case that this is set to be a value higher than
        ``right_position``, the two attributes will swap. Values will be
        clamped in the range [0.0, 1.0].
        """
        return self._dispatch.LeftPosition

    @left_position.setter
    def left_position(self, left_pos):
        self._dispatch.LeftPosition = left_pos

    @property
    def right_position(self):
        """float: The position of the right side of the master depth column as
        a fraction of the document width.
        
        In the case that this is set to be a value lower than
        ``left_position``, the two attributes will swap. Values will be
        clamped in the range [0.0, 1.0].
        """
        return self._dispatch.RightPosition

    @right_position.setter
    def right_position(self, right_pos):
        self._dispatch.RightPosition = right_pos

    @property
    def unit(self):
        """int: The depth unit

        The available units are the following:

        * 0 = meters
        * 1 = feet
        * 2 = seconds
        * 3 = milliseconds
        * 4 = Date/Time
        """
        return self._dispatch.Unit

    @unit.setter
    def unit(self, unit):
        self._dispatch.Unit = unit

    def set_position(self, left, right):
        """Sets the position and width of the master depth column.

        Values given outside the range of [0.0, 1.0] will be clamped. If
        ``left`` > ``right``, the arguments are swapped.

        Parameters
        ----------
        left : float
            The position of the left side of the depth column as a fraction of
            the document width.

        right : float
            The position of the right side of the depth column as a fraction of
            the document width.
        """
        self._dispatch.SetPosition(left, right)

    @property
    def scale_reversed(self):
        """bool: Whether the depth scale is reversed or not.
        By default, the depth is counted positive downward. If this option is set to True, it'll be counted negatively."""
        return self._dispatch.ScaleReversed

    @scale_reversed.setter
    def scale_reversed(self, value):
        self._dispatch.ScaleReversed = value

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
    def background_style(self):
        """int: The background style behind the depth strings. For example, if the depth strings
        are displayed on top a lithology column, selecting Opaque (0) will make them stand out.

        Available styles:
        0: opaque
        1: transparent

        If an invalid style is set, nothing will happen.
        """
        return self._dispatch.BackgroundStyle

    @background_style.setter
    def background_style(self, code):
        self._dispatch.BackgroundStyle = code

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
    def horz_text_align(self):
        """
        int: The index corresponding to the type of alignment of the depth strings within the column.
        0 = Left
        1 = Center
        2 = Right
        """
        return self._dispatch.HorzTextAlignment

    @horz_text_align.setter
    def horz_text_align(self, align_index):
        self._dispatch.HorzTextAlignment = align_index

    @property
    def text_orientation(self):
        """
        int: The index corresponding to the text orientation.
        0 = Normal
        1 = Left (90° clockwise rotation)
        2 = Right (90° counter-clockwise rotation)
        """
        return self._dispatch.TextOrientation

    @text_orientation.setter
    def text_orientation(self, orientation_index):
        self._dispatch.TextOrientation = orientation_index

    @property
    def indicators_per_spacing(self):
        """int: The number of depth strings per spacing."""
        return self._dispatch.IndicatorsPerSpacing

    @indicators_per_spacing.setter
    def indicators_per_spacing(self, value):
        self._dispatch.IndicatorsPerSpacing = value

    @property
    def ticks_position(self):
        """int: The index corresponding to the position of the ticks. Ticks are little extensions of the depth grid lines into the depth column.
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
    def time_zero(self):
        """int: The initial time of the Date/Time column in seconds with 0 corresponding to the 01/01/1970 at 00:00:00.
        For example, choosing 90130 will make it start on the 02/01/1970 at 01:02:10."""
        return self._dispatch.TimeZero

    @time_zero.setter
    def time_zero(self, enable):
        self._dispatch.TimeZero = enable

    @property
    def depth_font(self):
        """Gets the font used in a Comment Log for the depth."""
        return Font(self._dispatch.DepthFont)

    @depth_font.setter
    def depth_font(self, font):
        self._dispatch.DepthFont = font._dispatch