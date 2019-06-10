# Solution 1, two-pointer
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

# Solution 1.1, a different implementation
class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        is_same = word1 == word2
        i1 = i2 = float('-inf')
        res = float('inf')
        
        for i, word in enumerate(words):
            if word not in [word1, word2]:
                continue
            
            if is_same and word == word1:
                i1, i2 = i2, i
                res = min(res, i2 - i1)
                continue
            
            if word == word1:
                i1 = i
            if word == word2:
                i2 = i
            res = min(res, abs(i2 - i1))
        
        return res