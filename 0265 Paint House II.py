# Solution 1, DP 
# but O(n * k * k) complexity
# memory O(n * k), Could be simplified to O(n)
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        n, k = len(costs), len(costs[0]) if costs else 0
        
        dp = [[0 for _ in range(k)] for _ in range(n)]
        
        for j in range(k):
            dp[0][j] = costs[0][j]
        
        for i in range(1, n):
            for j in range(k):
                # dp[i][j] means minimum cost to paint all houses from 0 to i
                # and house i paints j-th color
                dp[i][j] = min(dp[i - 1][x] for x in range(k) if x != j) + costs[i][j]
        
        return min(dp[-1])

# Solution 2, DP
# O(n * k) complexity
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        n, k = len(costs), len(costs[0]) if costs else 0
        
        dp = [[0 for _ in range(k)] for _ in range(n)]
        
        for j in range(k):
            dp[0][j] = costs[0][j]
        
        for i in range(1, n):
            min_1 = min(dp[i - 1])
            min_1_idx = dp[i - 1].index(min_1)
            
            min_2 = min(dp[i - 1][x] for x in range(k) if x != min_1_idx)
            
            for j in range(k):
                if j == min_1_idx:
                    dp[i][j] = min_2
                else:
                    dp[i][j] = min_1
                dp[i][j] += costs[i][j]
        
        return min(dp[-1])