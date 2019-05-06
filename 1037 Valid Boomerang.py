class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # Instead of coupling with corner-cases that divisor could be zero
        # we can use multiplication instead
        x, y = points[0]
        diff = [[p[0] - x, p[1] - y] for p in points[1:]]
        
        return diff[0][1] * diff[1][0] != diff[0][0] * diff[1][1]