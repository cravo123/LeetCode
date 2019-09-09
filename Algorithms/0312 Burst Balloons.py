# Solution 1, interval DP, O(N ^ 3)
# dp[i][j] means maximum points we could get by bursting all balloons 
# from i to j inclusive
# so dp[i][j] = max(dp[i][j], 
#   nums[left - 1] * nums[k] * nums[right + 1] + dp[left][k - 1] + dp[k + 1][right])
# k is the last balloon in [i, j]

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n = len(nums)
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for length in range(1, n - 1):
            for i in range(1, n - length):
                left = i
                right = i + length - 1
                for k in range(left, right + 1):
                    dp[left][right] = max(dp[left][right],
                                         nums[left - 1] * nums[k] * nums[right + 1] + dp[left][k - 1] + dp[k + 1][right])
        
        return dp[1][-2]

# Solution 2, Top-down DP
class Solution(object):
    def dfs(self, left, right, nums, d):
        if (left, right) in d:
            return d[left, right]
        
        if left == right:
            d[left, right] = nums[left - 1] * nums[left] * nums[left + 1]
            return d[left, right]
        
        if left > right:
            return 0
        
        res = 0
        
        for k in range(left, right + 1):
            res = max(res, nums[left - 1] * nums[k] * nums[right + 1] + 
                     self.dfs(left, k - 1, nums, d) + self.dfs(k + 1, right, nums, d))
        d[left, right] = res
        return res
        
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = {i:c for i, c in enumerate(nums)}
        nums[-1] = 1
        nums[n] = 1
        d = {}
        
        res = self.dfs(0, n - 1, nums, d)
        return res