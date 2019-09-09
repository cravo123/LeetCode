# Solution 1, similar idea as Solution 2
# Only check 
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        s = [i for i, c in enumerate(start) if c != 'X']
        e = [i for i, c in enumerate(end) if c != 'X']
        
        return (len(s) == len(e) and 
            all(start[i] == end[j] and (i >= j if start[i] == 'L' else i <= j) 
                for i, j in zip(s, e)))

# Solution 2, observation
# 'L' can only move left and 'R' can only move right
# Since we need to transform from 'start' to 'end', we can 
# mark 'X' count difference
# cnt < 0 when we have 'L', cannot match
#   start: XLXX
#   end:   XXXL
# cnt > 0 when we have 'R', cannot match either
#   start: XXXR
#   end:   XRXX

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        i = j = 0
        m, n = map(len, (start, end))
        cnt = 0
        
        while i < m and j < n:
            while i < m and start[i] == 'X':
                cnt += 1
                i += 1
            while j < n and end[j] == 'X':
                cnt -= 1
                j += 1
            
            if i == m and j == n:
                return cnt == 0
            
            if i == m or j == n:
                return False
            
            # L can only go left and R can only go right
            if i < m and j < n:
                if start[i] != end[j]:
                    return False
                if start[i] == 'L' and cnt < 0:
                    return False
                if start[i] == 'R' and cnt > 0:
                    return False
                  
                i += 1
                j += 1
        return True