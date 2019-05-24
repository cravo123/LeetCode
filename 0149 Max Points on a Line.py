import collections
# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

# Solution 1, for each point i, iterate all j in range(i + 1, n)
# check how many points are on the same line.
class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
        
    def maxPoints(self, points: List[Point]) -> int:
        
        res = 0
        n = len(points)
        for i in range(n):
            same = 1
            d = collections.Counter()
            for j in range(i + 1, n):
                dx, dy = points[j][0] - points[i][0], points[j][1] - points[i][1]
                if dx == dy == 0:
                    same += 1
                else:
                    v = self.gcd(dx, dy)
                    if v != 0:
                        dx //= v
                        dy //= v
                    # (x, 0) -> (1, 0)
                    # (0, y) -> (0, 1)
                    d[dx, dy] += 1
            
            res = max(max(d.values() or [0]) + same, res)
        
        return res