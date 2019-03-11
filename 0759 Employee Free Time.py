# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from heapq import *

# Solution 1, Priority Queue, space efficient, but not as fast as built-in
class Solution:
    def employeeFreeTime(self, schedule: List[List[Interval]]) -> List[Interval]:
        q = []
        
        pre = float('inf')
        
        for i, row in enumerate(schedule):
            if row:
                heappush(q, [row[0].start, row[0].end, i, 0])
                pre = min(pre, row[0].start)
        
        res = []
        
        while q:
            start, end, i, j = heappop(q)
              
            if pre < start:
                res.append(Interval(pre, start))
            
            pre = max(pre, end)
            
            if j < len(schedule[i]) - 1:
                j += 1
                row = schedule[i][j]
                heappush(q, [row.start, row.end, i, j])
        return res

# Solution 2, built-in sort
class Solution:
    def employeeFreeTime(self, schedule: List[List[Interval]]) -> List[Interval]:
        if not schedule:
            return []
        q = []
        
        for row in schedule:
            q.extend(row)
        
        q.sort(key=lambda x: x.start)
        
        res = []
        pre = q[0].start
        
        for row in q:
            if pre < row.start:
                res.append(Interval(pre, row.start))
            pre = max(pre, row.end)
        
        return res