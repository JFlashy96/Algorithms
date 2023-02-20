class Solution():
	def findRotatedPosition(self, n, target):
		"""
			input: n - array of integers sorted in ascending order
				   target - value to find in n
			 output: index of target if found. If not, return [-1] 
		"""
		m = len(n)
		for i in range(m):
			if target in n:
				return [i]
			else:
				return [-1]

nums = [4,5,6,7,0,1,2]
target = 4
solution = Solution()
answer = solution.findRotatedPosition(nums, target)
if answer != [-1]:
	print("The target's position was found at {}".format(answer))
else:
	print("The target was not found.")