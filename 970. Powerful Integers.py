class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        res = []
        
        # 2**18 > bound
        for i in range(18):
            for j in range(18):
                num_temp = x**i + y**j
                if num_temp <= bound:
                    res.append(num_temp)
                else:
                    break
        
        return list(set(res))
