# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node):
        if node is None:
            return 0, float('inf'), float('-inf') # cnt, low, up
        
        L, R = self.dfs(node.left), self.dfs(node.right)
        
        if L[0] == -1 or R[0] == -1 or node.val <= L[2] or node.val >= R[1]:
            return -1, 0, 0
        
        curr = 1 + L[0] + R[0]
        self.res = max(self.res, curr)
        return curr, min(node.val, L[1]), max(node.val, R[2])
                
    def largestBSTSubtree(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root)
        
        return self.res