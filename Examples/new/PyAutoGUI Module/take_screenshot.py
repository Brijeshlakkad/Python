#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python


import pyautogui
s=input("Enter number of seconds..")
s=int(s)
for i in range(0,s):
	im=pyautogui.screenshot()
	print("saving screenshot..")
	im.save("screenshot"+str(i)+".png")