# Solution 1, simulation using dict
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        d = {c:i for i, c in enumerate(keyboard)}
        
        res = prev = 0
        
        for c in word:
            res += abs(d[c] - prev)
            prev = d[c]
        
        return res

# Solution 1.1, list comprehension
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        d = {c:i for i, c in enumerate(keyboard)}
        
        idx = [d[c] for c in word]
        res = sum(abs(curr - prev) for curr, prev in zip(idx, [0] + list(idx)))
        
        return res