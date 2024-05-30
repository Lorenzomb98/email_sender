#importing necessary modules
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

#creating email content
html = Template(Path("index.html").read_text())
email = EmailMessage()
email['from'] = 'Your Name'
email['to'] = 'recipient@email.com'
email['subject'] = 'Type your message'
email.set_content(html.substitute({'name': 'NameOfRecipient'}),'html')

#sending mail
with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
    smtp.connect("smtp.gmail.com",587)
    smtp.ehlo
    smtp.starttls()
    smtp.ehlo
    email_address = 'youremail@here.com'
    email_password = 'yourpassword'
    smtp.login(email_address, email_password )
    smtp.send_message(email)
    print('It is done')



