class Solution():

	def findPositions(self, n, target):
		"""
			input: n - array of integers sorted in non-decreaing order
				   target - value to find in n
			 output: target_pos - array of positions in n that target is found. 
			 		 			  Return [-1,-1] if target is not found.
		"""
		start_position = -1
		end_position = -1
		m = len(n)

		# first check that the array is not empty (m) and that the 
		# target value is neither less nor greater than the values in 
		# the given array
		if ((m != 0) and (target >= n[0]) and (target <= n[m-1])):
			print("true")
			for i in range(m):
				if start_position == -1:
					if n[i] == target:
						start_position = i
						end_position = i
					elif n[i] == target:
						end_position = i
					else:
						break
		else:
			print("false")
		return [start_position, end_position]

n = [5,7,7,8,8,10]
target = 8

example = Solution()
answer = example.findPositions(n, target)
print("The answer is {}".format(answer))
