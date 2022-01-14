from ._dispatch_wrapper import DispatchWrapper


class LithoBed(DispatchWrapper):
    """ This class represents a lithological bed. These are sections within a lithology log (Litho Log)

        You can find more information on your defined lithologies in your LithCAD library.

        Example
        -------
        >>> log = borehole.log("Lithology")
        >>> bed = log.litho_bed_at_depth(10.5)
        >>> bed.top_contact
        'undulating'
        >>> bed.top_contact = 'sharp'
        """

    @property
    def top_depth(self):
        """float: The top depth of a lithology bed in current depth
        units."""
        return self._dispatch.TopDepth

    @property
    def bottom_depth(self):
        """float: The bottom depth of a lithology bed in current depth
        units."""
        return self._dispatch.BottomDepth

    @property
    def value(self):
        """float: The hardness of the bed (between 0 and 1)"""
        return self._dispatch.Value

    @value.setter
    def value(self, hardness):
        self._dispatch.Value = hardness

    @property
    def litho_code(self):
        """str: The lithological code of the bed.

        You can use the LithCAD tool to see your lithological
        symbols and associated codes"""
        return self._dispatch.LithoCode

    @litho_code.setter
    def litho_code(self, value):
        self._dispatch.LithoCode = value

    @property
    def top_contact(self):
        """str: The contact code of the top of the bed."""
        return self._dispatch.TopContact

    @top_contact.setter
    def top_contact(self, value):
        self._dispatch.TopContact = value

    @property
    def bottom_contact(self):
        """str: The contact code of the bottom of the bed."""
        return self._dispatch.BottomContact

    @bottom_contact.setter
    def bottom_contact(self, value):
        self._dispatch.BottomContact = value


