#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python

import csv,os
os.mkdir("headerRemoved")

for csvFilename in os.listdir("."):
	if not csvFilename.endswith(".csv"):
		continue
	
	print("Removing header from %s...."% csvFilename)
	csvrows=[]
	csvfileObj=open(csvFilename)
	readerObj=csv.reader(csvfileObj)
	for row in readerObj:
		if readerOnj.line_num==1:
			continue
		csvrows.append(row)
	csvfileObj.close()
	csvfileObj=open(os.path.join("headerRemoved",csvFilename),'w',newline="")
	writerObj=csv.writer(csvfileObj)
	for row in csvrows:
		writerObj.writerow(row)
	csvfileObj.close()
print("Your Work is done")