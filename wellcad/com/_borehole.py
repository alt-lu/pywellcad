from ._dispatch_wrapper import DispatchWrapper
from ._log import Log
from ._depth import Depth
from ._header import Header
from ._title import Title
from ._page import Page
from ._workspace import Workspace
from ._odbc import Odbc


class Borehole(DispatchWrapper):
    @property
    def name(self):
        """Returns the title of a borehole document."""
        return self._dispatch.Name


    @name.setter	
    def name(self, name):
        """Sets the title of a borehole document.
        
        Arguments:
            name -- String specifying the new name of the document.
        """

        self._dispatch.Name = name


    @property
    def version_major(self):
        """Returns the major version number of WellCAD."""
        return self._dispatch.VersionMajor		


    @property
    def version_minor(self):
        """Returns the major version number of WellCAD."""
        return self._dispatch.VersionMinor		


    @property
    def version_build(self):
        """Returns the build number of WellCAD."""
        return self._dispatch.VersionBuild


    @property
    def auto_update(self):
        """Returns True if the auto update of the document is enabled."""
        return self._dispatch.AutoUpdate


    @auto_update.setter	
    def auto_update(self, flag):
        """Sets the auto update status of the borehole document.
        
        Arguments:
            flag -- set to True to enable the auto update or tp False
                    to disable the automatic refresh.

        """

        self._dispatch.AutoUpdate = flag


    def refresh_window(self):
        """Performs a one time refresh of the borehole view"""
        self._dispatch.RefreshWindow()


    def set_draft_mode(self, display_mode = 0):
        """Toggles the view of the borehole document.
        
        A borehole document can be displayed in the following modes:
        0 - Page Layout
        1 - Draft and fit
        2 - Draft

        Arguments:
            display_mode -- Integer specifying the document viewing mode
        """

        self._dispatch.SetDraftMode(display_mode)


    def minimize_document_window(self):
        """Shrinks the document window to an icon.
        
        Works only if document windows are not tabbed.
        """

        self._dispatch.MinimizeWindow()

    
    def maximize_document_window(self):
        """Enlarges the document window to fit the WellCAD frame.
        
        Works only if document windows are not tabbed.
        """

        self._dispatch.MaximizeWindow()
        
    @property
    def bottom_depth(self):
        """Returns the bottom of the document in actual depth units."""
        return self._dispatch.BottomDepth

    @property
    def top_depth(self):
        """Returns the top of the document in actual depth units."""
        return self._dispatch.TopDepth


    def set_visible_depth_range(self, top_depth, bottom_depth):	
        """Adjusts the depth range displayed in a borehole view.
        
        Arguments:
            top_depth -- Depth at which the data display should start.
            bottom_depth -- Depth at which the data display terminates.
        """

        self._dispatch.SetVisibleDepthRange(top_depth, bottom_depth)


    def get_depth(self):
        """Returns a depth object for the master depth axis."""
        obdepth = self._dispatch.Depth
        return Depth(obdepth)
        
        
    def get_header(self):
        """Header object for the entire borehole document header."""
        obheader = self._dispatch.Header
        return Header(obheader)


    def get_page(self):
        """Returns a page object for the borehole document."""
        obpage = self._dispatch.Page
        return Page(obpage)


    def create_new_workspace(self, workspace_type, config=""):
        """Creates a new workspace and return the corresponding object.

        For a full description of the parameters to be used in the
        configuration file refer to the WellCAD help documentation.

        Arguments:
            workspace_type -- 1 = ISI workspace
                              2 = Casing integrity
                              3 = NMR
        
            config -- Path and name of the .ini file containing the
                      workspace initialization parameters.
        """

        self._dispatch._FlagAsMethod("CreateNewWorkspace")
        obworkspace = self._dispatch.CreateNewWorkspace(workspace_type, config)
        return Workspace(obworkspace)


    def get_workspace(self,workspace_id):
        """Retrieve an object for a workspace in the document.
        
        Arguments: 
            workspace_id --- Zero based index or title of the workspace
                             present in the borehole document.
        """

        self._dispatch._FlagAsMethod("CreateNewWorkspace")
        obworkspace = self._dispatch.Workspace(workspace_id)
        return Workspace(obworkspace)


    def get_odbc(self):
        """Returns an object to access the ODBC module."""
        obj_odbc = self._dispatch.ODBC
        return Odbc(obj_odbc) 


    def connect_to(self, server_name, server_address, port_number="1600"):
        """Connect WellCAD to the ALT logging system.
        
        Arguments:
            server_name -- Must be set to 'TFD'.
            server_address -- IP address of the computer to connect to.
            port_number -- Part number used (default is 1600).
        
        """

        self._dispatch.ConnectTo (server_name, server_address, port_number)


    def disconnect_from(self, server_name, server_address):
        """Cuts the connection between WellCAD and the logging system.
        
        Arguments:
            server_name -- Must be set to 'TFD'.
            server_address -- IP address of the computer to connect to.
        """

        self._dispatch.DisconnectFrom (server_name, server_address)
        

    def save_as(self, file_name):
        """Saves the borehole document as WCL file.
        
        Arguments:
            file_name -- Path and file name (e.g. C:\Temp\Well1.wcl)

        Returns:
            True if the saving process was successfull. 
        """

        return self._dispatch.SaveAs(file_name)


    def file_export(self, 
                    file_name,
                    prompt_user=True,
                    config="",
                    logfile=""):
        """Exports the document to the specified file.
        
        Supported file formats are LAS, DLIS, EMF, CGM, JPG, PNG, TIF,
        BMP, WCL and PDF. Please refer to the WellCAD help file for a
        desciption of the export parameters to be used in the
        configuration file and parameter string.

        Arguments:
            file_name -- Path and name of the file to export.
            prompt_user -- If set to False no dialog box will be
                           displayed.
            config -- Path and name of the .ini file containing the
                      export parameters.
            logfile -- Path and name of the file to log error messages.
            
        """
        self._dispatch.FileExport(file_name,
                                 prompt_user,
                                 config,
                                 logfile)


    def print(self,
              enable_dialog,
              top_depth,
              bottom_depth,
              nb_of_copies):
        """Sends the current document to the printer.

        If the print dialog box is displayed the user can select the
        printer otherwise the printer installed as default is used.
        
        Arguments:
            enable_dialog -- Displays the print dialog box if True.
            top_depth -- Start depth of the interval to print.
            bottom_depth -- Base of the printed depth interval.
            nb_of_copies -- Defines the number of copies to be printed.
        """

        self._dispatch.DoPrint(self,
                             enable_dialog,
                             top_depth,
                             bottom_depth,
                             nb_of_copies)


