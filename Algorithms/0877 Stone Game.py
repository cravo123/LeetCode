# Solution 1, memoization
# d stores the maximum extra points 1st player could win over 2nd player
# if 1st player starts with piles bounded by left and right index
class Solution:
    def dfs(self, left, right, piles, d):
        if (left, right) in d:
            return d[(left, right)]
        if left == right:
            return piles[left]
        res = max(piles[left] - self.dfs(left + 1, right, piles, d), piles[right] - self.dfs(left, right - 1, piles, d))
        d[(left, right)] = res
        
        return res
        
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        d = {}
        
        self.dfs(0, n - 1, piles, d)
        
        return d[(0, n - 1)] > 0

# Solution 2, DP, same idea as Solution 1
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = piles[i]
        
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                left, right = i, i + l - 1
                dp[left][right] = max(piles[left] - dp[left + 1][right], piles[right] - dp[left][right - 1])
        
        return dp[0][n - 1] > 0
