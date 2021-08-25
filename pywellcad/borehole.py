from pywellcad.log import *
from pywellcad.depth import *
from pywellcad.header import *


class Borehole:
	def __init__(self, borehole_dispatch):
		self.dispatch = borehole_dispatch
		
	def SetName(self, name):
		self.dispatch.Name = name
		
		
	def EnableAutoUpdate(self, bEnable):
		self.dispatch.AutoUpdate(bEnable)
		
		
	def IsAutoUpdateEnabled(self):
		return self.dispatch.AutoUpdate()
		
		
	def GetBottomDepth(self):
		return self.dispatch.BottomDepth
		
		
	def GetLog(self, log):
		self.dispatch._FlagAsMethod("Log")
		obLog = self.dispatch.Log(log)
		return Log(obLog)
		
		
	def InsertNewLog(self, logType):
		obLog = self.dispatch.InsertNewLog(logType)
		return Log(obLog)
		
		
	def ConvertLogTo(self, log, logType, bPromptUser, config):
		self.dispatch._FlagAsMethod("ConvertLogTo")
		obLog = self.dispatch.ConvertLogTo(log, logType, bPromptUser, config)
		return Log(obLog)
		
		
	def GetDepth(self):
		obDepth = self.dispatch.Depth
		return Depth(obDepth)
		
		
	def GetHeader(self):
		obHeader = self.dispatch.Header
		return Header(obHeader)