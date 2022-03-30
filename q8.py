'''8.	Write a Python program to perform following operation on given string input:
	a) Count Number of Vowel in given string
	b) Count Length of string (donot use len() )
	c) Reverse string
	d) Find and replace operation
	e) check whether string entered is a palindrome or not	'''

word = input("Enter the string = ")

vcount = 0
count = 0
for i in word:
	if (i == 'a' or  i == 'e' or  i == 'i' or  i == 'o' or  i == 'u' or i == 'A' or  i == 'E' or  i == 'I' or  i == 'O' or  i == 'U'):
		vcount += 1
	count += 1

print("1.	Length of Vowel  = ", vcount)
print("2.	Length of string = ", count)
rev = word[::-1]
print("3.	Reverse of string = ",rev)

find = input("Enter find charector = ")
replace = input("Enter replace charector = ")
x=word.replace(find,replace)
print("4.	After replace = ",x)

if word == rev:
	print("5.	Strint is palindrom")
else:
	print("5.	Strint is not palindrom")





