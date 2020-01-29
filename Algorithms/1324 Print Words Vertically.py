# Solution 1, simulation
# Allocate lists with space string beforehand, similar to Problem 6, Zigzag conversion
class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        row = max(len(w) for w in words)
        col = len(words)
        
        res = [[' ' for _ in range(col)] for _ in range(row)]
        
        for j, word in enumerate(words):
            for i, c in enumerate(word):
                res[i][j] = c
        
        res = [''.join(x).rstrip() for x in res]
        
        return res