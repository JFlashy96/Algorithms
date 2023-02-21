"""
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
solution(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.
"""
def solution(inputString):
	hash = set()
	for i in inputString:
		if i not in hash:
			hash.add(i)
		else:
			hash.remove(i)
	if len(hash) > 1:
		return False
	return True
print(solution(inputString = "aabb"))
print(solution(inputString = "zyyzzzzz"))
print(solution(inputString = "abcad"))