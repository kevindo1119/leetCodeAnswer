class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        temp = min(nums) - 1
        for i in nums[:]:
            if i == temp:
                nums.remove(i)
            else:
                temp = i
        
        return len(nums)
        
