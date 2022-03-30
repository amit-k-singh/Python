''' 2. Python Program to Move all Zeros present in an Array/List to the End '''


num = int(input("Enter list length = "))
lst=[]
flist=[]
for i in range(num):
	no = int(input("Enter element {}= ".format(i+1)))
	lst.append(no)
lst2=[]
for i in lst:
	if i == 0:
		lst2.append(i)
	else:
		flist.append(i)
for i in lst2:
	flist.append(i)
print(flist)
	