# Methods for general log handling

    @property
    def nb_of_logs(self):
        """Number of logs present in the borehole document."""
        return self._dispatch.NbOfLogs

    
    def get_log(self, log):
        """Accesses and existing log and reates a new log object.
        
        Arguments:
            log -- The zero based index (integer) 
                   or the title (string) of the log.

        Returns:
            A log object.
        """

        self._dispatch._FlagAsMethod("Log")
        obLog = self._dispatch.Log(log)
        return Log(obLog)


    def get_title(self, log_name):
        """Returns an object for the tile of a log.

        Arguments:
            log_name -- Title of the log as shown in the propeties.

        """

        self._dispatch._FlagAsMethod("Title")
        obTitle = self._dispatch.Title(log_name)
        return Title(obTitle)


    def new_log(self, log_type):
        """Creates a new log and log object.
        
        The log type that will be created depends on the
        log_type parameter which can take the following values:
        1 - Well Log
        2 - Formula Log
        3 - Mud Log
        4 - FWS Log
        5 - Image Log
        6 - Structure Log
        7 - Litho Log
        8 - Comment Log
        9 - Engineering Log
        10 - RGB Log
        13 - Interval Log
        14 - Analysis Log
        15 - Percent Log
        16 - CoreDesc Log
        17 - Depth Log
        18 - Strata Log
        19 - Satcking Pattern Log
        20 - Polar and Rose Log
        21 - Cross Section Log
        22 - OLE Log
        23 - Shading Log
        24 - Marker Log
        25 - Breakout Log
        26 - Bio Log
        
        Arguments:
            log_type -- Integer specifying the type of log. 

        Returns:
            A log object.
        """

        obLog = self._dispatch.InsertNewLog(log_type)
        return Log(obLog)


    def convert_log_to(self,
                       log,
                       log_type,
                       prompt_user = True,
                       config = ""):
        """New log object by converting one log type into another.
        
        Please refer to the WellCAD documentation about which log type
        conversions are possible. Dialog boxes will be displayed if
        available when the bPromptUser flag is set to True. If set to
        False default parameters will be used or the conversion
        parameters will be taken from a configuration file or parameter
        string. The Automation Module chapter of the WellCAD help file
        provides a description of the file format and all parameters to
        be used in the configuration file / parameter string. 

        Arguments:
            log 		-- Title (string) or zero based index (Integer)
                              of the log to convert.
            log_type 	-- Integer specifying the type of log to be created.
            prompt_user -- (Optional) If set to True dialog boxes
                           will be displayed.
            config		-- (Optional) Path and filename of the
                           configuration file or parameter string.  

        Returns:
            The object of the new log.
        """
        
        self._dispatch._FlagAsMethod("ConvertLogTo")
        obLog = self._dispatch.ConvertLogTo(log, log_type, prompt_user, config)
        return Log(obLog)


    def copy_log(self, oblog):
        """Copy and pastes a log.
        
        Copies a log within the same or between two borehole documents.

        Arguments:
            oblog -- An object of the log to copy.

        Returns:
            An object of the copied log.
        """

        self._dispatch._FlagAsMethod("AddLog")
        oblog_copy = self._dispatch.AddLog(oblog.dispatch)
        return Log(oblog_copy)


    def remove_log(self, log):
        """Deletes the specified log from the borehole document.
        
        Arguments:
            log -- Zero based index (integer) or title (string)
                   of the log to delete.
        """

        self._dispatch.RemoveLog(log)


    def clear_log_contents(self, log):
        """Removes the data from a log and leaves the log empty.
        
        Arguments:
            log -- Zero based index (integer) or title (string).
        """

        self._dispatch.ClearLogContents(log)


    def apply_template(self,
                       path,
                       prompt_if_not_found = True,
                       create_new_logs = False,
                       create_new_layers = False,
                       apply_annotation_settings = False,
                       replace_header = False,
                       keep_charts = True,
                       new_charts = False,
                       overwrite_workspaces = False,
                       new_workspaces = False,
                       config = ""):
        """Loads and applies a document layout template (.WDT)

        For a more detailed description of all available parameters
        in the configuration file refer to the WellCAD help file.
        
        Arguments:
            path -- Path and name of the .WDT file.
            prompt_if_not_found -- If True a dialog box will be
                                  displayed for each log not found.
            create_new_layers -- If True new annotation layers will be
                                 loaded from the template.
            apply_annotation_settings -- Loads the layout settings for
                                         operational symbols.
            replace_header -- If True the current document header will
                              be replaced.
            keep_charts -- If True cross-plot charts will be kept in
                           the document.
            new_charts -- If True cross-plot charts will be loaded from
                          the template.
            overwrite_workspaces -- If True work spaces in the document
                                    will be overwritten.
            new_workspaces -- If True work spaces will be loaded from
                              the template.
            config -- Path and name of the configuraion file
                      or parameter string.
        """

        self._dispatch.ApplyTemplate(path,
                                    prompt_if_not_found,
                                    create_new_logs,
                                    create_new_layers,
                                    apply_annotation_settings,
                                    replace_header,
                                    keep_charts,
                                    new_charts,
                                    overwrite_workspaces,
                                    new_workspaces,
                                    config)


