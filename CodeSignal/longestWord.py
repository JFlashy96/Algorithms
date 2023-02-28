"""
Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

Example

For text = "Ready, steady, go!", the output should be
solution(text) = "steady".
"""
import re
def solution(text):
	return max(re.split('[^a-zA-Z]', text), key=len)
print(solution(text="Ready, steady, go!"))