#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python

import requests, bs4,webbrowser,sys
s=input("Amazon : ")
print("Searching product....")
res=requests.get("https://www.amazon.in/s/field-keywords="+s)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
linkElems=soup.select('.a-row .a-spacing-none > a')
numOpen = min(5,len(linkElems))
for i in range(numOpen):
	webbrowser.open(linkElems[i].get('href'))
	
	