# Common log edition

    def slice_log(self,
                  log,
                  slice_depth,
                  create_top = True,
                  create_bottom = True,
                  keep_original = True):
        """Cuts the specified log at the given depth.

        Arguments:
            log -- Zero based index (integer) or title (string) of the
                   log to slice.
            slice_depth -- Depth at which the cut will be made.
            create_top -- If set to True the upper part of the log will
                          be kept in the document. 
            create_bottom -- If set to True the lower part of the log
                             will remain in the document.
            keep_original -- If set to True the original log will
                             remain in the document.
        """

        self._dispatch.SliceLog(log,
                               slice_depth,
                               create_top,
                               create_bottom,
                               keep_original)


    def merge_logs(self,
                   log_a,
                   log_b,
                   ave_overlap = True,
                   create_new = True):
        """Merges two logs of the same type.

        Arguments:
            log_a -- Zero based index (integer) or title (string) of
                     the log.
            log_b -- Zero based index (integer) or title (string) of
                     the log.
            ave_overlap -- If set to False log_a will overwrite log_b.
            create_new -- If set to False log_b will be pushed
                          into log_a.
        """

        self._dispatch.MergeLogs(log_a, log_b, ave_overlap, create_new)


    def merge_same_log_items(self, log):
        """Merges data intervals with same litho codes or text.
        
        Arguments:
            log -- Zero based index (integer) or title (string) of
                   the Litho log.
        """

        self._dispatch.MergeSameLogItems(log)


    def extend_log(self, log, top_depth, bottom_depth):
        """Extends the depth range of a Well log type.
        
        Call this method to allocate the memory for the additional
        depth range of the Well Log.

        Arguments:
            log -- Zero based index (integer) or title (string) of
                   the Well log.
            top_depth -- Top of the final depth range.
            bottom_depth -- Base of the final depth range.
        """

        self._dispatch.ExtendLog(log, top_depth, bottom_depth)


    def depth_shift_log(self,
                        log,
                        shift,
                        top_depth="",
                        bottom_depth=""):
        """Performs a bulk shift to all the log's data.

        If top_depth and bottom_depth are specified the depth shift
        will be restricted to this interval.

        Arguments:
            log -- Zero based index (integer) or title (string) of
                   the log.
            shift -- Amount of the depth shift (positive = down,
                     negative = up).
            top_depth -- Upper depth limit of the shifted interval.
            bottom_depth -- Lower depth limit of the shifted interval.
        """

        self._dispatch.DepthShiftLog(log,
                                    shift,
                                    top_depth,
                                    bottom_depth)


    def depth_match_log(self, log="", depth_log=""):
        """Perfoms a depth matching using a shift table.

        The shift table will be provided as a Depth Log and the process
        of shifting is equivalent to the DepthMatcher in WellCAD. If
        the parameter list is empty or if no depth_log has been
        specified the DepthMatcher dialog box will be displayed.

        Arguments:
            log -- Zero based index (integer) or title (string) of
                   the log to match.
            depth_log -- Zero based index (integer) or title (string) of
                   the Depth Log containing the shift table.
        
        """
        
        self._dispatch.DepthMatchLog(log, depth_log)


    def fill_log(self,
                 log,
                 top_depth,
                 bottom_depth,
                 step,
                 thickness,
                 user_defined_intervals=True,
                 interval_log=""):
        """Creates intervals in Cross-section and Polar & Rose logs.
        
        Arguments:
            log -- Zero based index (integer) or title (string) of
                   the log to fill with intervals.
            top_depth -- Start depth of the first interval.
            bottom_depth -- Start depth of the last interval.
            step -- Interval frequency (enter 5 for an interval
                    starting every 5 meter or ft).
            thickness -- Interval thickness (in depth units).
            user_defined_intervals = If set to False the intervals
                                     will be loaded from a reference
                                     log.
            interval_log -- Zero based index (integer) or title
                            (string) of the log containing the
                            reference intervals.
        """

        self._dispatch.FillLog(log,
                              top_depth,
                              bottom_depth,
                              step,
                              thickness,
                              user_defined_intervals,
                              interval_log)


# Common log processes

    def filter_log(self, log, prompt_user=True, config=""):
        """Applies a user selected filter to Well Logs.

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 
        
        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        Returns:
            An object of the filtered log.
        """

        self._dispatch._FlagAsMethod("FilterLog")
        oblog = self._dispatch.FilterLog(log, prompt_user, config)
        return Log(oblog)


    def filter_log_average(self, log, filter_width, circular_data = False, data_unit = "degrees"):
        """Applies an average filter to a well log.
            
        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            filter_width -- Interger defining the length of the filter
                            window in samples.
            circular_data -- Boolean defining whether the log contain angular data.
            data_unit -- Either 'degrees' or 'radians'. 

        Returns:
            An object of the filtered log.
        """

        # compose in-line parameter string
        circular_data_flag = "no"
        if circular_data:
            circular_data_flag = "yes"
        config = "FilterType=MovingAverage, MaxDepthRange=yes,\
                  FilterWidth="+str(max(1,filter_width))\
                  +",CircularData="+circular_data_flag\
                  +",DataUnit="+data_unit
        # call method
        self._dispatch._FlagAsMethod("FilterLog")
        oblog = self._dispatch.FilterLog(log, False, config)
        return Log(oblog)


    def filter_log_median(self, log, filter_width, circular_data = False, data_unit = "degrees"):
        """Applies a median filter to a well log.
            
        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            filter_width -- Interger defining the length of the filter
                            window in samples.
            circular_data -- True if the log contains angular data
                             (default = False).
            data_unit -- Either 'degrees' or 'radians'
                         (default = 'degrees'). 

        Returns:
            An object of the filtered log.
        """

        # compose in-line parameter string
        circular_data_flag = "no"
        if circular_data:
            circular_data_flag = "yes"
        config = "FilterType=Median, MaxDepthRange=yes,\
                  FilterWidth="+str(max(1,filter_width))\
                  +",CircularData="+circular_data_flag\
                  +",DataUnit="+data_unit
        # call method
        self._dispatch._FlagAsMethod("FilterLog")
        oblog = self._dispatch.FilterLog(log, False, config)
        return Log(oblog)


    def filter_log_weighted_ave(self, log, filter_width, circular_data = False, data_unit = "degrees"):
        """Applies a weighted average filter to a well log.
            
        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            filter_width -- Interger defining the length of the filter
                            window in samples.
            circular_data -- True if the log contains angular data
                             (default = False).
            data_unit -- Either 'degrees' or 'radians'
                         (default = 'degrees'). 

        Returns:
            An object of the filtered log.
        """

        # compose in-line parameter string
        circular_data_flag = "no"
        if circular_data:
            circular_data_flag = "yes"
        config = "FilterType=WeightedAverage, MaxDepthRange=yes,\
                  FilterWidth="+str(max(1,filter_width))\
                  +",CircularData="+circular_data_flag\
                  +",DataUnit="+data_unit
        # call method
        self._dispatch._FlagAsMethod("FilterLog")
        oblog = self._dispatch.FilterLog(log, False, config)
        return Log(oblog)


    def block_log(self, log, prompt_user=True, config=""):
        """Calculates statistics for log data per depth interval.
        
        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """
        self._dispatch.BlockLog(log, prompt_user, config)


    def multi_log_statistics(self, logs, prompt_user=True, config=""):
        """Calculates statistical values from multiple logs.
        
        Statistical values are derived from multiple logs at the
        same depth.
        E.g. an avege density from two density logs.
        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation.

        Arguments:
            logs -- Title (string) or list of the log(s) to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.
        """

        self._dispatch.ExtractWellLogStatistics(logs, prompt_user, config)


    def normalize_perc_log(self, log, prompt_user=True, config=""):
        """Normalizes the data in a Percentage or Analysis Log.

        For a full list of prcessing parameters please refer to the
        WellCAD help documentation.

        Arguments:
            log -- Zero based index (integer) or title (string) of
                   the log to normalize.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.
        
        """

        self._dispatch.Normalize(log, prompt_user, config)


    def resample_log(self, log, prompt_user=True, config=""):
        """Resamples a data set using the new sample step provided.
        
        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """

        self._dispatch._FlagAsMethod("ResampleLog")
        oblog = self._dispatch.ResampleLog(log, prompt_user, config)
        return Log(oblog)


    def interpolate_log(self, log, prompt_user=True, config=""):
        """Applies a linear interpolation across gaps in a data set.
        
        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        Returns:
            An object of the interpolated log.
        """

        self._dispatch._FlagAsMethod("InterpolateLog")
        oblog = self._dispatch.InterpolateLog(log, prompt_user, config)
        return Log(oblog)


    def borehole_deviation(self, prompt_user=True, config=""):
        """Computes Azimuth, Tilt and RBR.
        
        The method uses accelerometer and inclinometer x,y,z components
        of an orientation sensor to compute borhole azimuth, tilt and
        relative bearing (RBR). The input logs are specified int the
        config file or in-line as part of the config string.
        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """
        
        self._dispatch.CalculateBoreholeDeviation(prompt_user, config)


    def borehole_coordinates(self, prompt_user=True, config=""):
        """Creates Northing, Easting and TVD data.
        
        Using borehole azimuth and tilt as input data this method
        calculates northing, easting and tvd coordinates and outputs
        them in well / mud logs.
        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation.

        Arguments:
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """

        self._dispatch.CalculateBoreholeCoordinates(prompt_user, config)


    def borehole_closure(self, prompt_user=True, config=""):
        """Derives closure distance, closure angle and dog-leg data.
        
        Using borehole azimuth, tilt, northing and easting as input
        data this method calculates the drift distance (closure), 
        drift angle (cllosure angle) and the dog-leg-severity and
        outputs the data in well / mud logs.
        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation.

        Arguments:
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """

        self._dispatch.CalculateBoreholeClosure(prompt_user, config)


    def elog_correction(self, prompt_user=True, config=""):
        """ Environmental corrections for normal resisitivity data.
        
        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation.

        Arguments:
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        Returns:
            An object of the last corrected log.
        """

        self._dispatch._FlagAsMethod("ElogCorrection")
        oblog = self._dispatch.ElogCorrection(prompt_user, config)
        return Log(oblog)


