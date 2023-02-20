class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            temp = s[i]
            s[i] = s[-i-1]
            s[-i-1] = temp 
        return s           
        
solution = Solution()
arr = ["h","e","l","l","o"]
print(solution.reverseString(arr))