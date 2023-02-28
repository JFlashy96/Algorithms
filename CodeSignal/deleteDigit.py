"""
Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

Example

For n = 152, the output should be
solution(n) = 52;
For n = 1001, the output should be
solution(n) = 101.
"""
def solution(n):
	tracker = []
	n = str(n)
	for i in range(0, len(n)):
		tracker.append(n[0:i]+""+n[i+1:len(n)])
	for i in range(0, len(tracker)):
		tracker[i] = int(tracker[i])
	return max(tracker)
print(solution(n=152))
print(solution(n=1001))