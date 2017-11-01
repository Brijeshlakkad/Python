#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python
from PIL import Image
catIm = Image.open('zophie.jpg')
croppedIm=catIm.crop((335,345,565,560))
croppedIm.save("xyz.png")