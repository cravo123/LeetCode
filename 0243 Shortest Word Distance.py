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