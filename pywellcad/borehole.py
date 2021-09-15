from pywellcad.log import *
from pywellcad.depth import *
from pywellcad.header import *
from pywellcad.title import *
from pywellcad.page import *
from pywellcad.workspace import *
from pywellcad.odbc import *


class Borehole:
	
	def __init__(self, borehole_dispatch):
		"""Creates the borehole object.
		
		Use the NewBorehole, OpenBorehole or FileImport methods
		of the wellcad object to retrieve a borehole.
		"""

		self.dispatch = borehole_dispatch


# Methods for general document handling

	def set_name(self, name):
		"""Sets the title of a borehole document.
		
		Arguments:
			name -- String specifying the new name of the document.
		"""

		self.dispatch.Name = name


	def get_name(self):
		"""Returns the title of a borehole document."""
		return self.dispatch.Name
		
		
	def enable_auto_update(self, enable):
		"""Enables/disables the automatic refresh of the screen.
		
		Arguments:
			enable -- Boolean enabling the auto refresh if set to True.
		"""

		self.dispatch.AutoUpdate = enable		

		
	def is_auto_update_enabled(self):
		"""Returns True if the automatic screen refresh is enabled."""
		return self.dispatch.AutoUpdate


	def refresh_window(self):
		"""Performs a one time refresh of the borehole view"""
		self.dispatch.RefreshWindow()


	def set_draft_mode(self, index):
		"""Toggles the view of the borehole document.
		
		A borehole document can be displayed in the following modes:
		0 - Page Layout
		1 - Draft and fit
		2 - Draft

		Arguments:
			index -- Integer specifying the document viewing mode
		"""

		self.dispatch.SetDraftMode(index)


	def minimize_window(self):
		"""Shrinks the document window to an icon.
		
		Works only if document windows are not tabbed.
		"""

		self.dispatch.MinimizeWindow()

	
	def maximize_window(self):
		"""Enlarges the document window to fit the WellCAD frame.
		
		Works only if document windows are not tabbed.
		"""

		self.dispatch.MaximizeWindow()
		

	def get_bottom_depth(self):
		"""Returns the bottom of the document in actual depth units."""
		return self.dispatch.BottomDepth


	def get_top_depth(self):
		"""Returns the top of the document in actual depth units."""
		return self.dispatch.TopDepth


	def set_visible_depth_range(self, top_depth, bottom_depth):	
		"""Adjusts the depth range displayed in a borehole view.
		
		Arguments:
			top_depth -- Depth at which the data display should start.
			bottom_depth -- Depth at which the data display terminates.
		"""

		self.dispatch.SetVisibleDepthRange(top_depth, bottom_depth)


	def get_depth(self):
		"""Returns a depth object for the master depth axis."""
		obdepth = self.dispatch.Depth
		return Depth(obdepth)
		
		
	def get_header(self):
		"""Header object for the entire borehole document header."""
		obheader = self.dispatch.Header
		return Header(obheader)


	def get_page(self):
		"""Returns a page object for the borehole document."""
		obpage = self.dispatch.Page
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

		self.dispatch._FlagAsMethod("CreateNewWorkspace")
		obworkspace = self.dispatch.CreateNewWorkspace(workspace_type, config)
		return Workspace(obworkspace)


	def get_workspace(self,workspace_id):
		"""Retrieve an object for a workspace in the document.
		
		Arguments: 
			workspace_id --- Zero based index or title of the workspace
							 present in the borehole document.
		"""

		self.dispatch._FlagAsMethod("CreateNewWorkspace")
		obworkspace = self.dispatch.Workspace(workspace_id)
		return Workspace(obworkspace)


	def get_odbc(self):
		"""Returns an object to access the ODBC module."""
		obj_odbc = self.dispatch.ODBC
		return ODBC(obj_odbc) 


	def connect_to(self, server_name, server_address, port_number="1600"):
		"""Connect WellCAD to the ALT logging system.
		
		Arguments:
			server_name -- Must be set to 'TFD'.
			server_address -- IP address of the computer to connect to.
			port_number -- Part number used (default is 1600).
		
		"""

		self.dispatch.ConnectTo (server_name, server_address, port_number)


	def disconnect_from(self, server_name, server_address):
		"""Cuts the connection between WellCAD and the logging system.
		
		Arguments:
			server_name -- Must be set to 'TFD'.
			server_address -- IP address of the computer to connect to.
		"""

		self.dispatch.DisconnectFrom (server_name, server_address)
		

	def save_as(self, file_name):
		"""Saves the borehole document as WCL file.
		
		Arguments:
			file_name -- Path and file name (e.g. C:\Temp\Well1.wcl)

		Returns:
			True if the saving process was successfull. 
		"""

		return self.dispatch.SaveAs(file_name)


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
		self.dispatch.FileExport(file_name,
								 prompt_user,
								 config,
								 logfile)


	def do_print(self,
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

		self.dispatch.DoPrint(self,
							 enable_dialog,
							 top_depth,
							 bottom_depth,
							 nb_of_copies)


# Methods for general log handling

	def get_nb_of_logs(self):
		"""Number of logs present in the borehole document."""
		return self.dispatch.NbOfLogs

	
	def get_log(self, log):
		"""Accesses and existing log and reates a new log object.
		
		Arguments:
			log -- The zero based index (integer) 
				   or the title (string) of the log.

		Returns:
			A log object.
		"""

		self.dispatch._FlagAsMethod("Log")
		obLog = self.dispatch.Log(log)
		return Log(obLog)


	def get_title(self, log_name):
		"""Returns an object fr the tile of a log.

		Arguments:
			log_name -- Title of the log as shown in the propeties.

		"""

		self.dispatch._FlagAsMethod("Title")
		obTitle = self.dispatch.Title(log_name)
		return Title(obTitle)


	def insert_new_log(self, log_type):
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
		25 - Marker Log
		
		Arguments:
			log_type -- Integer specifying the type of log. 

		Returns:
			A log object.
		"""

		obLog = self.dispatch.InsertNewLog(log_type)
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
		
		self.dispatch._FlagAsMethod("ConvertLogTo")
		obLog = self.dispatch.ConvertLogTo(log, log_type, prompt_user, config)
		return Log(obLog)


	def add_log(self, oblog_orig):
		"""Copy and pastes a log.
		
		Copies a log within the same or between two borehole documents.

		Arguments:
			oblog_orig -- An object of the log to copy.
		Returns:
			An object of the copied log.
		"""

		oblog_copy = self.dispatch.AddLog(oblog_orig)
		return Log(oblog_copy)


	def remove_log(self, log):
		"""Deletes the specified log from the borehole document.
		
		Arguments:
			log -- Zero based index (integer) or title (string)
				   of the log to delete.
		"""

		self.dispatch.RemoveLog(log)


	def clear_log_contents(self, log):
		"""Removes the data from a log and leaves the log empty.
		
		Arguments:
			log -- Zero based index (integer) or title (string).
		"""

		self.dispatch.ClearLogContents(log)


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

		self.dispatch.ApplyTemplate(path,
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

		self.dispatch.SliceLog(log,
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

		self.dispatch.MergeLogs(log_a, log_b, ave_overlap, create_new)


	def merge_same_log_items(self, log):
		"""Merges data intervals with same litho codes.
		
		Arguments:
			log -- Zero based index (integer) or title (string) of
				   the Litho log.
		"""

		self.dispatch.MergeSameLogItems(log)


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

		self.dispatch.ExtendLog(log, top_depth, bottom_depth)


	def depth_shift_log(self,
						log,
						shift,
						top_depth="",
						bottom_depth=""):
		"""Performs a bulk shift to all the data within the log.

		Arguments:
			log -- Zero based index (integer) or title (string) of
				   the log.
			shift -- Amount of the depth shift (positive = down,
					 negative = up).
			top_depth -- Upper depth limit of the shifted interval.
			bottom_depth -- Lower depth limit of the shifted interval.
		"""

		self.dispatch.DepthShiftLog(log,
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
		
		self.dispatch.DepthMatchLog(log, depth_log)


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

		self.dispatch.FillLog(log,
							  top_depth,
							  bottom_depth,
							  step,
							  thickness,
							  user_defined_intervals,
							  interval_log)


# Common log processes

	def normalize(self, log, prompt_user=True, config=""):
		"""Normalizes the data in a Percentage or Analysis Log.

		For a full list of prcessing parameters please refer to the
		WellCAD help documentation.

		Arguments:
			log -- Zero based index (integer) or title (string) of
				   the log to normalize.
			prompt_user -- If set to False the processing parameters
						   will be taken from config.
			config -- Path and name of the configuration file or
					  parameter string.
		
		"""

		self.dispatch.normalize(log, prompt_user, config)

