class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        """
        sort array decreasing order first
        Use check the closest three if they can form a triangle
        report zero if can not form any of them
        """
        A.sort(reverse=True)
        i = 0
        res = 0
        
        while i < len(A) - 2:
            if A[i+2] + A[i+1] > A[i]:
                res =  A[i] + A[i+1] + A[i+2]
                break
            else:
                i += 1
        
        return res
