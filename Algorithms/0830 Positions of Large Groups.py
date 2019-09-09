# Solution 1, simulation
class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        res = []
        j, n = 0, len(S)
        
        for i, c in enumerate(S):
            if c != S[j]:
                if i - j > 2:
                    res.append([j, i - 1])
                j = i
        if n - j > 2:
            res.append([j, n - 1])
            
        return res

# Solution 1.1, if we want to get rid of duplicate "if i - j > 2" statement
# we can use two while for better loop control
class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        i, n = 0, len(S)
        res = []
        
        while i < n:
            j = i
            while j < n and S[i] == S[j]:
                j += 1
            
            if j - i > 2:
                res.append([i, j - 1])
            i = j
        
        return res