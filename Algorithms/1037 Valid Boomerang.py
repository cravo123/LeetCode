# Solution 1, simulation
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        a, b, c = points
        
        d1 = [a[0] - b[0], a[1] - b[1]]
        d2 = [a[0] - c[0], a[1] - c[1]]
        
        # Instead of coupling with corner-cases that divisor could be zero
        # we can use multiplication instead
        return (a != b and a != c and b != c) and (d1[0] * d2[1] != d1[1] * d2[0])