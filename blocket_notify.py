from pywebnotify import pywebnotify
import urllib.request
import time

# Find the link based on the searched text
# Input works with string and array of strings alike
def get_offer_link(webpage, location, search_text, end_text):

	ending = 0
	
	if (isinstance(search_text, list)):
		for text in search_text:
			location = webpage.find(text, location)
	elif (isinstance(search_text, str)):
		location = webpage.find(text, location)
	
	ending = webpage.find(end_text, location)
	
	return location, webpage[location+len(text):ending]
	

if __name__ == '__main__':
		
	# Create new object
	blocket = pywebnotify()
	
	# Set Webpage address
	blocket.set_address("https://www.blocket.se/bostad/uthyres/stockholm?cg_multi=3020&sort=&ss=&se=&ros=&roe=&bs=&be=&mre=7000&q=&q=&q=&is=1&save_search=1&l=0&md=th&f=p&f=c&f=b&as=131_1&as=131_3&as=131_4&as=131_5&as=131_6&as=131_7&as=131_9&as=131_11&m=130&m=132")
	
	blocket.set_search_parameter ( "key_one", "param_one")
	
	# Print out all settings
	print (blocket.get_settings())
	
	while (True):
	
		webpage = str(urllib.request.urlopen(blocket.get_address()).read())
		
		location = 0
		n = 0
		
		while (location != -1):
		
			location, link = get_offer_link(webpage, location+1, ['<h4 class="media-heading">', 'href="'], '">')
			n += 1
			
			if (location==-1):
				break
			
			print (n, location, link)
		
		
		time.sleep(30)