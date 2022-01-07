from ._dispatch_wrapper import DispatchWrapper


class Header(DispatchWrapper):
    """The class that manages the headers fields.

    Example
    -------
    >>> header = borehole.header
    >>> for i in range(header.nb_of_items):
    >>>     print(header.item_name(i))
    COMPANY
    Title
    STATE
    FIELD
    Features
    email
    Complementary1
    Complementary2
    Tools
    """

    @property
    def nb_of_items(self):
        """int: Number of dynamic text fields in the entire header."""
        return self._dispatch.NbOfItems

    def get_item_text(self, name):
        """Contents of a dynamic text field in the header.

        Parameters
        ----------
        name : str
            ID of the text field as entered in HeadCAD.

        Returns
        -------
        str
            The text contained in the dynamic text field.
        """

        return self._dispatch.GetItemText(name)

    def set_item_text(self, name, text):
        """Adds the content of a dynamic text field in the header.

        Parameters
        ----------
        name : str
            ID of the text field as entered in HeadCAD.
        text : str
            Text to add into the dynamic text field.
        """

        self._dispatch.SetItemText(name, text)

    def item_name(self, index):
        """Returns the ID of a dynamic text field.

        Returns the ID of a dynamic text field in the header based on
        the zero based index. Use GetNbOfItems to retrieve the total
        number of text fields in the header.

        Parameters
        ----------
        index : int
            Zero based index of the dynamic text field.

        Returns
        -------
        str
            The ID of the dynamic text field.
        """

        return self._dispatch.ItemName(index)

    def allow_export_header(self, index, enable, password):
        """Changes the protection status to export the header design

        When dealing with a protected document you can use this method to
        enable / disable the protection to export the header attached to a
        borehole document as a WCH file. This assumes you are in possession
        of the password. You still have to export the header manually,
        this method only toggles the protection.

        Parameters
        ----------
        index : int
            index of the sub-header
        enable : bool
            Set this boolean to True to allow the export of the header.
            Set it to False to protect the header again.
        password : str
            String of the password needed to make changes to the
            protection level of a header.
        """

        self._dispatch.AllowExportHeader(index, enable, password)

    def allow_export_trailer(self, index, enable, password):
        """Changes the protection status to export the trailer design

        When dealing with a protected document you can use this method to
        enable / disable the protection to export the trailer attached to a
        borehole document as a WCH file. This assumes you are in possession
        of the password. You still have to export the trailer manually,
        this method only toggles the protection.

        Parameters
        ----------
        index : int
            index of the sub-trailer
        enable : bool
            Set this boolean to True to allow the export of the trailer.
            Set it to False to protect the trailer again.
        password : str
            String of the password needed to make changes to the
            protection level of a trailer.
        """

        self._dispatch.AllowExportTrailer(index, enable, password)
