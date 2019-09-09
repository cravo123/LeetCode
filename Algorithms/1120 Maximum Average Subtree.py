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
            return 0, 0
        L, R = self.dfs(node.left), self.dfs(node.right)
        
        total = L[0] + R[0] + node.val
        cnt = L[1] + R[1] + 1
        
        self.res = max(self.res, total / cnt)
        
        return total, cnt # curr_sum, curr_cnt
        
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.res = float('-inf')
        
        self.dfs(root)
        
        return self.res