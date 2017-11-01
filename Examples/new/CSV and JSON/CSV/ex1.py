#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python

import csv
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
print(exampleData)