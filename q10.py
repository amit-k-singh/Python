'''10.	Write a program in python to implement Factorial series up to user entered number.
(Use recursive Function)'''

def fect(n):
	if n == 1:
		return n
	else:
		return n*fect(n-1)

num=int(input("Enhter the number = "))

print("fextorial of ", num," is", fect(num))
