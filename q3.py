''' 3. Program to Find a Pair with the Given Sum in an Array in Python '''

num = int(input("Enter list length = "))
lst=[]
for i in range(num):
	no = int(input("Enter element {}= ".format(i+1)))
	lst.append(no)

value = int(input("Enter sum value = "))
temp=0

for i in lst:
	temp += 1
	for j in lst[temp::]:
		if value == i+j:
			print(i,j)
