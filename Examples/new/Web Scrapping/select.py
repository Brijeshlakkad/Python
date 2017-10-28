#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python

import bs4
exampleFile = open('example.html')
soup = bs4.BeautifulSoup(exampleFile, 'html.parser')
pElems = soup.select('p')
print(str(pElems[0]))
print(pElems[0].getText())
print(str(pElems[1]))
print(pElems[1].getText())
print(str(pElems[2]))
print(pElems[2].getText())