# Image & Structure logs processes
    
    def correct_image_traces(self, log):
        """ Replaces NoData traces in an image log.

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.

        """

        self._dispatch.CorrectBadTraces(log)

    
    def conditional_testing(self, log_if, log_then, prompt_user=True, config=""):
        """Applies If-Then-Else testing to image logs.

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation.

        Arguments:
            log_if -- Zero based index (integer) or title (string) of
                         the log used for the If clause.
            log_then -- Zero based index (integer) or title (string) of
                         the log used for the Then clause.		 
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """
        self._dispatch._FlagAsMethod("ApplyConditionalTesting")
        oblog = self._dispatch.ApplyConditionalTesting(log_if, log_then, prompt_user, config)
        return Log(oblog)


    def filter_image(self, log, prompt_user=True, config=""):
        """Average, median and clipping filter for image logs

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        Returns:
            An object of the filtered image log.

        """
        self._dispatch._FlagAsMethod("FilterImageLog")
        oblog = self._dispatch.FilterImageLog(log, prompt_user, config)
        return Log(oblog)


    def mirror_image(self, log):
        """Flips an image at the 180° position

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.

        """

        self._dispatch._FlagAsMethod("MirrorImage")
        self._dispatch.MirrorImage(log)


    def rotate_image(self, log, prompt_user=True, config=""):
        """Rotates an image log by a fixed or log value.

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.
        
        """

        self._dispatch.RotateImage(log, prompt_user, config)


    def orient_image_highside(self, log, prompt_user=True, config=""):
        """Rotates an image to the inverse direction of gravity.

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """
        self._dispatch.OrientImageToHighside(log, prompt_user, config)


    def orient_image_north(self, log, prompt_user=True, config=""):
        """Rotates an image to mag north.

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """

        self._dispatch.OrientImageToNorth(log, prompt_user, config)


    def image_statistics(self, log, prompt_user=True, config=""):
        """Extracts statistics across single or multiple image logs

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """
        self._dispatch.ExtractImageLogStatistics(log, prompt_user, config)

    
    def normalize_image(self, log, prompt_user=True, config=""):
        """Applies Static or Dynamic normalization to image logs

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        Returns:
            A log object of the normalized image.

        """

        self._dispatch._FlagAsMethod("NormalizeImage")
        oblog = self._dispatch.NormalizeImage(log, prompt_user, config)
        return Log(oblog)


    def image_dispatchplexity_map(self, log, prompt_user=True, config=""):
        """Computes the complexity map from an RGB or image log
  
        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        Returns:
            A log object of the complexity log.

        """

        self._dispatch._FlagAsMethod("ImageComplexityMap")
        oblog = self._dispatch.ImageComplexityMap(log, prompt_user, config)
        return Log(oblog)


    def fluid_velocity(self, log, prompt_user=True, config=""):
        """Estimates the fluid velocity from ATV travel time data

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        Returns:
            A log object of the velocity log.

        """
        self._dispatch._FlagAsMethod("CalculateFluidVelocity")
        oblog = self._dispatch.CalculateFluidVelocity(log, prompt_user, config)
        return Log(oblog)

    
    def acoustic_caliper(self, log, prompt_user=True, config=""):
        """Computes the borehole cdiameter from ATV travel time data

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """

        self._dispatch.CalculateAcousticCaliper(log, prompt_user=True, config="")


    def apparent_to_true(self, log, prompt_user=True, config=""):
        """Corrects apparent structure picks for borehole deviation

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        Returns:
            A log object of the corrected log.

        """

        self._dispatch._FlagAsMethod("ApplyStructureApparentToTrueCorrection")
        oblog = self._dispatch.ApplyStructureApparentToTrueCorrection(log, prompt_user, config)
        return Log(oblog)


    def true_to_apparent(self, log, prompt_user=True, config=""):
        """Returns true structure picks to apparent ones

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        Returns:
            A log object of the apparent picks.

        """

        self._dispatch._FlagAsMethod("ApplyStructureTrueToApparentCorrection")
        oblog = self._dispatch.ApplyStructureTrueToApparentCorrection(log, prompt_user, config)
        return Log(oblog)


    def recalculate_structure_azimuth(self, log, prompt_user=True, config=""):
        """Applies a rotation to the dip direction of structure picks

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """

        self._dispatch.RecalculateStructureAzimuth(log, prompt_user, config)


    def recalculate_structure_dip(self, log, prompt_user=True, config=""):
        """Corrects dip angles for caliper variations

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """
        
        self._dispatch.RecalculateStructureDip(log, prompt_user, config)


    def remove_structure_dip(self,log, prompt_user=True, config=""):
        """Conducts a residual dip analysis

        Removes a given regional dip and azimuth from the data in a
        structure log and recalculates new Dip and Azimuth angles.

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.
        
        Returns:
            A log object for the new structure picks.

        """

        self._dispatch._FlagAsMethod("RemoveStructuralDip")
        oblog = self._dispatch.RemoveStructuralDip(log, prompt_user, config)
        return Log(oblog)


    def color_dispatchponents(self, log, method=0, model=0, prompt_user=False):
        """Extracts color data like red, green and blue intensities

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            method -- 0 (Average), 1 (Mode), 2 (Image Log)
            model -- 0 (RGB), 1 (HSV), 2(YUV), 3 (CIELAB)
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """

        self._dispatch.ExtractColorComponents(log, method, model, prompt_user)


    def color_classification(self, log, prompt_user=True, config=""):
        """Performs a classification of color values in an RGB log

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        Returns:
            Object of the resulting Analysis log or RGB log

        """

        self._dispatch._FlagAsMethod("ColorClassification")
        oblog = self._dispatch.ColorClassification (log, prompt_user, config)
        return Log(oblog)


    def brightness_and_contrast(self, log, prompt_user=True):
        """Adjusts the brightness and contrast in RGB logs

        A full description of the method is given in the Automation
        Module chapter of the WellCAD help documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.

        """

        self._dispatch.AdjustImageBrightnessAndContrast(log, prompt_user)

    
    def structure_statistics(self, log, prompt_user=True, config=""):
        """Performs interval based statistics of Structure logs

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """

        self._dispatch._FlagAsMethod("ExtractStructureIntervalStatistic")
        oblog = self._dispatch.ExtractStructureIntervalStatistic(log, prompt_user, config)
        return Log(oblog)
    

    def rqd(self, log, prompt_user=True, config=""):
        """Rock quality designation based on Structure logs

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """

        self._dispatch._FlagAsMethod("RQD")
        oblog = self._dispatch.RQD(log, prompt_user, config)
        return Log(oblog)


    def representative_picks(self, log, prompt_user=True, config=""):
        """Determines the representative pick from pick clusters

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """

        self._dispatch._FlagAsMethod("RepresentativePicks")
        oblog = self._dispatch.RepresentativePicks(log, prompt_user, config)
        return Log(oblog)


