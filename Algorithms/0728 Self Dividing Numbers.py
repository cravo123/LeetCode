# Solution 1, simulation
class Solution:
    def divisable(self, val):
        for c in map(int, str(val)):
            if c == 0 or val % c != 0:
                return False
        return True
        
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = [val for val in range(left, right + 1) if self.divisable(val)]
        
        return res