#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python

import bs4
exampleFile = open('example.html')
soup = bs4.BeautifulSoup(exampleFile, 'html.parser')
pElems = soup.select('p')[0]
print(str(pElems))
print(pElems.get('id'))
print(pElems.attrs)
