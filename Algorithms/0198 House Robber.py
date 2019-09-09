# Solution 1, a more generic solution, O(N) space
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0, 0] for _ in range(n + 1)]
        
        for i in range(n):
            dp[i + 1][1] = nums[i] + dp[i][0]
            dp[i + 1][0] = max(dp[i][0], dp[i][1])
        
        return max(dp[-1])

# Solution 2, O(1) space
class Solution:
    def rob(self, nums: List[int]) -> int:
        do = not_do = 0
        
        for c in nums:
            do, not_do = c + not_do, max(do, not_do)
        
        return max(do, not_do)