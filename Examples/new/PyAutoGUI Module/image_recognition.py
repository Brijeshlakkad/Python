#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python


import pyautogui,time
time.sleep(5)
print(pyautogui.locateOnScreen('catlogo.png'))
print(pyautogui.center((576, 280, 215, 234)))
pyautogui.click((683, 397),button="right")

