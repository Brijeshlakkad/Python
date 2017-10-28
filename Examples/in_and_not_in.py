l=[10,20,30,60,70];
a=10;
b=50;
if(a in l):
	print("a is in list");
else:
	print("a is not in list");
if(b not in l):
	print("b is not in list");
else:
	print("b is in list");
print("a : %d and b :%d"% (a, b)," ",id(a))