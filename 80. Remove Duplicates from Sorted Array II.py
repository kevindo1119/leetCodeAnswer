class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        temp_1 = min(nums) - 2
        temp_2 = temp_1 + 1
        
        for i in nums[:]:
            if i == temp_2 and temp_2 == temp_1:
                nums.remove(i)
            elif i == temp_2 and temp_2 != temp_1:
                temp_1 = temp_2
            else:
                temp_2 = i
                
        return len(nums)
