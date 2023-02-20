"""
	Jonathan Alston
	February 2022
	The purpose of this code is to return the string within the deepest nest of 
	parenthesis or brackets.
"""
def deepestParen(s):
	st = []
	result = []
	for i, char in enumerate(s):
		if char == "(" or char == "{" or char == "[":
			st.append(char)
			tmp = char
			ind = i
		elif char == ")" or char == "}" or char == "]":
			if st[-1] == tmp:
				j = ind
				stng = ""
				for m in range(j+1, i):
					stng += s[m]
				result.append(stng)

			st.append(stng)

	if not st:
		return s
	return result

print(deepestParen("{(ab(gh){fmnu})}"))
print(deepestParen("mkh"))
print(deepestParen("{}"))

