import pdb 

"""
	The purpose of this file is to simply give me some practice doing pdb debugging. 
	Seems like a useful tool to use for my personal projects because I tend to code 
	mostly from a text editor and run my applications via the command line.
"""
def addition(a, b):
	answer = int(a) + int(b)
	return answer

pdb.set_trace()
x = input("Enter first number: ")
y = input("Enter second number: ")
sum = addition(x, y)
print(sum)