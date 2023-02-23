"""
Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.

Example

For name = "var_1__Int", the output should be
solution(name) = true;
For name = "qq-q", the output should be
solution(name) = false;
For name = "2w2", the output should be
solution(name) = false.
"""
def solution(name):
	if name[0].isdigit():
		return False
	for i in name:
		if i.isdigit() or i.isalpha() or i == "_":
			continue
		else:
			return False
	return True
print(solution(name="var_1_Int"))
print(solution(name="qq-q"))