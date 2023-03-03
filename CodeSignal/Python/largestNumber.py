"""
Given an integer n, return the largest number that contains exactly n digits.

Example

For n = 2, the output should be
solution(n) = 99.
"""
def solution(n):
	start = "1"
	for i in range(n):
		start += "0"
	return int(start) - 1
print(solution(2))