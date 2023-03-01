"""
Check if all digits of the given integer are even.
"""
def solution(n):
	n = str(n)
	for i in n:
		if (int(i) % 2) != 0:
			return False
	return True
print(solution(n=1234))
print(solution(n=2484))