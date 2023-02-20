class Solution(object):
	def merge_sorted_array(self, nums1, m, nums2, n):
		"""
		Input: nums1, nums2 - arrays sorted in ascending order to be merged
		Return none - modify nums1 with the merged values
		"""

		if n == 0:
			return nums1
		else:
			del nums1[-n:]
			for i in range(len(nums2)):
				nums1.append(nums2[i])
			nums1.sort()


solution = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

solution.merge_sorted_array(nums1, m, nums2, n)
print(nums1)

# Expected output of: [1,2,2,3,5,6]