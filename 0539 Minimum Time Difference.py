# Sorting is O(nlogn), if we use bucket sorting, then it is O(n)
class Solution:
    def diff(self, a, b):
        ah, am = a.split(':')
        bh, bm = b.split(':')
        
        res = int(bh) * 60 + int(bm) - int(ah) * 60 - int(am)
        
        return res
        
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        
        res = float('inf')
        
        for i in range(1, len(timePoints)):
            res = min(res, self.diff(timePoints[i - 1], timePoints[i]))
        
        res = min(res, abs(1440 - self.diff(timePoints[0], timePoints[-1])))
        
        return res