# Cased hole processes

    def dead_sensor_correction(self, log, prompt_user=True, config=""):
        """Corrects errorneous data columns in Image logs

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """
        self._dispatch.CorrectDeadSensor(log, prompt_user, config)

    
    def shift_correction(self, log, prompt_user=True, config=""):
        """Corrects the drift of data (e.g. MFC) in Image logs
        
        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """
        self._dispatch._FlagAsMethod("ShiftCorrection")
        oblog = self._dispatch.ShiftCorrection(log, prompt_user, config)
        return Log(oblog)

    
    def fluid_velocity(self, log, prompt_user=True, config=""):
        """Estimates the borehole fluid velocity from ATV travel times
        
        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """
        self._dispatch._FlagAsMethod("CalculateFluidVelocity")
        oblog = self._dispatch.CalculateFluidVelocity(log, prompt_user, config)
        return Log(oblog)


    def centralize(self, log, prompt_user=True, config=""):
        """Removes tool decentralization effects from ATV travel times 

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """
        self._dispatch._FlagAsMethod("Centralize")
        oblog = self._dispatch.Centralize(log, prompt_user, config)
        return Log(oblog)


    def acoustic_caliper(self, log, prompt_user=True, config=""):
        """Computes borehole diameter and radius from ATV travel times
        
        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """

        self._dispatch.CalculateAcousticCaliper(log, prompt_user, config)

    
    def casing_thickness(self, log, prompt_user=True, config=""):
        """Computes the thickness of a casing based on ATV travel times

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.
        
        """
        self._dispatch.CalculateCasingThickness(log, prompt_user, config)


    def metal_loss(self, log, prompt_user=True, config=""):
        """Metal loss computation from inner radius data of a pipe 

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.
        
        """

        self._dispatch._FlagAsMethod("CalculateApparentMetalLoss")
        oblog = self._dispatch.CalculateApparentMetalLoss(log, prompt_user, config)
        return Log(oblog)


    def radius_to_from_diameter(self, log, prompt_user=True, config=""):
        """Converts Image log data between radius and diameter

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """

        self._dispatch._FlagAsMethod("RadiusToFromDiameter")
        oblog = self._dispatch.RadiusToFromDiameter(log, prompt_user, config)
        return Log(oblog)


    def radius_to_diameter(self, log):
        """Converts radius data in an Image log to diameter values
    
        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the Image log to process.
        
        """
        prompt_user=False
        config="Method=TwoTimesRadius"
        self._dispatch._FlagAsMethod("RadiusToFromDiameter")
        oblog = self._dispatch.RadiusToFromDiameter(log, prompt_user, config)
        return Log(oblog)


    def diameter_to_radius(self, log):
        """Converts diameter data in an Image log to radius values

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the Image log to process.

        """
        prompt_user=False
        config="Method=HalfDiameter"
        self._dispatch._FlagAsMethod("RadiusToFromDiameter")
        oblog = self._dispatch.RadiusToFromDiameter(log, prompt_user, config)
        return Log(oblog)


    def outer_inner_radius_diameter(self, log, prompt_user=True, config=""):
        """Adds or subtracts thickness from inner radius or diameter data

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """
        self._dispatch._FlagAsMethod("OuterInnerRadiusDiameter")
        oblog = self._dispatch.OuterInnerRadiusDiameter(log, prompt_user, config)
        return Log(oblog)


    def casing_normalization(self, log, prompt_user=True, config=""):
        """Subtracts a trace average (or other) value from an Image log

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """

        self._dispatch._FlagAsMethod("CasedHoleNormalization")
        oblog = self._dispatch.CasedHoleNormalization(log, prompt_user, config)
        return Log(oblog)


