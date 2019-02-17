# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion
class Solution:
    def dfs(self, node, low, high):
        if node is None:
            return True
        if low < node.val < high:
            return self.dfs(node.left, low, node.val) and self.dfs(node.right, node.val, high)
        return False
        
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        return self.dfs(root, float('-inf'), float('inf'))

# Iteration
# In-order traverse BST to check if the order is monotonic increaseing
class Solution:
    def dfs(self, node, res):
        if node is None:
            return 
        
        self.dfs(node.left, res)
        res.append(node.val)
        self.dfs(node.right, res)
        
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        res = []
        self.dfs(root, res)
        
        return all(x < y for y, x in zip(res[1:], res))
