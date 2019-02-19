class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # replace all punctuation symboils with space
        paragraph = paragraph.replace("!", " ").replace("?", " ").replace("'", " ").replace(",", " ").replace(";", " ").replace(".", " ")
        
        dic = {}
        for word in paragraph.lower().split():
            #print word
            if word not in banned:
                if word not in dic:
                    dic[word] = 1
                else:
                    dic[word] += 1
                    
                    
        res = ""
        curMax = 0
        for key, value in dic.items():
            #print key, value
            if value > curMax:
                curMax = value
                res = key
                
        return res
