# Solution 1, simulation
# Basically this means the time travelled between two points is 
# equal to max(d_x, d_y)
class Solution:
    def calc_time(self, p1, p2):
        x_dist = abs(p1[0] - p2[0])
        y_dist = abs(p1[1] - p2[1])
        
        t = min(x_dist, y_dist)
        
        return t + abs(x_dist - t) + abs(y_dist - t)
        
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        res = 0
        
        for i in range(1, len(points)):
            res += self.calc_time(points[i], points[i - 1])
        
        return res