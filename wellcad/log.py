class Log:
	def __init__(self, log_dispatch):
		self.dispatch = log_dispatch
		
	
	def NbOfData(self):
		return self.dispatch.NbOfData
		
		
	def GetName(self):
		return self.dispatch.Name
		
		
	def SetName(self, name):
		self.dispatch.Name = name
		
