"""
Given array of integers, find the maximal possible sum of some of its k consecutive elements.

Example

For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
solution(inputArray, k) = 8.
All possible sums of 2 consecutive elements are:

2 + 3 = 5;
3 + 5 = 8;
5 + 1 = 6;
1 + 6 = 7.
Thus, the answer is 8.
"""
def solution(inputArray, k):
	ele_sum = max_sum = sum(inputArray[:k])
	for i in range(len(inputArray) - k):
		ele_sum += inputArray[i+k] - inputArray[i]
		max_sum = max(ele_sum, max_sum)
	return max_sum
print(solution(inputArray = [2, 3, 5, 1, 6], k = 2))