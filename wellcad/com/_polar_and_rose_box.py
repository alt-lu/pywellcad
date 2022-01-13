from ._dispatch_wrapper import DispatchWrapper


class PolarAndRoseBox(DispatchWrapper):
    """A polar or rose diagram with annotations. These diagrams or "boxes" are stored in a Polar & Rose Log.

    Polar & Rose boxes are sometimes refered to as Schmit boxes (see example below)

    Example
    -------
    >>> log = borehole.log("Rose Diagram")
    >>> box = log.schmit_box_at_depth(10.5)  # Polar & Rose box called schmit box
    >>> box.text
    "Intervals Automatically Determined"
    """

    @property
    def top_depth(self):
        """float: The top depth of the Polar & Rose box in current
        depth reference units.
        """
        return self._dispatch.TopDepth

    @property
    def bottom_depth(self):
        """float: The bottom depth of the Polar & Rose box in current
        depth reference units.
        """
        return self._dispatch.BottomDepth

    @property
    def text(self):
        """str: The text for a Polar & Rose Log box.

        The text is not displayed in the plot and is only visible in
        the tabular editor or when exporting the data.
        """
        return self._dispatch.Text

    @text.setter
    def text(self, value):
        self._dispatch.Text = value


