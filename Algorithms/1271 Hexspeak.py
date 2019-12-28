# Solution 1, simulation
class Solution:
    def toHexspeak(self, num: str) -> str:
        d = {
            0: 'O',
            1: 'I',
            10: 'A',
            11: 'B',
            12: 'C',
            13: 'D',
            14: 'E',
            15: 'F'
        }
        
        num = int(num)
        q = []
        
        while num > 0:
            num, residual = divmod(num, 16)
            if 1 < residual < 10:
                return 'ERROR'
            q.append(d[residual])
        
        res = ''.join(reversed(q))
        
        return res