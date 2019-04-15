# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# Solution 1, add newInterval to list and sort
# Time complexity, O(nlogn)
class Solution:
    def insert(self, intervals: List[Interval], newInterval: Interval) -> List[Interval]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x.start)
        
        q = []
        
        for p in intervals:
            if not q or q[-1].end < p.start:
                q.append(p)
            else:
                q[-1].end = max(q[-1].end, p.end)
        return q

# Solution 2, insert inplace
class Solution:
    def insert(self, intervals: List[Interval], newInterval: Interval) -> List[Interval]:
        q = []
        n = len(intervals)
        i = 0
        curr = newInterval
        while i < n and intervals[i].end < curr.start:
            q.append(intervals[i])
            i += 1
        
        while i < n and intervals[i].start <= curr.end:
            curr.start = min(curr.start, intervals[i].start)
            curr.end = max(curr.end, intervals[i].end)
            i += 1
        q.append(curr)
        
        while i < n:
            q.append(intervals[i])
            i += 1
        
        return q