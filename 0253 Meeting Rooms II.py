# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from heapq import *
# sweeping line solution
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        q = []
        
        for interval in intervals:
            heappush(q, [interval.start, 1])
            heappush(q, [interval.end, -1])
        
        curr = res = 0
        
        while q:
            t, flag = heappop(q)
            curr += flag
            res = max(res, curr)
        
        return res