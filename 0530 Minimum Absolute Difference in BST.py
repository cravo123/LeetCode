# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Same as In-order tree-traversal, and find minimum diff from two adjacent nodes

# Solution 1, Iteration
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        res = float('inf')
        prev = float('-inf')
        
        q = []
        p = root
        
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

# Solution 2, Recursion
class Solution:
    def dfs(self, node, prev):
        if node is None:
            return prev
        
        prev = self.dfs(node.left, prev)
        self.res = min(self.res, node.val - prev)
        
        return self.dfs(node.right, node.val)
        
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.res = float('inf')
        
        self.dfs(root, float('-inf'))
        
        return self.res