# Solution 1, simulation
class Solution:
    def findContestMatch(self, n: int) -> str:
        q = [str(i) for i in range(1, n + 1)]
        
        while len(q) > 1:
            tmp = []
            i, j = 0, len(q) - 1
            while i < j:
                tmp.append(('(%s,%s)') % (q[i], q[j]))
                i += 1
                j -= 1
            q = tmp
        return q[0]

# Solution 2, recursion
class Solution:
    def dfs(self, q):
        if len(q) == 1:
            return q
        
        res = []
        n = len(q) - 1
        
        for i in range(len(q) // 2):
            res.append('(%s,%s)' % (q[i], q[n - i]))
        
        return self.dfs(res)
    
    def findContestMatch(self, n: int) -> str:
        q = [str(i) for i in range(1, n + 1)]
        
        res = self.dfs(q)
        
        return res[0]