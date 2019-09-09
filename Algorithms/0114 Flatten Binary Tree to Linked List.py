# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, recursion
class Solution:
    def dfs(self, node):
        if node is None:
            return
        
        L, R = self.dfs(node.left), self.dfs(node.right)
        
        node.left = None
        node.right = L
        curr = node
        while curr.right:
            curr = curr.right
        curr.right = R
        return node
        
    def flatten(self, root: 'TreeNode') -> 'None':
        """
        Do not return anything, modify root in-place instead.
        """
        self.dfs(root)
