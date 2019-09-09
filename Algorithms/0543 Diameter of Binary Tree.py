# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node):
        if node is None:
            return 0
        L, R = self.dfs(node.left), self.dfs(node.right)
        
        self.res = max(self.res, L + R + 1)
        
        return 1 + max(L, R)
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        
        self.dfs(root)
        
        return max(self.res - 1, 0)