# FWS processes

    def correct_fws_traces(self, log):
        """Replaces NO DATA traces in a FWS log
        
        Arguments:
            log -- Zero based index (integer) or title (string) of
                   the log to process.

        """

        self._dispatch.CorrectBadTraces(log)


    def stack_fws_traces(self, log, prompt_user=True, config=""):
        """Stacks multiple FWS traces to create and average trace

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """

        self._dispatch._FlagAsMethod("StackTraces")
        oblog = self._dispatch.StackTraces(False, log, prompt_user, config)
        return Log(oblog)


    def reverse_fws_amplitude(self, log):
        """Inverts the amplitudes in a FWS log

        Arguments:
            log -- Zero based index (integer) or title (string) of
                   the log to process.

        """

        self._dispatch.ReverseAmplitude(log)


    def filter_fws(self, log, prompt_user=True, config=""):
        """Average, weighted average and frequency filter for FWS logs

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        Returns:
            Object of the filtered FWS log.

        """

        self._dispatch._FlagAsMethod("FilterFWSLog")
        oblog = self._dispatch.FilterFWSLog(log, prompt_user, config)
        return Log(oblog)


    def filter_fws_average(self, log, filter_width):
        """Applies a moving average filter to the traces of an FWS log

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            filter_width -- Length of the filter window in us.
        
        Returns:
            Object of the filtered FWS log.
            
        """

        config = "FilterType=MovingAverage, FilterWidth="+str(max(1,filter_width))
        self._dispatch._FlagAsMethod("FilterFWSLog")
        oblog = self._dispatch.FilterFWSLog(log, False, config)
        return Log(oblog)


    def filter_fws_weighted(self, log, filter_width):
        """Applies a weighted average filter to the traces of an FWS log

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            filter_width -- Length of the filter window in us.

        Returns:
            Object of the filtered FWS log.
        
        """

        config = "FilterType=WeightedAverage , FilterWidth="+str(max(1,filter_width))
        self._dispatch._FlagAsMethod("FilterFWSLog")
        oblog = self._dispatch.FilterFWSLog(log, False, config)
        return Log(oblog)	


    def filter_fws_frequency(self, log, low_pass, low_cut, high_pass, high_cut):
        """Applies a frequency filter to the traces of an FWS log

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            low_pass -- Low pass frequency of filter in kHz.
            low_cut -- Low cut-off frequency of filter in kHz.
            high_pass -- High pass frequency of filter in kHz.
            high_cut -- High cut-off frequency of filter in kHz.

        Returns:
            Object of the filtered FWS log.

        """

        config = "FilterType=Frequency,\
                 LowCut="+str(min(low_cut,low_pass))\
                 + ",LowPass="+str(max(low_cut,low_pass))\
                 + ",HighPass="+str(min(high_cut,high_pass))\
                 + ",HighCut="+str(max(high_cut,high_pass))	 
        self._dispatch._FlagAsMethod("FilterFWSLog")
        oblog = self._dispatch.FilterFWSLog(log, False, config)
        return Log(oblog)


    def correct_standoff(self, log, prompt_user=True, config=""):
        """Corrects intercept times for the stand-off of tool and formation
        
        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        Return:
            Object of the resulting log

        """

        self._dispatch._FlagAsMethod("ApplyStandOffCorrection")
        oblog = self._dispatch.ApplyStandOffCorrection(log, prompt_user, config)
        return Log(oblog)


    def compensated_velocity(self, log, prompt_user=True, config=""):
        """Slowness or velocity computed from two receiver arrival times

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """

        self._dispatch._FlagAsMethod("CompensatedVelocity")
        oblog = self._dispatch.CompensatedVelocity(log, prompt_user, config)
        return Log(oblog)


    def semblance_processing(self, prompt_user=True, config=""):
        """Performs a vlocity analysis for the multiple receivers
        
        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.
        
        Returns:
            Object of the resulting depth-slowness-semblance log

        """

        self._dispatch._FlagAsMethod("ApplySemblanceProcessing")
        oblog = self._dispatch.ApplySemblanceProcessing(prompt_user, config)
        return Log(oblog)


    def reflected_tubewave(self, log, prompt_user=True, config=""):
        """Extracts the cumulative energy from reflected tube waves

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        Returns:
            Object of the log containing the cumulative energy.

        """
        self._dispatch._FlagAsMethod("ProcessReflectedTubeWave")
        oblog = self._dispatch.ProcessReflectedTubeWave(log, prompt_user, config)
        return Log(oblog)


    def first_arrival(self, log, prompt_user=True, config=""):
        """Picks the intercept time of the first arrival

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.
        
        Returns:
            Object of the log containing the first arrival times.

        """

        self._dispatch._FlagAsMethod("PickFirstArrival")
        oblog = self._dispatch.PickFirstArrival(log, prompt_user, config)
        return Log(oblog)


    def cement_bond(self, log, prompt_user=True, config=""):
        """Determines the cement bond from first arrival amplitudes

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """

        self._dispatch.CementBond(log, prompt_user, config)
    

    def e1_arrival(self, log, prompt_user=True, config=""):
        """Determines the arrival time of the E1 amplitude 

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        Returns:
            Object of the log containing the E1 arrival times

        """

        self._dispatch._FlagAsMethod("PickE1Arrival")
        oblog = self._dispatch.PickE1Arrival(log, prompt_user, config)
        return Log(oblog)

    
    def e1_amplitude(self, fws_log, arrival_log, prompt_user=True):
        """Uses the E1 arrival time to extract the E1 amplitude

        A full description of the method is given in the Automation
        Module chapter of the WellCAD help documentation. 

        Arguments:
            fws_log	-- Zero based index (integer) or title (string) of
                          the log to process.
            arrival_log -- Index or title of the E1 arrival time log
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
        
        Returns:
            Object of the log containing the E1 amplitude.

        """

        self._dispatch._FlagAsMethod("ExtractE1Amplitude")
        oblog = self._dispatch.ExtractE1Amplitude(fws_log, arrival_log, prompt_user)
        return Log(oblog)


    def adjust_to_extremum(self, fws_log,
                          arrival_log,
                          prompt_user=True,
                          config=""):
        """Traveltime pick shifted to the nearest amplitude extremum

        A full description of the method is given in the Automation
        Module chapter of the WellCAD help documentation. 

        Arguments:
            fws_log	-- Zero based index (integer) or title (string) of
                          the log to process.
            arrival_log -- Index or title of the arrival time log
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.
        Returns:
            Object of the log containing the E1 amplitude.

        """

        self._dispatch._FlagAsMethod("AdjustPickToExtremum")
        oblog = self._dispatch.AdjustPickToExtremum (fws_log,
                                                    arrival_log,
                                                    prompt_user,
                                                    config)
        return Log(oblog)
    

    def window_amplitude(self, log, prompt_user=True, config=""):
        """Extracts the max amplitude from a given time window

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        Returns:
            Object of the amplitude log.

        """
        self._dispatch._FlagAsMethod("ExtractWindowPeakAmplitude")
        oblog = self._dispatch.ExtractWindowPeakAmplitude (log, prompt_user, config)
        return Log(oblog)


    def mechanical_properties(self, p_slowness, s_slowness, density=""):
        """Computes a set of rock mechanical parameters from the input data

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            p-slowness	-- Zero based index (integer) or title (string) of
                              the log containing the p-slowness data.
            s-slowness	-- Zero based index (integer) or title (string) of
                              the log containing the s-slowness data.
            density	-- Zero based index (integer) or title (string) of
                          the log containing the density data.

        """

        self._dispatch.CalculateMechanicalProperties (p_slowness, s_slowness, density)
        

    def integrated_traveltime(self, log, prompt_user=True, config=""):
        """Integrated traveltime from slowness or velocity data

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        Returns:
            Object of the integrated traveltime log.

        """

        self._dispatch._FlagAsMethod("IntegratedTravelTime")
        oblog = self._dispatch.IntegratedTravelTime(log, prompt_user, config)
        return Log(oblog)


