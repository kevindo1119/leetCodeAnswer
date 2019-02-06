class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 1
        
        temp = [x for x in xrange(1, len(nums) + 2, 1)]
        
        for i in nums:
            if i in temp:
                temp.remove(i)
                
        
        return min(temp)
