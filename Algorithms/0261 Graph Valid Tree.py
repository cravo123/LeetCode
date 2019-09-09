import collections

# A graph of n nodes is a valid tree if either condition below satisfies,
# 1. It has n - 1 edges and there is no cycle in it,
# 2. It has n - 1 edges and all nodes are connected

# Solution 1, Union-Find
class Solution:
    def find_parent(self, i, d):
        if d[i] != i:
            d[i] = self.find_parent(d[i], d)
        return d[i]
    
    def validTree(self, n: int, edges: List[List[int]]) -> bool: 
        d = {i:i for i in range(n)}
        
        for i, j in edges:
            p_i, p_j = self.find_parent(i, d), self.find_parent(j, d)
            if p_i == p_j:
                return False
            d[p_i] = p_j
        
        if any(self.find_parent(i, d) != self.find_parent(0, d) for i in range(n)):
            return False
        
        return True

# Solution 2, DFS, BFS
class Solution:
    def bfs(self, d):
        seen = set([0])
        
        q = collections.deque([0])
        
        while q:
            idx = q.popleft()
            
            for i in d[idx]:
                if i not in seen:
                    seen.add(i)
                    q.append(i)
        
        return seen
        
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        d = collections.defaultdict(set)
        
        for i, j in edges:
            d[i].add(j)
            d[j].add(i)
        
        seen = self.bfs(d)
        
        return len(seen) == n