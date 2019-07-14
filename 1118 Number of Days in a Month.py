# Solution 1, simulation
class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        d = set([1, 3, 5, 7, 8, 10, 12])
        
        if M == 2:
            if Y % 400 == 0 or (Y % 100 != 0 and Y % 4 == 0):
                return 29
            return 28
        elif M in d:
            return 31
        
        return 30