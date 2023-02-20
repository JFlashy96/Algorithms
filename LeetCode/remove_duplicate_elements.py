class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[k] = nums[i+1]
                k += 1
        return k

a = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
k = a.removeDuplicates(nums)
print(k)
