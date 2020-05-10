# Solution 1, simulation
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        curr_max = max(candies)
        
        return [c + extraCandies >= curr_max for c in candies]