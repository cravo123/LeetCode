# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# Solution 1, sorting
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        
        curr_end = float('-inf')
        
        for interval in intervals:
            if curr_end > interval.start:
                return False
            curr_end = interval.end
        
        return True
