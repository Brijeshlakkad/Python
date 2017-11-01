#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python


import pyautogui,time
time.sleep(5)
import pyautogui, time
def close():
	pyautogui.click(100, 100)
	pyautogui.typewrite('2 second after this window will be closed')
	time.sleep(2)
	pyautogui.hotkey('alt', 'f4')
	pyautogui.press(["right","enter"])
close()