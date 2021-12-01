from win32com.client import Dispatch
from ._borehole import Borehole

class Application:

    def __init__(self):
        """Creates the WellCAD object. 
        
        Ensure WellCAD has been started at least once by an
        administrator in order to register it in the computer registry.
        """

        self.dispatch = Dispatch("WellCAD.Application")
        

    def show_window(self):
        """Displays the WellCAD workspace on screen."""
        self.dispatch._FlagAsMethod("ShowWindow")
        return self.dispatch.ShowWindow()
        

    def minimize_window(self):
        """Collapses the application window to an icon."""
        self.dispatch.MinimizeWindow()
        
        
    def maximize_window(self):
        """Extends the application window to full screen."""
        self.dispatch.MaximizeWindow()
        
        
    def cascade(self):
        """Cascades all borehole document windows (unless tabbed)."""
        self.dispatch.Cascade()
        

    def tile_horizontally(self):
        """Arranges document windows horizontally (unless tabbed)."""
        self.dispatch.TileHorizontally()
        
    
    def tile_vertically(self):
        """Arranges document windows vertically (unless tabbed)."""
        self.dispatch.TileVertically()
        

    def new_borehole(self, template = ""):
        """Creates a new borehole document object.

        The new borehole object is blank by default, unless a template
        file is provided.
        
        Parameters
        ----------
        template : str
            An optional path to a borehole document template (.wdt).
            If provided, the new borehole will be created using the
            template.
        
        Returns
        -------
        Borehole
            The new borehole document.
        """

        self.dispatch._FlagAsMethod("NewBorehole")
        obBhole = self.dispatch.NewBorehole(template)
        return Borehole(obBhole)

        
    def open_borehole(self, path = ""):
        """Opens a WellCAD borehole document file (.wcl file).
        
        Parameters
        ----------
        path : str
            The file path to the WellCAD borehole document file to open.
            If an empty string is provided, the user will be prompted
            to select a file using a standard File Open dialog box.
        
        Returns
        -------
        Borehole
            The opened borehole document.
        """

        self.dispatch._FlagAsMethod("OpenBorehole")
        obBhole = self.dispatch.OpenBorehole(path)
        return Borehole(obBhole)
        

    def get_borehole(self, index = -1):
        """Gets an existing borehole document by index.
        
        Gets a borehole document object according to the zero-based index of
        the document open in WellCAD. If no parameter is provided, the most
        recent borehole document opened in WellCAD will be returned.
        
        Parameters
        ----------
        index : (str)
            An optional zero based index of the borehole document.
        
        Returns
        -------
        Borehole
            The borehole document object with the specified index.
        """

        if index == -1:
            index = self.dispatch.NbOfDocuments - 1
        self.dispatch._FlagAsMethod("GetBorehole")
        obBhole = self.dispatch.GetBorehole(index)
        return Borehole(obBhole)
        
        
    def get_active_borehole(self):
        """Gets the active borehole document (i.e. the one that currently has focus).
                   
        Returns
        -------
        Borehole
            The active borehole document object
        """

        obBhole = self.dispatch.GetActiveBorehole
        return Borehole(obBhole)
        
        
    def close_borehole(self, prompt_for_saving = True, index = -1):
        """Closes a specific borehole document.
        
        The borehole document that is closed can be specified by an index,
        or, if none is provided, the most recently opened borehole document
        will be closed.
        
        Parameters
        ----------
        prompt_for_saving : bool
            Whether or not to prompt the user to save the borehole document.
        index : int
            The (zero-based) index of the document to close. If not provided,
            the most recently opened document will be closed.
        """

        if index == -1:
            index = self.dispatch.NbOfDocuments - 1
        self.dispatch.CloseBorehole(prompt_for_saving, index)
        
        
    @property
    def borehole_count(self):
        """Returns the number of borehole documents open in WellCAD."""
        return self.dispatch.NbOfDocuments
        
    
    def file_import(self,
                    file_name = "",
                    prompt_user = True,
                    config_file = "",
                    log_file = ""):
        """Imports the specified file into a new borehole document.
        
        Allows import of TFD, LAS, DLIS, TXT, CSV and other file
        formats into WellCAD. Please refer to the WellCAD help
        file for a description of all import parameters to be used
        in the configuration file / parameter string. If filename
        is left blank the File Open dialog will be displayed. 

        Parameters
        ----------
        file_name : str
            The path of the file to import.
        prompt_user : bool
            Whether to display an import dialog box to allow the user
            to specify import settings.
        config_file : str
            Path and filename of the configuration file or parameter string.
        log_file : str
            Path and name of the file to log error messages.
        
        Returns
        -------
        Borehole
            A new borehole document containing the imported data.
        """

        self.dispatch._FlagAsMethod("FileImport")
        obBhole = self.dispatch.FileImport(file_name,
                                           prompt_user,
                                           config_file,
                                           log_file)
        return Borehole(obBhole)
        
        
    def multi_file_import(self, file_name = "",
                          prompt_user = True,
                          config_file = "",
                          log_file = ""):
        """Creates a single borehole document from all specified files.

        Allows import of multiple TFD, LAS, DLIS, TXT, CSV and other
        file formats into WellCAD. Imported data will be merged into
        the same document. Please refer to the WellCAD help file for
        a description of all import parameters to be used in the
        configuration file / parameter string. If filename is left
        blank the File Open dialog will be displayed.

        Parameters
        ----------
        file_name : str
            A comma separated list of input files (path and file name). 
        prompt_user : str
            Boolean to display the import dialog boxes.
        config_file : str
            Path and filename of the configuration file or parameter string.
        log_file : str
            Path and name of the file to log error messages.
        
        Returns
        -------
        Borehole
            A newly created borehole document containing the data from the
            imported files.
        """

        self.dispatch._FlagAsMethod("MultiFileImport")
        obBhole = self.dispatch.MultiFileImport(file_name,
                                                prompt_user,
                                                config_file,
                                                log_file)
        return Borehole(obBhole)
        
        
    def quit(self, prompt_for_saving = True):
        """Closes all borehole documents and exits WellCAD.
        
        Parameters
        ----------
        prompt_for_saving : bool
            Whether to display the Save As dialog box for unsaved documents.
        """

        self.dispatch.Quit(prompt_for_saving)