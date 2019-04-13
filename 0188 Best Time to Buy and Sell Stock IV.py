class Solution:
    def help(self, prices):
        res = sum(max(y - x, 0) for x, y in zip(prices, prices[1:]))
        return res
        
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        
        if k >= len(prices) // 2:
            return self.help(prices)
        
        dp = [[0 for _ in prices] for _ in range(k + 1)]
        
        for i in range(1, k + 1):
            curr_max = dp[i - 1][0] - prices[0]
            for j in range(1, len(prices)):
                dp[i][j] = max(dp[i][j - 1], curr_max + prices[j])
                curr_max = max(curr_max, dp[i - 1][j] - prices[j])
        
        return dp[-1][-1]