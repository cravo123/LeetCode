# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node, p, q):
        if node is None or node is p or node is q:
            return node
        L, R = self.dfs(node.left, p, q), self.dfs(node.right, p, q)
        
        if L is None:
            return R
        if R is None:
            return L
        return node
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p, q)