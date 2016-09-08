def fib(x):
	a ,b = 0,1
	for i in range(x):
		a,b = b , a+b
	return a