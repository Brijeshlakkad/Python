#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python

import bs4
exampleFile = open('example.html')
soup = bs4.BeautifulSoup(exampleFile, 'html.parser')
print(soup.prettify())