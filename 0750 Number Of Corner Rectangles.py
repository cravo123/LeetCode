import collections
# Solution 1, O(m * m * n * n), which is not efficient
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

# Solution 2, DP idea
# dp[(j, k)] records how many rows we have seen so far that have 1s at col j and k
class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        dp = collections.Counter()
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for k in range(j + 1, n):
                        if grid[i][k] == 1:
                            res += dp[j, k]
                            dp[j, k] += 1
        
        return res