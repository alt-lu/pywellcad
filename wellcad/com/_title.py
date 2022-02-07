from ._dispatch_wrapper import DispatchWrapper
from ._font import Font


class Title(DispatchWrapper):
    """Represents the title of a log.

    A title object is represented by a box at the top of a log. Inside the title box are three sections: the title, the comments and the properties.
    For each of these sections, you can specify properties such as text, font, color, alignment etc. The title box frame and background can also be customized.

    ::

        |-------------------|-----------------------------|-------------------|
        |                   |                             |                   |
        |     Title         |           Title             |                   |
        |                   |                             |                   |
        |                   |          comment            |      Title        |
        |                   |                             |                   |
        |    properties     |         properties          |                   |
        |-------------------|-----------------------------|-------------------|
        |                   |                             |                   |
        |                   |                             |                   |
        |    log data       |         log data            |     log data      |
        |                   |                             |                   |

    Example
    -------
    >>> borehole = app.get_active_borehole()
    >>> title = borehole.title("GR")
    >>> title.left_position
    0.2
    >>> title.box_height = 200
    """

    @property
    def left_position(self):
        """float: The position of the left side of a title for a log or group,
        as a fraction of the document width.

        If set for a group title, the logs that are a part of the group will
        be moved/scaled accordingly. In the case that this is set to be a value
        higher than ``right_position``, the two attributes will swap. Values
        will be clamped in the range [0.0, 1.0].
        """
        return self._dispatch.LeftPosition

    @left_position.setter
    def left_position(self, value):
        self._dispatch.LeftPosition = value

    @property
    def right_position(self):
        """float: The position of the right side of a title for a log or group,
        as a fraction of the document width.

        If set for a group title, the logs that are a part of the group will
        be moved/scaled accordingly. In the case that this is set to be a value
        lower than ``left_position``, the two attributes will swap. Values
        will be clamped in the range [0.0, 1.0].
        """
        return self._dispatch.RightPosition

    @right_position.setter
    def right_position(self, value):
        self._dispatch.RightPosition = value

    @property
    def box_height(self):
        """float: The title box height in mm."""
        return self._dispatch.BoxHeight

    @box_height.setter
    def box_height(self, value):
        self._dispatch.BoxHeight = value

    @property
    def display_frame(self):
        """bool: Whether the title box frame is displayed."""
        return self._dispatch.DisplayFrame

    @display_frame.setter
    def display_frame(self, flag):
        """Set to True to display the title box frame."""
        self._dispatch.DisplayFrame = flag

    @property
    def frame_color(self):
        """int: The color of the frame.

        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values.
        """
        return self._dispatch.FrameColor

    @frame_color.setter
    def frame_color(self, value):
        self._dispatch.FrameColor = value

    @property
    def frame_style(self):
        """int: The frame's display style.

        Available styles are:

        * 0 = solid
        * 1 = dashed
        * 2 = dotted
        * 3 = dash-dot
        * 4 =  dash-dot-dot
        """
        return self._dispatch.FrameStyle

    @frame_style.setter
    def frame_style(self, style):
        self._dispatch.FrameStyle = style

    @property
    def frame_width(self):
        """int: The line width of the frame in 1/10 mm."""
        return self._dispatch.FrameWidth

    @frame_width.setter
    def frame_width(self, value):
        self._dispatch.FrameWidth = value

    @property
    def background_color(self):
        """int: The background color of a group or log title.

        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values.
        """
        return self._dispatch.BackgroundColor

    @background_color.setter
    def background_color(self, value):
        self._dispatch.BackgroundColor = value

    @property
    def use_colored_background(self):
        """bool: Whether the colored background is used."""
        return self._dispatch.UseColoredBackground

    @use_colored_background.setter
    def use_colored_background(self, flag):
        self._dispatch.UseColoredBackground = flag

    @property
    def display_title(self):
        """bool: Whether the title partition is displayed."""
        return self._dispatch.DisplayTitle

    @display_title.setter
    def display_title(self, flag):
        self._dispatch.DisplayTitle = flag

    @property
    def display_comment(self):
        """bool: Whether the comment partition is displayed."""
        return self._dispatch.DisplayComment

    @display_comment.setter
    def display_comment(self, flag):
        self._dispatch.DisplayComment = flag

    @property
    def display_properties(self):
        """bool: Whether the property partition is displayed."""
        return self._dispatch.DisplayProperties

    @display_properties.setter
    def display_properties(self, flag):
        self._dispatch.DisplayProperties = flag

    @property
    def title_text(self):
        """str: The text for the title partition."""
        return self._dispatch.TitleText

    @title_text.setter
    def title_text(self, text):
        self._dispatch.TitleText = text

    @property
    def comment_text(self):
        """str: The text for the comment partition."""
        return self._dispatch.CommentText

    @comment_text.setter
    def comment_text(self, text):
        self._dispatch.CommentText = text

    @property
    def title_top(self):
        """float: The top of the title partition of a group or log
        title box as a fraction of the box height (value between 0 and 1)."""
        return self._dispatch.TitleTop

    @title_top.setter
    def title_top(self, value):
        self._dispatch.TitleTop = value

    @property
    def title_bottom(self):
        """float: The bottom of the title partition of a group or log
        title box as a fraction of the box height (value between 0 and 1)."""
        return self._dispatch.TitleBottom

    @title_bottom.setter
    def title_bottom(self, value):
        self._dispatch.TitleBottom = value

    @property
    def title_color(self):
        """int: The font color of the title part of a group or log
        title.

        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values.
        """
        return self._dispatch.TitleColor

    @title_color.setter
    def title_color(self, value):
        self._dispatch.TitleColor = value

    @property
    def comment_top(self):
        """float: The top of the comment partition of a group or log
        title box as a fraction of the box height (value between 0
        and 1)."""
        return self._dispatch.CommentTop

    @comment_top.setter
    def comment_top(self, value):
        self._dispatch.CommentTop = value

    @property
    def comment_bottom(self):
        """float: The bottom of the comment partition of a group or
        log title box as a fraction of the box height (value between 0
        and 1)."""
        return self._dispatch.CommentBottom

    @comment_bottom.setter
    def comment_bottom(self, value):
        self._dispatch.CommentBottom = value

    @property
    def comment_color(self):
        """int: The coment color of the title part of a group or log
        title.

        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values.
        """
        return self._dispatch.CommentColor

    @comment_color.setter
    def comment_color(self, value):
        self._dispatch.CommentColor = value

    @property
    def properties_top(self):
        """float: The top of the properties partition of a log title
        box as a fraction of the box height (value between 0 and 1).
        """
        return self._dispatch.PropertiesTop

    @properties_top.setter
    def properties_top(self, value):
        self._dispatch.PropertiesTop = value

    @property
    def properties_bottom(self):
        """float: The bottom of the properties partition of a log title
        box as a fraction of the box height (value between 0 and 1).
        """
        return self._dispatch.PropertiesBottom

    @properties_bottom.setter
    def properties_bottom(self, value):
        self._dispatch.PropertiesBottom = value

    @property
    def properties_color(self):
        """int: The font color of the property part of a group or log
        title.

        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values.
        """
        return self._dispatch.PropertiesColor

    @properties_color.setter
    def properties_color(self, value):
        self._dispatch.PropertiesColor = value

    @property
    def title_horizontal_position(self):
        """int: Index specifying the horizontal alignment of the title.

        Available options are:

        * 0 = left
        * 1 = center
        * 2 = right
        """
        return self._dispatch.TitleHorizontalPosition

    @title_horizontal_position.setter
    def title_horizontal_position(self, index):
        self._dispatch.TitleHorizontalPosition = index

    @property
    def title_vertical_position(self):
        """int: Index specifying the vertical alignment of the title.

        Available options are:

        * 0 = left
        * 1 = center
        * 2 = right
        """
        return self._dispatch.TitleVerticalPosition

    @title_vertical_position.setter
    def title_vertical_position(self, index):
        self._dispatch.TitleVerticalPosition = index

    @property
    def title_orientation(self):
        """int: Index specifying the title orientation.

        Available options are:

        * 0 = horizontal
        * 1 = rotated left
        * 2 = reversed
        * 3 = rotated right
        """
        return self._dispatch.TitleOrientation

    @title_orientation.setter
    def title_orientation(self, index):
        self._dispatch.TitleOrientation = index

    @property
    def comment_horizontal_position(self):
        """int: Index specifying the horizontal alignment of the comment.

        Available options are:

        * 0 = left
        * 1 = center
        * 2 = right
        """
        return self._dispatch.CommentHorizontalPosition

    @comment_horizontal_position.setter
    def comment_horizontal_position(self, index):
        self._dispatch.CommentHorizontalPosition = index

    @property
    def comment_vertical_position(self):
        """int: Index specifying the vertical alignment of the comment.

        Available options are:

        * 0 = left
        * 1 = center
        * 2 = right
        """
        return self._dispatch.CommentVerticalPosition

    @comment_vertical_position.setter
    def comment_vertical_position(self, index):
        self._dispatch.CommentVerticalPosition = index

    @property
    def comment_alignment(self):
        """int: Index specifying the comment alignment within the
        partition.

        Available options are:

        * 0 = left
        * 1 = center
        * 2 = right
        """
        return self._dispatch.CommentAlignment

    @comment_alignment.setter
    def comment_alignment(self, index):
        self._dispatch.CommentAlignment = index

    @property
    def comment_orientation(self):
        """int: Index specifying the comment orientation.

        Available options are:

        * 0 = horizontal
        * 1 = rotated left
        * 2 = reversed
        * 3 = rotated right
        """
        return self._dispatch.CommentOrientation

    @comment_orientation.setter
    def comment_orientation(self, index):
        self._dispatch.CommentOrientation = index

    @property
    def title_font(self):
        """Font: The font of the title partition of a group or log
        title."""
        return Font(self._dispatch.TitleFont)

    @property
    def comment_font(self):
        """Font: The font of the comment partition of a group or log
        title."""
        return Font(self._dispatch.CommentFont)

    @property
    def properties_font(self):
        """Font: The font of the properties  partition of a group or log
        title."""
        return Font(self._dispatch.PropertiesFont)
