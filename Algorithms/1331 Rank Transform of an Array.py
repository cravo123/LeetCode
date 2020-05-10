# Solution 1, simulation

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a = sorted(arr)
        d = {}
        
        i = 1
        for v in a:
            if v not in d:
                d[v] = i
                i += 1
        
        res = [d[v] for v in arr]
        
        return res