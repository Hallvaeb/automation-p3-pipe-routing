
import smtplib, ssl, re, pathlib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
path_to_dfa_folder = str(pathlib.Path().absolute().as_posix())+"/inputOutput/"


class EmailHandler():
	
		
	def valid_email(receiver_email): 
		''' Checks if reciever_email is set, and if it is a valid email. '''
		email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
		if(receiver_email == "your_email_please@gmail.com" or receiver_email == ""):
			# Email has not been set
			return -1 
		elif(re.fullmatch(email_regex, receiver_email)):
			# Email is valid
			return 0
		else:
			# Email is invalid, will not be sent
			return -1
	
	def send_design_to_email(design_id, receiver_email):
		
		if (EmailHandler.valid_email(receiver_email)):
			print(f"Email was not set or recognized: email: {receiver_email}")
			return
		subject = "Your DFA solution"
		body = "This is an email with attachment sent from Python"
		sender_email = "mailreservehallvard@gmail.com"
		receiver_email = receiver_email
		password = "V#6ydD@z#6F6bB%"

		# Create a multipart message and set headers
		message = MIMEMultipart()
		message["From"] = sender_email
		message["To"] = receiver_email
		message["Subject"] = subject
		# message["Bcc"] = receiver_email  # Recommended for mass emails, sends blind copies

		# Add body to email
		message.attach(MIMEText(body, "plain"))

		filepath = path_to_dfa_folder + "products/" + design_id + ".dfa"

		# Open PDF file in binary mode
		with open(filepath, "rb") as attachment:
			# Add file as application/octet-stream
			# Email client can usually download this automatically as attachment
			part = MIMEBase("application", "octet-stream")
			part.set_payload(attachment.read())

		# Encode file in ASCII characters to send by email    
		encoders.encode_base64(part)

		# Add header as key/value pair to attachment part
		part.add_header(
			"Content-Disposition",
			f"attachment; filename= {design_id}.dfa",
		)

		# Add attachment to message and convert message to string
		message.attach(part)
		text = message.as_string()

		# Log in to server using secure context and send email
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
			server.login(sender_email, password)
			server.sendmail(sender_email, receiver_email, text)
		print(f"Email sent to: {receiver_email}.")