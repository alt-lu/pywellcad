from ._dispatch_wrapper import DispatchWrapper


class Structure(DispatchWrapper):
    r"""Structures are picked features (strata, lineations, fractures, breakouts) within a Structure, Lineation
    or Breakout Log.

    Sinusoidal structures (for example factures crossing a borehole) can be partial with only limited visible portions.
    Lineations are penetrative linear elements within a rock and can be of various origin (mineral lineation, fold axis etc.)
    Breakouts structures are vertical fractures caused by compression forces on the borehole walls.
    Their length, aperture and orientation helps to understand the constraints applied to the rock formation.

    ::

       +-------------------------------------------------+-------------------------------------------------+
       |                                                 |                                                 |
       |                                                 |                                                 |
       |         Full structure with aperture            |      Structure with partial features            |
       |                                                 |                                                 |
       | 0                    180                     360| 0                    180                     360|
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
       |                                                 |                                                 |
       +-------------------------------------------------+-------------------------------------------------+

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
        |        aperture                                            |
        |                                                            |
        +------------------------------------------------------------+

        +------------------------------------------------+
        |                    Lineation log               |
        |                                                |
        |        trend                                   |
        |          |                                     |
        | 0        v           180                    360|
        +------------------------------------------------+
        |                                                |
        |                                                |
        |                     *=========*                |
        |        *                             *         |
        |       .\\                           //         |
        |       . \\                         //          |
        |       .  \\                       //           |
        |       .   \\                     //            |
        |       .____\\                   //             |
        |         ^   \\                 //              |
        |         |    *                //               |
        |         |                    //                |
        |     plunge                  //                 |
        |                            //                  |
        |                           //                   |
        |                          *                     |
        |                                                |
        +------------------------------------------------+

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
        """float : The depth of the center of a structure object in
        current depth units.

        This is different from ``feature_depth`` if part of the structure
        is not visible."""
        return self._dispatch.Depth

    @property
    def azimuth(self):
        """float: The azimuth angle for a structure in degrees.

        Azimuth is the angle of inclination of the structure measured
        downward from horizontal.
        Depending on the log type, azimuth has a different meaning:

            * dip direction for planar features (i.e. Structure log).
            * azimuthal position for breakouts and tensile fractures (i.e. Breakout Log).
            * trend for vector like structures (i.e. Lineation Log).
        """
        return self._dispatch.Azimuth

    @azimuth.setter
    def azimuth(self, value):
        self._dispatch.Azimuth = value

    @property
    def tilt(self):
        """float: The tilt angle for a structure in degrees.

        Tilt is measured from the horizontal. It corresponds to the
        structural dip angle.
        Depending on the log type, tilt has a different meaning:

            * dip angle for planar features (i.e. Structure log)
            * tilt angle between breakout and borehole axis (i.e. Breakout Log)
            * plunge for vector like structures (i.e. Lineation Log)."""
        return self._dispatch.Tilt

    @tilt.setter
    def tilt(self, value):
        self._dispatch.Tilt = value

    @property
    def aperture(self):
        """float: The vertical aperture of the sinusoidal structure
        in meters or the opening angle of a breakout structure in
        degrees."""
        return self._dispatch.Aperture

    @aperture.setter
    def aperture(self, value):
        self._dispatch.Aperture = value

    @property
    def length(self):
        """float: The length of a breakout structure in meters."""
        return self._dispatch.Length

    @length.setter
    def length(self, value):
        self._dispatch.Length = value

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
        parts of a sinusoidal structure in current depth units."""
        return self._dispatch.FeatureDepth

    @property
    def visible_azimuth_ranges(self):
        """str: The range of visible azimuths of the item.

        If there are partial sinusoidal structures, this property
        specifies the azimuth ranges where the structure is visible,
        otherwise it returns an empty string.

        Examples:

             * stucture entirely visible : ``""``
             * 1 visible azimuth range : ``"25.00-189.00"``
             * 2 visible azimuth range : ``"12.00-36.00-100.00-150.00"``
        """
        return self._dispatch.VisibleAzimuthRanges

    @visible_azimuth_ranges.setter
    def visible_azimuth_ranges(self, value):
        self._dispatch.VisibleAzimuthRanges = value

    @property
    def eccentricity(self):
        """float: Describes the offset between lineation (vector) and the
        center of the borehole.

        The property has a value of 0 for a
        lineation crossing right through the center of the borehole.
        Lineation intersecting the borehole off center have an
        eccentricity between -1 and 1."""
        return self._dispatch.Eccentricity