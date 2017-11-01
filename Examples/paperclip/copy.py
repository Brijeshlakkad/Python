#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python


import pyperclip
numbers = ''
for i in range(200):
	numbers = numbers + str(i) + '\n'
pyperclip.copy(numbers)