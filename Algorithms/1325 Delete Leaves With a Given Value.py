# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, recursion
class Solution:
    def delete(self, node, val):
        if node is None:
            return
        
        node.left = self.delete(node.left, val)
        node.right = self.delete(node.right, val)
        
        if node.left is None and node.right is None and node.val == val:
            return
        
        return node
        
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        
        return self.delete(root, target)