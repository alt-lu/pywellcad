class Header:
	def __init__(self, header_dispatch):
		self.dispatch = header_dispatch
		
	
	def GetItemText(self, item_name):
		return self.dispatch.ItemText(item_name)
	
	
	def SetItemText(self, item_name, item_text):
		self.dispatch.ItemText(item_name, item_text)
		
	def GetItemName(self, item_index):
		return self.dispatch.ItemName(item_name)
