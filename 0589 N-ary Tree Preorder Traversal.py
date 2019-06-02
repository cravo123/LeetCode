"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

# Solution 1, recursion
class Solution:
    def dfs(self, node, res):
        if node is None:
            return
        res.append(node.val)
        for p in node.children:
            self.dfs(p, res)
        
    def preorder(self, root: 'Node') -> 'List[int]':
        res = []
        self.dfs(root, res)
        return res

# Solution 2, iteration
class Solution:
    def preorder(self, root: 'Node') -> 'List[int]':
        res = []
        if root is None:
            return res
        
        q = [root]
        
        while q:
            p = q.pop()
            res.append(p.val)
            # Notice we need to reverse children so that it is pre-order
            for x in reversed(p.children):
                q.append(x)
        return res
