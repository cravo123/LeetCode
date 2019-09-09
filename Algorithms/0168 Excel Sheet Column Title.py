# Solution 1, simulation
class Solution:
    def convertToTitle(self, n: int) -> str:
        q = []
        
        while n > 0:
            idx = (n - 1) % 26
            q.append(chr(ord('A') + idx))
            n = (n - 1) // 26
        
        res = ''.join(q[::-1])
        
        return res

# Note Excel column is different from x-nary number
# in n-ary, it is illegal to write '00'
# but in Excel column, it is ok to write 'AA'