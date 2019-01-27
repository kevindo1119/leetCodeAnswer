class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        
        len_loop = len(list(A[0]))
        counter  = 0

        return len([s for s in zip(*A) if list(s) != sorted(s)])
