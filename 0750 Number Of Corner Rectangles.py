import collections
class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        d = collections.defaultdict(set)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    d[i].add(j)
        
        res = 0
        
        for i in range(m):
            for j in range(i):
                cnt = len(d[i] & d[j])
                res += cnt * (cnt - 1) // 2
        
        return res