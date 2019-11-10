# Solution 1, simulation using dict
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rs = collections.Counter()
        cs = collections.Counter()
        
        for i, j in indices:
            rs[i] += 1
            cs[j] += 1
        
        res = sum(1 for i in range(n) for j in range(m) if (rs[i] + cs[j]) % 2 == 1)
        
        return res
