# Solution 1, simulation
# Keep track of last attack time
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        
        res = 0
        prev = timeSeries[0]
        
        for t in timeSeries[1:]:
            res += min(t - prev, duration)
            prev = t
        
        return res + duration