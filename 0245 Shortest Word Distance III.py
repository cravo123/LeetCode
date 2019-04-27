class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        res = float('inf')
        
        w1, w2 = word1, word2
        i1, i2 = float('-inf'), float('-inf')
        
        for i, word in enumerate(words):
            if w1 == w2 == word:
                res = min(res, abs(i - i1))
                i1, i2 = i, i1
                continue
            if word == w1:
                i1 = i
            elif word == w2:
                i2 = i  
            res = min(res, abs(i1 - i2))

        return res