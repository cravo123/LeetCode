# Solution 1, knapsack, similar to LC 115 Distinct Subsequence
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m, n = amount, len(coins)
        
        dp = [[0 for _ in range(n + 1)] for _ in range(amount + 1)]
        
        for j in range(n + 1):
            dp[0][j] = 1
        
        for i in range(1, amount + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i][j - 1]
                if i >= coins[j - 1]:
                    dp[i][j] += dp[i - coins[j - 1]][j]
        
        return dp[-1][-1]

# Solution 2, space-optimized DP, knapsack
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        
        for c in coins:
            for i in range(1, amount + 1):
                if i - c >= 0:
                    dp[i] += dp[i - c]
        return dp[-1]