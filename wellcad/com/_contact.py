from ._dispatch_wrapper import DispatchWrapper


class Contact(DispatchWrapper):
    """Represents a contact belonging to a contact dictionary.
    Example
    -------
    log = litho_borehole.log("lithology")
    dictionary = log.contact_dictionary
    contact = dictionary.contact(0)
    """

    @property
    def code(self):
        """str: The code of the contact."""
        return self._dispatch.Code

    @property
    def description(self):
        """str: The description of the contact."""
        return self._dispatch.Description

    @description.setter
    def description(self, text):
        self._dispatch.Description = text

    @property
    def style(self):
        """int: The index corresponding to the contact style, between 0 and 34.
        0: Solid line
        1: Dash line
        2: Dot line
        3: Dash dot line
        4: Dash dot dot line
        5: Small wave line
        6: Question solid line
        7: Question dash line
        8: Question dot line
        9: Question dash dot line
        10: Question dash dot dot line
        11: Big wave line
        12: Hashed line
        13: Bioturbated line
        14: Faulting line
        15: Inclined line
        16: Poor exposure line
        17: Paleosol line
        18: Hardground line
        19: Firmground line
        20: Mud cracks line
        21: Stylolite line
        22: Karstified line
        23: No line
        24: Downward erosive line
        25: Upward erosive line
        26: Inclined downward erosive line
        27: Inclined upward erosive line
        28: Ball and pillar line
        29: Burrowed line
        30: Slickenside line
        31: Load flame line
        32: Intrusive line
        33: Loaded Line
        34: Contorted line
        """
        return self._dispatch.Style

    @style.setter
    def style(self, index):
        self._dispatch.Style = index

    @property
    def width(self):
        """int: The width of the pen used to draw the contact (in mm/10)."""
        return self._dispatch.Width

    @width.setter
    def width(self, value):
        self._dispatch.Width = value

    @property
    def cross_document(self):
        """BOOL: Whether the contact is drawn on the entire document or on the log only."""
        return self._dispatch.CrossDocument

    @cross_document.setter
    def cross_document(self, enable):
        self._dispatch.CrossDocument = enable

    @property
    def scale_factor(self):
        """float: The factor multiplying the size of the contact (1.00 = 100%)."""
        return self._dispatch.ScaleFactor

    @scale_factor.setter
    def scale_factor(self, value):
        self._dispatch.ScaleFactor = value

    @property
    def color(self):
        """int: The color of the contact.

        Colours are specified as a 32 bit integer with an ``xBGR`` structure.
        Each of the blue (B), green (G) and red (R) components are 8 bit
        values.
        """
        return self._dispatch.Color

    @color.setter
    def color(self, color):
        self._dispatch.Color = color