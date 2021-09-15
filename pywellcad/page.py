class Page:

	def __init__(self, page_dispatch):
		"""Creates the page object.
		
		Use the get_page method in the borehole object to retrieve
		an object for the document page.
		"""
		
		self.dispatch = page_dispatch