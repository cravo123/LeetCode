# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion
class Solution:
    def dfs(self, node, res):
        if node is None:
            return
        res.append(node.val)
        
        self.dfs(node.left, res)
        self.dfs(node.right, res)
        
    def preorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        res = []
        
        self.dfs(root, res)
        
        return res

# Iteration
class Solution:
    def preorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        res = []
        
        if root is None:
            return res
        
        q = [root]
        
        while q:
            p = q.pop()
            res.append(p.val)
            
            if p.right:
                q.append(p.right)
            if p.left:
                q.append(p.left)
        return res
