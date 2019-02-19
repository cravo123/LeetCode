# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion
class Solution:
    def dfs(self, node, low, high):
        if node is None:
            return
        if node.val < low:
            return self.dfs(node.right, low, high)
        if node.val > high:
            return self.dfs(node.left, low, high)
        node.left, node.right = self.dfs(node.left, low, high), self.dfs(node.right, low, high)
        return node
    
    def trimBST(self, root: 'TreeNode', L: 'int', R: 'int') -> 'TreeNode':
        return self.dfs(root, L, R)
