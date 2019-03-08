class Solution:
    def check(self, v):
        for c in str(v):
            if c == '0' or v % int(c) > 0:
                return False
        return True
        
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        res = [c for c in range(left, right + 1) if self.check(c)]
        
        return res