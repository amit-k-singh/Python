''' 7. Python Program to Put Even and Odd elements in a List into Two Different Lists '''



num = int(input("Enter list length = "))
lst=[]
for i in range(num):
	no = int(input("Enter element {}= ".format(i+1)))
	lst.append(no)

lstodd = lambda x: False  if x%2==0 else True
oddlist=list(filter(lstodd,lst))
print("Through lambda  odd list = ",oddlist)

lsteven = lambda x: True  if x%2==0 else False
evenlist=list(filter(lsteven,lst))
print("Through lambda even list = ",evenlist)


odd = []
even = []

for i in lst:
	if i%2 == 0:
		even.append(i)
	else:
		odd.append(i)

print("Even list = ",even)
print("Odd  list = ",odd)
