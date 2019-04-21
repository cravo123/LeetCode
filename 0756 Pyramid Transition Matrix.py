import collections

# Solution 1, check all possibilities
class Solution:
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        d = collections.defaultdict(set)
        
        for v in allowed:
            d[v[:2]].add(v[-1])
        
        q = list(set([c]) for c in bottom)
        
        while len(q) > 1:
            t = [set() for _ in range(len(q) - 1)]
            
            for i in range(len(q) - 1):
                for a in q[i]:
                    for b in q[i + 1]:
                        if a + b in d:
                            t[i] = t[i] | d[a + b]
            q = t
        return len(q) == 1 and len(q[0]) > 0

# Solution 2, DFS
# Solution 1 is level-traversal, or BFS
# BFS is good to find shortest-path, but if the goal is only to determine 
# if it is do-able, then DFS is actually a better choice since it has early termination
class Solution:
    def dfs(self, idx, bottom, path, res, d):
        if idx == len(bottom) - 1:
            res.append(''.join(path))
            return
        
        v = bottom[idx:(idx + 2)]
        if v in d:
            for c in d[v]:
                path.append(c)
                self.dfs(idx + 1, bottom, path, res, d)
                path.pop()
    
    def permutation(self, bottom, d):
        res = []
        path = []
        
        self.dfs(0, bottom, path, res, d)
        
        return res
    
    def solve(self, bottom, d):
        n = len(bottom)
        if n == 1:
            return True
        if n == 0:
            return False
        for level in self.permutation(bottom, d):
            if self.solve(level, d):
                return True
        return False
        
        
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        d = collections.defaultdict(set)
        
        for v in allowed:
            d[v[:2]].add(v[-1])
        
        return self.solve(bottom, d) 

# Solution 3, DFS with memoization
class Solution:
    def dfs(self, idx, bottom, path, res, d):
        if idx == len(bottom) - 1:
            res.append(''.join(path))
            return
        
        v = bottom[idx:(idx + 2)]
        if v in d:
            for c in d[v]:
                path.append(c)
                self.dfs(idx + 1, bottom, path, res, d)
                path.pop()
    
    def permutation(self, bottom, d):
        res = []
        path = []
        
        self.dfs(0, bottom, path, res, d)
        
        return res
    
    def solve(self, bottom, d, seen):
        if bottom in seen:
            return seen[bottom]
        n = len(bottom)
        if n == 1:
            return True
        if n == 0:
            return False
        for level in self.permutation(bottom, d):
            if self.solve(level, d, seen):
                seen[bottom] = True
                return True
        seen[bottom] = False
        return False
        
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        d = collections.defaultdict(set)
        
        for v in allowed:
            d[v[:2]].add(v[-1])
        
        seen = {}
        
        return self.solve(bottom, d, seen)