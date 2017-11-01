#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python


import pyautogui
im = pyautogui.screenshot()
print(im.getpixel((50, 200)))
print(pyautogui.pixelMatchesColor(50, 200, (50, 50, 50)))
print(pyautogui.pixelMatchesColor(50, 200, (255, 135, 50)))
print("saving screenshot..")
im.save("screenshot1.png")