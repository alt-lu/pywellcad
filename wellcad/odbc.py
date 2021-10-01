class Odbc:

	def __init__(self, odbc_dispatch):
		"""Creates the odbc object.
		
		Use the get_odbc method in the borehole object to retrieve
		an object for the ODBC module.
		"""
		
		self.dispatch = odbc_dispatch