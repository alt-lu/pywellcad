from ._dispatch_wrapper import DispatchWrapper


class MarkerItem(DispatchWrapper):
    """ A marker that can used to represent formation tops, major/minor contacts, unconformities, etc.

    Example
    -------
    >>> log = borehole.log("Formations")
    >>> marker = log.marker(0)
    >>> marker.name = 'shale'
    """

    @property
    def depth(self):
        """float: The depth of the marker in current depth
        units."""
        return self._dispatch.Depth

    @property
    def name(self):
        """str: The name of the marker."""
        return self._dispatch.Name

    @name.setter
    def name(self, value):
        self._dispatch.Name = value

    @property
    def comment(self):
        """str: The comment for this marker."""
        return self._dispatch.Comment

    @comment.setter
    def comment(self, value):
        self._dispatch.Comment = value

    @property
    def contact(self):
        """str: The name of the contact style to be used.
        
        This must be available in the contact dictionary of the Marker Log this
        marker is a part of.
        """
        return self._dispatch.Contact

    @contact.setter
    def contact(self, value):
        self._dispatch.Contact = value
