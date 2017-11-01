#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python

import imapclient
email=input("Enter Your Email Address : ")
password=input("Enter Your Password : ")
imapObj=imapclient.IMAPClient('imap.gmail.com',ssl=True)
imapObj.login(email,password)
imapObj.select_folder("INBOX",readonly=True)
UIDs=imapObj.search(['ON 29-oct-2017'])
print(UIDs)
rawMessages=imapObj.fetch([13274],["BODY[]","FLAGS"])
import pyzmail
message = pyzmail.PyzMessage.factory(rawMessages[13274][b"BODY[]"])
if(message.text_part != None):
	fileObj=open("xyz.txt","w")
	fileObj.write(message.text_part.get_payload().decode(message.text_part.charset))
if(message.html_part != None):
	fileObj=open("xyz.html","w")
	fileObj.write(message.html_part.get_payload().decode(message.html_part.charset))

fileObj.close()
imapObj.logout()