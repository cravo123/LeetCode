# Solution 1, enumerate all possibilities
class Solution:
    def check(self, a, b, c, d):
        x1, y1 = b[0] - a[0], b[1] - a[1]
        x2, y2 = d[0] - c[0], d[1] - c[1]
        
        return (x1 * x2 + y1 * y2 == 0 and x1 * x1 + y1 * y1 == x2 * x2 + y2 * y2
                and a[0] + b[0] == c[0] + d[0] and a[1] + b[1] == c[1] + d[1]
                and not (a[0] - b[0] == 0 and a[1] - b[1] == 0))
        
        
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        return (self.check(p1, p2, p3, p4) or self.check(p1, p3, p2, p4) 
                or self.check(p1, p4, p2, p3))