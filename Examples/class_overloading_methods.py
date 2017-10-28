#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python

class B:
	"Just example class"
	def __init__(self,a,b):
		self.a=a;
		self.b=b;
		print("a and b are set")
	def __str__(self):
		return ("vector %d and %d "%(self.a,self.b))
	def __add__(self,ex):
		return B(self.a+ex.a,self.b+ex.b)
	
	
ex1 = B(10,10);
print(ex1);
ex2 = B(20,25);
print(ex2);
print(ex1+ex2)