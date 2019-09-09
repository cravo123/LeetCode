# Solution 1, shoe-lace formula
class Solution:
    def calc_area(self, a, b, c):
        # shoelace formula
        res = abs(a[0] * b[1] + b[0] * c[1] + c[0] * a[1] 
            - a[1] * b[0] - b[1] * c[0] - c[1] * a[0])
        
        return res / 2
        
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = 0
        
        n = len(points)
        
        for i in range(2, n):
            for j in range(1, i):
                for k in range(j):
                    curr_area = self.calc_area(points[i], points[j], points[k])
                    res = max(res, curr_area)
        
        return res