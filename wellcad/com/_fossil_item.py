from ._dispatch_wrapper import DispatchWrapper


class FossilItem(DispatchWrapper):
    """ This class represents a fossil item. These are items within a CoreDesc log

    You can find more information on your defined fossils in your LithCAD library.

    Example
    -------
    >>> log = borehole.log("Fossils")
    >>> item = log.fossil_item_at_depth(10.5)
    >>> item.symbol_code
    'undulating'
    >>> item.abundance = 2
    """

    @property
    def top_depth(self):
        """float: The top depth of the item in current depth
        units."""
        return self._dispatch.TopDepth

    @property
    def bottom_depth(self):
        """float: The bottom depth of the item in current depth
        units."""
        return self._dispatch.BottomDepth

    @property
    def symbol_code(self):
        """str: The code of the item."""
        return self._dispatch.SymbolCode

    @symbol_code.setter
    def symbol_code(self, value):
        self._dispatch.SymbolCode = value

    @property
    def abundance(self):
        """float: The abundance of the item.

        Allowed values are :
        * 1 = rare
        * 2 = moderate
        * 3 = common
        * 4 = abundant
        * 5 = pervasive
        """
        return self._dispatch.Abundance

    @abundance.setter
    def abundance(self, value):
        self._dispatch.Abundance = value

    @property
    def dominance(self):
        """float: The dominance of the item.

        Allowed values are :

        * 0 = undifferentiated
        * 1 = minor
        * 2 = major
        """
        return self._dispatch.Dominance

    @dominance.setter
    def dominance(self, value):
        self._dispatch.Dominance = value
