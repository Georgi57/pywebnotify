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
	
	heading1 = webpage.find('<h4 class="media-heading">', first_offer)
			
	print (heading1, webpage[heading1:(heading1+100)])
	
	heading2 = webpage.find('href="', heading1)
	
	print (heading2, webpage[heading2:(heading2+100)])
	
	heading3 = webpage.find('">', heading2)
	
	print (heading3, webpage[heading2+6:heading3])
	
	#heading2 = webpage.find('">', first_offer)
	
	#print (heading1, heading2, webpage[heading1:heading2])

	