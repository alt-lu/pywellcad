from ._dispatch_wrapper import DispatchWrapper


class Font(DispatchWrapper):
    """ This class encapsulates the properties of fonts used throughout WellCAD

    For example, fonts can be specified in the following places:

    * Comment log
    * Comment partition
    * Property partition
    * Log title

    In general, attributes of this class reflect those of the ``LOGFONT``
    structure in the Win32 API. Documentation for this structure can be found
    `here <https://docs.microsoft.com/en-us/windows/win32/api/wingdi/ns-wingdi-logfonta>`_.

    Example
    -------
    >>> log = borehole.log("Comments")
    >>> font = log.font
    >>> font.name
    'Arial Narrow'
    >>> font.italic
    False
    """

    @property
    def name(self):
        """str: The name of the font type used."""
        return self._dispatch.Name

    @name.setter
    def name(self, new_name):
        self._dispatch.Name = new_name

    @property
    def weight(self):
        """int: The weight (boldness) of the font used.

        Values typically range from 100 to 900 where
        400 is regular weight and 700 is bold.
        """
        return self._dispatch.Weight

    @weight.setter
    def weight(self, new_weight):
        self._dispatch.Weight = new_weight

    @property
    def italic(self):
        """bool: Whether the font is italicized."""
        return self._dispatch.Italic

    @italic.setter
    def italic(self, flag):
        self._dispatch.Italic = flag

    @property
    def underline(self):
        """bool: Whether the font is underlined."""
        return self._dispatch.Underline

    @underline.setter
    def underline(self, flag):
        self._dispatch.Underline = flag

    @property
    def bold(self):
        """bool: Whether the font is bold."""
        return self._dispatch.Bold

    @bold.setter
    def bold(self, flag):
        self._dispatch.Bold = flag

    @property
    def strikethrough (self):
        """bool: Whether the font is struck through."""
        return self._dispatch.Strikethrough

    @strikethrough.setter
    def strikethrough(self, flag):
        self._dispatch.Strikethrough = flag

    @property
    def size(self):
        """int: The size of the font.

        See the Win32 ``LOGFONT`` documentation for more of an
        explanation.
        """
        return self._dispatch.Size

    @size.setter
    def size(self, new_size):
        self._dispatch.Size = new_size

    @property
    def charset(self):
        """int: The index of the character set used.
        
        The character set can be selected from a list of available values
        documented in the Win32 ``LOGFONT`` documentation).
        """
        return self._dispatch.Charset

    @charset.setter
    def charset(self, new_charset):
        self._dispatch.Charset = new_charset
