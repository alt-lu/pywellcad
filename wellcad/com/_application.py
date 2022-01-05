from win32com.client import Dispatch
from ._dispatch_wrapper import DispatchWrapper
from ._borehole import Borehole

class Application(DispatchWrapper):
    """The core class used to interact with WellCAD via its COM API.

    In general, it is the only class you should instantiate directly. All
    interaction with borehole documents, logs, etc, should be done through
    this initial ``Application`` instance.

    Instantiating an ``Application`` will automatically open a WellCAD instance
    if there is not one already open, or connect to an existing WellCAD
    instance if there is one open.

    Before using the COM API, ensure WellCAD has been started at least once by
    an administrator in order to register it in the computer registry.

    Example
    -------
    >>> import wellcad.com
    >>> app = wellcad.com.Application()
    >>> app.show_window()
    True
    >>> app.new_borehole()
    <wellcad.com._borehole.Borehole object at 0x000001D6973FBD30>
    """

    _DISPATCH_METHODS = ("ShowWindow", "NewBorehole", "OpenBorehole",
        "GetBorehole", "GetActiveBorehole", "FileImport", "MultiFileImport")
    
    def __new__(cls):
        return object.__new__(cls)
    
    def __init__(self):
        super().__init__(Dispatch("WellCAD.Application"))
        
    def show_window(self):
        """Attempts to display the WellCAD workspace on screen.
        
        Returns
        -------
        bool
            Whether the window was successfully shown.
        """
        return self._dispatch.ShowWindow()
        
    def minimize_window(self):
        """Collapses the application window to an icon."""
        self._dispatch.MinimizeWindow()
    
    def maximize_window(self):
        """Extends the application window to full screen."""
        self._dispatch.MaximizeWindow()
    
    def cascade(self):
        """Cascades all borehole document windows (unless tabbed)."""
        self._dispatch.Cascade()
    
    def tile_horizontally(self):
        """Arranges document windows horizontally (unless tabbed)."""
        self._dispatch.TileHorizontally()
    
    def tile_vertically(self):
        """Arranges document windows vertically (unless tabbed)."""
        self._dispatch.TileVertically()
    
    def new_borehole(self, template=None):
        """Creates a new borehole document object.

        The new borehole object is blank unless a template file is provided.
        
        Parameters
        ----------
        template : str, optional
            An optional path to a borehole document template (.wdt).
            If provided, the new borehole will be created using the
            template.
        
        Returns
        -------
        Borehole
            The new borehole document.
        """
        return Borehole(self._dispatch.NewBorehole(template))

        
    def open_borehole(self, path=None):
        """Opens a WellCAD borehole document file (.wcl file).
        
        Parameters
        ----------
        path : str, optional
            The file path to the WellCAD borehole document file to open. If no
            file path is provided, the user will be prompted to select a file
            using a standard File Open dialog box.
        
        Returns
        -------
        Borehole or None
            The opened borehole document, or ``None`` if opening the file
            failed.
        """
        return Borehole(self._dispatch.OpenBorehole(path))
        

    def get_borehole(self, index=None):
        """Gets an existing borehole document by index.
        
        Gets a borehole document object according to the zero-based index of
        the document open in WellCAD.
        
        Parameters
        ----------
        index : int, optional
            A zero based index of the borehole document. If no index is
            provided, the index of the most recently used document is used.
        
        Returns
        -------
        Borehole or None
            The borehole document object with the specified index, or ``None``
            if the index is out of bounds.
        """
        return Borehole(self._dispatch.GetBorehole(index))
        
        
    def get_active_borehole(self):
        """Gets the active borehole document (i.e. the one that currently has focus).
                   
        Returns
        -------
        Borehole or None
            The current active borehole document object, or ``None`` if no
            document has focus.
        """
        return Borehole(self._dispatch.GetActiveBorehole())
        
        
    def close_borehole(self, prompt_for_saving=None, index=None):
        """Closes a specific borehole document.
        
        The borehole document that is closed can be specified by an index,
        or, if none is provided, the most recently opened borehole document
        will be closed.
        
        Parameters
        ----------
        prompt_for_saving : bool, optional
            Whether or not to prompt the user to save the borehole document.
        index : int or str, optional
            The (zero-based) index of the document to close, or the document
            name. If not provided, the most recently opened document will be
            closed.
        """
        self._dispatch.CloseBorehole(prompt_for_saving, index)
    
    @property
    def nb_of_documents(self):
        """int: The number of borehole documents open in WellCAD."""
        return self._dispatch.NbOfDocuments
    
    def file_import(self,
                    file_name=None,
                    prompt_user=None,
                    config_file=None,
                    log_file=None):
        """Imports the specified file into a new borehole document.
        
        Allows import of TFD, LAS, DLIS, TXT, CSV and other file
        formats into WellCAD. Please refer to the WellCAD help
        file for a description of all import parameters to be used
        in the configuration file / parameter string. If filename
        is left blank the File Open dialog will be displayed. 

        Parameters
        ----------
        file_name : str, optional
            The path of the file to import.
        prompt_user : bool, optional
            Whether to display an import dialog box to allow the user
            to specify import settings.
        config_file : str, optional
            Path and filename of the configuration file or parameter string.
        log_file : str, optional
            Path and name of the file to log error messages.
        
        Returns
        -------
        Borehole
            A new borehole document containing the imported data.
        """
        return Borehole(self._dispatch.FileImport(file_name,
                                                  prompt_user,
                                                  config_file,
                                                  log_file))
        
    def multi_file_import(self,
                          file_name=None,
                          prompt_user=None,
                          config_file=None,
                          log_file=None):
        """Creates a single borehole document from all specified files.

        Allows import of multiple TFD, LAS, DLIS, TXT, CSV and other
        file formats into WellCAD. Imported data will be merged into
        the same document. Please refer to the WellCAD help file for
        a description of all import parameters to be used in the
        configuration file / parameter string. If filename is left
        blank the File Open dialog will be displayed.

        Parameters
        ----------
        file_name : str, optional
            A comma separated list of input files (path and file name). 
        prompt_user : bool, optional
            Boolean to display the import dialog boxes.
        config_file : str, optional
            Path and filename of the configuration file or parameter string.
        log_file : str, optional
            Path and name of the file to log error messages.
        
        Returns
        -------
        Borehole
            A newly created borehole document containing the data from the
            imported files.
        """
        return Borehole(self._dispatch.MultiFileImport(file_name,
                                                       prompt_user,
                                                       config_file,
                                                       log_file))       
    
    def quit(self, prompt_for_saving=None):
        """Closes all borehole documents and exits WellCAD.
        
        Parameters
        ----------
        prompt_for_saving : bool, optional
            Whether to display the Save As dialog box for unsaved documents.
            Default behaviour is to prompt the user.
        """
        self._dispatch.Quit(prompt_for_saving)