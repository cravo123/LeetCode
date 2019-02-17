"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

# Recursion
class Solution:
    def dfs(self, node):
        if node is None:
            return 0
        if not node.children:
            return 1
        return 1 + max(self.dfs(p) for p in node.children)
        
    def maxDepth(self, root: 'Node') -> 'int':
        return self.dfs(root)

# Iteration
class Solution:
    def maxDepth(self, root: 'Node') -> 'int':
        levels = 0
        if root is None:
            return levels
        q = [root]
        
        while q:
            levels += 1
            q = [x for p in q for x in p.children if x]
        
        return levels
