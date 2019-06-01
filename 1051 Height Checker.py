# Solution 1, simulation
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        target = heights[::]
        target.sort()
        
        res = sum(1 if a != b else 0 for a, b in zip(heights, target))
        
        return res