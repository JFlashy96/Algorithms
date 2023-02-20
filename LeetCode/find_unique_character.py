import collections

class Solution(object):
	def find_unique(self, s):
		"""
		Input: s - string to be iterated over
		Return: index - int that represents index of first unique character
				in s
		"""

		counter = collections.Counter(s)

		for index, char in enumerate(s):
			if counter[char] == 1:
				return index
		return -1

solution = Solution()
j = "jonathan"
e = "engineer"
answer_j = solution.find_unique(j)
answer_e = solution.find_unique(e)
print(answer_j)
print(answer_e)