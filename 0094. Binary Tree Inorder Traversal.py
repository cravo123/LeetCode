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
        
        self.dfs(node.left, res)
        res.append(node.val)
        self.dfs(node.right, res)
        
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        res = []
        
        self.dfs(root, res)
        
        return res

# Iteration
class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        res = []
        p, q = root, []
        
        while p or q:
            if p:
                q.append(p)
                p = p.left
            else:
                p = q.pop()
                res.append(p.val)
                p = p.right
        return res
