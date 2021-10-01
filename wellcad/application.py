from win32com.client import Dispatch
from .borehole import Borehole

class Application:

    def __init__(self):
        """Creates the WellCAD object. 
        
        Ensure WellCAD has been started at least once by an
        administrator in order to register it in the computer registry.
        """

        self.dispatch = Dispatch("WellCAD.Application")
		

    def show_window(self):
        """Displays the WellCAD workspace on screen."""
        self.dispatch.ShowWindow
		

    def minimize_window(self):
        """Collapses the application window to an icon."""
        self.dispatch.MinimizeWindow()
		
		
    def maximize_window(self):
        """Extends the application window to full screen."""
        self.dispatch.MaximizeWindow()
		
		
    def cascade(self):
        """Cascades all borehole document windows (unless tabbed)"""
        self.dispatch.Cascade()
		

    def tile_horizontally(self):
        """Arranges document windows horizontally (unless tabbed)"""
        self.dispatch.TileHorizontally()
		
	
    def tile_vertically(self):
        """Arranges document windows vertically (unless tabbed)"""
        self.dispatch.TileVertically()
		

    def new_borehole(self, template = ""):
        """Creates a borehole document object.
        
        Creates a new blank borehole document object unless the path
        to a WDT template file is provided.
        
        Arguments:
            template -- (Optional) String specifying the path to 
                        the template (.WDT). 
        
        Returns:
            Borehole document object.
        """

        self.dispatch._FlagAsMethod("NewBorehole")
        obBhole = self.dispatch.NewBorehole(template)
        return Borehole(obBhole)

        
    def open_borehole(self, path = ""):
        """Opens a WellCAD .WCL file.
        
        Creates a new borehole document object from a .WCL file. If
        the path is empty the File Open dialog box will be displayed.
        
        Arguments:
            path -- (Optional) String specifying the path to
                    the .WCL file. 
        
        Returns:
            Borehole document object.
        """

        self.dispatch._FlagAsMethod("OpenBorehole")
        obBhole = self.dispatch.OpenBorehole(path)
        return Borehole(obBhole)
        

    def get_borehole(self, index = -1):
        """Creates the object for an open borehole document.
        
        Creates a borehole document object according to the zero based
        index of the document open in WellCAD. If no parameter is
        provided the object of the last borehole document opened in
        WellCAD will be returned.
        
        Arguments:
           index -- Optional zero based index of the borehole document. 
        
        Returns:
           Borehole document object
        """

        if index == -1:
            index = self.dispatch.NbOfDocuments - 1
        self.dispatch._FlagAsMethod("GetBorehole")
        obBhole = self.dispatch.GetBorehole(index)
        return Borehole(obBhole)
        
        
    def get_active_borehole(self):
        """Creates an object of the active borehole document.
        
        Creates a borehole document object from the currently
        active borehole document (i.e. the one with the focus).
                   
        Returns:
            Borehole document object
        """

        obBhole = self.dispatch.GetActiveBorehole
        return Borehole(obBhole)
		
		
    def close_borehole(self, prompt_for_saving = True, index = -1):
        """Closes a specific borehole document.
        
        Closes the borehole document defined by the zero based index.
        If no index is specified the last opened borehole document will
        be closed. The SaveAs dialog box will be displayed if the
        prompt_for_saving isset to True (default). To close the borehole
        document without saving set the flag to False.
        
        Arguments:
            prompt_for_saving -- (Optional) Boolean.
            index -- (Optional) Zero based index of the document.
        """

        if index == -1:
            index = self.dispatch.NbOfDocuments - 1
        self.dispatch.CloseBorehole(prompt_for_saving, index)
		
		
    def get_borehole_count(self):
        """Returns the number of borehole documents open in WellCAD."""
        return self.dispatch.NbOfDocuments
		
	
    def file_import(self,
                    filename = "",
                    prompt_user = True,
                    config_file = "",
                    log_file = ""):
        """Imports the specified file and creates a borehole document.
        
        Allows import of TFD, LAS, DLIS, TXT, CSV and other file
        formats into WellCAD. Please refer to the WellCAD help
        file for a description of all import parameters to be used
        in the configuration file / parameter string. If filename
        is left blank the File Open dialog will be displayed. 

        Arguments:
           filename    -- (Optional) Path and name of the file to import.
           prompt_user -- (Optional) Boolean to display the import
                          dialog boxes.
           config_file -- (optional) Path and filename of the
                          configuration file or parameter string.
           log_file    -- (Optional) Path and name of the file to log
                          error messages.
        
        Returns:
           Borehole document object
        """

        self.dispatch._FlagAsMethod("FileImport")
        obBhole = self.dispatch.FileImport(filename,
                                           prompt_user,
                                           config_file,
                                           log_file)
        return Borehole(obBhole)
		
		
    def multi_file_import(self, filename = "",
                          prompt_user = True,
                          config_file = "",
                          log_file = ""):
        """Creates a single borehole document from all imported file.

        Allows import of multiple TFD, LAS, DLIS, TXT, CSV and other
        file formats into WellCAD. Imported data will be merged into
        the same document. Please refer to the WellCAD help file for
        a description of all import parameters to be used in the
        configuration file / parameter string. If filename is left
        blank the File Open dialog will be displayed.

        Arguments:
           filename    -- (Optional) Comma separated list of input
                          files (path and file name). 
           prompt_user -- (Optional) Boolean to display the import
                          dialog boxes.
           config_file -- (Optional) Path and filename of the
                          configuration file or parameter string.
           log_file    -- (Optional) Path and name of the file to log
                          error messages.
        
        Returns:
           Borehole document object.
        """

        self.dispatch._FlagAsMethod("MultiFileImport")
        obBhole = self.dispatch.MultiFileImport(filename,
                                                prompt_user,
                                                config_file,
                                                log_file)
        return Borehole(obBhole)
		
		
    def quit(self, prompt_for_saving = True):
        """Closes all borehole documents and exits WellCAD.
        
        When setting the prompt_for_saving parameter to True the SaveAs
        dialog box will be displayed for each document (default). If
        the prompt_for_saving parameter is set to False the borehole
        documents will be closed without saving.
        
        Arguments:
            prompt_for_saving -- Optional boolean to display the
                                 SaveAs dialog. 
        """

        self.dispatch.Quit(prompt_for_saving)