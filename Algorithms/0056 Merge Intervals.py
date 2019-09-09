# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# Solution 1, sort and merge
class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x.start)
        
        res = []
        curr = intervals[0]
        
        for i in range(1, len(intervals)):
            if curr.end < intervals[i].start:
                res.append(curr)
                curr = intervals[i]
            else:
                curr.end = max(curr.end, intervals[i].end)
        
        res.append(curr)
        
        return res

# Solution 2, heapq
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from heapq import *

class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        res = []
        if not intervals:
            return res
        
        intervals = [[x.start, x.end] for x in intervals]
        heapify(intervals)
        
        curr_start, curr_end = None, None
        while intervals:
            tmp = heappop(intervals)
            if curr_start is None:
                curr_start, curr_end = tmp
            elif curr_end < tmp[0]:
                res.append(Interval(curr_start, curr_end))
                curr_start, curr_end = tmp
            else:
                curr_end = max(curr_end, tmp[1])
        res.append(Interval(curr_start, curr_end))
        
        return res