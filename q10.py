''' 10	Python Program to Break a List into Chunks of Size N.	'''

lst = [31,44,55,86,37,78,39,82,115,152,2313,124,215,2162,172,128,129,220,221,202,7623,424,225]
lst1=[]
lst2=[]
num = int(input("Enter Chunks of size = "))
for i in range(len(lst)):
	lst1.append(lst[i])
	if (((i+1)%num) == 0):
		lst2.append(lst1)
		lst1=[]

print(lst2)
	 
	
		
		

