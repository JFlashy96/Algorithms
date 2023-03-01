"""
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
solution(inputArray) = 21.

7 and 3 produce the largest product.
"""
def solution(inputArray):
    largestNum = float("-inf")
    for i in range(0, len(inputArray)-1):
        if inputArray[i] * inputArray[i+1] > largestNum:
            largestNum = inputArray[i] * inputArray[i+1]
    return largestNum
print(solution(inputArray = [3, 6, -2, -5, 7, 3]))