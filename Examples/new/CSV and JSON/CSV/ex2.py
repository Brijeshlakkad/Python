#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python

import csv
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
        print('Row #' + str(exampleReader.line_num) + ' ' + str(row))