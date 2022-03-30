'''1.	Write a function intreverse(n) that takes as input a positive integer n and returns the
	integer obtained by reversing the digits in n.

	Here are some examples of how your function should work.
	>>> intreverse(783)
	387 '''

def intreverse(n):
	rem=0
	rev=0
	while n > 0:
		rem = n%10
		rev = (rev*10)+rem
		n //=10
	return rev

num=int(input("Enter posit number = "))

if num > 0:
	print("reverse = ",intreverse(num))
else:
	print(num,"is negetive number............!!!")
