# Solution 1, 1-dimension DP
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        if n < 3:
            return 0
        
        dp = [1 for _ in A]
        dp[1] = 2
        res = 0
        
        for i in range(2, n):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp[i] = max(dp[i - 1] + 1, 3)
                
                if dp[i] >= 3:
                    res += dp[i] - 2
        
        return res

# Solution 1.1,DP with O(1) memory
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        
        curr = 0
        res = 0
        
        for i in range(2, n):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                curr += 1
                res += curr
            else:
                curr = 0
        
        return res

# Solution 2, DP, TLE
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        res = 0
        for i in range(n):
            dp[i][i] = 1
        
        for i in range(n):
            for length in range(2, i + 2):
                left, right = i - length + 1, i
                if A[right] - A[left] == (A[right] - A[right - 1]) * (right - left):
                    dp[left][right] = dp[left][right - 1]
                if right - left > 1 and dp[left][right]:
                    res += 1
        
        return res