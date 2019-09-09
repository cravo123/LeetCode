# Solution 1, DP
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        dp = [[0 for _ in range(N)] for _ in range(N)]
        dp[r][c] = 1
        
        for _ in range(K):
            dp2 = [[0 for _ in range(N)] for _ in range(N)]
            
            for i in range(N):
                for j in range(N):
                    dp[i][j] /= 8
                    for di, dj in [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]:
                        x, y = i + di, j + dj
                        if 0 <= x < N and 0 <= y < N:
                            dp2[x][y] += dp[i][j]
            dp = dp2
        
        return sum(sum(row) for row in dp)

# Solution 2, Markov Chain, state matrix exponential
# t.b.c