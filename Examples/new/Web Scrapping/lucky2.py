#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python

import requests, bs4,webbrowser,sys
s=input("Google : ")
print("googling....")
res=requests.get("https://google.com/search?q="+s)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
linkElems=soup.select('.r a')
numOpen = min(5,len(linkElems))
for i in range(numOpen):
	webbrowser.open("https://google.com"+linkElems[i].get('href'))