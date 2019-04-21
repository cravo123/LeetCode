# Solution 1, Stack
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        s = input.split('\n')
        
        q = [[-1, '']]
        res = 0
        
        for v in s:
            cnt = v.count('\t')
            v = v[cnt:]
            
            while q and q[-1][0] >= cnt:
                q.pop()
        
            if '.' in v:
                # Cuz we add an extra '\\' at the beginning,
                # so it is len(q[-1][1]) + len(v) instead of
                # len(q[-1][1]) + len(v) + 1
                res = max(res, len(q[-1][1]) + len(v))
            else:
                q.append([cnt, q[-1][1] + '\\' + v])
                
        return res

# Solution 2, similar idea but without stack
# Actually we don't need to maintain a stack to track folder level
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        d = {}
        d[-1] = 0
        
        res = 0
        for s in input.split('\n'):
            cnt = s.count('\t')
            s = s[cnt:]
            
            if '.' in s:
                res = max(res, d[cnt - 1] + len(s))
            else:
                d[cnt] = d[cnt - 1] + 1 + len(s)
        return res