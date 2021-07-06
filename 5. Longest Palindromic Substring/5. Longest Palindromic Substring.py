class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        def countFromCenter(self, s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left+1:right]
        
        if not s:
            return ""
        
        res = s[0]
        for i in xrange(len(s)):
            # aba
            str_1 = countFromCenter(self, s, i, i)
            if len(str_1) > len(res):
                res = str_1
            # abba
            str_2 = countFromCenter(self, s, i, i+1)
            if len(str_2) > len(res):
                res = str_2
                
        return res
