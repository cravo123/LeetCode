# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion
class Solution:
    def dfs(self, node):
        if node is None:
            return
        L, R = self.dfs(node.left), self.dfs(node.right)
        if L is None and R is None and node.val == 0:
            return 
        node.left, node.right = L, R
        return node
        
    def pruneTree(self, root: 'TreeNode') -> 'TreeNode':
        return self.dfs(root)
