class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        """
        Create an array of the input integer array, sort them
        Time: O (NlogN)
        Space: O (N)
        """
        return sorted (x*x for x in A)
        
