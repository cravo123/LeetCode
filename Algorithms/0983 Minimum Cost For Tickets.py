# Solution 1, maintain all calendar days
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [float('inf') for _ in range(366)]
        dp[0] = 0
        days = set(days)
        
        duration = [1, 7, 30]
        
        for i in range(1, 366):
            if i not in days:
                dp[i] = dp[i - 1]
            else:
                for j, c in zip(duration, costs):
                    dp[i] = min(dp[max(i - j, 0)] + c, dp[i])
        
        return dp[-1]

# Solution 2, DP only on travel days
class Solution:
    def solve(self, i, d, costs, days):
        if i in d:
            return d[i]
        
        if i >= len(days):
            return 0
        
        res = float('inf')
        j = i
        for c, v in zip(costs, [1, 7, 30]):
            while j < len(days) and days[j] < days[i] + v:
                j += 1
            res = min(res, self.solve(j, d, costs, days) + c)
        d[i] = res
        
        return res
        
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        d = {}
        return self.solve(0, d, costs, days)