from ._dispatch_wrapper import DispatchWrapper


class Workspace(DispatchWrapper):
    """Use functionalities from the Image & Structure Interpretation Workspace (ISI Workspace)
    and the Casing Integrity Workspace.

    Example
    -------
    >>> borehole = app.get_active_borehole()
    >>> workspace = borehole.workspace("ISI workspace")
    >>> workspace.representative_picks(config_file_name=config_file)
    """
    _DISPATCH_METHODS = ("PickSimilarFeatures", "RepresentativePicks", )

    def auto_detect_zones(self):
        """Automaticaly detects zones in the image log of a workspace."""
        self._dispatch.AutoDetectZones()

    def pick_similar_features(self, config_file_name):
        """Runs an automated similar structure picking in ISI workspace.

        The Pick Similar Features process takes one or more manual
        picks as input, runs the automated picking and keeps only
        picks which do not deviate from the reference(s) by a defined
        tolerance value in Dip Azimuth and Dip angle. Picks detected
        as similar are then added to the pick repository.
        You need to have **manually** selected the input picks first
        in the WellCAD window.

        Parameters
        ----------
        config_file_name : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [PickSimilarFeatures]
                InputLog = (title of the log to process)
                TopDepth = 0 '(top of the interval to process)
                BottomDepth = 10 '(top of the interval to process)
                ImageType = 3 '(0 = RGB OTV, 1 = Greyscale OTV, 2 = Diamond Drilled ATV, 3 = RC Drilled ATV, 4 = FMI)
                DarkFeatures = yes /no
                BrightFeatures = yes / no
                Aperture = yes / no
                PartialPicks = yes / no
                AzimuthTolerance = 5.0
                TiltTolerance = 5.0 '(i.e. dip angle tolerance)
                UseDefaultSettings = yes / no

                ' Processing Paraemters
                ImageWidth = 144
                ImageSmoothingIterations = 2
                MinimumFeatureSize = 5
                DesiredFeatureStrength = 0.5
                MinimumFeatureStrength = 0.2
                MinimumStructureAperture = 0.008
                MaximumStructureAperture = 0.032
                SinusoidalDeviationTolerance = 30
                MaximumSinusoidAmplitude = 0.6
                MinimumSinusoidAmplitude = 0

                ' Advanced Processing Parameters
                FeatureDistanceDeviation = 2
                FeatureOrientationDeviation = 20
                HandleOverlappingSinusoids = 1 '(1 = yes, 0 = no)
                FeatureMergingConstraint = 0.6
                SinusoidCompleteness = 1 '(1 = yes, 0 = no)
                ClusterDipTolerance = 15
                ClusterAzimuthTolerance = 15
                DepthOffsetTolerance = 30
                PixelBrightnessTolerance = 1
                ImageSmoothingStrength = 20
                ImageSmoothingSpeed = 0.25
                ImageContrastSensitivity = 0.05

        """
        self._dispatch.PickSimilarFeatures(config_file_name)

    def representative_picks(self, config_file_name):
        """Runs the representative picks process in ISI

        The representative Picks process uses an adapted Ward
        algorithm to cluster picks which have the least dissimilarity
        in azimuth, dip, depth distance from each other and pick type
        (i.e. classification). As a result it determines the most
        representative pick of each cluster - i.e. the (real) pick
        with the highest confidence and closest to the center of each
        cluster.

        Parameters
        ----------
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [RepresentativePicks]
                InputLog = '(title of the log to process)
                TopDepth = 0 '(top of the interval to process)
                BottomDepth = 10 '(top of the interval to process)
                AzimuthWindow = 5.0
                TiltWindow = 5.0'(i.e. dip angle window)
                DepthWindow = 0.5
                KeepFeaturesUngrouped = yes / no
        """
        self._dispatch.RepresentativePicks(config_file_name)

    def automatic_picking(self, config_file_name):
        """Runs an automated structure picking in the ISI workspace

        The Auto Picker allows the detection of planar structures in
        televiewer (ATV, OTV) and electrical imager (e.g. FMI) images.
        3D core scans are similar to OTV images and can be processed
        as well.

        Parameters
        ----------
        config : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [AutomaticPicking]
                InputLog = Amplitude '(title of the log to process)
                TopDepth = 0 '(top of the interval to process)
                BottomDepth = 10 '(top of the interval to process)
                ImageType = 3 '(0 = RGB OTV, 1 = Greyscale OTV, 2 = Diamond Drilled ATV, 3 = RC Drilled ATV, 4 = FMI)
                DarkFeatures = yes /no
                BrightFeatures = yes / no
                Aperture = yes / no
                PartialPicks = yes / no
                UseDefaultSettings = yes / no

                ' Processing Parameters
                ImageWidth = 144
                ImageSmoothingIterations = 2
                MinimumFeatureSize = 5
                DesiredFeatureStrength = 0.5
                MinimumFeatureStrength = 0.2
                MinimumStructureAperture = 0.008
                MaximumStructureAperture = 0.032
                SinusoidalDeviationTolerance = 30
                MaximumSinusoidAmplitude = 0.6
                MinimumSinusoidAmplitude = 0

                ' Advanced Processing Parameters
                FeatureDistanceDeviation = 2
                FeatureOrientationDeviation = 20
                HandleOverlappingSinusoids = 1 '(1 = yes, 0 = no)
                FeatureMergingConstraint = 0.6
                SinusoidCompleteness = 1 '(1 = yes, 0 = no)
                ClusterDipTolerance = 15
                ClusterAzimuthTolerance = 15
                DepthOffsetTolerance = 30
                PixelBrightnessTolerance = 1
                ImageSmoothingStrength = 20
                ImageSmoothingSpeed = 0.25
                ImageContrastSensitivity = 0.05
        """
        self._dispatch.AutomaticPicking(config_file_name)

    def quick_pick(self, config_file_name):
        """Runs a quick pick in ISI

        The Quick Pick Process analyzes the image for features with
        the highest confidence within given Azimuth, Dip and Depth
        tolerances. E.g. if you would like to pick just the main event
        every 1m interval and leave all other features unaccounted you
        can use this process.

        Parameters
        ----------
        config_file_name : str, optional
            Path to a configuration file or a parameter string. The
            configuration file can contain the following options:

            .. code-block:: ini

                [QuickPick]
                InputLog = Amplitude '(title of the log to process)
                TopDepth = 0 '(top of the interval to process)
                BottomDepth = 10 '(top of the interval to process)
                ImageType = 3 '(0 = RGB OTV, 1 = Greyscale OTV, 2 = Diamond Drilled ATV, 3 = RC Drilled ATV, 4 = FMI)
                DarkFeatures = yes /no
                BrightFeatures = yes / no
                Aperture = yes / no
                PartialPicks = yes / no
                AzimuthWindow = 5.0
                TiltWindow = 5.0'(i.e. dip angle window)
                DepthWindow = 0.5
                UseDefaultSettings = yes / no

                ' Processing Parameters
                ImageWidth = 144
                ImageSmoothingIterations = 2
                MinimumFeatureSize = 5
                DesiredFeatureStrength = 0.5
                MinimumFeatureStrength = 0.2
                MinimumStructureAperture = 0.008
                MaximumStructureAperture = 0.032
                SinusoidalDeviationTolerance = 30
                MaximumSinusoidAmplitude = 0.6
                MinimumSinusoidAmplitude = 0

                ' Advanced Processing Parameters
                FeatureDistanceDeviation = 2
                FeatureOrientationDeviation = 20
                HandleOverlappingSinusoids = 1 '(1 = yes, 0 = no)
                FeatureMergingConstraint = 0.6
                SinusoidCompleteness = 1 '(1 = yes, 0 = no)
                ClusterDipTolerance = 15
                ClusterAzimuthTolerance = 15
                DepthOffsetTolerance = 30
                PixelBrightnessTolerance = 1
                ImageSmoothingStrength = 20
                ImageSmoothingSpeed = 0.25
                ImageContrastSensitivity = 0.05
        """

        self._dispatch.QuickPick(config_file_name)

    def apply_template(self, path, prompt_if_not_found=None, config_file_name=None):
        """Applies a workspace template
        
        Allows the application of an ISI Workspace,
        Casing Integrity Workspace or NMR Workspace template.

        Parameters
        ----------
        path: str
            String specifying the name and path of the
            workspace template to be applied (\*.ist). Please note
            that the file extension is different for the
            ISI, Casing Integrity and NMR Workspaces.
        prompt_if_not_found: bool, optional
            Boolean indicating whether the dialog box to
            prompt the user for logs not found in the
            template is displayed or not. The default is
            set to True.
        config_file_name : str, optional
            The configuration file. Read the WellCAD Help for
            information on the syntax of the file.

        Returns
        -------
        bool
            Always returns True except for the WellCAD Reader and
            Demo version for which the function returns False.
        """
        return self._dispatch.ApplyTemplate(path, prompt_if_not_found, config_file_name)

    def auto_joint_detection(self, config_file_name):
        """Detects the joints from the main log (data source) used
        in the workspace.

        Parameters
        ----------
        config_file_name : str
            \*.ini file containing the processing parameters.
            Read the WellCAD Help for information on the
            syntax of the file.
        """
        self._dispatch.AutoJointDetection(config_file_name)

    def add_joint_log_to_b_hole(self):
        """Adds the Marker Log from the Casing Integrity
        Workspace displaying the casing joints back to the
        borehole document.
        """
        self._dispatch.AddJointLogToBHole()

    def add_engin_log_from_driller_casing_table_to_b_hole(self):
        """Adds the Engineering Log from the Navigation Bar
        of the Casing Integrity Workspace displaying the
        drillers casing info back to the borehole document.
        """
        self._dispatch.AddEnginLogFromDrillerCasingTableToBHole()

    def add_engin_log_from_logger_casing_table_to_b_hole(self):
        """Adds the Engineering Log from the Navigation Bar
        of the Casing Integrity Workspace displaying the
        casing info derived from the logged data back to the
        borehole document.
        """
        self._dispatch.AddEnginLogFromLoggerCasingTableToBHole()
