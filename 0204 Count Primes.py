class Solution:
    def countPrimes(self, n: int) -> int:
        dp = [True for _ in range(max(n, 3))]
        dp[0] = dp[1] = False
        
        for i in range(2, int(n ** 0.5) + 1):
            if dp[i]:
                c = i + i
                while c < n:
                    dp[c] = False
                    c += i
        return sum(dp[:n])
        