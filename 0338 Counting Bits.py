class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0 for _ in range(num + 1)]
        for i in range(1, num + 1):
            dp[i] = dp[i // 2] + i % 2
        
        return dp