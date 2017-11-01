#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python
from PIL import Image
import os
FIT_SIZE=300
logoName="catlogo.png"
logo=Image.open(logoName)
logowidth,logoheight=logo.size
os.makedirs("withlogo",exist_ok=True)
for filename in os.listdir('.'):
	if not (filename.endswith(".png") or filename.endswith(".jpg")) or filename==logoName:
		continue
	print("Opening image %s....."% filename)
	Im=Image.open(filename)
	width,height=Im.size;
	if width>FIT_SIZE and height>FIT_SIZE:
		if width>height:
			height=int((FIT_SIZE/height)*height)
			width=FIT_SIZE
		else:
			width=int((FIT_SIZE/width)*width)
			height=FIT_SIZE
		width=int(width)
		height=int(height)
		print("Resizing image %s....."% filename)
		Im.resize((width,height))
	print("Adding logo to the image %s..."% filename)
	Im.paste(logo,(width-logowidth,height-logoheight), logo.convert("RGBA"))
	print("Saving the image %s..."% filename)
	Im.save(os.path.join("withlogo",filename))
print("All Images are proceeded...")