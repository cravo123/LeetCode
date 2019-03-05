# Solution 1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = curr_min = 0
        res = 0
        
        for i in range(1, len(prices)):
            dp = prices[i] - prices[i - 1]
            curr += dp
            curr_min = min(curr_min, curr)
            res = max(res, curr - curr_min)
        return res

# Solution 2
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        curr_min = float('inf')
        
        for c in prices:
            curr_min = min(curr_min, c)
            res = max(res, c - curr_min)
        
        return res