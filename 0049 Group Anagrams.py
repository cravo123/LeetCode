import collections

# Solution 1, sort
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        
        for word in strs:
            d[''.join(sorted(word))].append(word)
        
        res = list(d.values())
        
        return res

# Solution 2, DFS (TLE)
# Try to use DFS to solve this problem, although TLE
class Solution:
    def dfs(self, s, path, seen, strs):
        for _ in range(strs[s]):
            path.append(s)
        seen.add(s)
        
        for v in strs:
            if v not in seen and sorted(v) == sorted(s):
                self.dfs(v, path, seen, strs)
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs = collections.Counter(strs)
        seen = set()
        res = []
        
        for s in strs:
            if s not in seen:
                path = []
                self.dfs(s, path, seen, strs)
                res.append(path)
        
        return res