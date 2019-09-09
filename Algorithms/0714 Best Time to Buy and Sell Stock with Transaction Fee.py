# DP idea
# dp[i][1] means maximum cash we could have when holding one share of stock
# dp[i][0] means maximum cash we could have when holding no share of stock
# Similar idea could be applied to LC 309 Buy and Sell stock with cool-down

# Solution 1, O(n) memory DP 
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0, 0] for _ in prices]
        dp[0][1] = - prices[0] - fee
        
        for i in range(1, len(prices)):
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        
        return dp[-1][0]

# Solution 2, since time t result only depends on t - 1, 
# we can optimize to use O(1) memory