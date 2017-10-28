#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python

import bs4
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile,"html.parser")
type(exampleSoup)