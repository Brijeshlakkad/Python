for j in range(10,100):
	flag=0
	for i in range(2,j):
		if (j%i)==0:
			flag=1
	if (flag==0):
		print(j," is prime number")
	