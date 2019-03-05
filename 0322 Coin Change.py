# Solution 1, bottom-up dp
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        coins.sort(reverse=True)
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        
        return dp[-1] if dp[-1] < float('inf') else -1

# Solution 2, top-down dp(memoization)
class Solution(object):
    def dfs(self, coins, amount, d):
        if amount in d:
            return d[amount]
        if amount < 0:
            res = -1
        elif amount == 0:
            res = 0
        else:
            res = float('inf')
            for c in coins:
                t = self.dfs(coins, amount - c, d)
                if t != -1:
                    res = min(res, t + 1)
            res = res if res < float('inf') else -1
        d[amount] = res
        
        return res
        
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        d = {}
        
        self.dfs(coins, amount, d)
        
        return d[amount]