''' 2. Write a function matched(s) that takes as input a string s and checks if the brackets "("
and ")" in s are matched: that is, every "(" has a matching ")" after it and every ")" has
a matching "(" before it. Your function should ignore all other symbols that appear in s.
Your function should return True if s has matched brackets and False if it does not.
Hint: Keep track of the nesting depth of brackets. Initially the depth is 0. The depth increases
with each opening bracket and decreases with each closing bracket. What are the constraints
on the value of the nesting depth for all brackets to be matched?
Here are some examples to show how your function should work.

>>> matched("zb%78")
True '''




def match(s):
	on = 0
	of = 0
	for i in s:
		if i == '(':
			on +=1
		elif i == ')':
			if on > of:
				of +=1
			else:
				return False
	if on == of:
		return True
	else:
		return False
 
str1 = input("Enter your string = ")
print(match(str1))
