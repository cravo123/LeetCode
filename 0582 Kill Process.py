import collections

# Solution 1, DFS
class Solution:
    def dfs(self, pid, d, res):
        res.append(pid)
        
        for node in d[pid]:
            self.dfs(node, d, res)
        
    def killProcess(self, pid: 'List[int]', ppid: 'List[int]', kill: 'int') -> 'List[int]':
        d = collections.defaultdict(set)
        
        for node, parent in zip(pid, ppid):
            d[parent].add(node)
        
        res = []
        
        self.dfs(kill, d, res)
        
        return res

# Solution 2, BFS
# The difference between DFS and BFS is actually the data structure we use to store unvisited nodes
# For DFS it is stack, for BFS it is queue, for lowest cost it is priority queue
# Algorithms by Jeff Erickson has a very good explanation.
class Solution:
    def whatever_fs(self, node, d):
        res = []
        
        q = collections.deque([node])
        
        while q:
            # if it is BFS, then
            # p = q.popleft()
            p = q.pop()
            res.append(p)
            for t in d[p]:
                q.append(t)
        
        return res
        
    def killProcess(self, pid: 'List[int]', ppid: 'List[int]', kill: 'int') -> 'List[int]':
        d = collections.defaultdict(set)
        
        for node, parent in zip(pid, ppid):
            d[parent].add(node)
        
        res = self.whatever_fs(kill, d)
        
        return res
