from collections import deque 
class Solution(object):
	def rotate_array(self, nums, k):
		"""
		Input: nums - array to be rotated
			   k 	- number of places to move each element of nums
		Output: None - modify nums in place
		"""

		k = k % len(nums)
		print(k)
		i = 0
		d = deque(nums)
		while i < k:
			temp = d.pop()
			d.appendleft(temp)
			i += 1
		nums[:] = d 

solution = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
print(len(nums))
print(3 % 7)
solution.rotate_array(nums, k)
print(nums)

#[5,6,7,1,2,3,4]
