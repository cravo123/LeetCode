# Solution 1
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        n = len(candies)
        kinds = len(set(candies))
        
        return min(n // 2, kinds)