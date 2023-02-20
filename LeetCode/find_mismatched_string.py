"""
	Jonathan Alston
	February 2022
	Given a string and 90 of strings, find whether the array contains a string with
	one character difference from the given string. Array may contain strings of 
	different lengths. 
"""
def check(list, s):

	n = len(list)

	# Check that the list is not empty
	if (n == 0):
		return False

	# Check that the lenght of the words are the same
	for i in range(0, n, 1):
		if (len(list[i]) != len(s)):
			continue

		diff = False

		# Here each character from the list is compared with the same index of s
		for j in range(0, len(list), 1):
			if (list[i][j] != s[j]):

				# first mismatch
				if (diff == False):
					diff = True

				else:
					diff = False
					break

		if (diff):
			return True

	return False 


def check(list, s):

	n = len(list)

	# Check that the list is not empty
	if (n == 0):
		return False

	# Check that the length of the words are the same
	for i in range(0, n, 1):
		if (len(list[i]) != len(s)):
			continue

		diff = False

		# Here each character from the list is compared with the same index of s
		for j in range(0, len(list[i]), 1):
			if (list[i][j] != s[j]):

				# first mismatch
				if (diff == False):
					diff = True

				else:
					diff = False
					break

		if (diff):
			return True

	return False

# Driver code
s = []
s.append("bana")
s.append("apple")
s.append("banacb")
s.append("banamf")

t = []
t.append("bana")
t.append("apple")
t.append("banaba")
t.append("bonanzo")
t.append("banamf")

print(int(check(s, "banana")))
print(int(check(t, "banana")))