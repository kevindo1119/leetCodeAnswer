class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        res = []
        
        for i in A:
            if i not in res:
                res.append(i)
            else:
                return i
