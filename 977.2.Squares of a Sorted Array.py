class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        """
        Use Two point index_neg, index_pos, 
            trace for negative and positive respectively
        Time: O (N)
        Space: O (N)
        """
        A_len = len(A)
        index_pos = 0
        ans = []
        
        while index_pos < A_len and A[index_pos] < 0:
            index_pos += 1
        index_neg = index_pos - 1
        
        while index_neg >= 0 and index_pos < A_len:
            if abs(A[index_neg]) <= abs(A[index_pos]):
                ans.append(A[index_neg]**2)
                index_neg -= 1
            else:
                ans.append(A[index_pos]**2)
                index_pos += 1
                
        # add trivals
        while index_neg >= 0:
            ans.append(A[index_neg]**2)
            index_neg -= 1
            
        while index_pos < A_len:
            ans.append(A[index_pos]**2)
            index_pos += 1
            
        return ans
