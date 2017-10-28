#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python
import smtplib
import base64

filename = "test.txt"

# Read a file and encode it into base64 format
fo = open(filename, "rb")
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent)  # base64

sender = 'brijeshlakkad22@gmail.com'
receiver = 'lakkadbrijesh@gmail.com'

marker = "AUNIQUEMARKER"

body ="""
This is a test email to send an attachement.
"""
# Define the main headers.
part1 = """From: From Person <brijeshlakkad22@gmail.com>
To: To Person <lakkadbrijesh@gmail.com>
Subject: Sending Attachement
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=%s
--%s
""" % (marker, marker)

# Define the message action
part2 = """Content-Type: text/plain
Content-Transfer-Encoding:8bit

%s
--%s
""" % (body,marker)

# Define the attachment section
part3 = """Content-Type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=%s

%s
--%s--
""" %(filename, filename, encodedcontent, marker)
message = part1 + part2 + part3

try:
   server = smtplib.SMTP('smtp.gmail.com',587)
   server.ehlo()
   print("1")
   server.starttls()
   print("2")
   server.login("brijeshlakkad22@gmail.com","124567267b")
   print("3")
   server.sendmail(sender, receiver, message)         
   print("Successfully sent email")
   server.close()
except smtplib.SMTPException:
   print("Error: unable to send email")