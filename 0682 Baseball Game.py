class Solution:
    def calPoints(self, ops: 'List[str]') -> 'int':
        q = []
        
        for c in ops:
            if c == '+':
                q.append(q[-1] + q[-2])
            elif c == 'D':
                q.append(q[-1] * 2)
            elif c == 'C':
                q.pop()
            else:
                q.append(int(c))
        return sum(q)