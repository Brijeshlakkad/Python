#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python
from PIL import Image
catIm = Image.open('xyz.png')
print("size : ",catIm.size)
width, height = catIm.size
print("width : ",width)
print("height : ",height)
print("filename : ",catIm.filename)
print("format : ",catIm.format)
print("discription : ",catIm.format_description)
catIm.save('zophie.jpg')