''' Write a program which will allow user to enter 10 numbers and display largest odd
number from them. It will display appropriate message in case if no odd number is
found.'''

num=[]
print("*********** Enter 10 numbers ***********\n")
temp=0

for i in range(5):
	num.append(int(input("Enter {x} number = ".format(x=i+1))))

for i in range(5):
	if (num[i]%2) != 0:
		if temp < num[i]:
			temp = num[i]

if temp == 0:
	print("There is no any odd number ....!!!!")
else:
	print("Largest odd number = ",temp)
