class Header:

    def __init__(self, header_dispatch):
        """Creates the header object.
        
        Use the get_header method in the borehole object to retrieve
        the entire borehole document header.
        """
        
        self.dispatch = header_dispatch

    @property
    def nb_of_items(self):
        """Number of dynamic text fields in the entire header."""
        return self.dispatch.NbOfItems
    

    def get_item_text(self, item_name):
        """Contents of a dynamic text field in the header.
        
        Argumets:
            item_name -- ID of the text field as entered in HeadCAD.

        Returns:
            The text contained in the dynamic text field.
        """

        return self.dispatch.ItemText(item_name)
    

    def set_item_text(self, item_name, item_text):
        """Adds the content of a dynamic text field in the header.
        
        Argumets:
            item_name -- ID of the text field as entered in HeadCAD.
            item_text -- Text to add into the dynamic text field.
        """

        self.dispatch.ItemText(item_name, item_text)


    def get_item_name(self, item_index):
        """Returns the ID of a dynamic text field.

        Returns the ID of a dynamic text field in the header based on
        the zero based index. Use GetNbOfItems to retrieve the total
        number of text fields in the header.

        Argumets:
            item_index -- Zero based index of the dynamic text field.

        Returns:
            The ID of the dynamic text field.
        """
        
        return self.dispatch.ItemName(item_index)


    def allow_export_header(self, enable, password):
        """Changes the protection status to export the header design
        
            Arguments:
                enable -- Set the argument to True to protect the
                          header export.
                password -- String of the password used to protect
                            the header.
        """

        self.dispatch.AllowExportHeader(enable, password)


    def allow_export_trailer(self, enable, password):
        """Changes the protection status to export the trailer design
        
            Arguments:
                enable -- Set the argument to True to protect the
                          header export.
                password -- String of the password used to protect
                            the header.
        """

        self.dispatch.AllowExportTrailer(enable, password)