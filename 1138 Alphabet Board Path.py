# Solution 1, simulation
# Idea is to calculate start and end position
# Because 'Z' is a single value at the end, 
# so if start < end, then start can not be 'z', 
# so it is safe to first move cols then rows.
# if start > end, so end can not be 'z', 
# then it is safe to move rows 
class Solution:
    def cal_path(self, start, end):
        s = ord(start) - ord('a')
        e = ord(end) - ord('a')
        
        r_s = s // 5
        c_s = s % 5
        
        r_e = e // 5
        c_e = e % 5
        
        res = ''
        if s < e:
            res += ('R' if c_s < c_e else 'L') * abs(c_s - c_e)
            res += 'D' * (r_e - r_s)
        else:
            res += 'U' * (r_s - r_e)
            res += ('R' if c_s < c_e else 'L') * abs(c_s - c_e)
        
        return res + '!'
            
        
    def alphabetBoardPath(self, target: str) -> str:
        res = ''.join([self.cal_path(s, e) for s, e in zip('a' + target, target)])
        
        return res

# Solution 1.1, better implementation
# From observation in Solution 1
# t.b.c
