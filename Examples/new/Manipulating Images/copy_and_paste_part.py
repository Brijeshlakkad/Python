#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python
from PIL import Image
catIm = Image.open('zophie.jpg')
catCopyIm = catIm.copy()
faceIm = catIm.crop((235, 245, 465, 460))
print(faceIm.size)
catCopyIm.paste(faceIm, (0, 0))
catCopyIm.save('pasted.png')