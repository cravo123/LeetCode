import collections

# Typical DFS problem
# Solution 1, DFS
class Solution:
    def dfs(self, start, quiet, d, seen):
        res = start
        seen.add(start)
        
        for i in d[start]:
            if i not in seen:
                tmp = self.dfs(i, quiet, d, seen)
                if quiet[tmp] < quiet[res]:
                    res = tmp
        return res
        
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        d = collections.defaultdict(set)
        
        for x, y in richer:
            d[y].add(x)
        
        res = [i for i in range(len(quiet))]
        
        for i in range(len(quiet)):
            seen = set()
            res[i] = self.dfs(i, quiet, d, seen)
        
        return res

# Solution 2, DFS with cache, memoization
class Solution:
    def dfs(self, curr, quiet, d, seen):
        if curr in seen:
            return seen[curr]
        res = curr
        
        for i in d[curr]:
            t = self.dfs(i, quiet, d, seen)
            if quiet[t] < quiet[res]:
                res = t
        seen[curr] = res
        
        return res
        
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        d = collections.defaultdict(set)
        
        for x, y in richer:
            d[y].add(x)
        
        n = len(quiet)
        res = [_ for _ in quiet]
        seen = {}
        for i in range(n):
            res[i] = self.dfs(i, quiet, d, seen)
        
        return res