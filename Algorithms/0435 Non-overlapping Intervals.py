# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# Solution 1, Greedy
# Note there is a buy in LeetCode here, Interval is represented as list 
# of length 2 instead of real Interval class
class Solution:
    def eraseOverlapIntervals(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x[1])
        
        res = 0
        prev = float('-inf')
        
        for i in intervals:
            if prev > i[0]:
                res += 1
            else:
                prev = i[1]
        return res