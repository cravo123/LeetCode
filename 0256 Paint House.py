# Solution 1, this is an obvious dynamic programming solution
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[0 for _ in range(3)] for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            v = dp[i - 1]
            dp[i] = [min(v[1:]) + costs[i - 1][0], min(v[0], v[2]) + costs[i - 1][1], min(v[:-1]) + costs[i - 1][2]]
        
        return min(dp[-1])

# Solution 2, O(1) memory 
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        res = [0, 0, 0]
        
        for i in range(len(costs)):
            res = [min(res[1:]) + costs[i][0], min(res[0], res[2]) + costs[i][1], min(res[:-1]) + costs[i][2]]
        
        return min(res)