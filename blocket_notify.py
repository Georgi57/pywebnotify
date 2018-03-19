from pywebnotify import pywebnotify
import urllib.request

# Find the link based on the searched text
# Input works with string and array of strings alike
def get_offer_link(webpage, search_text, end_text):

	location = 0
	ending = 0
	
	if (isinstance(search_text, list)):
		for text in search_text:
			location = webpage.find(text, location)
	elif (isinstance(search_text, str)):
		location = webpage.find(text, location)
	
	ending = webpage.find(end_text, location)
	
	return webpage[location+len(text):ending]
	

if __name__ == '__main__':
		
	# Create new object
	blocket = pywebnotify()
	
	# Set Webpage address
	blocket.set_address("https://www.blocket.se/bostad/uthyres/stockholm?sort=&f=p&f=c&f=b")
	
	blocket.set_search_parameter ( "key_one", "param_one")
	
	# Print out all settings
	print (blocket.get_settings())
	
	webpage = str(urllib.request.urlopen(blocket.get_address()).read())
	
	print (get_offer_link(webpage, ['<h4 class="media-heading">', 'href="'], '">'))

	print (get_offer_link(webpage, ['<h4 class="media-heading">', '<span class="li_detail_params monthly_rent">'], "/span>"))