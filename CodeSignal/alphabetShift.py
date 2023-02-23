"""
Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be solution(inputString) = "dsbaz".
"""
def solution(inputString):
	new_inputString = []
	for i in range(0, len(inputString)):
		if inputString[i] == "z":
			new_inputString.append("a")
		else:
			loc = ord(inputString[i])
			new_inputString.append(chr(loc+1))
	new_inputString = "".join(new_inputString)
	return new_inputString
print(solution(inputString = "crazy"))