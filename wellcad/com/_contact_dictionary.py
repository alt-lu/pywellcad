from ._dispatch_wrapper import DispatchWrapper
from ._contact import Contact

class ContactDictionary(DispatchWrapper):
    """A dictionary containing several types of contact.

    Example
    -------
    >>> log = borehole.log("Lithology")
    >>> dict = log.litho_dictionary
    >>> dict.name
    'Sst'
    >>> dict.nb_of_contacts
    12
    """

    _DISPATCH_METHODS = ("Contact", "AddContact", "RemoveContact")

    @property
    def name(self):
        """str: The name of the dictionary."""
        return self._dispatch.Name

    @name.setter
    def name(self, value):
        self._dispatch.Name = value

    @property
    def nb_of_contacts(self):
        """int: The number of contacts in the dictionary."""
        return self._dispatch.NbOfContacts

    def contact(self, index_or_code):
        """Gets a contact by index or by code.

        Parameters
        ----------
        index_or_code : int or str
            The index or the code of the contact

        Returns
        -------
        Contact
            The Contact object.
        """
        return Contact(self._dispatch.Contact(index_or_code))

    def add_contact(self):
        """Adds and returns a new contact with default settings.
        Default settings:
        * Style = solid horizontal line
        * Pen width = 0.1 mm
        * Scale factor = 100%
        * Color = black
        * Cross document = False
        Returns
        -------
        Contact
            The new Contact object.
        """
        return Contact(self._dispatch.AddContact())

    def remove_contact(self, index_or_name):
        """Removes the contact corresponding to the index or code.

        Parameters
        ----------
        index_or_code : int or str
            The index or the code of the contact

        Returns
        -------
        BOOL
            Whether the contact has been removed or not.
        """
        return self._dispatch.RemoveContact(index_or_name)