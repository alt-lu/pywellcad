from ._dispatch_wrapper import DispatchWrapper
from ._attribute_category import AttributeCategory


class AttributeDictionary(DispatchWrapper):
    """A dictionary containing the different categories of an attribute.

    Example
    -------
    log = borehole.log("Structures")
    dict = log.get_attribute_dictionary(log.get_attribute_name(0))
    dict.name
    dict.nb_of_categories
    """

    _DISPATCH_METHODS = ("Category", "IsCategory", "AddCategory", "RemoveCategory")

    @property
    def name(self):
        """str: The name of the dictionary."""
        return self._dispatch.Name

    @name.setter
    def name(self, value):
        self._dispatch.Name = value

    @property
    def nb_of_categories(self):
        """int: The number of categories in the dictionary."""
        return self._dispatch.NbOfCategories

    def is_category(self, code):
        """Checks if the dictionary contains a category with the specified code.

        Parameters
        ----------
        code : str
            The code of the category.

        Returns
        -------
        bool
            True if successful, False otherwise.
        """
        return self._dispatch.IsCategory(code)

    def attribute_category(self, index_or_code):
        """Gets a category by index or by code.

        Parameters
        ----------
        index_or_code : int or str
            The index or the code of the category

        Returns
        -------
        AttributeCategory
            The AttributeCategory object.
        """
        return AttributeCategory(self._dispatch.Category(index_or_code))

    def add_category(self):
        """Adds and returns a new category with default settings.
        Default settings :
        * Body style = circle
        * Body color = black
        * Body size = small
        * Tail style = flat
        * Tail size = long
        * Tail color = black
        * Sinus pen style = solid
        * Sinus pen width = 0.1 mm

        Returns
        -------
        AttributeCategory
            The AttributeCategory object.
        """
        return AttributeCategory(self._dispatch.AddCategory())

    def remove_category(self, index_or_code):
        """Removes the category corresponding to the index or code.

        Parameters
        ----------
        index_or_code : int or str
            The index or the code of the category

        Returns
        -------
        BOOL
            Whether the targeted category has been deleted or not.
        """
        return self._dispatch.RemoveCategory(index_or_code)
