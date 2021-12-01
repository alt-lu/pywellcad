class Title:

    def __init__(self, title_dispatch):
        """Creates the title object.
        
        Use the get_title method in the borehole object to retrieve
        an object for the log title.
        """

        if not title_dispatch:
            raise TypeError("No title COM object supplied.")
        
        self.dispatch = title_dispatch


    @property
    def left_position(self):
        """Returns a value between 0 and 1 as left log column position."""
        return self.dispatch.LeftPosition 


    @left_position.setter
    def left_position(self, value):
        """Sets the left position of the log column.
        
        Arguments:
            value -- between 0 and 1 specifying the left position in
                     percent of the page width.

        """

        self.dispatch.LeftPosition = value


    @property
    def right_position(self):
        """Returns a value between 0 and 1 as right log column position."""
        return self.dispatch.RightPosition


    @right_position.setter
    def right_position(self, value):
        """Sets the right position of the log column.
        
        Arguments:
            value -- between 0 and 1 specifying the right position in
                     percent of the page width.

        """

        self.dispatch.RightPosition = value


    @property
    def box_height(self):
        """Returns the title box height in mm."""
        return self.dispatch.BoxHeight


    @box_height.setter
    def box_height(self, value):
        """Sets the title box height in mm.
        
        Arguments:
            value -- title box height in mm.

        """

        self.dispatch.BoxHeight = value


    @property
    def display_frame(self):
        """Returns True if the title box frame is displayed."""
        return self.dispatch.DisplayFrame


    @display_frame.setter
    def display_frame(self, flag):
        """Set to True to display the title box frame.
        
        Arguments:
            flag -- boolean to enable (True) or disable (False) the
                    display of the title box frame.

        """

        self.dispatch.DisplayFrame = flag


    @property
    def frame_color_int(self):
        """Returns an integer of the RGB color."""
        return self.dispatch.FrameColor


    @frame_color_int.setter
    def frame_color_int(self, value):
        """Set the title box frame color as an RGB integer value.
        
        Arguments:
            value -- integer of the RGB tuple.

        """

        self.dispatch.FrameColor = value


    def frame_color_rgb(self, red, green, blue):
        """Set the title box frame color as an RGB tuple.
        
        Arguments:
            red -- integer between 0 and 255 of the red intensity.
            green -- integer between 0 and 255 of the green intensity.
            blue -- integer between 0 and 255 of the blue intensity.

        """

        colorInt = red + (green * 256) + (blue * 256 * 256)
        self.dispatch.FrameColor = colorInt


    @property
    def frame_style(self):
        """Returns an integer of the frame's display style.
        
        0 = solid
        1 = dashed
        2 = dotted
        3 = dash-dot
        4 =  dash-dot-dot
        
        """
        return self.dispatch.FrameStyle


    @frame_style.setter
    def frame_style(self, style):
        """Set the display style of the title box frame.
        
        0 = solid
        1 = dashed
        2 = dotted
        3 = dash-dot
        4 =  dash-dot-dot

        Arguments:
            style -- integer representing the display style.

        """

        self.dispatch.FrameStyle = style


    @property
    def frame_width(self):
        """Returns the line width in 1/10 mm."""
        return self.dispatch.FrameWidth


    @frame_width.setter
    def frame_width(self, value):
        """Sets the line width of the title box frame.
        
        Arguments:
            value -- integer for the width of the line in 1/10 mm

        """

        self.dispatch.FrameWidth = value



    @property
    def background_color_int(self):
        """Returns an integer of the RGB color."""
        return self.dispatch.BackgroundColor 


    @background_color_int.setter
    def background_color_int(self, value):
        """Set the title background color as an RGB integer value.
        
        Arguments:
            value -- color integer from the RGB tuple.

        """

        self.dispatch.BackgroundColor  = value


    def background_color_rgb(self, red, green, blue):
        """Set the title background color as an RGB tuple.
        
        Arguments:
            red -- integer between 0 and 255 of the red intensity.
            green -- integer between 0 and 255 of the green intensity.
            blue -- integer between 0 and 255 of the blue intensity.

        """

        colorInt = red + (green * 256) + (blue * 256 * 256)
        self.dispatch.BackgroundColor  = colorInt


    @property
    def use_background(self):
        """Returns True if the colored background is used."""
        return self.dispatch.UseColoredBackground


    @use_background.setter
    def use_background(self, flag):
        """Set to True to use a colored background for the title box.
        
        Arguments:
            flag -- boolean to enable (True) or disable (False) the
                    display of the background.

        """

        self.dispatch.UseColoredBackground = flag


    @property
    def display_title(self):
        """Returns True if the title partition is displayed."""
        return self.dispatch.DisplayTitle


    @display_title.setter
    def display_title(self, flag):
        """Set to True to display the title partition.
        
        Arguments:
            flag -- boolean to enable (True) or disable (False) the
                    title partition within a log title box.

        """

        self.dispatch.DisplayTitle = flag


    @property
    def display_comment(self):
        """Returns True if the comment partition is displayed."""
        return self.dispatch.DisplayComment


    @display_comment.setter
    def display_comment(self, flag):
        """Set to True to display the comment partition.
        
        Arguments:
            flag -- boolean to enable (True) or disable (False) the
                    comment partition within a log title box.

        """

        self.dispatch.DisplayComment = flag


    @property
    def display_properties(self):
        """Returns True if the comment partition is displayed."""
        return self.dispatch.DisplayProperties


    @display_properties.setter
    def display_properties(self, flag):
        """Set to True to display the comment partition.
        
        Arguments:
            flag -- boolean to enable (True) or disable (False) the
                    comment partition within a log title box.

        """

        self.dispatch.DisplayProperties = flag


    @property
    def title_top(self):
        """Value between 0 and 1 indicating the top of the title partition."""
        return self.dispatch.TitleTop


    @title_top.setter
    def title_top(self, value):
        """Sets the top of the title partition.
        
        Arguments:
            value -- between 0 and 1 defining the top of the title
                     partition in a title box.

        """

        self.dispatch.TitleTop = value


    @property
    def title_bottom(self):
        """Value between 0 and 1 indicating the bottom of the title partition."""
        return self.dispatch.TitleBottom


    @title_bottom.setter
    def title_bottom(self, value):
        """Sets the bottom of the title partition.
        
        Arguments:
            value -- between 0 and 1 defining the bottom of the title
                     partition in a title box.

        """

        self.dispatch.TitleBottom = value


    @property
    def title_color_int(self):
        """Returns an integer of the RGB color."""
        return self.dispatch.TitleColor  


    @title_color_int.setter
    def title_color_int(self, value):
        """Set the title color as an RGB integer value.
        
        Arguments:
            value -- color integer from the RGB tuple.

        """

        self.dispatch.TitleColor   = value


    def title_color_rgb(self, red, green, blue):
        """Sets the title color as an RGB tuple.
        
        Arguments:
            red -- integer between 0 and 255 of the red intensity.
            green -- integer between 0 and 255 of the green intensity.
            blue -- integer between 0 and 255 of the blue intensity.

        """

        colorInt = red + (green * 256) + (blue * 256 * 256)
        self.dispatch.TitleColor   = colorInt


    @property
    def comment_top(self):
        """Value between 0 and 1 indicating the top of the comment partition."""
        return self.dispatch.CommentTop


    @comment_top.setter
    def comment_top(self, value):
        """Sets the top of the comment partition.
        
        Arguments:
            value -- between 0 and 1 defining the top of the comment
                     partition in a title box.

        """

        self.dispatch.CommentTop = value


    @property
    def comment_bottom(self):
        """Value between 0 and 1 indicating the bottom of the comment partition."""
        return self.dispatch.CommentBottom

    @comment_bottom.setter
    def comment_bottom(self, value):
        """Sets the bottom of the title partition.
        
        Arguments:
            value -- between 0 and 1 defining the bottom of the comment
                     partition in a title box.

        """

        self.dispatch.CommentBottom = value


    @property
    def comment_color_int(self):
        """Returns an integer of the RGB color."""
        return self.dispatch.CommentColor  


    @comment_color_int.setter
    def comment_color_int(self, value):
        """Set the comment color as an RGB integer value.
        
        Arguments:
            value -- color integer from the RGB tuple.

        """

        self.dispatch.CommentColor   = value


    def comment_color_rgb(self, red, green, blue):
        """Sets the comment color as an RGB tuple.
        
        Arguments:
            red -- integer between 0 and 255 of the red intensity.
            green -- integer between 0 and 255 of the green intensity.
            blue -- integer between 0 and 255 of the blue intensity.

        """

        colorInt = red + (green * 256) + (blue * 256 * 256)
        self.dispatch.CommentColor   = colorInt


    @property
    def properties_top(self):
        """Value between 0 and 1 indicating the top of the properties partition."""
        return self.dispatch.PropertiesTop


    @properties_top.setter
    def properties_top(self, value):
        """Sets the top of the properties partition.
        
        Arguments:
            value -- between 0 and 1 defining the top of the properties
                     partition in a title box.

        """

        self.dispatch.PropertiesTop = value


    @property
    def properties_bottom(self):
        """Value between 0 and 1 indicating the bottom of the properties partition."""
        return self.dispatch.PropertiesBottom


    @properties_bottom.setter
    def properties_bottom(self, value):
        """Sets the bottom of the properties partition.
        
        Arguments:
            value -- between 0 and 1 defining the bottom of the properties
                     partition in a title box.

        """

        self.dispatch.PropertiesBottom = value
    

    @property
    def properties_color_int(self):
        """Returns an integer of the RGB color."""
        return self.dispatch.PropertiesColor  


    @properties_color_int.setter
    def properties_color_int(self, value):
        """Set the properties color as an RGB integer value.
        
        Arguments:
            value -- color integer from the RGB tuple.

        """

        self.dispatch.PropertiesColor   = value


    def properties_color_rgb(self, red, green, blue):
        """Sets the properties color as an RGB tuple.
        
        Arguments:
            red -- integer between 0 and 255 of the red intensity.
            green -- integer between 0 and 255 of the green intensity.
            blue -- integer between 0 and 255 of the blue intensity.

        """

        colorInt = red + (green * 256) + (blue * 256 * 256)
        self.dispatch.PropertiesColor   = colorInt


    @property
    def title_horizontal_position(self):
        """Index specifying the horizontal alignment of the title.
        
        0 = left
        1 = center
        2 = right

        """

        return self.dispatch.TitleHorizontalPosition 


    @title_horizontal_position.setter
    def title_horizontal_position(self, index):
        """Sets the horizontal alignment of the log title.
        
        Arguments:
            index -- 0 = left, 1 = center, 2 = right.

        """

        self.dispatch.TitleHorizontalPosition = index


    @property
    def title_vertical_position(self):
        """Index specifying the vertical alignment of the title.
        
        0 = left
        1 = center
        2 = right

        """

        return self.dispatch.TitleVerticalPosition 


    @title_vertical_position.setter
    def title_vertical_position(self, index):
        """Sets the vertical alignment of the log title.
        
        Arguments:
            index -- 0 = left, 1 = center, 2 = right.

        """

        self.dispatch.TitleVerticalPosition = index


    @property
    def title_orientation(self):
        """Index specifying the title orientation.
        
        0 = horizontal
        1 = rotated left
        2 = reversed
        3 = rotated right

        """

        return self.dispatch.TitleOrientation 


    @title_orientation.setter
    def title_orientation(self, index):
        """Sets the orientation of the title line.
        
        Arguments:
            index -- 0 = horizontal, 1 = rotated left,
                     3 = reversed, 4 = rotated right.

        """

        self.dispatch.TitleOrientation = index


    @property
    def comment_horizontal_position(self):
        """Index specifying the horizontal alignment of the comment.
        
        0 = left
        1 = center
        2 = right

        """

        return self.dispatch.CommentHorizontalPosition 


    @comment_horizontal_position.setter
    def comment_horizontal_position(self, index):
        """Sets the horizontal alignment of the log comment.
        
        Arguments:
            index -- 0 = left, 1 = center, 2 = right.

        """

        self.dispatch.CommentHorizontalPosition = index


    @property
    def comment_vertical_position(self):
        """Index specifying the vertical alignment of the comment.
        
        0 = left
        1 = center
        2 = right

        """

        return self.dispatch.CommentVerticalPosition 


    @comment_vertical_position.setter
    def comment_vertical_position(self, index):
        """Sets the vertical alignment of the log comment.
        
        Arguments:
            index -- 0 = left, 1 = center, 2 = right.

        """

        self.dispatch.CommentVerticalPosition = index


    @property
    def comment_alignment(self):
        """Index specifying the comment alignment within the partition.
        
        0 = left
        1 = center
        2 = right

        """

        return self.dispatch.CommentAlignment 


    @comment_alignment.setter
    def comment_alignment(self, index):
        """Sets the alignment of the comment lines within the partition.
        
        Arguments:
            index -- 0 = left, 1 = center, 2 = right.

        """

        self.dispatch.CommentAlignment = index


    @property
    def comment_orientation(self):
        """Index specifying the comment orientation.
        
        0 = horizontal
        1 = rotated left
        2 = reversed
        3 = rotated right

        """

        return self.dispatch.CommentOrientation 


    @comment_orientation.setter
    def comment_orientation(self, index):
        """Sets the orientation of the comment lines.
        
        Arguments:
            index -- 0 = horizontal, 1 = rotated left,
                     3 = reversed, 4 = rotated right.

        """

        self.dispatch.CommentOrientation = index
