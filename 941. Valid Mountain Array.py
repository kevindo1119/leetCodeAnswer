class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        
        N = len(A)
        i = 0
        
        if N < 3:
            return False
        
        while i < N - 1 and A[i] < A[i+1]:
            i += 1
            
        if i == 0 or i == N - 1:
            return False
        
        while i < N - 1 and A[i] > A[i+1]:
            i += 1
            
        return i == N-1
