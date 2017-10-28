#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python
import webbrowser, sys,pyperclip
n=3
s=[];
print("Enter Your 3 url list : ")
for i in range(0,n):
	s.append(input("enter here : "))
	
	
if len(s) > 1:
	for i in range(0,n):
		webbrowser.open('https://www.google.com/maps/place/' + s[i])
else:
    # Get address from clipboard.
	address = pyperclip.paste()
	webbrowser.open('https://www.google.com/maps/place/' + address)