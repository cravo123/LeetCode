class Solution:
    def dfs(self, idx, graph, color, d):
        d[idx] = color
        
        for j in graph[idx]:
            if j in d and d[j] != 1 - color:
                return False
            if j not in d:
                if not self.dfs(j, graph, 1 - color, d):
                    return False
        return True
        
    def isBipartite(self, graph: List[List[int]]) -> bool:
        d = {}
        
        n = len(graph)
        
        for i in range(n):
            if i not in d:
                if not self.dfs(i, graph, 0, d):
                    return False
        return True