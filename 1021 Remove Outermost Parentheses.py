class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = ['']
        j = 0
        cnt = 0
        for i, c in enumerate(S):
            if c == '(':
                cnt += 1
            elif c == ')':
                cnt -= 1
                if cnt == 0:
                    if j + 1 != i:
                        res.append(S[(j + 1):i])
                    j = i + 1
        
        res = ''.join(res)
        
        return res