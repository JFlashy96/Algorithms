"""
Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
solution(st) = "abcdcba".
"""
def solution(st):
	for i in range(0, len(st)):
		if (st[i:len(st)] == st[i:len(st)][::-1]):
			return st[0:i] + st[i:len(st)] + st[0:i][::-1]
print(solution(st="abcdc"))