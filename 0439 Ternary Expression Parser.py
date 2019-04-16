# Solution 1, Stack + Reverse traversal is elegant
class Solution:
    def parseTernary(self, expression: str) -> str:
        s = expression
        i, n = 0, len(s)
        
        q = []
        
        for i in range(n - 1, -1, -1):
            c = s[i]
            if q and q[-1] == '?':
                q.pop() # '?'
                first = q.pop()
                q.pop() # ':'
                second = q.pop()
                
                if c == 'T':
                    q.append(first)
                else:
                    q.append(second)
            else:
                q.append(c)
        
        return q[0]

# Solution 2, recursion
class Solution:
    def dfs(self, start, end, s):
        if start == end:
            return s[start]
        
        flag = s[start]
        
        i = start
        cnt = 0
        while i <= end:
            if s[i] == '?':
                cnt += 1
            elif s[i] == ':':
                cnt -= 1
                if cnt == 0:
                    break
            i += 1
        
        if flag == 'T':
            return self.dfs(start + 2, i - 1, s)
        return self.dfs(i + 1, end, s)
        
        
    def parseTernary(self, expression: str) -> str:
        s = expression
        
        n = len(s)
        
        res = self.dfs(0, n - 1, s)
        
        return res