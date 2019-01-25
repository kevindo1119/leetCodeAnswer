class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        
        
        temp_time = -1
        ans_1 = -1
        ans_2 = -1
        ans_3 = -1
        ans_4 = -1
        for a, b, c, d in itertools.permutations(A):
            cur_time = (10*a + b) * 60 + 10*c + d
            if cur_time > temp_time and (10*a + b) <= 23 and (10*c + d) <= 59:
                temp_time = cur_time
                ans_1 = a
                ans_2 = b
                ans_3 = c
                ans_4 = d
        
        if temp_time != -1:
            return str(ans_1) + str(ans_2) + ":" + str(ans_3) + str(ans_4)
        else:
            return ""
