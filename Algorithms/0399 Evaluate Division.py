import collections
# Solution 1, DFS
class Solution:
    def dfs(self, start, end, curr, d, seen):
        if start == end:
            return curr
        seen.add(start)
        
        for p in d[start]:
            if p not in seen:
                v = self.dfs(p, end, curr * d[start][p], d, seen) 
                if v is not None:
                    return v
        return None
        
    def solve(self, x, y, d):
        curr = 1.0
        
        if x not in d or y not in d:
            return None
        
        seen = set()
        res = self.dfs(x, y, curr, d, seen)
        
        return res
        
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = collections.defaultdict(dict)
        
        for equation, val in zip(equations, values):
            x, y = equation
            d[x][y] = val
            d[y][x] = 1 / val
        
        res = []
        for x, y in queries:
            v = self.solve(x, y, d)
            res.append(v if v is not None else -1.0)
        
        return res

# Solution 2, BFS
class Solution:     
    def solve(self, x, y, d):
        if x not in d or y not in d:
            return None
        q = collections.deque([[x, 1.0]])
        seen = set()
        
        while q:
            x, v = q.popleft()
            if x == y:
                return v
            seen.add(x)
            for i in d[x]:
                if i not in seen:
                    q.append([i, v * d[x][i]])
        
        return None
        
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = collections.defaultdict(dict)
        
        for equation, val in zip(equations, values):
            x, y = equation
            d[x][y] = val
            d[y][x] = 1 / val
        
        res = []
        for x, y in queries:
            v = self.solve(x, y, d)
            res.append(v if v is not None else -1.0)
        
        return res