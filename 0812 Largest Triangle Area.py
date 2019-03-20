class Solution:
    def calc_area(self, a, b, c):
        # shoelace theorem
        res = abs(a[0] * b[1] + b[0] * c[1] + c[0] * a[1] - a[1] * b[0] - b[1] * c[0] - c[1] * a[0])
        
        return res / 2
        
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = 0
        
        n = len(points)
        
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    curr_area = self.calc_area(points[i], points[j], points[k])
                    res = max(res, curr_area)
        
        return res