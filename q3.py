''' 3. Write a function sumprimes(l) that takes as input a list of integers l and retuns the sum
of all the prime numbers in l.
Here are some examples to show how your function should work.
>>>sumprimes([3,3,1,13])
19 '''

def sumprimes(l):
	flist=[]
	addition=0
	for i in l:
		temp = 0
		for j in range(2,i):
			if (i%j) == 0:
				temp = 1
				break
		if temp == 0:
			flist.append(i)
	for i in flist:
		addition += i
	return addition

num = int(input("Enter list length = "))
lst=[]
for i in range(num):
	no = int(input("Enter element {}= ".format(i+1)))
	lst.append(no)
print(sumprimes(lst))
