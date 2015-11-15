import requests
import smtplib
import time

def SendMessage(user, pwd, recipient, subject, body):
	gmail_user = user
	gmail_pwd = pwd
	FROM = user
	TO = recipient if type(recipient) is list else [recipient]
	SUBJECT = subject
	TEXT = body

	message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
	""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
	try:
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.ehlo()
		server.starttls()
		server.login(gmail_user, gmail_pwd)
		server.sendmail(FROM, TO, message)
		server.close()
		print ("Sending successful")
	except:
		print ("Sending failed")

url = "" #add the url of the site you want to check
#gmail details
user = "" #sender's email
pwd = "" #password of the sender's email
recipient = "" #email of the recipient
subject = "" #email subject
body = "" #body of the email

page = requests.get(url)
content = page.content
print (page.url)
while (True):
	page = requests.get(url)
	if (content != page.content):
		content = page.content
		SendMessage(user, pwd, recipient, subject, body)
	time.sleep(60)
