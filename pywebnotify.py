import urllib.request

class pywebnotify:

	def __init__ ( self ):
		self.address = ""
		self.parameters = {}

	def get_settings ( self ):
		
		# Address
		settings = ""
		settings += self.address + "\n"
		
		# Parameters
		for param in self.parameters:
			settings += str ( param ) + " : " + str ( self.parameters[param] ) + "\n"
		
		return settings
	
	def set_address ( self, address ):
		self.address = str(address)
		
	def get_address ( self ):
		return self.address
	
	def set_search_parameter (self, key, value):
		self.parameters[key]=value
	
