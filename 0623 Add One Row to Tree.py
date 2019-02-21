# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS
class Solution:
    def addOneRow(self, root: 'TreeNode', v: 'int', d: 'int') -> 'TreeNode':
        dummy = TreeNode(0)
        dummy.left = root
        
        idx = 0
        curr = [dummy]
        
        while idx < d - 1:
            curr = [x for p in curr for x in [p.left, p.right] if x]
            idx += 1
            
        for p in curr:
            q = TreeNode(v)
            q.left = p.left
            p.left = q
            q = TreeNode(v)
            q.right = p.right
            p.right = q
        return dummy.left

# DFS
class Solution:
    def dfs(self, node, curr, target, v):
        if node is None:
            return
        if curr == target - 1:
            p = TreeNode(v)
            p.left = node.left
            node.left = p
            
            p = TreeNode(v)
            p.right = node.right
            node.right = p
        else:
            self.dfs(node.left, curr + 1, target, v)
            self.dfs(node.right, curr + 1, target, v)
        
        
    def addOneRow(self, root: 'TreeNode', v: 'int', d: 'int') -> 'TreeNode':
        if d == 1:
            p = TreeNode(v)
            p.left = root
            return p
        
        self.dfs(root, 1, d, v)
        
        return root