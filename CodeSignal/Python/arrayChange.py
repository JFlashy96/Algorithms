"""
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
solution(inputArray) = 3.
"""
def solution(inputArray):
	min_moves = 0
	for i in range(1, len(inputArray)):
		if inputArray[i] <= inputArray[i-1]:
			diff = inputArray[i-1] - inputArray[i] + 1
			inputArray[i] = inputArray[i-1] + 1
			min_moves += diff
	return min_moves
print(solution(inputArray = [1, 1, 1]))
print(solution(inputArray = [-1000, 0, -2, 0]))