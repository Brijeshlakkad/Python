#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python
sender = 'brijeshlakkad22@gmail.com'
receivers = ['lakkadbrijesh@gmail.com']

SMTPserver = 'smtp.gmail.com'
sender =     'brijeshlakkad22@gmail.com'
destination = ['lakkadbrijesh@gmail.com']

USERNAME = "brijeshlakkad22@gmail.com"
PASSWORD = "124567267b"

# typical values for text_subtype are plain, html, xml
text_subtype = 'plain'


content="""\
Test message
"""

subject="Sent from Python"

import sys
import os
import re

from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
# from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)

# old version
# from email.MIMEText import MIMEText
from email.mime.text import MIMEText

try:
    msg = MIMEText(content, text_subtype)
    msg['Subject']=       subject
    msg['From']   = sender # some SMTP servers will do this automatically, not all

    conn = SMTP(SMTPserver)
    conn.set_debuglevel(False)
    conn.login(USERNAME, PASSWORD)
    try:
        conn.sendmail(sender, destination, msg.as_string())
    finally:
        conn.quit()

except Exception:
    sys.exit( "mail failed" ) # give a error message