"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
# Solution 1, DFS, cache node -> node copy first
class Solution:
    def dfs(self, node, d):
        d[node] = Node(node.val, None)
        
        for p in node.neighbors:
            if p not in d:
                self.dfs(p, d)
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        d = {}
        
        self.dfs(node, d)
        
        for p in d:
            d[p].neighbors = [d[x] for x in p.neighbors]
        
        return d[node]
        