# Spectral gamma processes
    
    def stack_spectra(self, log, prompt_user=True, config=""):
        """Stacks multiple spectra to derive n average spectrum

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        Returns:
            Object of the stacked spectra in an FWS log type.

        """

        self._dispatch._FlagAsMethod("StackTraces")
        oblog = self._dispatch.StackTraces(True, log, prompt_user, config)
        return Log(oblog)


    def borehole_correction(self, log, prompt_user=True, config=""):
        """Applies corrections to FWS and Well logs
        
        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        Returns:
            Object of the corrected log.
            
        """

        self._dispatch._FlagAsMethod("ApplyNaturalGammaBoreholeCorrection ")
        oblog = self._dispatch.ApplyNaturalGammaBoreholeCorrection (log, prompt_user, config)
        return Log(oblog)


    def gamma_calibration(self, log, k_factor, prompt_user=False):	
        """Multiples total gamma values with the k-factor.
        
        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            k_factor -- Calibration factir for GR measurement.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.

                
        """
        config = "K-Factor="+str(k_factor)
        self._dispatch.ApplyTotalGammaCalibration(log, prompt_user, config)


    def spectrum_statistics(self, log, prompt_user=True, config=""):
        """Derives min, max and total counts from spectra in a FWS log type
        
        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """

        self._dispatch.CalculateSpectrumTotalCount(log, prompt_user, config)	


    def spectrometric_ratios(self, log_a, log_b, log_c, prompt_user=True, config=""):
        """Computes spectrometric ratios like U/Th or U/k
        
        By default the ratios log_b/log_a, log_b/log_c and log_c/log_a
        will be computed.

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log_a	-- Zero based index (integer) or title (string) of
                          the log to process.
            log_b	-- Zero based index (integer) or title (string) of
                          the log to process.
            log_c	-- Zero based index (integer) or title (string) of
                          the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """

        self._dispatch.SpectrometricRatios(log_a, log_b, log_c, prompt_user, config)


    def full_spectrum_analysis(self, log_spectrum, log_time, prompt_user=True, config=""):
        """ Full spectrum analysis using a calibration from Medusa Systems

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log_spectrum -- Zero based index (integer) or title (string) of
                                  log to process.
            log_time -- Zero based index (integer) or title (string) of
                           the sample time log.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """

        self._dispatch.ProcessMedusaSpectrumData(log_spectrum, log_time, prompt_user, config)


    def process_spectrum(self, log, prompt_user=True, config=""):
        """Performs a windows stripping based on a calibration model

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.
        
        """

        self._dispatch.ProcessSpectrumData(log, prompt_user, config)	


    def compute_gr(self, log_k, log_u, log_th, prompt_user=True, config=""):
        """Computes total gamma ray from K, U and Th isotope concentrations

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log_k	-- Zero based index (integer) or title (string) of
                          the log containing the concentrations of K.
            log_u	-- Zero based index (integer) or title (string) of
                          the log containing the concentrations of U.
            log_th	-- Zero based index (integer) or title (string) of
                          the log containing the concentrations of Th.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string. 

        """
        self._dispatch._FlagAsMethod("ComputeGR")
        oblog = self._dispatch.ComputeGR(log_k, log_u, log_th, prompt_user, config)
        return Log(oblog)


# NMR processes

    def process_nmr(self, log, prompt_user=True, config=""):
        """Performs a post-processing of NMRSA's BMR tool raw data
        
         A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            log	-- Zero based index (integer) or title (string) of
                   the log to process.
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file/string.
            config -- Path and name of the configuration file or
                      a parameter string.

        """

        self._dispatch.ProcessNMRSAData(log, prompt_user, config)	


# Groundwater processes

    def water_salinity(self, log, prompt_user=True, config=""):
        """Salinity estimation from fluid conductivity or resisitivity.

        The log's unit will be used to distinguish between conductivity
        (S/m, S/cm, uS/cm) and resistivity (ohm.m, ohm.cm) as input.
        For a full description of the method and processing parameters
        please refer to the Automation chapter of the WellCAD help
        documentation.

        Arguments:
        log -- Name or index of the well or mud log containing the
               conductivity or resisitivity values.
        prompt_user -- If set to False the processing parameters
                       will be taken from the config file/string.
        config -- Path and name of the configuration file or
                  a parameter string.

        Returns:
        Log object of the resulting salinity log.

        """

        self._dispatch._FlagAsMethod("WaterSalinity")
        oblog = self._dispatch.WaterSalinity(log, prompt_user, config)
        return Log(oblog)


    def water_resistivity(self, log, prompt_user=True, config=""):
        """Temperature correction for fluid conductivity or resisitivity.

        For a full description of the method and processing parameters
        please refer to the Automation chapter of the WellCAD help
        documentation.

        Arguments:
        log -- Name or index of the well or mud log containing the
               conductivity or resisitivity values.
        prompt_user -- If set to False the processing parameters
                       will be taken from the config file/string.
        config -- Path and name of the configuration file or
                  a parameter string.

        """

        self._dispatch.WaterResistivity(log, prompt_user, config)	


    def shale_volume(self, log, prompt_user=True, config=""):
        """Estimates the shale volume from Gamma Ray or SP data.

        For a full description of the method and processing parameters
        please refer to the Automation chapter of the WellCAD help
        documentation.

        Arguments:
        log -- Name or index of the well or mud log containing the
               Gamma Ray or SP values.
        prompt_user -- If set to False the processing parameters
                       will be taken from the config file/string.
        config -- Path and name of the configuration file or
                  a parameter string.

        Returns:
        Log object of the resulting shale volume log.

        """

        self._dispatch._FlagAsMethod("ShaleVolume")
        oblog = self._dispatch.ShaleVolume(log, prompt_user, config)
        return Log(oblog)


    def porosity_sonic(self, log, prompt_user=True, config=""):
        """Computes porosity from transit time data.

        For a full description of the method and processing parameters
        please refer to the Automation chapter of the WellCAD help
        documentation.

        Arguments:
        log -- Name or index of the well or mud log containing the
               formation resistivty (Rt) values.
        prompt_user -- If set to False the processing parameters
                       will be taken from the config file/string.
        config -- Path and name of the configuration file or
                  a parameter string.

        Returns:
        Log object of the resulting porosity log.

        """

        self._dispatch._FlagAsMethod("PorositySonic")
        oblog = self._dispatch.PorositySonic(log, prompt_user, config)
        return Log(oblog)


    def porosity_archie(self, log, prompt_user=True, config=""):
        """Computes porosity from formation resistivity data.

        For a full description of the method and processing parameters
        please refer to the Automation chapter of the WellCAD help
        documentation.

        Arguments:
        log -- Name or index of the well or mud log containing the
               formation resistivty (Rt) values.
        prompt_user -- If set to False the processing parameters
                       will be taken from the config file/string.
        config -- Path and name of the configuration file or
                  a parameter string.

        Returns:
        Log object of the resulting porosity log.

        """

        self._dispatch._FlagAsMethod("PorosityArchie")
        oblog = self._dispatch.PorosityArchie(log, prompt_user, config)
        return Log(oblog)


    def porosity_density(self, log, prompt_user=True, config=""):
        """Computes porosity from density data.

        For a full description of the method and processing parameters
        please refer to the Automation chapter of the WellCAD help
        documentation.

        Arguments:
        log -- Name or index of the well or mud log containing the
               density values.
        prompt_user -- If set to False the processing parameters
                       will be taken from the config file/string.
        config -- Path and name of the configuration file or
                  a parameter string.
        
        Returns:
        Log object of the resulting porosity log.

        """

        self._dispatch._FlagAsMethod("PorosityDensity")
        oblog = self._dispatch.PorosityDensity(log, prompt_user, config)
        return Log(oblog)


    def porosity_neutron(self, log, prompt_user=True, config=""):
        """Applies a shale correction to neutron porosity data.

        For a full description of the method and processing parameters
        please refer to the Automation chapter of the WellCAD help
        documentation.

        Arguments:
        log -- Name or index of the well or mud log containing the
               neutron porosity values.
        prompt_user -- If set to False the processing parameters
                       will be taken from the config file/string.
        config -- Path and name of the configuration file or
                  a parameter string.
        
        Returns:
        Log object of the corrected porosity log.

        """

        self._dispatch._FlagAsMethod("PorosityNeutron")
        oblog = self._dispatch.PorosityNeutron (log, prompt_user, config)
        return Log(oblog)


    def permeability(self, log, prompt_user=True, config=""):
        """Estimates permeabilty from porosity data.

        Porosity values should be between 0 and 1.
        For a full description of the method and processing parameters
        please refer to the Automation chapter of the WellCAD help
        documentation.

        Arguments:
        log -- Name or index of the well or mud log containing the
               porosity values.
        prompt_user -- If set to False the processing parameters
                       will be taken from the config file/string.
        config -- Path and name of the configuration file or
                  a parameter string.
        
        Returns:
        Log object of the resulting permeability log.

        """
        
        self._dispatch._FlagAsMethod("Permeability")
        oblog = self._dispatch.Permeability(log, prompt_user, config)
        return Log(oblog)


    def hydraulic_conductivity(self, log, prompt_user=True, config=""):
        """Computes the hydraulic conductivity from permeability data.

        For a full description of the method and processing parameters
        please refer to the Automation chapter of the WellCAD help
        documentation.

        Arguments:
        log -- Name or index of the log containing the
               permeability values.
        prompt_user -- If set to False the processing parameters
                       will be taken from the config file/string.
        config -- Path and name of the configuration file or
                  a parameter string.
        
        Returns:
        Log object of the resulting log.

        """

        self._dispatch._FlagAsMethod("HydraulicConductivity")
        oblog = self._dispatch.HydraulicConductivity(log, prompt_user, config)
        return Log(oblog)


