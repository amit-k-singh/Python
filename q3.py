# Write a program to make a simple calculator (using functions).

n1 = int(input("Enter first number  = "))
n2 = int(input("Enter second number = "))

print("Select Option\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")

ch = int(input("Enter your chpice = "))

def add(a,b):
	print("Addition = ",a+b)
def sub(a,b):
	print("Subtraction = ",a-b)
def mul(a,b):
	print("Multiplication = ",a*b)
def div(a,b):
	print("Division = ",a/b)

if ch == 1:
	add(n1,n2)
elif ch == 2:
	sub(n1,n2)
elif ch == 3:
	mul(n1,n2)
elif ch == 4:
	div(n1,n2)
else:
	print("Enter valid choice")

