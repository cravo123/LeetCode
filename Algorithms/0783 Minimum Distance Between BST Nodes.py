# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, recursion
# DFS returns previous value
class Solution:
    def dfs(self, node, prev_val):
        if node is None:
            return prev_val
        
        prev_val = self.dfs(node.left, prev_val)
        self.res = min(self.res, node.val - prev_val)
        prev_val = self.dfs(node.right, node.val)
        
        return prev_val
        
    def minDiffInBST(self, root: TreeNode) -> int:
        self.res = float('inf')
        
        self.dfs(root, float('-inf'))
        
        return self.res

# Solution 2, iteration
# Just in-order traversal
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        prev = float('-inf')
        res = float('inf')
        
        p, q = root, []
        
        while p or q:
            if p:
                q.append(p)
                p = p.left
            else:
                p = q.pop()
                res = min(res, p.val - prev)
                prev = p.val
                p = p.right
        return res