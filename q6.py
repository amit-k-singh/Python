# 6. rite a Python program to check if the number provided by the user is an Armstrong number.

num = int(input("Enter the number = "))

num1 = num
count = 0
while num1 > 0:
	num1 //= 10
	count +=1

total = 0
num1 = num
temp = 0
for i in range(count):
	temp = num1%10
	num1 //= 10
	t1 = 1
	for j in range(count):
		t1 *= temp
	total += t1

if total == num:
	print(num,"Number is Armstrong")
else:
	print("Number is not Armstrong")
	
