# Solution 1, back-tracking
# TLE
class Solution:
    def dfs(self, idx, s):
        if idx == len(s):
            return 1
        if s[idx] == '0':
            return 0
        res = 0
        res += self.dfs(idx + 1, s)
        if 10 <= int(s[idx:(idx + 2)]) <= 26:
            res += self.dfs(idx + 2, s)
        return res
        
    def numDecodings(self, s: str) -> int:
        res = self.dfs(0, s)
        
        return res

# Solution 2, back-tracking with memoization
# THis will solve TLE.
class Solution:
    def dfs(self, idx, s, d):
        if idx in d:
            return d[idx]
        if idx == len(s):
            res = 1
        elif s[idx] == '0':
            res = 0
        else:
            res = 0
            res += self.dfs(idx + 1, s, d)
            if 10 <= int(s[idx:(idx + 2)]) <= 26:
                res += self.dfs(idx + 2, s, d)
        d[idx] = res
        return res
        
    def numDecodings(self, s: str) -> int:
        d = {}
        res = self.dfs(0, s, d)
        
        return res

# Solution 3, DP, O(n) memory
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        
        dp = [0 for _ in range(n)]
        
        for i in range(n):
            if s[i] != '0':
                dp[i] += dp[i - 1] if i - 1 >= 0 else 1
            if i >= 1 and 10 <= int(s[(i - 1):(i + 1)]) <= 26:
                dp[i] += dp[i - 2] if i - 2 >= 0 else 1
        return dp[-1]

# Solution 4, DP, O(1) memory
class Solution:
    def numDecodings(self, s: str) -> int:
        prev1 = 1 # number of decode ways at i - 1 position
        prev2 = 1 # number of decode ways at i - 2 position
        
        n = len(s)
        
        for i in range(n):
            curr = 0
            if s[i] != '0':
                curr += prev1
            if i > 0 and 10 <= int(s[(i - 1):(i + 1)]) <= 26:
                curr += prev2
            prev2, prev1 = prev1, curr
        
        return curr