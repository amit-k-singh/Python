''' 8. Python Program to Read a List of Words and Return the Length of the Longest Word '''

num = int(input("Enter the lenth of list = "))
lst=[]
for i in range(num):
	no = input("Enter {} string = ".format(i+1))
	lst.append(no)

print(lst)
temp=''
length=0
for i in range(len(lst)):
	l = len(lst[i])
	if l >= length:
		length=l
		temp=lst[i]

print("Longest word = ",temp)
print("Length of string = ",len(temp))
