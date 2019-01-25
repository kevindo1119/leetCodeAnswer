class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        res = []
        
        for i in A:
            if i in res:
                return i
            else:
                res.append(i)
