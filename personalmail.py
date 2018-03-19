# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Send a test mail to myself
if __name__ == '__main__':

	# Get my personal email details first. Obviously not on github
	file = open("personalmail.txt", "r")
	personal_email_details = file.read()
	file.close()
	separation = personal_email_details.find(" ")
	personal_email = personal_email_details[:separation]
	personal_email_app_password = personal_email_details[separation+1:]
	
	# Sign into a gmail server
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(personal_email, personal_email_app_password)

	# Send a test mail
	server.sendmail(personal_email, personal_email, "Just testing the mail sending capability of a python script")
	server.quit()
	
	print ("Test email sent")