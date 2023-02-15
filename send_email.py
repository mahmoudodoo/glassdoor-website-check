import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os
from getpass import getpass
from datetime import datetime


now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

sender = "mahmoudqudah2123@gmail.com"
password = "zsfngfcfptsfbxnx"
recipient = "mahmoudqudah2123@gmail.com"
#password = getpass(f"Hi {sender} Please Enter Your password to send the Email:\n")
message = MIMEMultipart("mixed")
message.add_header("Subject", "Glassdoor Website Check")
lines = ""

with open('email_template.html') as f:
    lines = f.read()

html = f"{lines} Date: {dt_string}"

for file_name in os.listdir("gd_screenshots"):
  with open(f"gd_screenshots/{file_name}", "rb") as f:
    msgImage = MIMEImage(f.read())

  msgImage.add_header('Content-ID', f'<{file_name}>')
  msgImage.add_header('Content-Disposition', 'attachment', filename=f'{file_name}.png')
  message.attach(msgImage)



part = MIMEText(html, "html",'utf-8')
message.attach(part)


smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.starttls()
smtp.login(sender, password)
smtp.sendmail(sender, recipient, message.as_string())
smtp.quit()
print('Mail Sent')
