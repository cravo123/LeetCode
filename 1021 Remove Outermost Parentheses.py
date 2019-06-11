# Solution 1, simulation
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = []
        j = 0
        cnt = 0
        for i, c in enumerate(S):
            if c == '(':
                cnt += 1
            elif c == ')':
                cnt -= 1
                if cnt == 0:
                    res.append(S[(j + 1):i])
                    j = i + 1
        res.append(S[(j + 1):-1])
        res = ''.join(res)
        
        return res

# Solution 2, temp save
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = []
        q = []
        cnt = 0
        
        for c in S:
            q.append(c)
            if c == '(':
                cnt += 1
            else:
                cnt -= 1
                
                if cnt == 0:
                    res.append(''.join(q[1:-1]))
                    q = []
        res.append(''.join(q[1:-1]))
        res = ''.join(res)
        
        return res