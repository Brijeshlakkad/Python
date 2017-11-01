#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python

from PIL import Image
w=input("Enter Width: ")
h=input("Enter Height: ")
c=input("Enter Color: ")
s=input("Enter name of image: ")
w=int(w)
h=int(h)
print("processing....")
im = Image.new('RGBA', (w, h), c)
print("saving...")
im.save(s+'.png')
print("Image saved successfully")