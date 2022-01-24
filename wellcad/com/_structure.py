from ._dispatch_wrapper import DispatchWrapper


class Structure(DispatchWrapper):
    """ Structures are picked features (strata, contacts, fractures) within a Structure Log.

    These structures can be partial with only limited visible portions.

    ::

       +-------------------------------------------------+-------------------------------------------------+
       |                                                 |                                                 |
       |                                                 |                                                 |
       |         Full structure with aperture            |      Structure with partial features            |
       |                                                 |                                                 |
       | 0                 180                        360| 0                 180                        360|
       +-------------------------------------------------+-------------------------------------------------+
       |                                                 |                                                 |
       |         XXXXXXX                                 |         .......                                 |
       |      XXX:::::::XXX                              |      ...       ...                              |
       |    XX:::::::::::::XX                            |    ..             ..                            |
       |   X:::::XXXXXX::::::X                           |   .                 .                           |
       |  X:::XXX      XXX::::X                          |  .                   .                          |
       | X::XX            XX:::X                         | .                     .                         |
       |X::X                X:::X<- depth               X|.                       .<- depth                |
       |::X                  X:::X                     X:|                         .                       |
       |:X                    X:::X                   X::|                          X                   X  |
       |X                      X:::X                 X::X|                           X                 X   |
       |                        X:::XX             XX::X |            feature_depth ->XX             XX    |
       |                         X::::XXX       XXX:::X  |                              XXX       XXX      |
       |                +-        X:::::XXXXXXX::::::X   |                                XXXXXXX          |
       |       aperture |           XX:::::::::::::XX    |                                                 |
       |                |             XXX:::::::XXX      |                                                 |
       |                +-              XXXXXXX          |                                                 |

    Example
    -------
    >>> log = borehole.log("Structure")
    >>> struct = log.structure(0)  # The Structure object at depth index 0
    >>> struct.tilt
    37.59
    >>> struct.get_attribute_value("Type")
    '2 - Bed / Lamina'
    """

    @property
    def depth(self):
        """float : The depth of the "middle" of a structure object in
        current depth units.

        This is different from ``feature_depth`` if part of the structure
        is not visible."""
        return self._dispatch.Depth

    @property
    def azimuth(self):
        """float: The azimuth angle for a structure in degrees.

        Azimuth is the angle of inclination of the structure measured
        downward from horizontal."""
        return self._dispatch.Azimuth

    @azimuth.setter
    def azimuth(self, value):
        self._dispatch.Azimuth = value

    @property
    def tilt(self):
        """float: The tilt angle for a structure in degrees.

        Tilt is measured from the horizontal. It corresponds to the
        structural dip angle."""
        return self._dispatch.Tilt

    @tilt.setter
    def tilt(self, value):
        self._dispatch.Tilt = value

    @property
    def aperture(self):
        """float: The vertical aperture of the structure in meters."""
        return self._dispatch.Aperture

    @aperture.setter
    def aperture(self, value):
        self._dispatch.Aperture = value

    def get_attribute_value(self, attribute_name):
        """Gets the value from the specified attribute class
        belonging to the structure object.

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
        belonging to the structure object.

        Parameters
        ----------
        attribute_name : str
            Name of the attribute class from which to modify the code.
        attribute_value : str
            The code from the above attribute class you would like to
            assign to the picked feature.
        """

        self._dispatch.SetAttributeValue(attribute_name, attribute_value)

    @property
    def feature_depth(self):
        """float: The depth of the centre of the range of all visible
        parts of the structure in current depth units."""
        return self._dispatch.FeatureDepth

    @property
    def visible_azimuth_ranges(self):
        """str: The range of visible azimuths of the item.

        If there are partial structures, this property specifies the
        azimuth ranges where the structure is visible, otherwise it
        returns an empty string.

        Examples:

             * stucture entirely visible : ""
             * 1 visible azimuth range : "25-189"
             * 2 visible azimuth range : "25-189, 200-260"
        """
        return self._dispatch.VisibleAzimuthRanges

    @visible_azimuth_ranges.setter
    def visible_azimuth_ranges(self, value):
        self._dispatch.VisibleAzimuthRanges = value
