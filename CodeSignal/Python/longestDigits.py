"""
Given a string, output its longest PREFIX which contains only digits.

Example

For inputString = "123aa1", the output should be
solution(inputString) = "123".
"""
def solution(inputString):
	dig = ""
	for i in inputString:
		if i.isdigit():
			dig += i
		else:
			break
	return dig

print(solution(inputString = "123aa1"))
