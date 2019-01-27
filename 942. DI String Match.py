class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # notice that the first I must be zero, the first D must be N, the result must be add the last trail
        
        N = len(list(S))
        index_I = 0
        index_D = N
        res = []
        
        for i in range(N):
            if S[i] == "I":
                res.append(index_I)
                index_I += 1
            else:
                res.append(index_D)
                index_D -= 1
        
        res.append(index_I)
        
        return res
