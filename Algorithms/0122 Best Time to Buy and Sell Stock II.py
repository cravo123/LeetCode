class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        return sum(max(y - x, 0) for y, x in zip(prices[1:], prices))