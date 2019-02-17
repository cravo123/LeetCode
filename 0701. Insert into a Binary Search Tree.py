# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion
class Solution:
    def dfs(self, node, val):
        if node is None:
            return TreeNode(val)
        if node.val < val:
            node.right = self.dfs(node.right, val)
        else:
            node.left = self.dfs(node.left, val)
        return node
        
    def insertIntoBST(self, root: 'TreeNode', val: 'int') -> 'TreeNode':
        return self.dfs(root, val)

class Solution_Iteration:
    def insertIntoBST(self, root: 'TreeNode', val: 'int') -> 'TreeNode':
        new_node = TreeNode(val)
        if root is None:
            return new_node
        curr = root
        
        while curr:
            if curr.val < val:
                if curr.right is None:
                    curr.right = new_node
                    break
                curr = curr.right
            else:
                if curr.left is None:
                    curr.left = new_node
                    break
                curr = curr.left
        return root
