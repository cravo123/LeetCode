# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node, target):
        if node is None:
            return -1
        if node.val != target:
            return node.val
        L, R = self.dfs(node.left, target), self.dfs(node.right, target)
        
        if L == -1:
            return R
        if R == -1:
            return L
        return min(L, R)
        
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root is None:
            return -1
        res = self.dfs(root, root.val)
        
        return res