''' 9. Python Program to Replace Every List Element by Multiplication of Previous and Next '''

num = int(input("Enter list length = "))
lst=[]
for i in range(num):
	no = int(input("Enter element {}= ".format(i+1)))
	lst.append(no)

print(lst)
newlist=[]
l=len(lst)
for i in range(len(lst)):
	if i == 0:
		newlist.append(lst[1])
	elif i == l-1:
		newlist.append(lst[-2])
	else:
		mlt= lst[i-1]*lst[i+1]
		newlist.append(mlt)

print(newlist)
