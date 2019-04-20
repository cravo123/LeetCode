# Solution 1, memoization, top-down DP
class Solution:
    def dfs(self, start, end, nums, d):
        if start > end:
            return 0
        if (start, end) in d:
            return d[start, end]
        res = max(nums[start] - self.dfs(start + 1, end, nums, d), nums[end] - self.dfs(start, end - 1, nums, d))
        
        d[start, end] = res
        
        return res
        
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        
        d = {}
        
        return self.dfs(0, n - 1, nums, d) >= 0

# Solution 2, bottom-up DP, interval-DP
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        
        dp = [[float('-inf') for _ in range(n)] for _ in range(n)]
        
        for l in range(1, n + 1):
            for i in range(n - l + 1):
                left, right = i, i + l - 1
                if left == right:
                    dp[left][right] = nums[left]
                else:
                    dp[left][right] = max(nums[left] - dp[left + 1][right],
                                          nums[right] - dp[left][right - 1])
        
        return dp[0][n - 1] >= 0

# Solution 3, bottom-up DP with O(n) memory
# So we can use left and right index directly
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        
        dp = [float('-inf') for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[j] = nums[i]
                else:
                    dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
        
        return dp[n - 1] >= 0