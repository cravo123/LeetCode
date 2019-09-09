# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, recursion
class Solution:
    def dfs(self, node, val):
        if node is None or node.val == val:
            return node
        if node.val < val:
            return self.dfs(node.right, val)
        return self.dfs(node.left, val)
        
    def searchBST(self, root: 'TreeNode', val: 'int') -> 'TreeNode':
        return self.dfs(root, val)

# Solution 2, iteration
class Solution:
    def searchBST(self, root: 'TreeNode', val: 'int') -> 'TreeNode':
        curr = root
        
        while curr:
            if curr.val < val:
                curr = curr.right
            elif curr.val > val:
                curr = curr.left
            else:
                return curr
        return 
