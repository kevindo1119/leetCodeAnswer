class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        
        res_1 = []
        res_2 = []
        
        for words in logs:
            for i in range(len(words)-1):
                if words[i] == ' ' and words[i+1].isalpha():
                    res_1.append(words)
                    break
                elif words[i] == ' ' and words[i+1].isdigit():
                    res_2.append(words)
                    break
        
        res_1.sort(key=lambda log: log.split()[0])
        res_1.sort(key=lambda log: log.split()[1:]) 
        return res_1 + res_2
