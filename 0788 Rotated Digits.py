# Solution 1, Brute-Force
class Solution:
    def is_good(self, num):
        n = str(num)
        if any(c in n for c in '347'):
            return False
        if all(c in '018' for c in n):
            return False
        return True
        
    def rotatedDigits(self, N: int) -> int:
        res = 0
        for i in range(1, N + 1):
            if self.is_good(i):
                res += 1
        return res

# Solution 2, DP
class Solution:
    def rotatedDigits(self, N: int) -> int:
        dp = [[0, 0] for _ in range(N + 1)]
        # dp[i][0] = 1 means it rotate to itself
        # dp[i][1] = 1 means it rote to a different number
        dp[0] = [1, 0] 
        
        res = 0
        for i in range(1, N + 1):
            left = i // 10
            right = i % 10
            
            if right in [3, 4, 7]:
                continue
            
            if right in [0, 1, 8]:
                if dp[left][1]:
                    dp[i][1] = 1
                dp[i][0] = dp[left][0]
            else:
                dp[i][1] = 1 if dp[left][0] + dp[left][1] > 0 else 0 
            
            res += dp[i][1]
        
        return res