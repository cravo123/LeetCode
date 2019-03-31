# Solution 1, O(m * n) memory
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0]) if obstacleGrid else 0
        
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][1] = 1
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if obstacleGrid[i - 1][j - 1] == 0:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        
        return dp[-1][-1]

# Solution 2, O(n) memory
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0]) if obstacleGrid else 0
        
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if obstacleGrid[i - 1][j - 1] == 0:
                    dp[j] = dp[j - 1] + dp[j]
                else:
                    dp[j] = 0
        
        return dp[-1]

# There are different follow-ups on these questions
# Follow-up 1, improve memory efficiency to O(n) as in Solution 2

# Follow-up 2, start from top-left to top-right, each step can be 
# right, right-up and right-down.
# we need two O(n) array to maintain prev and curr column results.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # top-left to top-right, each step is right, right-up, and right-down
        
        prev = [0 for _ in range(m)]
        curr = prev[::]
        prev[0] = 1
        
        for j in range(1, n):
            for i in range(m):
                curr[i] = prev[i]
                
                if i > 0:
                    curr[i] += prev[i - 1]
                if i + 1< m:
                    curr[i] += prev[i + 1]
                   
            prev, curr = curr, prev
            
        return prev[0]

# Follow-up 3, same as Follow-up 2, but with one more constraint. There is a lower 
# bound H, find all paths that touch or go through lower bound.
