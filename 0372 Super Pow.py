# a ^ (xy) means a ^ (10x) * a ^ y
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mo = 1337
        curr = pow(a, b[0]) % mo
        
        for c in b[1:]:
            curr = pow(curr, 10) % mo
            curr = (curr * (pow(a, c) % mo)) % mo
        
        return curr