# CoreCAD processes

    def grainsize_statistics(self, log, prompt_user=True, config=""):
        """Computes statistics from a grainsize distribution curve.

        For a full description of the method and processing parameters
        please refer to the Automation chapter of the WellCAD help
        documentation.

        Arguments:
        log -- Name or index of the log containing the
               grainsize values.
        prompt_user -- If set to False the processing parameters
                       will be taken from the config file/string.
        config -- Path and name of the configuration file or
                  a parameter string.

        """

        self._dispatch.ExtractGrainSizeStatistics(log,
                                                 prompt_user,
                                                 config)


    def grainsize_sorting(self,
                          log_min,
                          log_max,
                          prompt_user=True,
                          config=""):
        """Classifies grainsize values based on min and max logs.

        For a full description of the method and processing parameters
        please refer to the Automation chapter of the WellCAD help
        documentation.	
        
        Arguments:
        log_min -- Name or index of the log containing the logged
                   minimum grainsize value.
        log_max -- Name or index of the log containing the logged
                   maximum grainsize value.
        prompt_user -- If set to False the processing parameters
                       will be taken from the config file/string.
        config -- Path and name of the configuration file or
                  a parameter string.

        Returns:
        Log object of the resulting classified log.

        """

        self._dispatch._FlagAsMethod("GrainSizeSorting")
        oblog = self._dispatch.GrainSizeSorting(log_min,
                                               log_max,
                                               prompt_user,
                                               config)
        return Log(oblog)


# Protection options

    def allow_protection(self, enable, password):
        """Changes the protection status of a document.

        Arguments:
            enable -- Set to True to protect the borehole document.
            password -- String of the password used to protect
                        the borehole document.

        """

        self._dispatch.EnableProtection(enable, password)


    def enable_protection(self, password):
        """Enables the document protection.

        Arguments:
            password -- String of the password used to protect
                        the borehole document.

        """

        self._dispatch.EnableProtection(True, password)	


    def disable_protection(self, password):
        """Disables the document protection.

        Arguments:
            password -- String of the password used to protect
                        the borehole document.

        """

        self._dispatch.EnableProtection(False, password)	


    def allow_insert_log(self, enable, password):
        """Changes the protection status for inserting new logs.

        Arguments:
            enable -- Set to True to allow adding new annotations
                      to the borehole document.
            password -- String of the password used to protect
                        the borehole document.

        """

        self._dispatch.AllowInsertLog(enable, password)

    
    def allow_save_template(self, enable, password):
        """Changes the protection status for saving layout templates.

        Arguments:
            enable -- Set to True to allow saving layout templates
                      of the borehole document.
            password -- String of the password used to protect
                        the borehole document.

        """

        self._dispatch.AllowSaveTemplate(enable, password)


    def allow_file_export(self, enable, password):
        """Changes the protection status for exporting data.

        Arguments:
            enable -- Set to True to allow the export of data
                      from the borehole document.
            password -- String of the password used to protect
                        the borehole document.

        """

        self._dispatch.AllowExportFile(enable, password)


    def allow_modify_annotation(self, enable, password):
        """Changes the protection status to modify annotations.

        Arguments:
            enable -- Set to True to allow editing existing annotations
                      in the borehole document.
            password -- String of the password used to protect
                        the borehole document.

        """

        self._dispatch.AllowModifyAnnotation(enable, password)
    

    def allow_insert_annotation(self, enable, password):
        """Changes the protection status for inserting annotations.

        Arguments:
            enable -- Set to True to allow adding new annotations
                      to the borehole document.
            password -- String of the password used to protect
                        the borehole document.

        """

        self._dispatch.AllowInsertAnnotation(enable, password)


    def allow_modify_header(self, enable, password):
        """Changes the protection status of the header content.

        Arguments:
            enable -- Set to True to allow edition of the
                      document header data.
            password -- String of the password used to protect
                        the borehole document.

        """

        self._dispatch.AllowModifyHeadersContent (enable, password)	