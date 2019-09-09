# Solution 1, DP, O(N) space
class Solution:
    def minCostClimbingStairs(self, cost: 'List[int]') -> 'int':
        n = len(cost)
        dp = [0 for _ in range(n + 1)]
        
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
        return dp[-1]

# Solution 2, DP, O(1) space
class Solution:
    def minCostClimbingStairs(self, cost: 'List[int]') -> 'int':
        prev = curr = 0
        idx = 2
        n = len(cost)
        while idx < n + 1:
            tmp = min(prev + cost[idx - 2], curr + cost[idx - 1])
            prev, curr = curr, tmp
            idx += 1
        return curr