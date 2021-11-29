class Workspace:

    def __init__(self, workspace_dispatch):
        """Creates the workspace object.
        
        Use the get_workspace method in the borehole object to retrieve
        an object for the workspace.
        """
        
        self.dispatch = workspace_dispatch


    def apply_template(self, template, prompt_user=True, config=""):
        """Applies a workspace template
        
        This mehtod applies a template to ISI, Casing Integrity and
        NMR workspaces.
        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation.

        Arguments:
            template --- string specifying the path and name of the
                         template file
            prompt_user -- If set to False the processing parameters
                           will be taken from the config file.
            config -- Path and name of the configuration file.

        """

        self.dispatch.ApplyTemplate(template, prompt_user, config)


# Image and Structure Interpretation (ISI) workspace

    def auto_zonation(self):
        """Detects zones from the ICM in the ISI workspace
        
        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation.

        """

        self.dispatch.AutoDetectZones()


    def auto_picking(self, config):
        """Runs an automated structure picking in the ISI workspace
        
        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation.

        Arguments:
            config -- Path and name of the configuration file
                      containing the processing parameters.	

        """

        self.dispatch.AutomaticPicking(config)


    def pick_similar_features(self, config):
        """Runs an automated similar structure picking in ISI
        
        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation.

        Arguments:
            config -- Path and name of the configuration file
                      containing the processing parameters.	

        """

        self.dispatch.PickSimilarFeatures(config)


    def pick_similar_features(self, config):
        """Runs a quick pick in ISI
        
        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation.

        Arguments:
            config -- Path and name of the configuration file
                      containing the processing parameters.	

        """

        self.dispatch.QuickPick(config)


    def representative_picks(self, config):
        """Runs the representative picks process in ISI
        
        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation.

        Arguments:
            config -- Path and name of the configuration file
                      containing the processing parameters.	

        """

        self.dispatch.RepresentativePicks(config)


# Casing integrity workspace

    def joint_detection(self, config):
        """Detects joints from the main log in the Casing Integrity workspace
        
        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation.

        Arguments:
            config -- Path and name of the configuration file
                      containing the processing parameters.

        """

        self.dispatch.AutoJointDetection(config)


    def export_driller_engineering_log(self):
        """Adds the log generated from the driller table to the document
        
        A full description of the method is given
        in the Automation Module chapter of the WellCAD help
        documentation.

        """

        self.dispatch.AddEnginLogFromDrillerCasingTableToBHole()


    def export_logger_engineering_log(self):
        """Adds the log generated from the logged data to the document
        
        A full description of the method is given
        in the Automation Module chapter of the WellCAD help
        documentation.

        """

        self.dispatch.AddEnginLogFromLoggerCasingTableToBHole()


    def export_joints(self):
        """Adds the log containing the joints to the borehole document
        
        A full description of the method is given
        in the Automation Module chapter of the WellCAD help
        documentation.

        """

        self.dispatch.AddJointLogToBHole()