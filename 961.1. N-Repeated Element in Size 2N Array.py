class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        counter = len(A) / 2
        
        dic = dict()
        
        B = list(set(A))
        
        for i in B:
            dic[i] = 0
            
        for j in range(len(A)):
            dic[A[j]] += 1
        
        for key, value in dic.items():
            if value > 1:
                return key
