import sys;
def fibonacci(n):
	a,b,count=0,1,0;
	while True:
		if (count>n-1):
			break;
		yield a;
		a,b=b,a+b;
		count+=1;
f=fibonacci(5);
while True:
	try:
		print(next(f));
	except StopIteration:
		sys.exit();