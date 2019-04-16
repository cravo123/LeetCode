class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0]) if dungeon else 0
        
        dp = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
        
        dp[m - 1][n] = 1
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                v = min(dp[i][j + 1], dp[i + 1][j])
                dp[i][j] = max(1, v - dungeon[i][j])
        
        return dp[0][0]