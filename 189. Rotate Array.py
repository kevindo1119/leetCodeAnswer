class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        nums_len = len(nums)
        nums[:] = nums[nums_len - k: nums_len] + nums[0:nums_len - k]
