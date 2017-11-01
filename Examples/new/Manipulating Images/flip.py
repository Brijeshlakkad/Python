#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python
from PIL import Image
catIm = Image.open('zophie.jpg')
catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')