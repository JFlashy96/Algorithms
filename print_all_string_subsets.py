"""
	Jonathan Alston 
	January 2022
	This program finds all subsets of a given string.
"""

s = "abc"
n = len(s)
# For holding all the formed substrings
arr = []

for i in range(0,n):
	for j in range(i,n):
		arr.append(s[i:(j+1)])

print("All subsets for the given string are:")
for i in arr:
	print(i)