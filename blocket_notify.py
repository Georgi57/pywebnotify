from pywebnotify import pywebnotify
import urllib.request

if __name__ == '__main__':
		
	# Create new object
	blocket = pywebnotify()
	
	# Set Webpage address
	blocket.set_address("https://www.blocket.se/bostad/uthyres/stockholm?sort=&f=p&f=c&f=b")
	
	blocket.set_search_parameter ( "key_one", "param_one")
	
	# Print out all settings
	print (blocket.get_settings())
	
	webpage = str(urllib.request.urlopen(blocket.get_address()).read())
	
	first_offer = webpage.find("<div itemscope itemtype=")
	second_offer = webpage.find("<div itemscope itemtype=", first_offer+1)
	
	print (first_offer, second_offer)