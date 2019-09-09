# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        q = [(x[0], i) for i, x in enumerate(intervals)]
        q.sort()
        
        res = []
        
        for x in intervals:
            j = bisect.bisect_left(q, (x[1], float('-inf')))
            res.append(q[j][1] if j < len(intervals) else -1)
        
        return res