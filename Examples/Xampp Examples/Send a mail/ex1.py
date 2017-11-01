#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python
import smtplib

sender = 'brijeshlakkad22@gmail.com'
receivers = ['lakkadbrijesh@gmail.com']

message = """From: From Person <brijeshlakkad22@gmail.com>
To: To Person <lakkadbrijesh@gmail.com>
Subject: SMTP e-mail test


This is a test e-mail message.
"""

try:
   server = smtplib.SMTP('smtp.gmail.com',587)
   server.ehlo()
   print("1")
   server.starttls()
   print("2")
   server.login("brijeshlakkad22@gmail.com","124567267b")
   print("3")
   server.sendmail(sender, receivers, message)         
   print("Successfully sent email")
   server.close()
except smtplib.SMTPException:
   print("Error: unable to send email")