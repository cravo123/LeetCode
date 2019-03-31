# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node):
        if node is None:
            return True
        L, R = self.dfs(node.left), self.dfs(node.right)
        
        if not (L and R):
            return False
        
        if node.left and node.left.val != node.val:
            return False
        if node.right and node.right.val != node.val:
            return False
        
        self.res += 1
        return True
        
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.res = 0
        
        self.dfs(root)
        
        return self.res