# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node):
        if node is None:
            return 0, None
        L, R = self.dfs(node.left), self.dfs(node.right)
        
        if L[0] > R[0]:
            return L[0] + 1, L[1]
        if L[0] < R[0]:
            return R[0] + 1, R[1]
        
        return L[0] + 1, node
        
        
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        _, res = self.dfs(root)
        
        return res