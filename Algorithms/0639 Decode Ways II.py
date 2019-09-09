# Solution 1, DP, very complex conditions
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        dp = [0 for _ in range(n + 1)]
        
        dp[0] = 1
        
        for i in range(1, n + 1):
            if s[i - 1] == '*':
                dp[i] += 9 * dp[i - 1]
                if i > 1:
                    if s[i - 2] == '1':
                        dp[i] += 9 * dp[i - 2]
                    if s[i - 2] == '2':
                        dp[i] += 6 * dp[i - 2]
                    if s[i - 2] == '*':
                        dp[i] += 15 * dp[i - 2]
            else:
                if s[i - 1] != '0':                    
                    dp[i] += dp[i - 1]
                if i > 1:
                    if s[i - 2] == '*':
                        dp[i] += dp[i - 2]
                        if '0' <= s[i - 1] <= '6':
                            dp[i] += dp[i - 2]
                    else:
                        if '10' <= s[(i - 2):i] <= '26':
                            dp[i] += dp[i - 2]
        return dp[-1] % int(10 ** 9 + 7)

# Solution 2, elegant
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        
        for i in range(1, n + 1):
            if s[i - 1] == '*':
                dp[i] += dp[i - 1] * 9
            elif s[i - 1] != '0':
                dp[i] += dp[i - 1]
            
            if i > 1:
                v = s[(i - 2):i]
                if v == '**':
                    dp[i] += 15 * dp[i - 2]
                elif v[0] == '*':
                    dp[i] += dp[i - 2]
                    if '0' <= v[1] <= '6':
                        dp[i] += dp[i - 2]
                elif v[1] == '*':
                    if v[0] == '1':
                        dp[i] += 9 * dp[i - 2]
                    elif v[0] == '2':
                        dp[i] += 6 * dp[i - 2]
                    
                elif '10' <= v <= '26':
                    dp[i] += dp[i - 2]
        
        return dp[-1] % (int(10 ** 9 + 7))