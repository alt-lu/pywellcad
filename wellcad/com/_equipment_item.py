from ._dispatch_wrapper import DispatchWrapper


class EquipmentItem(DispatchWrapper):
    """A Equipment Item found in an engineering log gives information about the elements present in a borehole.

    Base available equipments are listed below, but you can modify or add your own in the Equipment dictionary.
    
        * plain casing
        * wire wound casing
        * slotted casing
        * perforated casing
        * centralizer
        * shoe
        * packer
        * water
        * wedge
        * headWorks
        * transducer
        * gauge
        * cement
        * gravel
        * normal thread
        * reverse thread
        * plug

    Example
    -------
    >>> log = borehole.log("Well Sketch")
    >>> equipment_item = log.eqp_item(5)
    >>> equipment_item.name
    "Plain casing"
    >>> equipment_item.type
    2  # Hollow item
    """
    @property
    def top_depth(self):
        """float: The top depth of the equipment item in current
        depth units."""
        return self._dispatch.TopDepth

    @top_depth.setter
    def top_depth(self, value):
        """Value must be smaller than bottom_depth."""
        self._dispatch.TopDepth = value

    @property
    def bottom_depth(self):
        """float: The bottom depth of the equipment item in current
        depth units."""
        return self._dispatch.BottomDepth

    @bottom_depth.setter
    def bottom_depth(self, value):
        """Value must be greater than top_depth."""
        self._dispatch.BottomDepth = value

    @property
    def axis_position(self):
        """float: The axis position for a solid item in an
        Engineering Log in same units as the drill diameter."""
        return self._dispatch.AxisPosition

    @axis_position.setter
    def axis_position(self, value):
        self._dispatch.AxisPosition = value

    @property
    def external_diameter(self):
        """float: The external diameter for a hollow or solid item in
        an Engineering Log in the same units as the drill diameter."""
        return self._dispatch.ExternalDiameter

    @external_diameter.setter
    def external_diameter(self, value):
        """Value must be greater than internal_diameter."""
        self._dispatch.ExternalDiameter = value

    @property
    def internal_diameter(self):
        """float: The internal diameter for a hollow item in an
        Engineering Log in the same units as the drill diameter."""
        return self._dispatch.InternalDiameter

    @internal_diameter.setter
    def internal_diameter(self, value):
        """Value must be smaller than external_diameter."""
        self._dispatch.InternalDiameter = value

    @property
    def injection_position(self):
        """float: The injection position for a liquid item in an
        Engineering Log in same units as the drill diameter."""
        return self._dispatch.InjectionPosition

    @injection_position.setter
    def injection_position(self, value):
        self._dispatch.InjectionPosition = value

    @property
    def injection_depth(self):
        """float: The injection depth for a liquid item in an
        Engineering Log in current depth reference units."""
        return self._dispatch.InjectionDepth

    @injection_depth.setter
    def injection_depth(self, value):
        """The depth must be between top_depth and bottom_depth"""
        self._dispatch.InjectionDepth = value

    @property
    def type(self):
        """int: The type of the equipment item.

        Possible types are:

        * 0 = Undefined
        * 1 = Solid Item
        * 2 = Hollow Item
        * 3 = Liquid Item
        """
        return self._dispatch.Type

    @property
    def name(self):
        """str: The name of the equipment item.

        It is the same name as shown in the first column of the
        tabular editor."""
        return self._dispatch.Name

    @property
    def description(self):
        """str: A more descriptive name for an equiment item."""
        return self._dispatch.Description

    @property
    def comment(self):
        """str: The comment associated with the equipment item."""
        return self._dispatch.Comment

    @comment.setter
    def comment(self, value):
        self._dispatch.Comment = value

    @property
    def weight(self):
        """float: The weight of a hollow item in lbs/ft"""
        return self._dispatch.Weight

    @weight.setter
    def weight(self, value):
        self._dispatch.Weight = value
        
    @property
    def thickness(self):
        """float: The thickness of a hollow item in the same units as
        the drill diameter."""
        return self._dispatch.Thickness

    @thickness.setter
    def thickness(self, value):
        """When modifying the thickness, the inner diameter of the
        equipment item is changed"""
        self._dispatch.Thickness = value

    @property
    def grade(self):
        """str: The grade (e.g. type of casing) of a hollow item."""
        return self._dispatch.Grade

    @grade.setter
    def grade(self, value):
        self._dispatch.Grade = value

