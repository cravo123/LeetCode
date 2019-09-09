class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        k = 2
        dp = [[0 for _ in prices] for _ in range(k + 1)]
        
        for i in range(1, k + 1):
            curr_max = dp[i - 1][0] - prices[0]
            for j in range(1, len(prices)):
                dp[i][j] = max(dp[i][j - 1], curr_max + prices[j])
                curr_max = max(curr_max, dp[i - 1][j] - prices[j])
        
        return dp[-1][-1]