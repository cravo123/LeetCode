# Solution 1, DFS
# Color node alternatively by 0 and 1
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

# Solution 1.1, DFS using stack
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        d = {}
        
        for i in range(len(graph)):
            if i not in d:
                q = [i]
                d[i] = 0
                
                while q:
                    idx = q.pop()
                    
                    for j in graph[idx]:
                        if j in d and d[j] == d[idx]:
                            return False
                        if j not in d:
                            d[j] = 1 - d[idx]
                            q.append(j)
        return True

# Solution 2, BFS
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        d = {}
        
        for i in range(len(graph)):
            if i not in d:
                q = [i]
                color = 0
                
                while q:
                    tmp = []
                    
                    for i in q:
                        if i in d and d[i] != color:
                            return False
                        if i not in d:
                            d[i] = color
                            tmp.extend(graph[i])
                    q = tmp
                    color = 1- color
                    
        return True