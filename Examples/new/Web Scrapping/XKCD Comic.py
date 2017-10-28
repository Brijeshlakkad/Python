#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python

import requests, bs4,webbrowser,sys,os

print("connecting...")
url="http://xkcd.com"
os.mkdir("xkcd")
while not url.endswith('#'):
	print("Downloading Page: %s....."% url)
	res=requests.get(url)
	res.raise_for_status()
	soup=bs4.BeautifulSoup(res.text)
	comicElem=soup.select("#comic img")
	if comicElem==[]:
		print("could not find image")
	else:
			comicUrl="http:"+comicElem[0].get('src')
			print("Downloading image %s....."% comicUrl)
			res=requests.get(comicUrl)
			res.raise_for_status()
			imageFile=open(os.path.join("xkcd",os.path.basename(comicUrl)),'wb')
			for chunk in res.iter_content(100000):
				imageFile.write(chunk)
			imageFile.close()
			prevlink=soup.select(".comicNav  a[rel='prev']")[0]
			s=prevlink.get("href")
			print("prev link : ",s)
			url="http://xkcd.com"+s
			continue
			
print("Done")