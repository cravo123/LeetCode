# Solution 1, two-pointer
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        first, second = float('-inf'), float('inf')
        res = float('inf')
        
        for i, word in enumerate(words):
            if word not in [word1, word2]:
                continue
            if word == word1:
                first = i
            elif word == word2:
                second = i
            res = min(res, abs(first - second))
        
        return res

# Solution 2, two-pointer, similar idea
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        i = j = 0
        n = len(words)
        
        res = float('inf')
        
        while i < n and j < n:
            while i < n and words[i] != word1:
                i += 1
            
            while j < n and words[j] != word2:
                j += 1
            
            if i < n and j < n:
                res = min(res, abs(i - j))
                if i < j:
                    i += 1
                else:
                    j += 1
        return res