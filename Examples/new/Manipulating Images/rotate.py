#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python
from PIL import Image
catIm = Image.open('zophie.jpg')
catIm.rotate(6).save('rotated6.png')
catIm.rotate(6, expand=True).save('rotated6_expanded.png')