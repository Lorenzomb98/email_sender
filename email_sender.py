# Importing necessary modules
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
import csv

# Opening the csv file with the names and emails to iterate through
with open('email_list.csv') as csvfile:
    email_addys=csv.reader(csvfile)
    for row in email_addys:

    # Creating email content
        html = Template(Path("index.html").read_text())
        email = EmailMessage()
        email['from'] = '<Your Name>'
        email['to'] = row[1]
        email['subject'] = '<Your subject>'
        email.set_content(html.substitute({'name': row[0]}),'html')

        # Sending mail
        with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
            smtp.connect("smtp.gmail.com",587)
            smtp.ehlo
            smtp.starttls()
            smtp.ehlo
            gmail_address = '<YourEmail@gmail.com>'
            gmail_app_password = '<Your Google app password>'
            smtp.login(gmail_address, gmail_app_password )
            smtp.send_message(email)
            print(f'Email sent to {row[1]}')



