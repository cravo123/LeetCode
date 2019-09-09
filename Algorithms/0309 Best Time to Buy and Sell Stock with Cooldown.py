# Solution 1, DP
# The idea is general to LC 0309 and LC 0714.
# We set two sets, holding stock and holding cash
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        dp = [[0, 0] for _ in prices]
        dp[0][1] = -prices[0]
        
        for i in range(1, len(prices)):
            dp[i][1] = max(dp[i - 1][1], dp[max(i - 2, 0)][0] - prices[i])
            
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        
        return dp[-1][0]
        