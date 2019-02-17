"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

# Recursion
class Solution:
    def dfs(self, node, res):
        if node is None:
            return
        for p in node.children:
            self.dfs(p, res)
        res.append(node.val)
        
    def postorder(self, root: 'Node') -> 'List[int]':
        res = []
        self.dfs(root, res)
        
        return res

# Iteration
# Post-order is Left -> Right -> Node
# The idea is that if we traverse Tree by Node -> Right -> Left, 
# then reversing the final results will give us the desired output.
class Solution:
    def postorder(self, root: 'Node') -> 'List[int]':
        res = []
        if root is None:
            return res
        q = [root]
        
        while q:
            p = q.pop()
            res.append(p.val)
            
            for x in p.children:
                q.append(x)
        return res[::-1]
