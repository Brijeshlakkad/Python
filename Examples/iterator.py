import sys;
l=list(range(5));
print(l);
it=iter(l);
print(next(it));
print(next(it));
print("----------for-----------")
for x in it:
	print(x);
it=iter(l);
while True:
	try:
		print(next(it));
	except StopIteration:
		sys.exit();   #you have to import sys module for this