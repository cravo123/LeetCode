# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from heapq import *

# Solution 1, sort and merge
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        
        res = []
        left, right = intervals[0]
        
        for x, y in intervals:
            if right < x:
                res.append([left, right])
                left, right = x, y
            else:
                right = max(right, y)
        
        res.append([left, right])
        
        return res

# Solution 2, heapq
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