'''9.	Write a program in python to implement Fibonacci series up to user entered number.
(Use recursive Function)  '''

def fibo(n):
	if n<=1:
		return n
	else:
		return(fibo(n-1)+fibo(n-2))
num=int(input("Enter the number = "))

for i in range(num):
	print(fibo(i))
