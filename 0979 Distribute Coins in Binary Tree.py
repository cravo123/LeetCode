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
        move = node.val + L + R - 1
        self.res += abs(move)
        return move
        
    def distributeCoins(self, root: TreeNode) -> int:
        self.res = 0
        
        self.dfs(root)
        
        return self.res