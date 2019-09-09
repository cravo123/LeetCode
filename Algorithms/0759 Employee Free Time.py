# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from heapq import *

# Solution 1, Priority Queue, space efficient, but not as fast as built-in
# priority queue saves "iterator of each person's time"
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
    def employeeFreeTime(self, schedule: List[List[List[int]]]) -> List[List[int]]:
        q = []
        
        for ts in schedule:
            q.extend(ts)
        
        q.sort()
        
        res = []
        
        curr = q[0][1]
        
        for t in q:
            if curr < t[0]:
                res.append([curr, t[0]])
            curr = max(curr, t[1])
        
        return res

# Solution 3, sweep line
class Solution:
    def employeeFreeTime(self, schedule: List[List[List[int]]]) -> List[List[int]]:
        q = []
        
        for ts in schedule:
            for t in ts:
                q.append([t[0], 1])
                q.append([t[1], -1])
        
        q.sort()
        cnt = 0
        prev = q[0][0]
        res = []
        
        for t, tag in q:
            if cnt == 0 and prev < t:
                res.append([prev, t])
            prev = max(prev, t)
            cnt += tag
        
        return res