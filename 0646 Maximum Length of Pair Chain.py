# Solution 1, DP
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if not pairs:
            return 0
        
        pairs.sort()
        
        n = len(pairs)
        dp = [1 for _ in range(n)]
        
        for i in range(1, n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

# Solution 2, greedy, sort by end point
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        curr = float('-inf')
        res = 0
        
        pairs.sort(key=lambda x: x[1])
        
        for p in pairs:
            if curr < p[0]:
                res += 1
                curr = p[1]
        return res