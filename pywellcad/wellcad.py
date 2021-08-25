from win32com.client import Dispatch
from pywellcad.borehole import *

class Application:

	def __init__(self) :
		self.dispatch = Dispatch("WellCAD.Application")
		

	def ShowWindow(self):
		self.dispatch.ShowWindow
		

	def MinimizeWindow(self):
		self.dispatch.MinimizeWindow()
		
		
	def MaximizeWindow(self):
		self.dispatch.MaximizeWindow()
		
		
	def Cascade(self):
		self.dispatch.Cascade()
		
	def TileHorizontally(self):
		self.dispatch.TileHorizontally()
		
	
	def TileVertically(self):
		self.dispatch.TileVertically()
		

	def NewBorehole(self, szTemplate = ""):
		self.dispatch._FlagAsMethod("NewBorehole")
		obBhole = self.dispatch.NewBorehole(szTemplate)
		return Borehole(obBhole)
		
		
	def OpenBorehole(self, szPath = ""):
		self.dispatch._FlagAsMethod("OpenBorehole")
		obBhole = self.dispatch.OpenBorehole(szPath)
		return Borehole(obBhole)
			
			
	def GetBorehole(self, index):
		self.dispatch._FlagAsMethod("GetBorehole")
		obBhole = self.dispatch.GetBorehole(index)
		return Borehole(obBhole)
		
		
	def GetActiveBorehole(self):
		obBhole = self.dispatch.GetActiveBorehole
		return Borehole(obBhole)
		
		
	def CloseBorehole(self, bPromptForSaving = True, index = -1):
		if index == -1:
			index = self.dispatch.NbOfDocuments - 1
		self.dispatch.CloseBorehole(bPromptForSaving, index)
		
		
	def GetBoreholeCount(self):
		return self.dispatch.NbOfDocuments
		
	
	def FileImport(self, filename = "", bPromptUser = True, configfile = "", logfile = ""):
		self.dispatch._FlagAsMethod("FileImport")
		obBhole = self.dispatch.FileImport(filename, bPromptUser, config, logfile)
		return Borehole(obBhole)
		
		
	def MultiFileImport(self, filename = "", bPromptUser = True, configfile = "", logfile = ""):
		self.dispatch._FlagAsMethod("MultiFileImport")
		obBhole = self.dispatch.MultiFileImport(filename, bPromptUser, config, logfile)
		return Borehole(obBhole)
		
		
	def Quit(self, bPromptForSaving = True):
		self.dispatch.Quit(bPromptForSaving)