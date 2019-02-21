# With memorization
class Solution:
    def dfs(self, curr, target, path, res, graph):
        if curr == target:
            res.append(path + [target])
            return 
        path.append(curr)
        
        for neighbor in graph[curr]:
            self.dfs(neighbor, target, path, res, graph)
        path.pop()
        
    def allPathsSourceTarget(self, graph: 'List[List[int]]') -> 'List[List[int]]':
        res = []
        path = []
        
        n = len(graph)
        
        self.dfs(0, n - 1, path, res, graph)
        
        return res

# Solution 2, with memorization
class Solution:
    def dfs(self, curr, target, graph, d):
        if curr in d:
            return d[curr]
        if curr == target:
            return [[target]]
        
        res = []
        
        for neighbor in graph[curr]:
            for path in self.dfs(neighbor, target, graph, d):
                res.append([curr] + path)
        d[curr] = res
        
        return res
        
    def allPathsSourceTarget(self, graph: 'List[List[int]]') -> 'List[List[int]]':
        d = {}
        
        self.dfs(0, len(graph) - 1, graph, d)
        
        return d[0]