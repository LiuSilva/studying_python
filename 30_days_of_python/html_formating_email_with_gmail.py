# para funcionar no Gmail tem que permitir logar em apps menos seguros.
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host = "smtp.gmail.com"
port = 587
username = "hungrypy@gmail.com"
password = "iamhungry2016"
from_email = username
to_list = [username]

try:
	email_conn = smtplib.SMTP(host, port)
	email_conn.ehlo()
	email_conn.starttls()
	email_conn.login(username, password)
	the_msg = MIMEMultipart("alternative")
	the_msg['Subject'] = "Hello Python Test!"
	the_msg['From'] = from_email
	the_msg['To'] = to_list[0]
	plain_text = "Testing the message"
	html_text = """\
	<html>
		<head></head>
		<body>
			<p>Hey!<br>
				Testing this email <b>message</b>. Studying through <em>Udemy</em>!
			</p>
		</body>
	</html>
	"""
	part_1 = MIMEText(plain_text, 'plain')
	part_2 = MIMEText(html_text, 'html')
	the_msg.attach(part_1)
	the_msg.attach(part_2)
	email_conn.sendmail(from_email, to_list, the_msg.as_string())
	email_conn.quit() #logout
except smtplib.SMTPException:
	print("error sending message")