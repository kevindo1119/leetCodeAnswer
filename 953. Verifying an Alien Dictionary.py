class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        
        
        dic = dict()
        counter = 0
        
        for i in order:
            dic[i] = counter
            counter += 1
        
        return words == sorted(words, key=lambda word: [dic[ch] for ch in word])
