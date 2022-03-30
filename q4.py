
num=int(input("How many number you want = "))

arr=[]

for i in range(num):
	#print('Enter a[{}] ='.format(arr.append(int(input(i)))))
	#.append(int(input()))
	#n=int(input("Enter a[{}]=".format(i)))
	arr.append(int(input("Enter a[{x}] = ".format(x=i))))

#print(arr[0],arr[1],arr[2])

def max_fun(n1,n2,n3):
	if n1>n2:
		if n1>n3:
			print("Max number is = ",n1)
	elif n2>n3:
		print("Max number is = ",n2)
	else:
		print("Max number is = ",n3)

max_fun(arr[0],arr[1],arr[2])

def min_fun(n1,n2,n3):
	if n1<n2:
		if n1<n3:
			print("Min number is = ",n1)
	elif n2<n3:
		print("Min number is = ",n2)
	else:
		print("Min number is = ",n3)

min_fun(arr[0],arr[1],arr[2])
