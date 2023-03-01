"""
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
solution(inputArray) = ["aba", "vcd", "aba"].
"""
def solution(inputArray):
    longest_strings = []
    max_count = 0
    for i in range(0, len(inputArray)):
        if len(inputArray[i]) == max_count:
            longest_strings.append(inputArray[i])
        if len(inputArray[i]) > max_count:
            max_count = len(inputArray[i])
            longest_strings = []
            longest_strings.append(inputArray[i])
    return longest_strings

inputArray = ["aba", "aa", "ad", "vcd", "aba"]
print(solution(inputArray))