# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, recursion
class Solution:
    def dfs(self, node, val):
        res = TreeNode(val)
        if node is None or node.val < val:
            res.left = node
            return res
        node.right = self.dfs(node.right, val)
        
        return node
        
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        return self.dfs(root, val)

# Solution 2, iteration
