"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

# Recursion
class Solution:
    def dfs(self, node, level, res):
        if node is None:
            return
        if level >= len(res):
            res.append([])
        res[level].append(node.val)
        
        for p in node.children:
            self.dfs(p, level + 1, res)
        
    def levelOrder(self, root: 'Node') -> 'List[List[int]]':
        res = []
        
        self.dfs(root, 0, res)
        
        return res


# Iteration
class Solution:
    def levelOrder(self, root: 'Node') -> 'List[List[int]]':
        res = []
        
        if root is None:
            return res
        
        q = [root]
        
        while q:
            res.append([p.val for p in q])
            
            q = [x for p in q for x in p.children]
        
        return res
