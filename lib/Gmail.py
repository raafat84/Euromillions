def send_email(gmail_user, gmail_pwd, FROM, TO, SUBJECT, TEXT):
	"""Send an HTML email with a Gmail account"""
	import smtplib
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText
	
	"""START GMAIL settings"""
	SERVER = "smtp.gmail.com"
	PORT = 587 # Google says 465 works too

	"""START Message settings"""
	message = MIMEMultipart('alternative')
	message['Subject'] = SUBJECT
	message['From'] = FROM
	message['To'] = ", ".join(TO)
	html = "<html><head></head><body>" + TEXT + "</body></html>"#We add here HTML wrapping tags
	part = MIMEText(html, 'html')
	message.attach(part)
	
	try:
		server = smtplib.SMTP(SERVER, PORT)
		server.ehlo()
		server.starttls()
		server.login(gmail_user, gmail_pwd)
		server.sendmail(FROM, TO, message.as_string())
		server.close()
		#At this point, the email has been sent successfully!
	except:
		raise