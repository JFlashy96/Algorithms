"""
Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
solution(inputString) = true;
For inputString = "abac", the output should be
solution(inputString) = false;
For inputString = "a", the output should be
solution(inputString) = true.
"""
def solution(inputString):
    return inputString == inputString[::-1]
print(solution(inputString = "aabaa"))
print(solution(inputString = "abac"))
print(solution(inputString = "a"))