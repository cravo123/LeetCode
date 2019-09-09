# Solution 1, typical DFS 
# Without memorization
class Solution:
    def dfs(self, idx, path, res, graph):
        path.append(idx)
        
        if idx == len(graph) - 1:
            res.append(path[::])
        else:
            for j in graph[idx]:
                self.dfs(j, path, res, graph)
        
        path.pop()
        
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = []
        res = []
        
        self.dfs(0, path, res, graph)
        
        return res

# Solution 2, DFS with memorization
class Solution:
    def dfs(self, idx, graph, d):
        if idx in d:
            return d[idx]
        
        res = []
        if idx == len(graph) - 1:
            res.append([idx])
        else:
            for j in graph[idx]:
                for next_path in self.dfs(j, graph, d):
                    res.append([idx] + next_path)
        
        d[idx] = res
        
        return res
        
        
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        d = {}
        
        return self.dfs(0, graph, d)