#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python

import imapclient
email=input("Enter Your Email Address : ")
password=input("Enter Your Password : ")
imapObj=imapclient.IMAPClient('imap.gmail.com',ssl=True)
imapObj.login(email,password)
imapObj.select_folder("INBOX",readonly=True)
UIDs=imapObj.search(["ON 10-jul-2017"])
print(UIDs)
rawMessages = imapObj.fetch([11548], ['BODY[]', 'FLAGS'])
import pyzmail
message = pyzmail.PyzMessage.factory(rawMessages[11548][b'BODY[]'])
print(message.get_subject())
print(message.get_addresses('from'))
print(message.get_addresses('to'))
print(message.get_addresses('cc'))
print(message.get_addresses('bcc'))
if (message.text_part != None):
	print(message.text_part.get_payload().decode(message.text_part.charset))
if (message.html_part != None):
	print(message.html_part.get_payload().decode(message.html_part.charset))

imapObj.logout()