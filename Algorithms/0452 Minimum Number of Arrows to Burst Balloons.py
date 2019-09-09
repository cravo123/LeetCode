# Solution 1, sort by end point
# In interval-related problems, sometimes we need to sort intervals by
# end-point instead of start-point to have correct/optimal results.
# Another example is task-scheduler

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        
        res = 0
        curr = float('-inf')
        print(points)
        for p in points:
            if not p[0] <= curr <= p[1]:
                res += 1
                curr = max(curr, p[1])
        
        return res

# Solution 2, optimized condition
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        
        prev = float('-inf')
        res = 0
        
        for p in points:
            if prev < p[0]:
                res += 1
                prev = p[1]
        
        return res