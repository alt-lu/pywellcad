from ._dispatch_wrapper import DispatchWrapper
from ._log import Log
from ._depth import Depth
from ._header import Header
from ._title import Title
from ._page import Page
from ._workspace import Workspace
from ._odbc import Odbc


class Borehole(DispatchWrapper):
    _DISPATCH_METHODS = ("Log", "ApplyStructureTrueToApparentCorrection", "ApplyStructureApparentToTrueCorrection",
                         "RemoveStructuralDip", "ExtractStructureIntervalStatistic", "ColorClassification",
                         "RepresentativePicks", "ImageComplexityMap", "NormalizeImage", "OrientImageToNorth",
                         "FilterImageLog", "ApplyConditionalTesting", "RQD", "GrainSizeSorting", "StackTraces",
                         "AverageFilterFWSLog", "FreqFilterFwsLog", "ApplyStandOffCorrection",
                         "CompensatedVelocity", "ApplySemblanceProcessing", "ProcessReflectedTubeWave",
                         "PickFirstArrival", "PickE1Arrival", "ExtractE1Amplitude", "AdjustPickToExtremum",
                         "ExtractWindowPeakAmplitude", "ApplyNaturalGammaBoreholeCorrection",
                         "ApplyTotalGammaCalibration", "CorrectDeadSensor", "CalculateFluidVelocity",
                         "CalculateApparentMetalLoss", "GetLog", "CreateNewWorkspace",  "Workspace", "FileExport",
                         "ConvertLogTo", "FilterLog", "ResampleLog", "InterpolateLog", "ElogCorrection",
                         "NMRFluidVolumes", "ROPAverage", )

    @property
    def name(self):
        """str: The title of a borehole document."""
        return self._dispatch.Name

    @name.setter
    def name(self, name):
        self._dispatch.Name = name

    @property
    def version_major(self):
        """int: The major version number of WellCAD."""
        return self._dispatch.VersionMajor

    @property
    def version_minor(self):
        """int: The minor version number of WellCAD."""
        return self._dispatch.VersionMinor

    @property
    def version_build(self):
        """int: The build number of WellCAD."""
        return self._dispatch.VersionBuild

    @property
    def top_depth(self):
        """float: The top depth of a borehole in units of the master depth axis."""
        return self._dispatch.TopDepth

    @property
    def bottom_depth(self):
        """float: The bottom depth of a borehole in units of the master depth axis."""
        return self._dispatch.BottomDepth

    @property
    def nb_of_logs(self):
        """int: The number of logs in a borehole."""
        return self._dispatch.NbOfLogs

    @property
    def auto_update(self):
        """bool: The auto update status of the borehole."""
        return self._dispatch.AutoUpdate

    @auto_update.setter
    def auto_update(self, flag):
        self._dispatch.AutoUpdate = flag

    def refresh_window(self):
        """Performs a one time refresh of the borehole view"""
        self._dispatch.RefreshWindow()

    def show_window(self):
        """Puts the borhole into focus."""
        self._dispatch.ShowWindow()

    def set_draft_mode(self, display_mode=None):
        """Toggles the view of the borehole document.

        Parameters
        ----------
        display_mode : int, optional
            The document viewing mode.  A borehole document can be displayed in the following modes:

                * 0 = Page Layout
                * 1 = Draft and fit
                * 2 = Draft
        """
        self._dispatch.SetDraftMode(display_mode)

    def minimize_window(self):
        """Shrinks the document window to an icon.

        Works only if document windows are not tabbed.
        """
        self._dispatch.MinimizeWindow()

    def maximize_window(self):
        """Enlarges the document window to fit the WellCAD frame.

        Works only if document windows are not tabbed.
        """
        self._dispatch.MaximizeWindow()

    def set_visible_depth_range(self, top_depth=None, bottom_depth=None):
        """Adjusts the depth range displayed in a borehole view.

        Parameters
        ----------
        top_depth : float
            The top depth of the visible depth range.
            If not provided, the current top depth of the document will be used
        bottom_depth : float
            The bottom depth of the visible depth range.
            If not provided, the current bottom depth of the document will be used
        """
        self._dispatch.SetVisibleDepthRange(top_depth, bottom_depth)

    @property
    def depth(self):
        """Depth: The reference/master vertical axis. Can be in depth or time."""
        return Depth(self._dispatch.Depth)

    @property
    def header(self):
        """Header: The document header for this borehole document."""
        return Header(self._dispatch.Header)

    @property
    def page(self):
        """Page: A page object for the borehole document."""
        return Page(self._dispatch.Page)

    def create_new_workspace(self, workspace_type, config):
        """Creates a new workspace object.

        Parameters
        ----------
        workspace_type : int
            * 1 = ISI workspace
            * 2 = Casing integrity
            * 3 = NMR
        config : str
            Path to a configuration file containing the workspace initialization parameters. The
            configuration file can contain the following options:

            .. code-block:: ini

                [ISIWorkspace]
                Name= workspace name
                Log= log name
                Caliper=100
                DepthOfImage=0
                CaliperUnit=mm / inch
                ApertureUnit=mm / inch/10
                LengthUnit=m / mm / cm / ft / inch / inch/10
                RunApparentToTrue=yes
                Azimuth= log name
                Tilt= log name
                ImageOrientation=North / High Side
                RunRecalculateAzimuth=yes
                RotationAngle=-12
                NavigationLog=ICM (log name or nothing)
                ' RGB OTV image
                ImageType= 0,
                'Greyscale OTV image.
                ImageType=1
                ' Diamond-drilled hole, ATV image
                ImageType=2
                'RC-drilled hole, ATV image
                ImageType=3
                'FMI image
                ImageType=4
                ICMPalette=0,0,0,255,56,255,0,0,12,64,224,208,21,50,205,50,31,255,255,0,39,255,215,0,47,255,104,32
                [CasingIntegrityWorkspace]
                Name= workspace name
                Log= log name
                LogUnit=mm / inch
                DataType=radius / diameter
                DrillerCasingTable=C:/Temp/Table.txt
                DrillerCasingTableDepthUnit=meters / feet
                DrillerCasingTableWeightUnit=lbs/ft / kg/m
                DrillerCasingTableODUnit=inch / mm
                [NMRWorkspace]
                Name= workspace name
                T2Distribution= log name
                TraceUnitOfT2Distribution=milliseconds / seconds
                DefaultLithoDatabase=C:/Program Files/Advanced Logic Technology/WellCAD/Dictionaries/NMR Volumes.lth
                FluidVolumeComponents=Bound Water, Moveable Water
                FluidVolumeLithoUseAssociatedColor=no
                DefaultCutoffValues=33
                LastDefaultCutoffValueMax=yes
                DisplayPermeabilityTIMModel=yes
                PermeabilityTIMModelVariableC=1 (i.e. premultiplier)
                PermeabilityTIMModelExponentM=4
                PermeabilityTIMModelExponentN=2
                PermeabilityTIMModelBFVandFFVLimit= Bound Water
                DisplayPermeabilitySDRModel=yes
                PermeabilitySDRModelVariableC=1 (i.e. premultiplier)
                PermeabilitySDRModelExponentM=4
                PermeabilitySDRModelExponentN=2
                DisplayDryMatrixDensity=no
                BulkDensity=Bulk_Density

        Returns
        -------
        Workspace
            The new workspace object.
        """
        return Workspace(self._dispatch.CreateNewWorkspace(workspace_type, config))

    def workspace(self, workspace_id):
        """Gets an existing workspace object in the document.

        Parameters
        ----------
        workspace_id : int or str
            The zero based index or the name of the workspace
        Returns
        -------
        Workspace or None
            The workspace object with the specified index or name, or ``None``
            if the index is out of bounds or if name does not match any of the workspace name.
        """
        return Workspace(self._dispatch.Workspace(workspace_id))

    def check_formula(self, formula):
        """Verifies the syntax of a formula used in a Formula Log.

        Parameters
        ----------
        formula : str
            The formula that needs to be checked.
            Example: "({GR}-min({GR}))/(max({GR})- min({GR}))"

        Returns
        -------
        bool
            Whether the formula is correct or not.
        """
        return self._dispatch.CheckFormula(formula)

    @property
    def odbc(self):
        """Odbc: An ODBC object that allows interaction with a database."""
        return Odbc(self._dispatch.ODBC)

    def connect_to(self, server_name, server_address, port_number):
        """Connects the current borehole document to an external data source provider.

        Parameters
        ----------
        server_name : str
            The name of the server (TFD is currently the only one supported)
        server_address : str
            The IP address of the computer to connect to.
        port_number : int
            The part number to connect to.
        Returns
        -------
        bool
            True if successful, False otherwise.
        """

        self._dispatch.ConnectTo(server_name, server_address, port_number)

    def disconnect_from(self, server_name, server_address):
        """Cuts the connection between the borehole document and the external data source provider.

        Parameters
        ----------
        server_name : str
            The name of the server (TFD is currently the only one supported)
        server_address : str
            The IP address of the computer connected to.
        Returns
        -------
        bool
            True if successful, False otherwise.
        """
        self._dispatch.DisconnectFrom(server_name, server_address)

    def save_as(self, path):
        """Saves the borehole document as WCL file.

        Parameters
        ----------
        path : str, optional
            The file path to the WellCAD borehole document file to save. If no
            file path is provided, the user will be prompted to select a file
            using a standard File Save As dialog box.
        Returns
        -------
        bool
            True if successful, False otherwise.
        """
        return self._dispatch.SaveAs(path)

    def file_export(self, file_name=None, prompt_user=None, config=None, log_file=None):
        """Exports the document to the specified file.

        Supported file formats are LAS, DLIS, EMF, CGM, JPG, PNG, TIF,
        BMP, WCL and PDF. Please refer to the WellCAD help file for a
        description of the export parameters to be used in the
        configuration file and parameter string.

        Parameters
        ----------
        file_name : str, optional
            The path and name of the file to export.
            If not provided, the dialog will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [LASExport]
                ; LAS files
                ; For compatibility with older versions of WellCAD:
                NbEndDepthDigits = 4
                NbSmpRateDigits = 4
                LASVersion = 2 / 3
                Log1 = Depth,Auto,Auto (Log name, Precision, Column width)
                Log2 = GR, 0, 10
                'Log3 = … (if no Log is specified all logs will be exported)
                MaxDepthRange = yes / no
                TopDepth = 0.0
                BottomDepth = 150.0
                SamplingRate = 0.1
                EnableHeader = yes / no
                EnableWrap = yes / no
                NullValue = -999.25
                Delimiter = 0 (Comma) /1 (Tab) / 2 (Space)
                CheckConstSmpRate = yes (optional)
                LimitLineLength = no (optional)
                ShortMnemonics = no (optional)
                AlignColumns = yes (optional)
                ForceDecimalPoint = yes (optional)
                SignificantDigits = 7 (optional)
                [DLISExport]
                ; DLIS files
                ; If no Log is specified all logs will be exported
                Log1 = GR
                Log2 = RHO
                [ImageExport]
                ; JPG, PNG, BMP, GIF, TIF files
                MaxDepthRange = yes / no
                TopDepth= 0.0
                BottomDepth= 10.0
                Resolution=300
                [EMFExport]
                ; EMF files
                MaxDepthRange = yes / no
                TopDepth= 0.0
                BottomDepth= 10.0
                [CGMExport]
                ; CGM files
                MaxDepthRange = yes / no
                TopDepth= 0.0
                BottomDepth= 10.0
                [PDFExport]
                ; PDF files
                MaxDepthRange = yes / no
                TopDepth= 0.0
                BottomDepth= 10.0
                ; Single page
                PageStyle=Single
                ShowProgress=TRUE
                OpenPDFFile=TRUE
                ; Standard page
                PageStyle=Standard
                Orientation=Portrait / Landscape
                PaperSize=A4
                ShowProgress=TRUE
                OpenPDFFile=TRUE
                ; Custom page
                PageStyle=Custom
                Orientation=Portrait
                'Orientation=Landscape
                PaperWidth=2100
                PaperLength=2970
                ShowProgress=TRUE
                OpenPDFFile=TRUE
                [WCLExport]
                ; WCL files
                Format = 5.0
        log_file : str, optional
            Path and name of the file to log error messages.

        Returns
        -------
        bool
            True if successful, False otherwise.
        """
        return self._dispatch.FileExport(file_name, prompt_user, config, log_file)

    def do_print(self, enable_dialog=None, top_depth=None, bottom_depth=None, nb_of_copies=None):
        """Sends the current document to the printer.
        If the print dialog box is displayed the user can select the
        printer otherwise the printer installed as default is used.

        Parameters
        ----------
        enable_dialog : bool, optional
            Whether to display the print dialog box or not.
        top_depth : float, optional
            The start depth of the interval to print
            If not provided, the current top depth of the document will be used.
        bottom_depth : float, optional
            The bottom depth of the printed depth interval.
            If not provided, the current bottom depth of the document will be used.
        nb_of_copies : int, optional
            The number of copies to be printed.
        """
        self._dispatch.DoPrint(enable_dialog, top_depth, bottom_depth, nb_of_copies)

    def read_database(self, script_path):
        """Opens and interprets an SQL script to download data from a database.

        Parameters
        ----------
        script_path : str
            The path to the SQL script to be called

        Returns
        -------
        bool
            Whether the operation was successful or not.
        """
        return self._dispatch.ReadDatabase(script_path)

    def write_database(self, script_path):
        """Opens and interprets an SQL script to upload data to a database.

        Parameters
        ----------
        script_path : str
            The path to the SQL script to be called

        Returns
        -------
        bool
            Whether the operation was successful or not.
        """
        return self._dispatch.WriteDatabase(script_path)

    def get_log(self, index_or_name):
        """Gets an existing log object in the document.

        Parameters
        ----------
        index_or_name :  int or str
            The zero based index or the name of the log.
        Returns
        -------
        Log
            The log object with the specified index or name, or ``None``
            if the index is out of bounds or if name does not match any of the log name.
        """
        return Log(self._dispatch.GetLog(index_or_name))

    def title(self, name):
        """Gets the title object for the specified name.

        Parameters
        ----------
        name : str, optional
            The name of the log or the name of a title box.
        Returns
        -------
        Title
            The Title object if found, otherwise "None"
        """
        return Title(self._dispatch.Title(name))

    def insert_new_log(self, log_type):
        """Creates a new log and log object.

        Parameters
        ----------
            log_type : int, optional
                The type of log.  Allowed values are :

                    * 1 = Well Log
                    * 2 = Formula Log
                    * 3 = Mud Log
                    * 4 = FWS Log
                    * 5 = Image Log
                    * 6 = Structure Log
                    * 7 = Litho Log
                    * 8 = Comment Log
                    * 9 = Engineering Log
                    * 10 = RGB Log
                    * 13 = Interval Log
                    * 14 = Analysis Log
                    * 15 = Percent Log
                    * 16 = CoreDesc Log
                    * 17 = Depth Log
                    * 18 = Strata Log
                    * 19 = Stacking Pattern Log
                    * 20 = Polar and Rose Log
                    * 21 = Cross Section Log
                    * 22 = OLE Log
                    * 23 = Shading Log
                    * 24 = Marker Log
                    * 25 = Breakout Log
                    * 26 = Bio Log
                    * 27 = Lineation Log
        Returns
        -------
        Log
            A log object.
        """
        return Log(self._dispatch.InsertNewLog(log_type))

    def convert_log_to(self, log, log_type, prompt_user=None, config=None):
        """New log object by converting one log type into another.

        Please refer to the WellCAD documentation about which log type
        conversions are possible.

        Parameters
        ----------
        log : str or int
            The title or the zero based index of the log to convert.
        log_type : int
            The type of log to be created.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [ConvertLog]
                ; Analysis, Percentage Log to Litho log
                ; ComponentNames : list of component names to convert, if not specified all components are taken
                ComponentNames=A,B
                ; Bio Log to Bio Log
                ; TaxonNames : list of taxon names to convert, if not specified all taxons are taken
                TaxonNames=A,B
                ; Image, RGB Log to WellLog
                StartIndex=0
                Increment=1
                ; Breakout Log to Breakout, Mud Log
                FilterOnAttributes= yes / no
                AttributeName1=Type
                AttributeList1=RF,MB,…
                AttributeName2=Condition
                AttributeList2=Open,Loose,…
                FilterOnAzimuth= yes / no
                AzimuthLow=0
                AzimuthHigh=360
                FilterOnTilt= yes / no
                TiltLow=30
                TiltHigh=90
                FilterOnLength= yes / no
                LengthLow=0
                LengthHigh=100
                FilterOnOpening= yes / no
                OpeningLow=0
                OpeningHigh=45
                ; Comment Log to Litho Log
                LithoDatabase=C:/Default.lth
                ; CoreDesc Log to Interval Log
                ; CoreDescItemNames : list of symbol codes to convert
                CoreDescItemNames=AX3, AX5, BZ5
                ; Structure Log to Structure, Mud Log
                FilterOnAttributes=TRUE
                AttributeName1=Type
                AttributeList1=RF,MB
                AttributeName2=Condition
                AttributeList2=Open,Loose
                FilterOnAzimuth= yes / no
                AzimuthLow=0
                AzimuthHigh=360
                FilterOnTilt= yes / no
                DipLow=30
                DipHigh=90
                FilterOnOpening= yes / no
                ApertureLow=0
                ApertureHigh=100
                ; Structure, Breakout Log to Marker Log
                DisplayIndex= yes / no
                DisplayAzimuth= yes / no
                DisplayTilt= yes / no
                DisplayAttributes= yes / no
                ; Interval Log to Mud Log
                ; ConvertValue : 0=Min, 1=Max, 2=Ave
                ; AttachDepthTo : 1=attach to top, 2=middle, 3=bottom
                ConvertValue=0
                AttachDepthTo=2
                ; Mud Log to Well Log
                ; Interpolation : 0 = No Interpolation, 1 = Prev. Data, 2 = Interpol.
                CreateNewLog= yes / no
                SamplingRate=0.1
                MaximumGap=10.0
                Interpolation=0
                Tolerance=0.1
                CircularData = yes / no
                DataUnit = degrees / radians
                ; Mud Log to Depth Log
                ; ConversionType : 1=from m, 2=from ft, 3=from sec; 4=msec, 5=usec
                ConversionType=1
                ; Mud Log to Litho Log
                ; <ClassifierName>=<LithoName> (classification name and corresponding litho code)
                LithoDatabase=C:/Default.lth
                className1 = Coal
                className2 = Limestone
                ; Percent Log to Analysis Log
                SamplingRate=0.1
                ; RGB Log to Image Log (int, float 2 and float 4)
                ; Color : 0=all, 1=red, 2=green, 3=blue
                Color=0
                ; Stack Log to Well Log
                SamplingRate=0.1
                ; Strata Log to Comment, Litho Log
                ; ColumnNames : list of column titles
                ColumnNames=columnname1, columname4
                ; VSP Log to Well Log
                ; TraceNames : list of trace titles
                TraceNames=
                ; Well Log to Depth Log
                ; ConversionType : 1=from m, 2=from ft, 3=from sec; 4=msec, 5=usec
                ConversionType=1
                ; Well Log to Litho Log
                ; <ClassifierName>=<LithoName> (classification name and corresponding litho code)
                ; SplitLithoLog : creates one litho column per litho type
                LithoDatabase=C:/Default.lth
                className1 = Coal
                className2 = Limestone
                SplitLithoLog= yes / no
                ; Litho Log to Strata Log
                ; SplitColumns : creates one column per litho type
                SplitColumns= yes / no (creates one column per litho type)
                ; Litho Log to Litho Log
                ; LithoBedNames : list of litho codes to convert, if not specified all components are taken
                LithoBedNames=sst,lst,dst

        Returns
        -------
        Log
            The object of the new log.
        """
        return Log(self._dispatch.ConvertLogTo(log, log_type, prompt_user, config))

    def add_log(self, log):
        """Adds the log object passed as argument of the function into the calling borehole document.

        Parameters
        ----------
        log : Log
            An object of the log to copy.
        Returns
        -------
        Log
            A copy of the log.
        """
        return Log(self._dispatch.AddLog(log._dispatch))

    def remove_log(self, log):
        """Deletes the specified log from the borehole document.

        Parameters
        ----------
        log : str or int
            The title or the zero based index of the log to remove.
        """
        self._dispatch.RemoveLog(log)

    def clear_log_contents(self, log):
        """Removes the data from a log and leaves the log empty.

        Parameters
        ----------
        log : str or int
            The title or the zero based index of the log to remove.
        """
        self._dispatch.ClearLogContents(log)

    def apply_template(self, path, prompt_if_not_found=None, create_new_logs=None, create_new_layers=None,
                       apply_annotation_settings=None, replace_header=None, keep_charts=None, new_charts=None,
                       overwrite_workspaces=None, new_workspaces=None, delete_non_associated_logs=None, config=None):
        """Loads and applies a document layout template (.WDT)

        Parameters
        ----------
        path : str
            The path and name of the template WDT file.
        prompt_if_not_found : bool, optional
            If True, a dialog box will be displayed for each log not found. Default : True.
        create_new_logs : bool, optional
            If True, new logs will be loaded from the template. Default : False.
        create_new_layers : bool, optional
            If True, new annotation layers will be loaded from the template. Default : False.
        apply_annotation_settings : bool, optional
            If True, settings  will be applied to annotations. Default : False.
        replace_header : bool, optional
            If True, the current document header will be replaced. Default : True.
        keep_charts : bool, optional
            If True, cross-plot charts will be kept in the document. Default : True.
        new_charts : bool, optional
            If True, cross-plot charts will be loaded from the template. Default : False.
        overwrite_workspaces : bool
            If True, work spaces in the document will be overwritten. Default : False.
        new_workspaces : bool, optional
            If True, work spaces will be loaded from the template. Default : False.
        delete_non_associated_logs : bool, optional
            If True, only logs from the template will be kept in the document. Default : True.
        config : str, optional
            Path and filename of the configuration file or parameter string.
        Returns
        -------
        bool
            True if successful, False otherwise.
        """
        return self._dispatch.ApplyTemplate(path, prompt_if_not_found, create_new_logs, create_new_layers,
                                            apply_annotation_settings, replace_header, keep_charts, new_charts,
                                            overwrite_workspaces, new_workspaces, delete_non_associated_logs, config)

    def slice_log(self, log, slice_depth, create_top=None, create_bottom=None, keep_original=None):
        """Allows the separation of the log data into a top and bottom section. New logs can be created \
        holding the data of the top and bottom parts of the data set.

        Parameters
        ----------
        log : str or int
            The title or the zero based index of the log to slice.
        slice_depth : float
            The depth at which the slice will be made.
        create_top : bool, optional
            If set to TRUE (default) a new log will be created holding the data from the current
            top of the data set down to the slice depth..
        create_bottom : bool, optional
            If set to TRUE (default) a new log will be created holding the data from the slice depth
            down to the bottom of the data set.
        keep_original : bool, optional
            If set to TRUE (default) the original log will be kept in the document.
        """
        self._dispatch.SliceLog(log, slice_depth, create_top, create_bottom, keep_original)

    def merge_logs(self, log_a, log_b, ave_overlap=None, create_new=None):
        """Merges the data of the two specified logs.

        Parameters
        ----------
        log_a : str or int
            The title or the zero based index of the log. If no new log is created this log
            will receive the data from log_b.
        log_b : str or int
            The title or the zero based index of the log.
        ave_overlap : bool, optional
            If set to False log_a will overwrite log_b, if set to True, data from the two logs will be averaged
            over the depth overlap.
        create_new : bool
            If set to False log_b will be pushed into log_a and the log_b will be removed
        """
        self._dispatch.MergeLogs(log_a, log_b, ave_overlap, create_new)

    def merge_same_log_items(self, log):
        """Merges consecutive data intervals of same litho codes, text or data within the specified log.
        This function applies to Litho, Comment, Engineering, CoreDesc, Interval, Stack and Bio logs.

        Parameters
        ----------
        log : str or int, optional
            The title or the zero based index of the log.
        """
        self._dispatch.MergeSameLogItems(log)

    def extend_log(self, log, top_depth, bottom_depth):
        """Extends the allocated depth range of Well, Formula and Analysis Logs.

        Parameters
        ----------
        log : str or int
            The title or the zero based index of the Well log.
        top_depth : float
            The new top depth of the log in units of the current depth axis.
        bottom_depth : float
            The new bottom depth of the log in units of the current depth axis.
        """
        self._dispatch.ExtendLog(log, top_depth, bottom_depth)

    def depth_shift_log(self, log, shift, top_depth=None, bottom_depth=None):
        """Allows the depth shifting of the log's data by the specified amount.
        By default, the entire data column will be shifted (i.e. block shift). If a Top and Bottom depth
        has been specified only the data within the specified interval will be shifted.

        Parameters
        ----------
        log : str or int
            The title or the zero based index of the log.
        shift : float
            The amount of depth shift to be applied. A negative value will shift the data up and
            a positive value applies a downward shift.
        top_depth : float, optional
            The upper depth limit of the shifted interval.
            If not provided, this is the current top depth of the log
        bottom_depth : float, optional
            The lower depth limit of the shifted interval.
            If not provided, this is the current bottom depth of the log
        """
        self._dispatch.DepthShiftLog(log, shift, top_depth, bottom_depth)

    def depth_match_log(self, log=None, depth_log=None):
        """Depth matches the specified log using the links created from the specified depth_log (i.e. a shift table).

        Parameters
        ----------
        log : str or int, optional
            The title or the zero based index of the log.
            If not provided, the Depth Matcher dialog box will be displayed.
        depth_log : str or int, optional
            The title or the zero based index of the Depth log containing the shift table.
            If not provided, the Depth Matcher dialog box will be displayed.
        """
        self._dispatch.DepthMatchLog(log, depth_log)

    def fill_log(self, log, top_depth, bottom_depth, step, thickness, user_defined_intervals=None, interval_log=None):
        """Fill a Cross-section Log or a Polar & Rose Log with intervals automatically.

        Parameters
        ----------
        log : str or int
            The title or the zero based index of the log.
        top_depth : float
            The top depth of the first interval in units of the current depth axis.
        bottom_depth : float
            The last depth at which an interval could start in units of the current depth axis.
        step : float
            The frequency of the intervals in units of the current depth axis (every 2 m).
        thickness : float
            The interval thickness in units of the current depth axis.
        user_defined_intervals : bool, optional
            If set to False the intervals will be loaded from a reference log.
        interval_log : str or int, optional
            The title or the zero based index of the log containing the reference intervals.
        """
        self._dispatch.FillLog(log, top_depth, bottom_depth, step, thickness, user_defined_intervals, interval_log)

    def filter_log(self, log, prompt_user=None, config=None):
        """Calculates a new filtered data set of a Well Log.

        Parameters
        ----------
        log : str or int
            The title or the zero based index of the log.
            If not provided, the process returns ''None''.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [FilterLog]
                ; FilterType : Median, MovingAverage, WeightedAverage
                ; DataUnit : degrees, radians
                FilterType =
                FilterWidth = 5
                MaxDepthRange = yes
                TopDepth = 5.0
                BottomDepth = 10.0
                CircularData = yes
                DataUnit = degrees

        Returns
        -------
        Log
            An object of the filtered log.
        """
        return Log(self._dispatch.FilterLog(log, prompt_user, config))

    def block_log(self, log=None, prompt_user=None, config=None):
        """Calculates statistical values for each depth interval determined from a
        reference log or specified by the user.

        Parameters
        ----------
        log : str or int, optional
            The title or the zero based index of the log.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [BlockLog]
                CircularData = yes / no
                DataUnit = degrees / radians
                ReferenceInterval = Lithology / 10.0
                Cumulate = yes / no
                OutputLogAsText = yes / no
                OutputLogAsGraphic = yes / no
                Minimum = yes / no
                Maximum = yes / no
                Mode = yes / no
                Average = yes / no
                Median = yes / no
                StdDev = yes / no
                Percentage = yes / no
                Sum = yes / no
                SumNorm= yes / no
                Area = yes / no
                MeanAbsoluteDeviation = yes / no
                GeometricMean = yes / no
                GeometricStdDev = yes / no
                Skewness = yes / no
                Kurtosis = yes / no
                Quartiles = yes / no
                AveragePlusStdDev = yes / no
                AverageMinusStdDev = yes / no
                RMS = Yes / No
                Value1 = 50 / NULL
                Value2 = 100
                Resolution = 0.1
                EmptyIntervalMode = Interpolate / Maximum / Minimum / Null
        """
        self._dispatch.BlockLog(log, prompt_user, config)

    def extract_well_log_statistics(self, logs=None, prompt_user=None, config=None):
        """Extracts minimum, maximum, average, median and other statistical values fulfilling
        an optional condition from each Well log

        Parameters
        ----------
        logs : list, optional
            The list of the titles or the zero base indexes of the logs to process.
            If not provided, the process dialog box will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [ExtractWellLogStatistics]
                ; Condition : 0=None, 1=lower than Value 1, 2=larger than Value1, 3=lower and equal,
                ; 4=larger and equal,5=equal, 6=not equal, 7=between Value1 and Value2,
                ; 8=between and equal to Value1 and Value2
                Minimum = yes / no
                Maximum = yes / no
                Mode = yes / no
                Average = yes / no
                Median = yes / no
                StandardDeviation = yes / no
                Percentage = yes / no
                MeanAbsoluteDeviation = yes / no
                GeometricMean = yes / no
                GeometricStandardDeviation = yes / no
                Skewness = yes / no
                Kurtosis = yes / no
                Quartiles = yes / no
                RMS = yes / no
                RMSD = yes / no
                Condition = 0
                Value1 = 50
                Value2 = 100
                OneOutputlogPerImageLog = yes / no
        """
        self._dispatch.ExtractWellLogStatistics(logs, prompt_user, config)

    def normalize(self, log=None, prompt_user=None, config=None):
        """Normalizes the data in a Percentage or Analysis Log.

        Parameters
        ----------
        log : str or int, optional
            The title or the zero based index of the log.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [AnalysisLogNormalize]
                ComponentsToDelete= 20, 05#1, Artifacts (Codes of the patterns to be
                removed separated by commas)
                CreateNewLog=yes
                At100=yes
        """
        self._dispatch.Normalize(log, prompt_user, config)

    def tvd(self, log=None, prompt_user=None, config=None):
        """Calculates a TVD either from another TVD log (Depth Log) or from a tilt log (Well Log).

        Parameters
        ----------
        log : str or int, optional
            The title or the zero based index of the log.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [TVD]
                Output=TVD /Elevation
                ExtrapolateBack=yes /no
                TVDAtZero=0.0

        Returns
        -------
        Log
            The newly created Log containing the TVD data.
        """
        return Log(self._dispatch.TVD(log, prompt_user, config))

    def rop_average(self, log=None, prompt_user=None, config=None):
        """Computes the average rate of penetration over specified depth intervals
        for a Mud Log or a Well Log.

        Parameters
        ----------
        log : str or int, optional
            The title or the zero based index of the log.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [ROPAverage]
                ReferenceInterval=Litho ; log title or constant value indicating the interval height
                OutputLogAsGraphic=no
                OutputLogAsText=yes
                DepthRange=Maximum ;Maximum, UserDefined, Zones, LogZones
                TopDepth=105
                BottomDepth=120
                ;LogZones : top1, bot1, top2, bot2, ... topN, botN
                LogZones=
                ; LogZonesDepthRange=logname, depthsectionName1, depthsectionName2, ....depthsectionname3
                LogZonesDepthRange=Litho,06,05#1

        Returns
        -------
        Log
            The newly created Log.
        """
        
        return Log(self._dispatch.ROPAverage(log, prompt_user, config))

    def unit_conversion(self, log=None, prompt_user=None, config=None):
        """Converts the units used in a log.

        Units are organized in categories (e.g. Length, Weight or Temperature).

        Parameters
        ----------
        log : str or int, optional
            The title or the zero based index of the log.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [UnitConversion]
                Category=Length / Weight / Temperature
                FromUnit=mm
                ToUnit=in
                CreateNewLogs=yes/no
        """
        self._dispatch.UnitConversion(log, prompt_user, config)

    def zonation(self, logs=None, prompt_user=None, config=None):
        """Splits log data into zones.

        This is an automated version of the Zonation process in WellCAD.

        Parameters
        ----------
        logs : list, optional
            The list of the titles or the zero base indexes of the logs to process.
            If not provided, the process dialog box will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [Zonation]
                UseIntervalThickness = yes/no (set to "no" to neglect theNbOuptutIntervals parameter)
                NbOutputIntervals = 2
                IntervalMinThickness = 0.5
                UseLithoLogAsOutput = yes/no
        """
        self._dispatch.Zonation(logs, prompt_user, config)

    def resample_log(self, log, prompt_user=None, config=None):
        """Resamples a data set according to a new constant sampling rate or sample point
        determined from a reference log.

        Parameters
        ----------
        log : str or int
            The title or the zero based index of the log.
            If not provided, the process returns ''None''.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [ResampleLog]
                ; For mud / well logs
                ; ReferenceLog : log title of a Mud or Percentage Log
                SamplingRate = 0.1
                ReferenceLog = Plugs
                UseReferenceLog = yes / no
                UseNearestPoint = yes / no
                CircularData = yes / no
                DataUnit = degrees / radians
                ; For image logs
                VerticalSamplingFactor = 1
                RadialSamplingFactor = 1
                RadialDownSampling = yes / no
        """
        return Log(self._dispatch.ResampleLog(log, prompt_user, config))

    def interpolate_log(self, log, prompt_user=None, config=None):
        """Allows the interpolation of Mud and Well Log data to close no data gaps in a data set.

        Parameters
        ----------
        log : str or int
            The title or the zero based index of the log.
            If not provided, the process returns ''None''.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [InterpolateLog]
                MaximumGap = 0.25
                CircularData = yes / no
                DataUnit = degrees / radians
        Returns
        -------
        Log
            An object of the interpolated log.
        """
        return Log(self._dispatch.InterpolateLog(log, prompt_user, config))

    def calculate_borehole_deviation(self, prompt_user=None, config=None):
        """Calculates borehole Azimuth, RBR and Tilt from magnetometer and inclinometer / accelerometer data.

        Parameters
        ----------
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [CalculateBoreholeDeviation]
                ; MagX, MagY, MagZ : the title of the corresponding log
                ; InclX, InclY, InclZ : the title of the corresponding log
                MagX = Mag X
                MagY = Mag Y
                MagZ = Mag Z
                InclX = Acc X
                InclY = Acc Y
                InclZ =
                MagXPositive = yes / no
                MagYPositive = yes / no
                MagZPositive = yes / no
                InclXPositive = yes / no
                InclYPositive = yes / no
                InclZPositive = yes / no
                IsAccelerometer = yes / no
                MarkerPosition = 182.5
        """
        self._dispatch.CalculateBoreholeDeviation(prompt_user, config)

    def calculate_borehole_volume(self, prompt_user=None, config=None):
        """Calculates the volume of an entire hole or annulus (e.g. between casing and borehole wall)
        from an Image logs containing radius values or a Well logs providing caliper values.

        Parameters
        ----------
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [VolumeProcess]
                InnerDiam = 100 / log name
                InnerDiamUnit = mm/in/cm/ft/yd
                OuterDiam = 110 / log name
                OuterDiamUnit = mm/in/cm/ft/yd
                AnnularVolume = yes/no
                BottomToTop = yes/no
                VolumeUnit = litre/cu.yd/cu.ft/cu.in/cu.cm/cu.m
                DisplayTick = yes/no
                SmallTickFreq = 1
                MediumTickFreq = 10
                LargeTickFreq = 100
                DisplayNumerical = yes/no
                NumericalFreq = 10
                DisplayCurve = yes/no
                DisplayInterval = yes/no
                IntervalRef = 10
                MaxDepthRange = yes/no
                TopDepth = 0.0
                BottomDepth = 123.5

        """
        self._dispatch.CalculateBoreholeVolume(prompt_user, config)

    def calculate_borehole_coordinates(self, prompt_user=None, config=None):
        """Calculates the deviation path coordinates Northing, Easting and TVD.

        Parameters
        ----------
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [CalculateBoreholeCoordinates]
                ; Method : Classic Tangential, Balanced Tangential, Radius Of Curvature, MinimumCurvature
                ; AzimuthLog : the title of the log corresponding to the azimuth.
                ; TiltLog : the title of the log corresponding to the tilt.
                Method = Classic Tangential
                Unit = m / ft
                AzimuthLog = AZI
                TiltLog = TILT
                NewDepthLog = yes / no
                CountTVDFromLogTop = yes / no
                TVDStartDepth = 0.0
                MagDeclination = 11.5
                EstimateErrors = yes / no
                AziError = 0.1
                TiltError = 0.1
        """
        self._dispatch.CalculateBoreholeCoordinates(prompt_user, config)

    def calculate_borehole_closure(self, prompt_user=None, config=None):
        """Calculates the deviation path closure distance, closure angle and DLS.

        Parameters
        ----------
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [CalculateBoreholeClosure]
                ; AzimuthLog : the title of the log corresponding to the azimuth.
                ; TiltLog : the title of the log corresponding to the tilt.
                ; NorthingLog : the title of the log corresponding to the deviation along the north axis.
                ; EastingLog : the title of the log corresponding to the deviation along the east axis.
                AzimuthLog = AZI
                TiltLog = TILT
                NorthingLog = NORTH
                EastingLog = EAST
        """
        self._dispatch.CalculateBoreholeClosure(prompt_user, config)

    def elog_correction(self, prompt_user=None, config=None):
        """Applies the environmental corrections for normal resisitivity data.

        Parameters
        ----------
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [ElogCorrection]
                ; Method : QL40-Elog (Bridle), QL40-Elog (Surface fish), Schlumberger
                ; LogN8 : the title of the log corresponding to the electrode N8.
                ; LogN16 : the title of the log corresponding to the electrode N16.
                ; LogN32 : the title of the log corresponding to the electrode N32.
                ; LogN64 : the title of the log corresponding to the electrode N64.
                ; LogNx : the title of the log corresponding to the electrode Nx.
                Method=QL40-Elog (Bridle)
                LogN8=N8
                LogN16=N16
                LogN32=
                LogN64=
                LogNx=
                ElectrodeSpacingNx=8
                ElectrodeSpacingNxUnit=inch (in inch, in, inches or mm)
                ElectrodeDiameter=1.57
                ElectrodeDiameterUnit=inch (in inch, in, inches or mm)
                BoreholeDiameter=2.20
                BoreholeDiameterUnit=inch (in inch, in, inches or mm)
                FluidResistivity=25 (log name or value in ohm.m)
        Returns
        -------
        Log
            An object of the last corrected log.
        """
        return Log(self._dispatch.ElogCorrection(prompt_user, config))

    def correct_bad_traces(self, log=None):
        """Replaces NULL data traces in Image, RGB and FWS logs.

        Parameters
        ----------
        log : str or int, optional
            Zero based index (integer) or title (string) of
            the log to process. If not provided, a dialog box
            displaying a list of available logs will be displayed.
        """
        self._dispatch.CorrectBadTraces(log)

    def stack_traces(self, is_spectrum=None, log=None, prompt_user=None, config=None):
        """Stacks multiple FWS traces to create and average trace.

        Parameters
        ----------
        is_spectrum : bool, optional
            Whether the log is a spectrum or not.
        log : int or str, optional
            Zero based index or title of the log to process.
            If not provided, the process returns None.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [StackTraces]
                NumberOfStacks = 5
        Returns
        -------
        Log
            The resulting log.
        """

        return Log(self._dispatch.StackTraces(is_spectrum, log, prompt_user, config))

    def apply_conditional_testing(self, log_if=None, log_then=None, prompt_user=None, config=None):
        """Applies conditional testing (If-Then-Else) to image log
        values.

        Parameters
        ----------
        log_if : str or int, optional
            Zero based index (integer) or title (string) of
            the log used for the 'If' clause.
        log_then : str or int, optional
            Zero based index (integer) or title (string) of
            the log used for the 'Then' clause.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with
            the user. If set to ``False`` the processing parameters
            will be retrieved from the specified configuration
            file. If no configuration file has been specified,
            default values will be used.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [ApplyConditionalTesting]
                Condition = != / <= / >= / > / < / ==
                ConditionValue = 100.0
                IsSecondCondition = yes / no
                SecondLogTest = <title of second log to test>
                OperatorSecondCondition = AND / OR
                SecondCondition = != / <= / >= / > / < / ==
                SecondConditionValue = 120.0
                ThenValue = NULL
                ElseValue = Amplitude

        Returns
        -------
        Log
            A newly created log.
        """
        return Log(self._dispatch.ApplyConditionalTesting(log_if, log_then, prompt_user, config))

    def filter_image_log(self, log=None, prompt_user=None, config=None):
        """Average, median and clipping filter for image logs.

        Parameters
        ----------
        log : str or int, optional
            Zero based index (integer) or title (string) of
            the log to process. If not provided, a dialog box
            displaying a list of available logs will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with
            the user. If set to  ``False`` the processing parameters
            will be retrieved from the specified configuration
            file. If no configuration file has been specified,
            default values will be used.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [FilterImageLog]
                FilterType = Average / Median / Despiking
                FilterWidth = 3
                FilterHeight = 3
                HighCutLimit = 75
                LowCutLimit = 15

        Returns
        -------
        Log
            The computed log.
        """
        return Log(self._dispatch.FilterImageLog(log, prompt_user, config))

    def mirror_image(self, log=None):
        """Rearranges the data within an image log so that the data
        appears mirrored when compared to the original image.

        Parameters
        ----------
        log : str or int, optional
            Zero based index (integer) or title (string) of
            the log to process. If not provided, a dialog box
            displaying a list of available logs will be displayed.
        """
        self._dispatch.MirrorImage(log)

    def rotate_image(self, log=None, prompt_user=None, config=None):
        """Rotate the image data by adding an angle (clockwise
        rotation) or subtracting it (counterclockwise rotation).

        Parameters
        ----------
        log : str or int, optional
            Zero based index (integer) or title (string) of
            the log to process. If not provided, a dialog box
            displaying a list of available logs will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with
            the user. If set to  ``False`` the processing parameters
            will be retrieved from the specified configuration
            file. If no configuration file has been specified,
            default values will be used.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [RotateImage]
                RotateBy= 1.2 / Log
                RotateClockwise = yes / no
        """
        self._dispatch.RotateImage(log, prompt_user, config)

    def orient_image_to_highside(self, log=None, prompt_user=None, config=None):
        """Rotates an image log to high side according to the
        deviation channels provided.

        Parameters
        ----------
        log : str or int, optional
            Zero based index (integer) or title (string) of
            the log to process. If not provided, a dialog box
            displaying a list of available logs will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with
            the user. If set to  ``False`` the processing parameters
            will be retrieved from the specified configuration
            file. If no configuration file has been specified,
            default values will be used.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [OrientImageToHighside]
                InclX = Acc X
                InclY = Acc Y
                InclZ =
                InclXPositive = yes / no
                InclYPositive = yes / no
                InclZPositive = yes / no
                IsAccelerometer = yes / no
                MarkerPosition = 180.2
        """
        self._dispatch.OrientImageToHighside(log, prompt_user, config)

    def orient_image_to_north(self, log=None, prompt_user=None, config=None):
        """Rotates an image log to magnetic north according to the
        deviation channels provided.

        Parameters
        ----------
        log : str or int, optional
            Zero based index (integer) or title (string) of
            the log to process. If not provided, a dialog box
            displaying a list of available logs will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with
            the user. If set to  ``False`` the processing parameters
            will be retrieved from the specified configuration
            file. If no configuration file has been specified,
            default values will be used.
        config : str, optional
                        Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [OrientImageToNorth]
                MagX = Mag X
                MagY = Mag Y
                MagZ = Mag Z
                InclX = Acc X
                InclY = Acc Y
                InclZ =
                MagXPositive = yes / no
                MagYPositive = yes / no
                MagZPositive = yes / no
                InclXPositive = yes / no
                InclYPositive = yes / no
                InclZPositive = yes / no
                IsAccelerometer = yes / no
                MarkerPosition = 180.2
        """
        self._dispatch.OrientImageToNorth(log, prompt_user, config)

    def extract_image_log_statistics(self, log=None, prompt_user=None, config=None):
        """Extracts minimum, maximum, average, median and other
        statistical values fulfilling an optional condition from each
        image log trace.

        Parameters
        ----------
        log : str or int, optional
            Zero based index (integer) or title (string) of
            the log to process. If not provided, a dialog box
            displaying a list of available logs will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with
            the user. If set to  ``False`` the processing parameters
            will be retrieved from the specified configuration
            file. If no configuration file has been specified,
            default values will be used.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [ExtractImageLogStatistics]
                Minimum = yes / no
                Maximum = yes / no
                Mode = yes / no
                Average = yes / no
                Median = yes / no
                StandardDeviation = yes / no
                Percentage = yes / no
                MeanAbsoluteDeviation = yes / no
                GeometricMean = yes / no
                GeometricStandardDeviation = yes / no
                Skewness = yes / no
                Kurtosis = yes / no
                Quartiles = yes / no
                RMS = yes / no
                RMSD = yes / no
                Condition = 0 (None) / 1 (lower than Value 1) / 2 (larger than Value1) / 3 (lower and equal)
                / 4 (larger and equal) / 5 (equal) / 6 (not equal) / 7 (between Value1 and Value2)
                / 8 (between and equal to Value1 and Value2)
                Value1 = 50
                Value2 = 100
                OneOutputlogPerImageLog = yes / no
                DepthRange = Maximum / UserDefined / Zones / LogZones
                TopDepth = 1.0
                BottomDepth = 200.0
                ZonesDepthRange = 10.0, 20.0, 50.0, 80.0 (top1, bottom1,...,topN, bottomN)
                LogZonesDepthRange=Litho,06,05 (log name, interval code 1, interval code 2,...)
        """
        self._dispatch.ExtractImageLogStatistics(log, prompt_user, config)

    def normalize_image(self, log=None, prompt_user=None, config=None):
        """Applies Static or Dynamic normalization to image logs

        Parameters
        ----------
        log : str or int, optional
            Zero based index (integer) or title (string) of
            the log to process. If not provided, a dialog box
            displaying a list of available logs will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with
            the user. If set to  ``False`` the processing parameters
            will be retrieved from the specified configuration
            file. If no configuration file has been specified,
            default values will be used.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [NormalizeImage]
                Mode = Static /Dynamic_1D / Dynamic_2D / HighPass
                WindowHeight = 0.3
                WindowWidth = 5


        Returns
        -------
        Log
            The normalized log.
        """
        return Log(self._dispatch.NormalizeImage(log, prompt_user, config))

    def image_complexity_map(self, log=None, prompt_user=None, config=None):
        """Computes the complexity map from an RGB or image log.

        Parameters
        ----------
        log : str or int, optional
            Zero based index (integer) or title (string) of
            the log to process. If not provided, a dialog box
            displaying a list of available logs will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with
            the user. If set to  ``False`` the processing parameters
            will be retrieved from the specified configuration
            file. If no configuration file has been specified,
            default values will be used.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [ImageComplexityMap]
                LogType=1
                ;RGB OTV image: 0,
                ;Greyscale OTV image: 1,
                ;Diamond-drilled hole, ATV image: 2,
                ;RC-drilled hole, ATV image: 3,
                ;FMI image: 4,
                Palette=0,0,0,255,56,255,0,0,12,64,224,208,21,50,205,50,31,255,255,0,39,255,215,0,47,255,104,32


        Returns
        -------
        Log
            The computed log.
        """
        return Log(self._dispatch.ImageComplexityMap(log, prompt_user, config))

    def apply_structure_apparent_to_true_correction(self, log=None, prompt_user=None, config=None):
        """Corrects the apparent azimuth and dip angles in a
        Structure log

        Parameters
        ----------
        log : str or int, optional
            Zero based index (integer) or title (string) of
            the log to process. If not provided, a dialog box
            displaying a list of available logs will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with
            the user. If set to  ``False`` the processing parameters
            will be retrieved from the specified configuration
            file. If no configuration file has been specified,
            default values will be used.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

            [ApplyStructureApparentToTrueCorrection]
            AzimuthLog = azimuth log name
            TiltLog = tilt log name
            ReferenceIsNorth = yes / no

        Returns
        -------
        Log
            The corrected log.
        """
        return Log(self._dispatch.ApplyStructureApparentToTrueCorrection(log, prompt_user, config))

    def apply_structure_true_to_apparent_correction(self, log=None, prompt_user=None, config=None):
        """Recalculates the apparent azimuth and dip angles in a
        Structure log from the true structure angles.

        Parameters
        ----------
        log : str or int, optional
            Zero based index (integer) or title (string) of
            the log to process. If not provided, a dialog box
            displaying a list of available logs will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with
            the user. If set to  ``False`` the processing parameters
            will be retrieved from the specified configuration
            file. If no configuration file has been specified,
            default values will be used.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [ApplyStructureApparentToTrueCorrection]
                AzimuthLog = azimuth log name
                TiltLog = tilt log name
                ReferenceIsNorth = yes / no

        Returns
        -------
        Log
            The computed log.
        """
        return Log(self._dispatch.ApplyStructureTrueToApparentCorrection(log, prompt_user, config))

    def recalculate_structure_azimuth(self, log=None, prompt_user=None, config=None):
        """Adds or subtracts a value from all Azimuth data within a
        structure log.

        Parameters
        ----------
        log : str or int, optional
            Zero based index (integer) or title (string) of
            the log to process. If not provided, a dialog box
            displaying a list of available logs will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with
            the user. If set to  ``False`` the processing parameters
            will be retrieved from the specified configuration
            file. If no configuration file has been specified,
            default values will be used.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [RecalculateStructureAzimuth]
                Angle = 45 / Log
                RotateClockwise = yes / no
                MaxDepthRange = yes / no
                TopDepth = 0.0
                BottomDepth = 1.0

        """
        self._dispatch.RecalculateStructureAzimuth(log, prompt_user, config)

    def recalculate_structure_dip(self, log=None, prompt_user=None, config=None):
        """Correct the dip angle data within a structure log for new
        caliper settings.

        Parameters
        ----------
        log : str or int, optional
            Zero based index (integer) or title (string) of
            the log to process. If not provided, a dialog box
            displaying a list of available logs will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with
            the user. If set to  ``False`` the processing parameters
            will be retrieved from the specified configuration
            file. If no configuration file has been specified,
            default values will be used.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [RecalculateStructureDip]
                Caliper = Log / 200.0
                CaliperUnit = mm / in
                MaxDepthRange = yes / no
                TopDepth = 0
                BottomDepth = 1

        """
        self._dispatch.RecalculateStructureDip(log, prompt_user, config)

    def remove_structural_dip(self, log=None, prompt_user=None, config=None):
        """Removes a given regional dip and azimuth from the data in
        a structure log and recalculates new Dip and Azimuth angles.

        Parameters
        ----------
        log : str or int, optional
            Zero based index (integer) or title (string) of
            the log to process. If not provided, a dialog box
            displaying a list of available logs will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with
            the user. If set to  ``False`` the processing parameters
            will be retrieved from the specified configuration
            file. If no configuration file has been specified,
            default values will be used.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [RemoveStructuralDip]
                Azimuth = Log /45
                Dip = Log /10
                MaxDepthRange = yes / no
                TopDepth = 0.0
                BottomDepth = 1.0

        Returns
        -------
        Log
            The computed log.
        """
        return Log(self._dispatch.RemoveStructuralDip(log, prompt_user, config))

    def extract_color_components(self, log=None, method=None, color_model=None, prompt_user=None):
        """Allows the extraction of color data from an RGB Log.

        Parameters
        ----------
        log : str or int, optional
            Zero based index (integer) or title (string) of
            the log to process. If not provided, a dialog box
            displaying a list of available logs will be displayed.
        method : int, optional
            The methode used.
            Available models are:

            * 0 = Average
            * 1 = Mode
            * 2 = Image Log
        color_model : int, optional
            The color model used.
            Available models are:

            * 0 = RGB
            * 1 = HSV
            * 2 = YUV
            * 3 = CIELAB
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with
            the user. If set to  ``False`` the processing parameters
            will be retrieved from the specified configuration
            file. If no configuration file has been specified,
            default values will be used.
        """
        self._dispatch.ExtractColorComponents(log, method, color_model, prompt_user)

    def color_classification(self, log=None, prompt_user=None, config=None):
        """Builds color classes from an RGB Log based on user
        specified reference colors.

        Parameters
        ----------
        log : str or int, optional
            Zero based index (integer) or title (string) of
            the RGB log to process.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with
            the user. If set to  ``False`` the processing parameters
            will be retrieved from the specified configuration
            file. If no configuration file has been specified,
            default values will be used.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [ColorClassification]
                OutputImage = yes
                OutputAnalysis = yes
                NoiseReduction = 10
                Class1="Class 1";"0,255,0";58;50;"166,143,81"
                Class2="Class 2";"255,0,255";37;50;"44,42,34"
                Class3="Class 3";"255,255,0";34;50;"251,165,75"

        Returns
        -------
        Log
            Returns an RGB Log or an Analysis Log depending on the configuration file.
            Returns the RGB Log if both options are selected.
        """
        return Log(self._dispatch.ColorClassification(log, prompt_user, config))

    def adjust_image_brightness_and_contrast(self, log=None, prompt_user=None):
        """Adjusts the brightness and contrast in RGB logs

        Parameters
        ----------
        log : str or int, optional
            A string specifying the log name or an integer
            representing the index of the log to be processed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with
            the user. If set to False, the new brightness and
            contrast values will be determined automatically.
        """
        self._dispatch.AdjustImageBrightnessAndContrast(log, prompt_user)

    def extract_structure_interval_statistic(self, log=None, prompt_user=None, config=None):
        """Allows determination of statistical values (e.g. frequency
        of dips) per interval from a structure log.

        Parameters
        ----------
        log : str or int, optional
            Zero based index (integer) or title (string) of
            the log to process. If not provided, a dialog box
            displaying a list of available logs will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with
            the user. If set to  ``False`` the processing parameters
            will be retrieved from the specified configuration
            file. If no configuration file has been specified,
            default values will be used.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [ExtractStructureIntervalStatistic]
                Reference = 5.0 / Log
                OutputMinAzimuth = yes / no
                OutputMaxAzimuth = yes / no
                OutputAverageAzimuth = yes / no
                OutputMinDip = yes / no
                OutputMaxDip = yes / no
                OutputAverageDip = yes / no
                OutputMinTilt = yes / no
                OutputMaxTilt = yes / no
                OutputAverageTilt = yes / no
                OutputMinAperture = yes / no
                OutputMaxAperture = yes / no
                OutputAverageAperture = yes / no
                OutputMinLength = yes / no
                OutputMaxLength = yes / no
                OutputAverageLength = yes / no
                OutputMinOpening = yes / no
                OutputMaxOpening = yes / no

        Returns
        -------
        Log
            One of the computed log.
        """
        return Log(self._dispatch.ExtractStructureIntervalStatistic(log, prompt_user, config))

    def rqd(self, log=None, prompt_user=None, config=None):
        """Computes the Rock Quality Designation from the structure
        picks in a Structure Log.

        Parameters
        ----------
        log : str or int, optional
            Zero based index (integer) or title (string) of
            the log to process. If not provided, a dialog box
            displaying a list of available logs will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with
            the user. If set to  ``False`` the processing parameters
            will be retrieved from the specified configuration
            file. If no configuration file has been specified,
            default values will be used.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [RQD]
                CorePieceLength = 0.1
                CoreLength = 1
                AttributeName1 = Defect Type
                AttributeValues1 = JT-MAJ, JT-MED, JT-MIN,
                AttributeName2 = Defect Condition
                AttributeValues2 = cont, part
                DepthRange = Maximum / UserDefined / Zones
                'UserDefined
                TopDepth=25
                BottomDepth=30
                'Zones
                ZonesDepthRange = 20,26, 24,30

        Returns
        -------
        Log
            The computed log.
        """
        return Log(self._dispatch.RQD(log, prompt_user, config))

    def representative_picks(self, log=None, prompt_user=None, config=None):
        """Used to derive the most representative picks from a
        Structure log given user defined classification limits.

        Parameters
        ----------
        log : str or int, optional
            Zero based index (integer) or title (string) of
            the log to process. If not provided, a dialog box
            displaying a list of available logs will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with
            the user. If set to  ``False`` the processing parameters
            will be retrieved from the specified configuration
            file. If no configuration file has been specified,
            default values will be used.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [RepresentativePicks]
                TopDepth=0.0
                BottomDepth=10.0
                TiltWindow=5.0 (structural dip angle interval, here +/- 5 degrees)
                AzimuthWindow=15.0 (structural azimuth angle interval, here +/- 15 degrees)
                DepthWindow=0.5
                KeepFeaturesUngrouped=TRUE / FALSE

        Returns
        -------
        Log
            The computed log.
        """
        return Log(self._dispatch.RepresentativePicks(log, prompt_user, config))

    def correct_dead_sensor(self, log=None, prompt_user=None, config=None):
        """Corrects the Null and invalid data columns in Image logs.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log to process.
            If not provided, the process returns ''None''.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [DeadSensor]
                ; Method : Automatic, Range, Columns
                ; ReplaceBy : Null, Average, Median, Interpolate, LogName or a numerical value
                Method = Automatic
                ReplaceBy = Average
                ; If Method = Automatic
                WindowHeight = 0
                Discrimination = 0.125
                MinDataHeight = 0
                ; If Method = Range
                WindowHeight = 0
                Low = 0
                High = 0
                ; If Method = Columns
                ; Columns : single index value or range like 15-20
                Columns = 1
        Returns
        -------
        Log
            A log with the corrected data.
        """
        return Log(self._dispatch.CorrectDeadSensor(log, prompt_user, config))

    def shift_correction(self, log=None, prompt_user=None, config=None):
        """Corrects the drift of data (e.g. MFC) in Image logs.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log to process.
            If not provided, the process returns ''None''.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : bool, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [ShiftCorrection]
                ; Zone1 : name, top, bottom, value
                OutputCorrections = yes / no
                ExtendTrends = yes / no
                Zone1=ref1, 25.0, 26.0, 101.2
                Zone2=ref2, 45.0, 47.0, 125.3

        Returns
        -------
        Log
            A log that has been corrected.
        """
        return Log(self._dispatch.ShiftCorrection(log, prompt_user, config))

    def calculate_fluid_velocity(self, log=None, prompt_user=None, config=None):
        """Estimates the fluid velocity from travel time measurements and given calibration points.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log to process.
            If not provided, the process dialog box will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : bool, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [CalculateFluidVelocity]
                ; If the AutoFill option is used the CalibrationPoints are not used.
                ; ToolRadius : in mmm
                ; TimeWindow : log name or value
                ; CalibrationPoint1 : depth, diameter in mm
                ; AutoFillFrom : depth value or 'Top'
                 ; AutoFillTo : depth value or 'Bottom'
                TravelTimeUnit = 0.1
                ToolRadius = 19
                TimeWindow = TimeWndLog / 74
                CalibrationPoint1 = 20.44, 96
                CalibrationPoint2 = 36.85, 96
                CalibrationPoint3 = ...
                ExtendTrends = yes / no
                AutoFillFrom = 0 / Top
                AutoFillTo = 0 / Bottom
                AutoFillCaliper = 0 / Log Name
                AutoFillStepSize = 1.0

        Returns
        -------
        Log
            A log giving the fluid velocity.
        """
        return Log(self._dispatch.CalculateFluidVelocity(log, prompt_user, config))

    def centralize(self, log=None, prompt_user=None, config=None):
        """Corrects travel time or multi-finger-caliper data for de-centralization effects
        and outputs a new image log.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log to process.
            If not provided, the process returns ''None''.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : bool, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [Centralize]
                ; UseRange : use clipping range
                UseRange = yes / no
                CaliperLow = 0
                CaliperHigh = 0
                OutputEccentricity = yes / no
                OutputEccentricityDir = yes / no

        Returns
        -------
        Log
            A log with the data corrected for decentralization.
        """
        return Log(self._dispatch.Centralize(log, prompt_user, config))

    def calculate_acoustic_caliper(self, log=None, prompt_user=None, config=None):
        """Calculates borehole radius and caliper values from acoustic travel time measurements.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log to process.
            If not provided, the process dialog box will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : bool, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [CalculateAcousticCaliper]
                ; CaliperUnit : mm, cm, in
                ; FluidVelocityUnit : m/s, km/s, m/ms, m/us, ft/s, ft/ms, ft/us, s/km, s/m, us/m, s/ft, us/ft
                ; ToolRadius : in mm
                TravelTimeUnit = 0.1
                CaliperUnit = mm
                ToolRadius = 19
                TimeWindow = TimeWndLog / 74
                FluidVelocity = VelocityLog / 1440
                FluidVelocityUnit= m/s
                CurveOutput = yes / no
                ImageOutput  = yes / no
        """
        self._dispatch.CalculateAcousticCaliper(log, prompt_user, config)

    def calculate_casing_thickness(self, log=None, prompt_user=None, config=None):
        """Calculates thickness values for a casing pipe from acoustic thickness travel time measurements.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log to process.
            If not provided, the process dialog box will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : bool, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [CalculateCasingThickness]
                ; ThicknessUnit : mm, cm, in
                ; SteelVelocityUnit : m/s, km/s, m/ms, m/us, ft/s, ft/ms, ft/us, s/km, s/m, us/m, s/ft, us/ft
                ; CurveOutput : output min, max, average thickness
                ; ImageOutput  : output the thickness as an image log
                TravelTimeUnit = 0.01
                SteelVelocity = VelocityLog / 5200
                SteelVelocityUnit= m/s
                CurveOutput = yes / no
                ImageOutput = yes / no
        """
        self._dispatch.CalculateCasingThickness(log, prompt_user, config)

    def calculate_apparent_metal_loss(self, log=None, prompt_user=None, config=None):
        """Calculates an apparent metal loss value for each trace of radius values stored in an image log.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log to process.
            If not provided, the process dialog box will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : bool, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [CalculateApparentMetalLoss]
                ; The units of the internal / external pipe radius values must be the same as the unit
                ; of the radius values in the image log.
                InternalPipeRadius = 1.9
                ExternalPipeRadius = 2.2
        Returns
        -------
        Log
            A log giving the metal loss.
        """
        return Log(self._dispatch.CalculateApparentMetalLoss(log, prompt_user, config))

    def radius_to_from_diameter(self, log=None, prompt_user=None, config=None):
        """Converts values data in an Image log from radius to diameter values or vice versa.

        Parameters
        ----------
        log : int or str
            Zero based index or title of the log to process.
            If not provided, the process returns ''None''.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [RadiusToFromDiameter]
                ;  Method : TwoTimesRadius, OppositeValues, HalfDiameter
                Method = TwoTimesRadius
        Returns
        -------
        Log
            A log giving diameter/radius.
        """
        return Log(self._dispatch.RadiusToFromDiameter(log, prompt_user, config))

    def outer_inner_radius_diameter(self, log=None, prompt_user=None, config=None):
        """The process takes an Image, Well or Mud log as input and computes from radius/diameter
        and thickness values an outer radius/diameter value.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log to process.
            If not provided, the process returns ''None''.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [OuterInnerRadiusDiameter]
                ; InputType : InnerRadius, OuterRadius, InnerDiameter, OuterDiameter
                ; OutputType : InnerRadius, OuterRadius, InnerDiameter, OuterDiameter
                ; Thickness = log name or value
                Thickness = THK
                InputType = InnerRadius
                OutputType = OuterDiameter
        Returns
        -------
        Log
            A log giving the outer radius/diameter.
        """
        return Log(self._dispatch.OuterInnerRadiusDiameter(log, prompt_user, config))

    def cased_hole_normalization(self, log=None, prompt_user=None, config=None):
        """Subtracts the trace average, median, min, max or a custom value from all data points
        of the same trace.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log to process.
            If not provided, the process returns ''None''.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : bool, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [CasedHoleNormalization]
                ; Method : Mean, Median, Min, Max, Other
                ; The Value parameter is used when the Method has been set to Other
                ; Value : log name or constant numerical value
                Method = Mean
                Value = 10.5

        Returns
        -------
        Log
            The resulting log.
        """
        return Log(self._dispatch.CasedHoleNormalization(log, prompt_user, config))

    def reverse_amplitude(self, log=None):
        """Inverts the amplitudes in a FWS log.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log to process.
            If not provided, a dialog box displaying a list of available logs will be displayed.
        """

        self._dispatch.ReverseAmplitude(log)

    def average_filter_fws_log(self, log=None, filter_width=None, filter_type=None):
        """Applies a moving average filter to the traces of an FWS log.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log to process.  If not provided, the process returns None.
        filter_width : float, optional
            Length of the filter window in us.  If not provided, default value will be used.
        filter_type : int, optional
            If not provided, default value will be used.
            Type of the filter :

                * 0 = moving average
                * 1 = weighted average

        Returns
        -------
        Log
            The resulting log.
        """

        return Log(self._dispatch.AverageFilterFWSLog(log, filter_width, filter_type))

    def freq_filter_fws_log(self, log, low_cut, low_pass, high_pass, high_cut):
        """Applies a frequency filter to the traces of an FWS log.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log to process.  If not provided, the process returns None.
        low_cut : float
            The low cut-off frequency of filter in kHz. If not provided, default value will be used.
        low_pass : float
            The low pass frequency of filter in kHz. If not provided, default value will be used.
        high_pass : float
            The high pass frequency of filter in kHz. If not provided, default value will be used.
        high_cut : float
            The high cut-off frequency of filter in kHz. If not provided, default value will be used.

        Returns
        -------
        Log
            Object of the filtered FWS log.
        """

        return Log(self._dispatch.FreqFilterFwsLog(log, low_cut, low_pass, high_pass, high_cut))

    def apply_stand_off_correction(self, log=None, prompt_user=None, config=None):
        """Corrects intercept times for the stand-off of tool and formation.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log to process.
            If not provided, the process dialog settings will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [ApplyStandOffCorrection]
                ; LogUnit : s, ms, msec, us, usec, sec
                ; ToolSpacingUnit, ToolDiameterUnit, HoleDiameterUnit : m, mm, inch, cm, ft
                ; FluidVelocityUnit : us/ft, us/m, ft/us, m/s
                ; VelocityUnit : us/ft, us/m, ft/us, m/s
                ; HoleDiameter, FluidVelocity : log name or constant
                LogUnit=us
                ToolSpacing=0.6
                ToolSpacingUnit=m ; m, mm, inch, cm, ft
                ToolDiameter=50
                ToolDiameterUnit=mm
                HoleDiameter=100
                HoleDiameterUnit=mm
                FluidVelocity=1500
                FluidVelocityUnit=m/s
                VelocityUnit=m/s

        Returns
        -------
        Log
            The resulting log.
        """

        return Log(self._dispatch.ApplyStandOffCorrection(log, prompt_user, config))

    def compensated_velocity(self, log=None, prompt_user=None, config=None):
        """Slowness or velocity computed from two receiver arrival times.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log containing the travel times to the first receiver.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [FwsCompensatedVelocity]
                ; RX1Log, RX2Log : log name
                ; RX1LogUnit, RX2LogUnit : s, ms, msec, us, usec, sec
                ; SpacingUnit : m, mm, inch, ft, cm
                ; VelocityUnit : us/ft, us/m, ft/us, m/s
                RX1Log =RX1 - dt
                RX2Log = RX2 - dt
                RX1LogUnit = us
                RX2LogUnit = us
                Spacing = 0.2
                SpacingUnit = m
                VelocityUnit =us/m

        Returns
        -------
        Log
            The resulting log.
        """

        return Log(self._dispatch.CompensatedVelocity(log, prompt_user, config))

    def apply_semblance_processing(self, prompt_user=None, config=None):
        """Performs a velocity analysis for the multiple receivers.

        Parameters
        ----------
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file.
            The configuration file can contain the following options:

            .. code-block:: ini

                [ApplySemblanceProcessing]
                Rx1_Log = RX1
                Rx1_Offset = 0.0
                Rx1_TxDistance = 0.6
                Rx1_Unit = m
                Rx2_Log = RX2
                Rx2_Offset = 0.0
                Rx2_TxDistance = 0.8
                Rx2_Unit = m
                Rx3_Log= ...

                [FwsVelocityAnalysis]
                EnableFilter=false
                FreqFilterLowPass=2.5 ; in kHz
                FreqFilterLowPass=5.0
                FreqFilterHighPass=30.0
                FreqFilterHighCut=35.0
                ToolDiameter=50.0
                ToolDiameterUnit=mm ;mm, cm, inch
                BoreholeDiameter=100.0
                BoreholeDiameterUnit=mm ;mm, cm, inch
                FluidSlowness=666.67
                FluidSlownessUnit=us/m ; us/ft, us/m, ft/us, m/s, us/m

        Returns
        -------
        Log
            The log containing the semblance results.
        """

        return Log(self._dispatch.ApplySemblanceProcessing(prompt_user, config))

    def process_reflected_tube_wave(self, log=None, prompt_user=None, config=None):
        """Extracts the cumulative energy from reflected tube wave arrivals.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log to process.
            If not provided, the process dialog settings will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [ProcessReflectedTubeWave]
                ; Side : both,  upper, lower
                Side = both
                Offset = 25.0 'measured in us
                Blanking = 50.0 'measured in us
                FluidSlowness = 696.0 'measured in us/m
                TxFrequency = 15000.0 'measured in Hz

        Returns
        -------
        Log
            The resulting log containing the cumulative energy.
        """

        return Log(self._dispatch.ProcessReflectedTubeWave(log, prompt_user, config))

    def pick_first_arrival(self, log=None, prompt_user=None, config=None):
        """Picks the first arrival time using the standard threshold or advanced method.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log to process.  If not provided, the process returns None.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file.
            The configuration file can contain the following options:

            .. code-block:: ini

                [FwsFirstArrival]
                ;Method=Standard Threshold Pickup Algorithm
                Method=Advanced Threshold Pickup Algorithm

                [Standard Threshold Pickup Algorithm]
                Blanking=100.0
                Threshold=15.0
                BackInterpolation=yes
                LockToSampling=yes
                ; the next two are advanced settings
                BaseLine=0.0
                AutoAdjustThreshold=no

                [Advanced Threshold Pickup Algorithm]
                Blanking=0.0
                Threshold=3.0
                LargeWidth=120.0
                SmallWidth=40.0

        Returns
        -------
        Log
            The resulting log containing the first arrival times.
        """

        return Log(self._dispatch.PickFirstArrival(log, prompt_user, config))

    def cement_bond(self, log=None, prompt_user=None, config=None):
        """Determines the cement bond based on the Standard Gate Method.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log to process.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [CementBondProcess]
                ; Logs : comma-separated FWS log names of the receivers to be processed
                Logs=WVFS1,WVFS2,WVFS3
                AreRadiiSectors=no
                EnableT0Gate=yes
                EnableTXGate=no
                T0GateStart=237.4
                T0GateLength=40
                TXGateBlanking=0
                TXGateThreshold=15
                EnableCalibration=no
                BLGateStart=50
                BLGateLength=25
                FreePipeTargetAmplitude=100
                FreePipeTargetAmplitudeUnits=mV
                FreePipeTopDepth=0
                FreePipeBotDepth=0
        """

        self._dispatch.CementBond(log, prompt_user, config)

    def pick_e1_arrival(self, fws_log=None, dt_log=None, prompt_user=None, config=None):
        """Determines the arrival time of the E1 amplitude.

        Parameters
        ----------
        fws_log : int or str, optional
            Zero based index or title of the FWS log to process.
            If not provided, the process dialog box will be displayed.
        dt_log : int or str, optional
            Zero based index or title of the arrival time log to process.
            If not provided, the process dialog box will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [PickE1Arrival]
                PickPositivPolarity = yes
                FilterWidth = 5

        Returns
        -------
        Log
            The resulting log containing the E1 arrival times.
        """

        return Log(self._dispatch.PickE1Arrival(fws_log, dt_log, prompt_user, config))

    def extract_e1_amplitude(self, fws_log=None, arrival_log=None, prompt_user=None):
        """Uses the E1 arrival time to extract the E1 amplitude.

        Parameters
        ----------
        fws_log : int or str, optional
            Zero based index or title of the log to process.
        arrival_log : int, str or float, optional
            int, str : Zero based index or title of the log containing the first E1 arrival times.
            float : constant E1 arrival time
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.

        Returns
        -------
        Log
            The resulting log containing the E1 amplitude.
        """

        return Log(self._dispatch.ExtractE1Amplitude(fws_log, arrival_log, prompt_user))

    def adjust_pick_to_extremum(self, fws_log=None, arrival_log=None, prompt_user=None, config=None):
        """Adjusts the pick given in arrival_log to the next maximum or minimum amplitude in fws_log.

        Parameters
        ----------
        fws_log : int or str, optional
            Zero based index or title of the fws log.
            If not provided, the process dialog box will be displayed.
        arrival_log : int or str, optional
            Zero based index or title of the arrival time log.
            If not provided, the process dialog box will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [AdjustPickToExtremum]
                PickPositivPolarity = yes
                FilterWidth = 5

        Returns
        -------
        Log
            Object of the log containing the pick times shifted to the nearest amplitude extremum.
        """

        return Log(self._dispatch.AdjustPickToExtremum(fws_log, arrival_log, prompt_user, config))

    def extract_window_peak_amplitude(self, log=None, prompt_user=None, config=None):
        """Extracts the maximum amplitude found in a time window of a FWS log trace.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log to process.
            If not provided, the process returns None.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [ExtractWindowPeakAmplitude]
                ; WindowStart : value or log name, units : us
                ; WindowLength : value, units : us
                ; PickType : 0 = peak, 1 = max, 2 = average
                WindowStart=0
                WindowLength=15
                PickMax=yes
                PickPos=yes
                PickType=1
                EnableResampling=yes

        Returns
        -------
        Log
            The resulting log containing the amplitude.
        """

        return Log(self._dispatch.ExtractWindowPeakAmplitude(log, prompt_user, config))

    def calculate_mechanical_properties(self, p_slowness=None, s_slowness=None, density=None):
        """Computes a set of rock mechanical parameters from the input data.

        Parameters
        ----------
        p_slowness : int or str, optional
            Zero based index or title of the log containing the p-slowness data.
            If not provided, the process dialog box will be displayed.
        s_slowness : int or str, optional
            Zero based index or title of the log containing the s-slowness data.
            If not provided, the process dialog box will be displayed.
        density :int or str, optional
            Zero based index or title of the log containing the density data.
        """

        self._dispatch.CalculateMechanicalProperties(p_slowness, s_slowness, density)

    def integrated_travel_time(self, log=None, prompt_user=None, config=None):
        """Computes the integrated travel time from slowness or velocity data.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log to process.
            If not provided, the process returns None.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [IntegratedTravelTime]
                TimeOffset = 0 'in us
                TWT = Yes/No

        Returns
        -------
        Log
            The resulting log containing the integrated times.
        """

        return Log(self._dispatch.IntegratedTravelTime(log, prompt_user, config))

    def bond_index(self, log=None, prompt_user=None, config=None):
        """Computes the bond index of the cement behind the casing.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log to process.
            If not provided, the process returns None.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [FwsBondIndex]
                CementAmplitude = 2 'in mV
                FreePipeAmplitude = 62.2 'in mV

        Returns
        -------
        Log
            The resulting log containing the bond index.
        """

        return Log(self._dispatch.BondIndex(log, prompt_user, config))

    def compressive_strength(self, log=None, prompt_user=None, config=None):
        """Computes the compressive strength of the cement behind a casing.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log to process.  A cement bond amplitude log (Well or Mud log type)
            or amplitude map (Image log) can be used.
            If not provided, the process returns None.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [FwsCompressiveStrength]
                CasingOD = 7 ' in inch
                CasingWeight = 23 ' in lbs/ft

        Returns
        -------
        Log
            The resulting log containing the compressive strength.
        """

        return Log(self._dispatch.CompressiveStrength(log, prompt_user, config))

    def apply_natural_gamma_borehole_correction(self, log=None, prompt_user=None, config=None):
        """Applies borehole corrections to FWS and Well logs

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log to process.
            If not provided, the process dialog box will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [BoreholeConditionCorrections]
                DeadTime = 7.2 ' in us
                EnableDeadTime = yes
                EnableFactors = yes
                FactorName1 = Water Factor
                FactorName2 = Pipe Factor
                Top1 = 0.0
                Bot1 = 2.85
                Factor1-1 = 1
                Factor1-2 = 1.49
                Top2 = 2.85
                Bot2 = bot
                Factor2-1 = 1.12
                Factor2-2 = 1

        Returns
        -------
        Log
            A log containing the corrected count rates.
        """

        return Log(self._dispatch.ApplyNaturalGammaBoreholeCorrection(log, prompt_user, config))

    def apply_total_gamma_calibration(self, log=None, prompt_user=None, config=None):
        """Applies a calibration factor or equation to the values in the specified Well Log.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log to process.
            If not provided, the process dialog box will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [BoreholeConditionCorrections]
                K-Factor=2*0.00001028

        Returns
        -------
        Log
            A log containing the modified gamma values.
        """

        return Log(self._dispatch.ApplyTotalGammaCalibration(log, prompt_user, config))

    def calculate_spectrum_total_count(self, log=None, prompt_user=None, config=None):
        """Extracts the total count, min, max, average or median from each spectrum trace of the specified log

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log to process.
            If not provided, the process dialog box will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [SpectralGamma_Statistic]
                ; WinLow, WinHigh expressed in channel number or keV according to Channel
                Total = yes
                Min = yes
                Max = yes
                Ave = yes
                Median = yes
                UseWindow = yes
                Channel = yes
                WinLow = 410
                WinHigh = 2850
        """

        self._dispatch.CalculateSpectrumTotalCount(log, prompt_user, config)

    def spectrometric_ratios(self, log_a=None, log_b=None, log_c=None, prompt_user=None, config=None):
        """Computes spectrometric ratios like U/Th or U/k

        By default, the ratios log_b/log_a, log_b/log_c and log_c/log_a
        will be computed.

        Parameters
        ----------
        log_a : int or str, optional
            Zero based index or title of the log to process.
        log_b : int or str, optional
            Zero based index or title of the log to process.
        log_c : int or str, optional
            Zero based index or title of the log to process.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [SpectrometricRatios]
                ; ratio : A / B
                A=K
                B=U
        """

        self._dispatch.SpectrometricRatios(log_a, log_b, log_c, prompt_user, config)

    def process_medusa_spectrum_data(self, log_spectrum=None, log_time=None, prompt_user=None, config=None):
        """Performs a full spectrum analysis using a calibration after Medusa

        Parameters
        ----------
        log_spectrum : int or str, optional
            Zero based index or title of the log to process.
            If not provided, the process dialog box will be displayed.
        log_time : int or str, optional
            Zero based index or title of the log with the live time data.
            If not provided, the process dialog box will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [SpectralGammaMedusaProcess]
                CalibrationFilePath = C:\\Temp\\NSG1234.mcf
                EnableFittedSpectrum = yes
                EnableConcentrationErrors = yes
                EnableStabilizationFactor = yes
                DeadTime = 5 (in us/pulse)
                HoleDiameter = 96 / Caliper (fixed value or data from log in mm)
                CasingThickness = 8 / Thickness (fixed value or data from log mm)
                CasingType = 0 (Steel) / 1 (PVC)
                FluidDensity = 1.1 / RHOFL (fixed value or data from log in g/ccm)
                FluidK = 0.0 / K (Potassium concentration in the fluid; fixed value or data from log in Bq/kg)
                FluidU = 0.0 / U (eq Uranium concentration in the fluid; fixed value or data from log in Bq/kg)
                FluidTh = 0.0 / Th (Thorium concentration in the fluid; fixed value or data from log in Bq/kg)
                ToolPosition = 0 (Alongside) / 1 (Centered)
                """
        self._dispatch.ProcessMedusaSpectrumData(log_spectrum, log_time, prompt_user, config)

    def process_spectrum_data(self, log=None, prompt_user=None, config=None):
        """Performs a windows stripping based on a calibration model

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log to process.
            If not provided, the process dialog box will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [SpectralGamma]
                OutputWindowCounts = yes / no
                ProcessModel = "C:\Temp\Test.sgm"
        """

        self._dispatch.ProcessSpectrumData(log, prompt_user, config)

    def compute_gr(self, log_k=None, log_u=None, log_th=None, prompt_user=None, config=None):
        """Computes total gamma ray from K, U and Th isotope concentrations using the MEDUSA
        calibration file.

        Parameters
        ----------
        log_k : int or str, optional
            Zero based index or title of the log containing the concentrations of K.
        log_u : int or str, optional
            Zero based index or title of the log containing the concentrations of U.
        log_th : int or str, optional
            Zero based index or title of the log containing the concentrations of Th.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [SpectralGammaMedusaCGR]
                CalibrationFilePath=C:\Tools\Calibrations\QL40-SGR-154904.mcf

        Returns
        -------
        Log
            A log containing the gamma ray values.
        """

        return Log(self._dispatch.ComputeGR(log_k, log_u, log_th, prompt_user, config))

    def process_nmrsa_data(self, log=None, prompt_user=None, config=None):
        """Performs a post-processing of NMRSA's BMR tool raw data.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log to process.
            If not provided, the process dialog box will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path and name of the configuration file or a parameter string.  The configuration file or
            string can contain the following options:

            .. code-block:: ini

                [NMRSA]
                UseDefaultOutputs = yes / no
                MasterCalibrationFile=
                ProcessingConfigurationFile=
                DepthRange=Maximum / UserDefined / Zones /LogZones
                TopDepth=20
                BottomDepth=22
                LogZones : top1, bot1, top2, bot2, ... topN, botN
                LogZonesDepthRange=logname, depthsectionName1, depthsectionName2, ....depthsectionname3
        """

        self._dispatch.ProcessNMRSAData(log, prompt_user, config)

    def nmr_total_porosity(self, log=None, prompt_user=None, config=None):
        """Computes the total porosity from a T2 distribution.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log to process.
            If not provided, the process dialog box will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path and name of the configuration file or a parameter string.  The configuration file
            or string can contain the following options:

            .. code-block:: ini

                [NMRTotalPorosity]
                MaxCutoffValue=-1
                UseTimeMaxCutoff= yes / no

                DepthRange=Maximum / UserDefined / Zones /LogZones
                TopDepth=20
                BottomDepth=22
                LogZones : top1, bot1, top2, bot2, ... topN, botN
                LogZonesDepthRange=logname, depthsectionName1, depthsectionName2, ....depthsectionname3

        Returns
        -------
        Log
            The resulting log object
        """

        return Log(self._dispatch.NMRTotalPorosity(log, prompt_user, config))

    def nmr_permeability(self, log=None, prompt_user=None, config=None):
        """Computes the permeability from a T2 distribution.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log to process.
            If not provided, the process dialog box will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path and name of the configuration file or a parameter string.  The configuration file
            or string can contain the following options:

            .. code-block:: ini

            [NMRPermeability]
            T2DistributionTraceUnit= seconds / milliseconds
            UseTimeMaxCutoff= yes / no
            MaxCutoffValue=-1
            DisplayTIMModel= yes / no
            VariableCforTIMModel=1
            ExponentMforTIMModel=4
            BFVCutoffForTIMModel=2
            BFVCutoffForTIMModel=0.3
            UseTimeMaxForFFVCutoff= yes / no
            FFVCutoffForTIMModel=0
            DisplaySDRModel= yes / no
            VariableCforSDRModel=4
            ExponentMforSDRModel=4
            ExponentNforSDRModel=2
            DisplayT2LogMean= yes / no
            DepthRange=Maximum / UserDefined / Zones /LogZones
            TopDepth=20
            BottomDepth=22
            LogZones : top1, bot1, top2, bot2, ... topN, botN
            LogZonesDepthRange=logname, depthsectionName1, depthsectionName2, ....depthsectionname3
        """

        self._dispatch.NMRPermeability(log, prompt_user, config)

    def nmr_fluid_volumes(self, log=None, prompt_user=None, config=None):
        """Computes the fluid volumes from a T2 distribution.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log to process.
            If not provided, the process dialog box will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path and name of the configuration file or a parameter string.  The configuration file
            or string can contain the following options:

            .. code-block:: ini

            [NMRFluidVolumes]
            LithoDatabase=
            UseLithoDatabaseAssociatedColor= yes/no
            Components=
            Cutoff=
            DepthRange=Maximum / UserDefined / Zones /LogZones
            TopDepth=20
            BottomDepth=22
            LogZones : top1, bot1, top2, bot2, ... topN, botN
            LogZonesDepthRange=logname, depthsectionName1, depthsectionName2, ....depthsectionname3

        Returns
        -------
        Log
            The resulting log object
        """

        return Log(self._dispatch.NMRFluidVolumes(log, prompt_user, config))

    def water_salinity(self, log=None, prompt_user=None, config=None):
        """Salinity estimation from fluid conductivity.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the fluid conductivity log to process.
            If not provided, the process returns None.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [WaterSalinity]
                Temperature = log name or constant value
                TemperatureUnit = degC / degF / degK

        Returns
        -------
        Log
            A log of the resulting salinity.
        """

        return Log(self._dispatch.WaterSalinity(log, prompt_user, config))

    def water_resistivity(self, log=None, prompt_user=None, config=None):
        """Temperature correction for fluid conductivity or resistivity.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log containing the conductivity or resistivity values.
            If not provided, the process returns None.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : bool, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

             .. code-block:: ini

                [WaterResistivity]
                Temperature = log name or constant value
                TemperatureUnit = degC / degF / degK
                RefTemperature = log name or constant value
                RefTemperatureUnit = degC / degF / degK
                Method = 0 (Arp) / 1 (Hilchie)

        Returns
        -------
        Log
            A log of the corrected conductivity or resistivity.
        """

        return Log(self._dispatch.WaterResistivity(log, prompt_user, config))

    def shale_volume(self, log=None, prompt_user=None, config=None):
        """Estimates the shale volume from Gamma Ray or SP data.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the well or mud log containing the Gamma Ray or SP values.
            If not provided, the process returns None.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : bool, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

             .. code-block:: ini

                [ShaleVolume]
                Equation = 0
                ; 0 = Linear (default), 1 = Larionov (Tertiary), 2 = Steiber,
                ; 3 = Clavier, 4 = Larionov (older rocks)
                Shale=150
                ShaleValueType=1
                ; ...Type: 0 = value, 1 = minmax, 2 = avginterval
                ShaleTopDepth=0
                ShaleBotDepth=0
                Sandstone=75
                SandstoneValueType=1
                ; ...Type: 0 = value, 1 = minmax, 2 = avginterval
                SandstoneTopDepth=0
                SandstoneBotDepth=0

        Returns
        -------
        Log
            A log of the resulting shale volume.
        """

        return Log(self._dispatch.ShaleVolume(log, prompt_user, config))

    def porosity_sonic(self, log=None, prompt_user=None, config=None):
        """Computes porosity from transit time data.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the well or mud log containing the formation resistivity (Rt) values.
            If not provided, the process returns None.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : bool, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [PorositySonic]
                ; Method : 0 = Wylie, 1 = WylieCompaction, 2 = AbbreviatedRaymerHunt, 3 = RaymerHunt
                ; Slowness units: us/ft, us/m, ft/us, m/s
                Method = 1
                MatrixSlowness = log name or constant value
                MatrixSlownessUnit = us/ft
                FluidSlowness= = log name or constant value
                FluidSlownessUnit = us/ft
                Compaction= = log name or constant value
                C = 0.67

        Returns
        -------
        Log
            A log of the resulting porosity.
        """

        return Log(self._dispatch.PorositySonic(log, prompt_user, config))

    def porosity_archie(self, log=None, prompt_user=None, config=None):
        """Computes porosity from formation resistivity data.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the well or mud log containing the formation resistivity (Rt) values.
            If not provided, the process returns None.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : bool, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [PorosityArchie]
                ; Method : 0 = Standard, 1 = FreshWater, 2 = shale, 3= shaleAndFreshWater
                ; Rw and Rsh units: ohm.m, ohm.ft
                Method = 1
                Vsh = log name or constant value
                Rw = log name or constant value
                RwUnit=ohm.m
                Rsh = 30.0
                RshUnit=ohm.m
                CementationFactor = 1.0
                CementationExponent = 2.0
                Cs = 1.0

        Returns
        -------
        Log
            A log of the resulting porosity.
        """

        return Log(self._dispatch.PorosityArchie(log, prompt_user, config))

    def porosity_density(self, log=None, prompt_user=None, config=None):
        """Computes porosity from density data.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the well or mud log containing the  density values.
            If not provided, the process returns None.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : bool, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [PorosityDensity]
                ; Method : 0 = Standard, 1 = Shale
                ; MatrixDensity, FluidDensity, ShaleVolume : value or log
                ; Density units: g/cc or kg/m3
                MatrixDensity=2.7
                MatrixDensityUnit=g/cc
                FluidDensity=1.0
                FluidDensityUnit=g/cc
                ShaleVolume=0
                ShaleDensity=1.5
                ShaleDensityUnit=g/cc

        Returns
        -------
        Log
            A log of the resulting porosity.
        """

        return Log(self._dispatch.PorosityDensity(log, prompt_user, config))

    def porosity_neutron(self, log=None, prompt_user=None, config=None):
        """Applies a shale correction to neutron porosity data.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the well or mud log containing the neutron porosity values.
            If not provided, the process returns None.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : bool, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [PorosityNeutron]
                ; Vsh : log name
                ; ShaleNPhi = value
                Vsh=VSh
                ShaleNPhi=50

        Returns
        -------
        Log
            A log of the resulting corrected porosity.
        """

        return Log(self._dispatch.PorosityNeutron(log, prompt_user, config))

    def permeability(self, log=None, prompt_user=None, config=None):
        """Estimates permeability from porosity data.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the well or mud log containing the neutron porosity values.
            If not provided, the process returns None.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : bool, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [Permeability]
                CementationFactor=1.0

        Returns
        -------
        Log
            A log of the resulting permeability.
        """

        return Log(self._dispatch.Permeability(log, prompt_user, config))

    def hydraulic_conductivity(self, log=None, prompt_user=None, config=None):
        """Computes the hydraulic conductivity from permeability data.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the well or mud log containing the permeability values.
            If not provided, the process returns None.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : bool, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [HydraulicConductivity]
                ; Density, Viscosity, DensityTemperature, ViscosityTemperature : log name or value
                ; Temperature units : degC, degF, degK
                ; Permeability units : m2, Darcy, mD, sq.ft
                ; Density units : kg/m3, g/m3, g/cc, lb/in3, lb/ft3
                ; Viscosity units : Pa.s, cP, p, dyn.s/cm2
                Density=1000
                DensityUnit= kg/m3
                Viscosity=0.000890439
                ViscosityUnit=Pa.s
                DensityTemperature=25
                DensityTemperatureUnit=degC
                ViscosityTemperature=25
                ViscosityTemperatureUnit=degC

        Returns
        -------
        Log
            A Log object of the resulting hydraulic conductivity.
        """

        return Log(self._dispatch.HydraulicConductivity(log, prompt_user, config))

    def extract_grain_size_statistics(self, log=None, prompt_user=None, config=None):
        """Computes statistics from a grain size distribution curve.

        Parameters
        ----------
        log : int or str, optional
            Zero based index or title of the log containing the grain size values.
            If not provided, a dialog box displaying a list of available logs will be displayed.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : bool, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

             .. code-block:: ini

                [GrainSizeStatistics]
                ; Method : 0 = Logarithmic (original Folk and Ward; default),
                ; 1 = Geometric (modified Folk and Ward),
                ; 2 = Logarithmic method of moments,
                ; 3= Geometric method of moments
                Mean = yes
                Median = yes
                Sorting = yes
                Skewness = yes
                Kurtosis = yes
                Histo = yes
        """

        self._dispatch.ExtractGrainSizeStatistics(log, prompt_user, config)

    def grain_size_sorting(self, log_min, log_max, prompt_user=None, config=None):
        """Classifies grain size values based on min and max logs.

        Parameters
        ----------
        log_min : int or str, optional
            Zero based index or title of the log containing logged minimum grain size value.
            If not provided, the method returns None.
        log_max : int or str, optional
            Zero based index or title of the log containing logged maximum grain size value.
            If not provided, the method returns None.
        prompt_user : bool, optional
            Whether dialog boxes are displayed to interact with the user.
            If set to ``False`` the processing parameters will be retrieved from the specified
            configuration.  If no configuration has been specified, default values will be used.
            Default is True.
        config : bool, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

             .. code-block:: ini

                [GrainSizeSorting]
                ; Method : 0 = Logarithmic (original Folk and Ward; default),
                ; 1 = Geometric (modified Folk and Ward),
                ; 2 = Logarithmic method of moments,
                ; 3= Geometric method of moments
                BlockedAverage = yes

        Returns
        -------
        Log
            A log containing the sorted values
        """

        return Log(self._dispatch.GrainSizeSorting(log_min, log_max, prompt_user, config))

    def enable_protection(self, enable, password):
        """Changes the protection status of a document using a password

        Parameters
        ----------
        enable : bool
            Set to True to protect the borehole document.
        password : str
            The password used to allow this option.
        """

        self._dispatch.EnableProtection(enable, password)

    def allow_insert_log(self, enable, password):
        """Changes the protection status for inserting new logs.

        Parameters
        ----------
        enable : bool
            Set to True to allow adding new logs to the borehole document.
        password : str
            The password used to allow this option.
        """

        self._dispatch.AllowInsertLog(enable, password)

    def allow_save_template(self, enable, password):
        """Changes the protection status for saving layout templates.

        Parameters
        ----------
        enable : bool
            Set to True to allow saving layout templates of the borehole document.
        password : str
            The password used to allow this option.
        """

        self._dispatch.AllowSaveTemplate(enable, password)

    def allow_export_file(self, enable, password):
        """Changes the protection status for exporting data.

        Parameters
        ----------
        enable : bool
            Set to True to allow the export of data from the borehole document.
        password : str
            The password used to allow this option.
        """

        self._dispatch.AllowExportFile(enable, password)

    def allow_modify_annotation(self, enable, password):
        """Changes the protection status to modify annotations.

        Parameters
        ----------
        enable : bool
            Set to True to allow editing existing annotations in the borehole document.
        password : str
            The password used to allow this option.
        """

        self._dispatch.AllowModifyAnnotation(enable, password)

    def allow_insert_annotation(self, enable, password):
        """Changes the protection status for inserting annotations.

        Parameters
        ----------
        enable : bool
            Set to True to allow adding new annotations in the borehole document.
        password : str
            The password used to allow this option.
        """

        self._dispatch.AllowInsertAnnotation(enable, password)

    def allow_modify_headers_content(self, enable, password):
        """Changes the protection status of the header content.

        Parameters
        ----------
        enable : bool
            Set to True to allow edition of the document header data.
        password : str
            The password used to allow this option.
        """

        self._dispatch.AllowModifyHeadersContent(enable, password)
        