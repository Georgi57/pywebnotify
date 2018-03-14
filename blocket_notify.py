from pywebnotify import pywebnotify

if __name__ == '__main__':
		
	# Create new object
	blocket = pywebnotify()
	
	# Set Webpage address
	blocket.set_address("https://www.blocket.se/bostad/uthyres/stockholm?sort=&f=p&f=c&f=b")
	
	blocket.set_search_parameter ( "key_one", "param_one")
	
	# Print out all settings
	print (blocket.get_settings())
	
    #page = urllib.request.urlopen(blocket)
