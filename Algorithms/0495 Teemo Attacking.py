class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        
        res = 0
        curr = timeSeries[0]
        
        for t in timeSeries[1:]:
            if curr + duration < t:
                res += duration
            else:
                res += t - curr
            curr = t
            
        res += duration
        
        return res