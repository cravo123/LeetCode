# Solution 1, sweeping line algorithm
class Solution:
    def check(self, s, left, right):
        n = len(s)
        
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        
        return left + 1, right
        
    def longestPalindrome(self, s: str) -> str:
        res = ''
        res_len = 0
        n = len(s)
        for i in range(n):
            left, right = self.check(s, i, i)
            if right - left > res_len:
                res_len = right - left
                res = s[left:right]
            
            left, right = self.check(s, i, i + 1)
            if right - left > res_len:
                res_len = right - left
                res = s[left:right]
        
        return res

# Solution 2, dynamic programming
# Notice corner-case of length 1 and length 2
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        n = len(s)
        
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            if i > 0:
                dp[i][i - 1] = True
        
        res = s[0]
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                left, right = i, i + length - 1
                if s[left] == s[right] and dp[left + 1][right - 1]:
                    dp[left][right] = True
                    if len(res) < right - left + 1:
                        res = s[left:(right + 1)]
        return res