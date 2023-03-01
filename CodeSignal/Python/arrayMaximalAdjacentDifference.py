"""
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
solution(inputArray) = 3.
"""
def solution(inputArray):
	max_diff = 0
	for i in range(1,len(inputArray)-1):
		diff = max((inputArray[i] - inputArray[i-1]), (inputArray[i] - inputArray[i+1]))
		if diff > max_diff:
			max_diff = diff
	if (inputArray[-1] - inputArray[-2]) > max_diff:
		max_diff = (inputArray[-1] - inputArray[-2])
	return max_diff
print(solution(inputArray = [2, 4, 1, 0]))