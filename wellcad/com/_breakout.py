from ._dispatch_wrapper import DispatchWrapper


class Breakout(DispatchWrapper):
    """Characterises borehole wall breakouts and tensile fractures picked from an image.

    Breakouts are vertical fractures caused by compression forces on the borehole walls.
    Their length, aperture and orientation help to understand the constraints applied
    to the rock formation.
    
    ::
    
        +------------------------------------------------------------+
        |                    Breakout log                            |
        |                                                            |
        |      azimuth                                               |
        |         |                                                  |
        | 0       v                   180                         360|
        +------------------------------------------------------------+
        |                                                            |
        |                                                            |
        |      +++++                          +-         +++++       |
        |      +:::+                          |          +:::+       |
        |      +:::+                          |          +:::+       |
        |       +:::+                         |         +:::+        |
        |       +:::+                         |         +:::+        |
        |       +:::+                         |         +:::+        |
        |        +:::+  <- depth    length -> |        +:::+         |
        |        +:::+                        |        +:::+         |
        |        +:::+                        |        +:::+         |
        |         +:::+                       |       +:::+          |
        |         +:::+                       |       +:::+          |
        |         +:::+                       |       +:::+          |
        |         +++++                       +-      +++++          |
        |                                                            |
        |         |____|                        mirrored breakout    |
                 aperture



    Example
    -------
    >>> log = borehole.log("breakout_log")
    >>> breakout = log.breakout(0)  # The Breakout object at depth index 0
    >>> breakout.tilt
    37.59
    >>> breakout.get_attribute_value("Type")
    '2'
    """

    @property
    def depth(self):
        """float: The depth of the breakout determined at the center
        of the breakout in current depth units"""
        return self._dispatch.Depth

    @property
    def azimuth(self):
        """float: Azimuthal position of the breakout on the borehole
        wall in degrees."""
        return self._dispatch.Azimuth

    @azimuth.setter
    def azimuth(self, value):
        self._dispatch.Azimuth = value

    @property
    def tilt(self):
        """float: The angle between the axis of the borehole and the
        center line of the breakout."""
        return self._dispatch.Tilt

    @tilt.setter
    def tilt(self, value):
        self._dispatch.Tilt = value

    @property
    def aperture(self):
        """float: The aperture (or opening) of the breakout in degrees."""
        return self._dispatch.Aperture

    @aperture.setter
    def aperture(self, value):
        self._dispatch.Aperture = value

    @property
    def length(self):
        """float: The length of a breakout in meters."""
        return self._dispatch.Length

    @length.setter
    def length(self, value):
        self._dispatch.Length = value

    def get_attribute_value(self, attribute_name):
        """Gets the value from the specified attribute class
        belonging to the breakout object.

        Attributes are elements of a key-value map specified by the
        user.

        Parameters
        ----------
        attribute_name : str
            Name of the attribute class from which to retrieve the code.

        Returns
        -------
        str
            The code associated with this attribute
        """

        return self._dispatch.GetAttributeValue(attribute_name)

    def set_attribute_value(self, attribute_name, attribute_value):
        """Sets the value from the specified attribute class
        belonging to the breakout object.

        Parameters
        ----------
        attribute_name : str
            Name of the attribute class from which to modify the code.
        attribute_value : str
            The code from the above attribute class you would like to
            assign to the picked feature.
        """

        self._dispatch.SetAttributeValue(attribute_name, attribute_value)
