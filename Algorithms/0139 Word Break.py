# Solution 1, Backward Split, memoization
class Solution:
    def dfs(self, idx, s, d, memo):
        if idx == len(s):
            return True
        if idx in memo:
            return memo[idx]
        flag = False
        for i in range(idx + 1, len(s) + 1):
            word = s[idx:i]
            if word in d and self.dfs(i, s, d, memo):
                flag = True
                break
        memo[idx] = flag
        
        return flag
        
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = set(wordDict)
        memo = {}
        
        return self.dfs(0, s, d, memo)

# Solution 2, DP, forward split
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = set(wordDict)
        
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in d:
                    dp[i] = True
        
        return dp[-1]
