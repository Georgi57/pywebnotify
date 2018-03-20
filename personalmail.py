# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class pymailnotify:

	def __init__ ( self ):
		# Get my personal email details first.
		# Saved in a separate file. Obviously not commited.
		
		# Read from file
		file = open( "personalmail.txt", "r" )
		personal_email_details = file.read()
		file.close()
		
		# email and its password are separated by a space
		separation = personal_email_details.find(" ")
		self.personal_email = personal_email_details[:separation]
		self.personal_email_password = personal_email_details[separation+1:]
		
		print (self.personal_email, "used for notifications")
		
	def notify( self, message ):
	
		# DO not want to be logged in all the time, so logging in separately all the time
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(self.personal_email, self.personal_email_password)
		
		msg = MIMEText(message)
		
		msg['Subject'] = 'Python notification'
		msg['From'] = self.personal_email
		msg['To'] = self.personal_email
		
		# Send a test mail
		server.sendmail( "", self.personal_email, msg.as_string() )
		server.quit()
		
		print ("Notification email sent")

# Send a test mail to myself
if __name__ == '__main__':

	mail_service = pymailnotify()
	mail_service.notify("Just testing the mail sending capability of a python script")